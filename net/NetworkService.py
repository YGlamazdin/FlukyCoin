from protos import network_pb2, network_pb2_grpc
import datetime
import grpc

class NetworkService(network_pb2_grpc.NetworkServiceServicer):
    def __init__(self, local_address, version, data_processor):
        self.local_address = local_address
        self.version = version
        self.data_processor = data_processor
        self.known_peers = set(data_processor.initial_peers)  # Все известные адреса
        self.active_peers = set()  # Активные адреса

    # Реализация метода Ping
    def Ping(self, request, context):
        return network_pb2.Empty()  # Просто возвращает пустой ответ

    def RegisterPeer(self, request, context):
        address = request.address
        self.known_peers.add(address)
        # Проверяем, является ли адрес активным
        if self.check_active(address):
            self.active_peers.add(address)
        return network_pb2.PeerResponse(peers=list(self.active_peers))

    def GetPeers(self, request, context):
        # Возвращаем только активные адреса
        return network_pb2.PeerResponse(peers=list(self.active_peers))

    def GetNodeInfo(self, request, context):
        data = self.data_processor.fetch_data()
        return network_pb2.NodeInfoResponse(version=self.version, state="active", current_time=data)

    def check_active(self, address):
        try:
            with grpc.insecure_channel(address) as channel:
                stub = network_pb2_grpc.NetworkServiceStub(channel)
                stub.Ping(network_pb2.Empty(), timeout=1)  # Установка таймаута для пинга
                return True
        except grpc.RpcError as e:
            # print(f"Failed to ping {address}: {str(e)}")
            return False