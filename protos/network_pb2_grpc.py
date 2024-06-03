# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import protos.network_pb2 as network__pb2

GRPC_GENERATED_VERSION = '1.64.0'
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
        self.GetNodeInfo = channel.unary_unary(
                '/NetworkService/GetNodeInfo',
                request_serializer=network__pb2.NodeInfoRequest.SerializeToString,
                response_deserializer=network__pb2.NodeInfoResponse.FromString,
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

    def GetNodeInfo(self, request, context):
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
            'GetNodeInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNodeInfo,
                    request_deserializer=network__pb2.NodeInfoRequest.FromString,
                    response_serializer=network__pb2.NodeInfoResponse.SerializeToString,
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
    def GetNodeInfo(request,
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
            '/NetworkService/GetNodeInfo',
            network__pb2.NodeInfoRequest.SerializeToString,
            network__pb2.NodeInfoResponse.FromString,
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
