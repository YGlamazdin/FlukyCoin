"""

Управление нодой

"""
import time

from core.Block import Block
from core.Transactions import Transaction
from core.protocol import Protocol
from storage.mempool import Mempool
from storage.miners_storage import MinerStorage
from storage.chain import Chain
import signal
import datetime
from net.client import Client
from net.network_manager import NetworkManager
from tools.time_sync import NTPTimeSynchronizer
from tools.logger import Log
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from net.GrpcServer import GrpcServer
from net.ClientHandler import ClientHandler


class NodeManager:
    """

    """

    def __init__(self, config, log=Log()):
        self.log = log
        self.config = config

        if "is_miner" not in self.config:
            self.config['is_miner'] = False
        # self.wallet_address = config.get("address")
        # self.log.info(f"Blockchain Node address {self.wallet_address}")

        self.start_time = time.time()

        self.initial_peers = config.get("initial_peers", ["localhost:5555"])
        # self.initial_peers.append(self.address)
        self.version = Protocol.VERSION

        self.peer_info = []


        self.time_ntpt = NTPTimeSynchronizer(log=log)

        self.mempool = Mempool(config)

        self.chain = Chain(config=self.config, mempool=self.mempool, log=self.log)

        self.miners_storage = MinerStorage(config)

        self.server = GrpcServer(self.config, self)

        self.client_handler = ClientHandler(self.server.servicer, self)

        self.server.start()

        self.block_candidate = "123"

        self._synced = False
        self.timer_drop_synced = None
        self.running = True

        self.executor = ThreadPoolExecutor(max_workers=2)



        self.enable_load_info = True
    def is_synced(self):
        return self._synced

    def set_node_synced(self, state):
        self._synced = state
        self.log.info(f"Node sync is {self._synced}")

    def add_transaction_to_mempool(self, transaction):
        """ ДОбавление новой транзакции """

        if not self.mempool.check_hash_transaction(transaction.txhash):
            """ Требуется провести валидацию, и возможно перетащить метод из основного класса """

            print("Добавлена новая транзакция", transaction.txhash)
            self.mempool.add_transaction(transaction)

    def add_new_transaction(self, transaction: Transaction):
        if not self.mempool.check_hash_transaction(transaction.txhash):

            """ добавить валидацию транзакции в цепи """

            if not self.chain.validate_transaction(transaction):
                print("Транзакция отклонена", transaction.txhash)
                return

            self.add_transaction_to_mempool(transaction)

            # Запускаем дистрибуцию хэша в отдельном потоке
            self.executor.submit(self.client_handler.distribute_transaction_hash, transaction.txhash)

            print("New transaction added and hash distributed.")

    def create_block(self, address_reward=None):
        """ """

        last_block = self.chain.block_candidate

        """ требуется откат индекса секретного колюча, если свой блок перебит"""

        if last_block is not None and last_block.signer in self.miners_storage.keys:
            return None

        for miner_address in list(self.miners_storage.keys.keys()):

            for address_miner in self.miners_storage.keys.keys():
                if self.chain.try_address_candidate(address_miner, miner_address):
                    miner_address = address_miner

            if last_block is not None:
                if self.chain.try_address_candidate(last_block.signer, miner_address):
                    # self.log.info("Кандидат сильнее")
                    return None

            # Лучший блок
            if last_block is not None and miner_address == last_block.signer:
                # self.log.info("кандидат устоял")
                return None

            if miner_address in self.miners_storage.keys and self.miners_storage.keys[miner_address].count_sign() <= 0:
                # self.log.info("Кончились подписи", miner_address)
                self.miners_storage.close_key(miner_address)
                continue

            if miner_address not in self.miners_storage.keys:
                continue

            # self.log.info(
            #     f"miner_address: {miner_address} count signs: {self.miners_storage.keys[miner_address].count_sign()}")

            # берем ключ из хранилища
            xmss = self.miners_storage.keys[miner_address]

            next_idx = self.chain.next_address_nonce(miner_address)
            if xmss.keyPair.SK.idx != next_idx - 1:
                # self.log.info(f"xmss.keyPair.SK.idx {xmss.keyPair.SK.idx}")
                edited_idx = xmss.set_idx(next_idx - 1)
                # self.log.warning(
                #     f"Не верное количество подписей между ключом и цепью. Ставим количество цепи {edited_idx}")

            """ Сбор блока под выбранный адрес """
            # self.log.info("Свой адрес победил, создаем блок")

            last_block_time = self.chain.last_block().timestamp_seconds if self.chain.last_block() is not None else self.chain.time()

            time_candidat = last_block_time + Protocol.BLOCK_TIME_INTERVAL
            # синхронизированное время цепи
            block_timestamp_seconds = time_candidat if time_candidat > self.chain.time() else self.chain.time()

            # создание блока со своим адресом
            transactions = []

            for tr in list(self.mempool.transactions.values()):
                if self.chain.validate_transaction(tr):
                    transactions.append(tr)
                    self.mempool.remove_transaction(tr.txhash)

            # block.hash_block()
            block_candidate = Block.create(self.chain.blocks_count(), self.chain.last_block_hash(),
                                           block_timestamp_seconds, transactions, address_miner=xmss.address,
                                           address_reward=address_reward)

            block_candidate.make_sign(xmss)

            # self.log.info("Блок создан", block_candidate.hash_block())

            if not self.chain.validate_block(block_candidate):
                # self.log.info("Блок не прошел валидацию")

                # не тратим подпись, то что было подписано выше откатываем:
                xmss.set_idx(xmss.idx() - 1)

                block_candidate = None
            else:
                self.miners_storage.save_storage_to_disk(block_candidate)

            return block_candidate

        # self.log.error("Нет подписей")
        self.miners_storage.generate_keys()
        return None
        # self.create_block()

    def uptime(self):
        return time.time() - self.start_time

    def check_sync(self, peer_info):
        """ проверка синхронности ноды """

        drop_sync_signal = False
        count_sync = 0
        if not self._synced:
            for address, info in peer_info.items():
                """ """
                # print(address, "info.blocks", info.blocks, info.synced)
                if info.synced:
                    count_sync += 1
                    if info.blocks > self.chain.blocks_count():
                        """ На синхронной ноде больше блоков. """

                        # возможен расинхрон
                        drop_sync_signal = True

                        block_number_to_load = self.chain.blocks_count()
                        block = self.client_handler.get_block_by_number(block_number_to_load, info.network_info)

                        if self.chain.validate_and_add_block(block):
                            print(f"Block [{block_number_to_load + 1}/{info.blocks}] added {block.hash_block()}")
                            if self.chain.blocks_count() % 100 == 0:
                                print("Save chain")
                                self.chain.save_chain_to_disk()
                        else:
                            print(f"{block_number_to_load + 1} reset")
                            self.chain.drop_last_block()
                            self.chain.drop_last_block()

        if self._synced and drop_sync_signal and self.timer_drop_synced is not None:
            self.timer_drop_synced = time.time()
            print("Включен таймер потери синхронизации")

        if count_sync == 0 and self._synced is False and time.time() > self.start_time + Protocol.TIME_WAIN_CONNECT_TO_NODES_START:
            self.log.info("Ноды не найдены, включаем синхронизацию")
            self.set_node_synced(True)

        if count_sync > 0 and len(peer_info) > 1 and drop_sync_signal is False and self._synced is False:

            self.timer_drop_synced = None

            last_block_time = self.chain.last_block().timestamp_seconds if self.chain.last_block() is not None else self.chain.time()

            # дожидаемся начала блока и не начина
            if self.chain.time() > last_block_time + Protocol.BLOCK_START_CHECK_PAUSE and self.chain.time() < last_block_time + Protocol.BLOCK_TIME_INTERVAL / 2:
                print("Нода синхронизирована")
                self.set_node_synced(True)
            else:
                print("Ждем начала блока")

        # отключен механизм потери синхронизации
        # if self.timer_drop_synced is not None:
        #     if time.time() > self.timer_drop_synced + Protocol.TIME_CONFIRM_LOST_SYNC:
        #         print("Нода потеряла синхронизацию по таймеру")
        #         self.set_node_synced(False)

        if self._synced:

            unsinc_count = 0

            last_block_time = self.chain.last_block().timestamp_seconds if self.chain.last_block() is not None else self.chain.time()

            # чтобы не создавать спам пакетов на срезах блоков, деламем паузу
            if self.chain.time() > last_block_time + Protocol.BLOCK_START_CHECK_PAUSE:

                """ если засинхрино, проверяем кандидаты """
                for address, info in peer_info.items():
                    """ """
                    if info.synced:
                        if info.block_candidate != 'None':
                            if info.latest_block == self.chain.last_block_hash():
                                if info.block_candidate == self.chain.block_candidate_hash:
                                    # print(""" На синхронной ноде кандидат отличается """)
                                    candidate_from_peer = self.client_handler.get_block_candidate(info.network_info)

                                    if self.chain.validate_block(candidate_from_peer):
                                        if self.chain.validate_candidate(candidate_from_peer):
                                            if self.chain.add_block_candidate(candidate_from_peer):
                                                print(""" Новый кандидат добавлен """)
                                                print(""" Делаем рассылку  """)
                                                self.client_handler.distribute_block(candidate_from_peer)
                            else:
                                """ На нодах разные последние блоки, признаки рассинхрона """
                                print("Различие  в блоках", info.latest_block, self.chain.last_block_hash())
                                unsinc_count += 1
            if unsinc_count + 1 == len(peer_info) and  len(peer_info) >2:
                print("Наша нода единственная отличается от цепи")
                self.set_node_synced(False)

    def technical_block(self):

        timer_get_nodes = 0
        timer_ping_peers = 0

        while self.running:
            try:
                if timer_ping_peers + Protocol.TIME_PAUSE_PING_PEERS < time.time():
                    timer_ping_peers = time.time()
                    self.client_handler.ping_peers()
                    try:
                        self.client_handler.connect_to_peers()
                    except Exception as e:
                        print("error connect_to_peers", e)

                    if self.enable_load_info:
                        print("fetch_info_from_peers")
                        self.peer_info = self.client_handler.fetch_info_from_peers()

                if self.enable_load_info:
                    self.check_sync(self.peer_info)

                if self._synced and timer_get_nodes + Protocol.TIME_PAUSE_GET_PEERS < time.time():
                    timer_get_nodes = time.time()

                    self.client_handler.get_peers_list()
                    self.client_handler.fetch_transactions_from_all_peers()

                if not self._synced:
                    continue

                time.sleep(1)
            except KeyboardInterrupt:
                self.running = False
                exit()
            except Exception as e:
                print("Ошибка технического блока ", e)

    def toggle_feature(self):
        """ Для дебага управление функционалом ноды """

        while True:
            command = input("Enter command: ").strip().split()
            if len(command) == 1:
                if command[0] == "1":
                    self.enable_load_info = not self.enable_load_info
                    print(f"enable_load_info {'enabled' if self.enable_load_info else 'disabled'}.")
                elif command[0] == "b":
                    feature_b_enabled = not feature_b_enabled
                    print(f"Feature B {'enabled' if feature_b_enabled else 'disabled'}.")
                else:
                    print(f"No such feature: {command[1]}")
            elif command[0] == "exit":
                print("Exiting...")
                break
            else:
                print("Unknown command.")

    def run_node(self):
        """ Основной цикл  """

        self.executor.submit(self.technical_block)

        self.executor.submit(self.toggle_feature)

        while True:

            if not self._synced:
                self.log.info(
                    f"---synced {self._synced}-------is_miner {self.config.get('is_miner', 'False')}-----------active_peers: {self.server.servicer.active_peers}")
                # self.log.info(
                #     f"active_peers: {self.server.servicer.active_peers}")
                # self.log.info(
                #     f"known_peers: {self.server.servicer.known_peers}")

            if not self._synced:
                # нода не синхронна, не работаем
                time.sleep(Protocol.BLOCK_TIME_INTERVAL_LOG)
                continue

            ###############################################
            ######   создание блока и обмен блоками
            ###############################################

            new_block = None

            if self.config.get('is_miner', "False"):

                last_block_time = self.chain.last_block().timestamp_seconds if self.chain.last_block() is not None else self.chain.time()

                # чтобы не создавать спам пакетов на срезах блоков, делаем паузу
                if self.chain.blocks_count() == 0 or self.chain.time() > last_block_time + Protocol.BLOCK_TIME_PAUSE_AFTER_CLOSE:
                    # создать свой блок
                    new_block = self.create_block(self.config.get("address_reward"))
            # print(len(self.mempool.transactions.keys()), self.mempool.transactions.keys())
            # new_block = self.create_block()

            if self.chain.add_block_candidate(new_block):
                self.log.info(f"Свой Блок кандидат добавлен", new_block.hash,
                              new_block.signer)
                # self.network_manager.distribute_block(self.chain.block_candidate)
                # print("self.server.servicer.active_peers", self.server.servicer.active_peers)

                self.executor.submit(self.client_handler.distribute_block, self.chain.block_candidate)

            needClose = self.chain.need_close_block()
            if needClose and self.chain.block_candidate is not None:

                # блок еще закрытый, его нет в цепи
                num_block_to_close = self.chain.blocks_count() + 1

                self.log.info(f"*** START CLOSE {num_block_to_close} ****************", )

                if not self.chain.close_block():
                    self.log.info("last_block", self.chain.last_block_hash())
                    self.log.info("candidate", self.chain.block_candidate_hash)
                    self.chain.reset_block_candidat()
                    # time.sleep(0.45)
                    continue
                last_block = self.chain.last_block()
                if last_block is not None:
                    self.log.info(f"Chain {len(self.chain.blocks)} blocks , последний: ", last_block.hash_block(),
                                  last_block.signer, self.chain.next_address_nonce(last_block.signer))

                self.chain.save_chain_to_disk()
                self.miners_storage.save_storage_to_disk()
                self.mempool.save_mempool()

                self.log.info(f"{datetime.datetime.now()} Дата закрытого блока: {self.chain.last_block().datetime()}")
                if Protocol.is_key_block(self.chain.last_block().hash):
                    self.log.info("СЛЕДУЮЩИЙ КЛЮЧЕВОЙ БЛОК")
                self.log.info(
                    f"*** END CLOSE {num_block_to_close} **************** Active peers: {self.server.servicer.active_peers}", )
                # print(self.chain.transaction_storage.nonces)
                continue

            # print(len(self.mempool.transactions.keys()), self.mempool.transactions.keys())

            text = f"Check: {self.chain.blocks_count()} peers[{len(self.server.servicer.active_peers)}] txs[{self.mempool.size()}] "
            if self.chain.block_candidate is not None:
                text += f"delta: {self.chain.block_candidate.timestamp_seconds - self.chain.time():0.2f}  {self.chain.block_candidate.hash_block()[:5]}...{self.chain.block_candidate.hash_block()[-5:]}  singer: ...{self.chain.block_candidate.signer[-5:]}"
            self.log.info(text)

            time.sleep(Protocol.BLOCK_TIME_INTERVAL_LOG)
