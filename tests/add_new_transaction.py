# from core.Transactions import Transaction
# from net.client import Client
# from core.protocol import Protocol
#
# import random
# if __name__ == '__main__':
#     """ """
#
#     t = Transaction("coinbase", random.randint(0,100000), "2", "100")
#     t.make_hash()
#     # print(t.get_data_hash().hexdigest())
#     print(t.txhash)
#
#     # client = Client(host = "127.0.0.1", port = 9334)
#     client = Client(host = "192.168.0.26", port = 9334)
#
#     response = client.send_request(
#         {'command': 'version', 'ver': Protocol.VERSION, 'address': "127.0.0.1:888"})
#     print(response)
#
#     response = client.send_request(
#         {'command': 'tx', 'tx_data': {'tx_json':t.to_json(), 'tx_sign':t.signature}})
#     print(response)

import os, sys
# Получаем путь на директорию выше
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Добавляем этот путь в sys.path
sys.path.append(parent_directory)



import time

import json
import hashlib
from core.protocol import Protocol
from crypto.xmss import XMSS, XMSSPublicKey, SigXMSS, XMSS_verify
from tools.logger import Log


import grpc
from protos import network_pb2, network_pb2_grpc

from core.Transactions import Transaction, TransferTransaction

def add_transaction(server_address, transaction:Transaction):
    # Создание gRPC канала
    channel = grpc.insecure_channel(server_address)
    stub = network_pb2_grpc.NetworkServiceStub(channel)

    json_data = transaction.to_json()
    # Создание объекта транзакции
    transaction = network_pb2.Transaction(json_data=json_data)

    # Отправка транзакции на сервер
    try:
        response = stub.AddTransaction(transaction)
        if response.success:
            print("Transaction successfully added.")
        else:
            print("Failed to add transaction.")
    except grpc.RpcError as e:
        print(f"Failed to connect to server: {str(e)}")

if __name__ == "__main__":
    # Пример использования
    server_address = '192.168.0.26:9334'  # Адрес сервера
    # server_address = '127.0.0.1:9335'  # Адрес сервера

    xmss = XMSS.create(seed_phrase =input())
    # xmss = XMSS.create(seed_phrase = )
    print(xmss.address)

    # tt = TransferTransaction(xmss.address, ["Runsb7FX8Qzr3SBxzWmBpNJD3sG2HCSxLHgbXEfiUTPiGLEfbQsZ"], [10000000], message_data=["test message"])
    tt = TransferTransaction(xmss.address, ["YGPieNA3cqvCKSKm8NkR2oE6gCLf4pkNaie3g1Kmc2Siiprh3cjA"], [1000000000], message_data=["test message"])
    tt.nonce = 5
    tt.make_hash()
    tt.make_sign(xmss)
    json_transaction = tt.to_json()

    add_transaction(server_address, tt)
