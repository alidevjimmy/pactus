# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import utils_pb2 as utils__pb2


class UtilsStub(object):
    """Utils service defines RPC methods for utility functions such as message
    signing and verification.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SignMessageWithPrivateKey = channel.unary_unary(
                '/pactus.Utils/SignMessageWithPrivateKey',
                request_serializer=utils__pb2.SignMessageWithPrivateKeyRequest.SerializeToString,
                response_deserializer=utils__pb2.SignMessageWithPrivateKeyResponse.FromString,
                )
        self.VerifyMessage = channel.unary_unary(
                '/pactus.Utils/VerifyMessage',
                request_serializer=utils__pb2.VerifyMessageRequest.SerializeToString,
                response_deserializer=utils__pb2.VerifyMessageResponse.FromString,
                )
        self.BLSPublicKeyAggregation = channel.unary_unary(
                '/pactus.Utils/BLSPublicKeyAggregation',
                request_serializer=utils__pb2.BLSPublicKeyAggregationRequest.SerializeToString,
                response_deserializer=utils__pb2.BLSPublicKeyAggregationResponse.FromString,
                )
        self.BLSSignatureAggregation = channel.unary_unary(
                '/pactus.Utils/BLSSignatureAggregation',
                request_serializer=utils__pb2.BLSSignatureAggregationRequest.SerializeToString,
                response_deserializer=utils__pb2.BLSSignatureAggregationResponse.FromString,
                )


class UtilsServicer(object):
    """Utils service defines RPC methods for utility functions such as message
    signing and verification.
    """

    def SignMessageWithPrivateKey(self, request, context):
        """SignMessageWithPrivateKey signs message with provided private key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyMessage(self, request, context):
        """VerifyMessage verifies signature with public key and message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BLSPublicKeyAggregation(self, request, context):
        """BLSPublicKeyAggregation aggregates bls public keys.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BLSSignatureAggregation(self, request, context):
        """BLSSignatureAggregation aggregates bls signatures.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UtilsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SignMessageWithPrivateKey': grpc.unary_unary_rpc_method_handler(
                    servicer.SignMessageWithPrivateKey,
                    request_deserializer=utils__pb2.SignMessageWithPrivateKeyRequest.FromString,
                    response_serializer=utils__pb2.SignMessageWithPrivateKeyResponse.SerializeToString,
            ),
            'VerifyMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyMessage,
                    request_deserializer=utils__pb2.VerifyMessageRequest.FromString,
                    response_serializer=utils__pb2.VerifyMessageResponse.SerializeToString,
            ),
            'BLSPublicKeyAggregation': grpc.unary_unary_rpc_method_handler(
                    servicer.BLSPublicKeyAggregation,
                    request_deserializer=utils__pb2.BLSPublicKeyAggregationRequest.FromString,
                    response_serializer=utils__pb2.BLSPublicKeyAggregationResponse.SerializeToString,
            ),
            'BLSSignatureAggregation': grpc.unary_unary_rpc_method_handler(
                    servicer.BLSSignatureAggregation,
                    request_deserializer=utils__pb2.BLSSignatureAggregationRequest.FromString,
                    response_serializer=utils__pb2.BLSSignatureAggregationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pactus.Utils', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Utils(object):
    """Utils service defines RPC methods for utility functions such as message
    signing and verification.
    """

    @staticmethod
    def SignMessageWithPrivateKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Utils/SignMessageWithPrivateKey',
            utils__pb2.SignMessageWithPrivateKeyRequest.SerializeToString,
            utils__pb2.SignMessageWithPrivateKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Utils/VerifyMessage',
            utils__pb2.VerifyMessageRequest.SerializeToString,
            utils__pb2.VerifyMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BLSPublicKeyAggregation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Utils/BLSPublicKeyAggregation',
            utils__pb2.BLSPublicKeyAggregationRequest.SerializeToString,
            utils__pb2.BLSPublicKeyAggregationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BLSSignatureAggregation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Utils/BLSSignatureAggregation',
            utils__pb2.BLSSignatureAggregationRequest.SerializeToString,
            utils__pb2.BLSSignatureAggregationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
