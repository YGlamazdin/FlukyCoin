# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import protos.network_pb2 as network__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in network_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class NetworkServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterPeer = channel.unary_unary(
                '/NetworkService/RegisterPeer',
                request_serializer=network__pb2.PeerRequest.SerializeToString,
                response_deserializer=network__pb2.PeerResponse.FromString,
                _registered_method=True)
        self.GetPeers = channel.unary_unary(
                '/NetworkService/GetPeers',
                request_serializer=network__pb2.PeerRequest.SerializeToString,
                response_deserializer=network__pb2.PeerResponse.FromString,
                _registered_method=True)
        self.Ping = channel.unary_unary(
                '/NetworkService/Ping',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.Empty.FromString,
                _registered_method=True)
        self.GetPeerInfo = channel.unary_unary(
                '/NetworkService/GetPeerInfo',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.PeerInfoResponse.FromString,
                _registered_method=True)
        self.BroadcastTransactionHash = channel.unary_unary(
                '/NetworkService/BroadcastTransactionHash',
                request_serializer=network__pb2.TransactionHash.SerializeToString,
                response_deserializer=network__pb2.Ack.FromString,
                _registered_method=True)
        self.GetFullTransaction = channel.unary_unary(
                '/NetworkService/GetFullTransaction',
                request_serializer=network__pb2.TransactionHash.SerializeToString,
                response_deserializer=network__pb2.Transaction.FromString,
                _registered_method=True)
        self.AddTransaction = channel.unary_unary(
                '/NetworkService/AddTransaction',
                request_serializer=network__pb2.Transaction.SerializeToString,
                response_deserializer=network__pb2.Ack.FromString,
                _registered_method=True)
        self.GetAllTransactions = channel.unary_unary(
                '/NetworkService/GetAllTransactions',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.TransactionList.FromString,
                _registered_method=True)
        self.BroadcastBlock = channel.unary_unary(
                '/NetworkService/BroadcastBlock',
                request_serializer=network__pb2.Block.SerializeToString,
                response_deserializer=network__pb2.Ack.FromString,
                _registered_method=True)
        self.GetBlockByNumber = channel.unary_unary(
                '/NetworkService/GetBlockByNumber',
                request_serializer=network__pb2.BlockRequest.SerializeToString,
                response_deserializer=network__pb2.BlockResponse.FromString,
                _registered_method=True)
        self.GetBlockCandidate = channel.unary_unary(
                '/NetworkService/GetBlockCandidate',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.BlockResponse.FromString,
                _registered_method=True)
        self.GetAddressInfo = channel.unary_unary(
                '/NetworkService/GetAddressInfo',
                request_serializer=network__pb2.AddressRequest.SerializeToString,
                response_deserializer=network__pb2.AddressInfoResponse.FromString,
                _registered_method=True)
        self.GetNetInfo = channel.unary_unary(
                '/NetworkService/GetNetInfo',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.NetInfoResponse.FromString,
                _registered_method=True)
        self.GetAllAddresses = channel.unary_unary(
                '/NetworkService/GetAllAddresses',
                request_serializer=network__pb2.Empty.SerializeToString,
                response_deserializer=network__pb2.AddressList.FromString,
                _registered_method=True)
        self.BroadcastBlockHash = channel.unary_unary(
                '/NetworkService/BroadcastBlockHash',
                request_serializer=network__pb2.BlockHash.SerializeToString,
                response_deserializer=network__pb2.BlockHashResponse.FromString,
                _registered_method=True)


class NetworkServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterPeer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Добавляем метод Ping
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPeerInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastTransactionHash(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFullTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllTransactions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockByNumber(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockCandidate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAddressInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNetInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllAddresses(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BroadcastBlockHash(self, request, context):
        """Новый метод
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterPeer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterPeer,
                    request_deserializer=network__pb2.PeerRequest.FromString,
                    response_serializer=network__pb2.PeerResponse.SerializeToString,
            ),
            'GetPeers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeers,
                    request_deserializer=network__pb2.PeerRequest.FromString,
                    response_serializer=network__pb2.PeerResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.Empty.SerializeToString,
            ),
            'GetPeerInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPeerInfo,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.PeerInfoResponse.SerializeToString,
            ),
            'BroadcastTransactionHash': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastTransactionHash,
                    request_deserializer=network__pb2.TransactionHash.FromString,
                    response_serializer=network__pb2.Ack.SerializeToString,
            ),
            'GetFullTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFullTransaction,
                    request_deserializer=network__pb2.TransactionHash.FromString,
                    response_serializer=network__pb2.Transaction.SerializeToString,
            ),
            'AddTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTransaction,
                    request_deserializer=network__pb2.Transaction.FromString,
                    response_serializer=network__pb2.Ack.SerializeToString,
            ),
            'GetAllTransactions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllTransactions,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.TransactionList.SerializeToString,
            ),
            'BroadcastBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastBlock,
                    request_deserializer=network__pb2.Block.FromString,
                    response_serializer=network__pb2.Ack.SerializeToString,
            ),
            'GetBlockByNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockByNumber,
                    request_deserializer=network__pb2.BlockRequest.FromString,
                    response_serializer=network__pb2.BlockResponse.SerializeToString,
            ),
            'GetBlockCandidate': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockCandidate,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.BlockResponse.SerializeToString,
            ),
            'GetAddressInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAddressInfo,
                    request_deserializer=network__pb2.AddressRequest.FromString,
                    response_serializer=network__pb2.AddressInfoResponse.SerializeToString,
            ),
            'GetNetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNetInfo,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.NetInfoResponse.SerializeToString,
            ),
            'GetAllAddresses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllAddresses,
                    request_deserializer=network__pb2.Empty.FromString,
                    response_serializer=network__pb2.AddressList.SerializeToString,
            ),
            'BroadcastBlockHash': grpc.unary_unary_rpc_method_handler(
                    servicer.BroadcastBlockHash,
                    request_deserializer=network__pb2.BlockHash.FromString,
                    response_serializer=network__pb2.BlockHashResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NetworkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('NetworkService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NetworkService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterPeer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/RegisterPeer',
            network__pb2.PeerRequest.SerializeToString,
            network__pb2.PeerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPeers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetPeers',
            network__pb2.PeerRequest.SerializeToString,
            network__pb2.PeerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/Ping',
            network__pb2.Empty.SerializeToString,
            network__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPeerInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetPeerInfo',
            network__pb2.Empty.SerializeToString,
            network__pb2.PeerInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BroadcastTransactionHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/BroadcastTransactionHash',
            network__pb2.TransactionHash.SerializeToString,
            network__pb2.Ack.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFullTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetFullTransaction',
            network__pb2.TransactionHash.SerializeToString,
            network__pb2.Transaction.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/AddTransaction',
            network__pb2.Transaction.SerializeToString,
            network__pb2.Ack.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllTransactions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetAllTransactions',
            network__pb2.Empty.SerializeToString,
            network__pb2.TransactionList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BroadcastBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/BroadcastBlock',
            network__pb2.Block.SerializeToString,
            network__pb2.Ack.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetBlockByNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetBlockByNumber',
            network__pb2.BlockRequest.SerializeToString,
            network__pb2.BlockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetBlockCandidate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetBlockCandidate',
            network__pb2.Empty.SerializeToString,
            network__pb2.BlockResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAddressInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetAddressInfo',
            network__pb2.AddressRequest.SerializeToString,
            network__pb2.AddressInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetNetInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetNetInfo',
            network__pb2.Empty.SerializeToString,
            network__pb2.NetInfoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAllAddresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/GetAllAddresses',
            network__pb2.Empty.SerializeToString,
            network__pb2.AddressList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BroadcastBlockHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/NetworkService/BroadcastBlockHash',
            network__pb2.BlockHash.SerializeToString,
            network__pb2.BlockHashResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
