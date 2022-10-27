# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import transaction_pb2 as transaction__pb2


class TransactionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTransaction = channel.unary_unary(
                '/pactus.Transaction/GetTransaction',
                request_serializer=transaction__pb2.TransactionRequest.SerializeToString,
                response_deserializer=transaction__pb2.TransactionResponse.FromString,
                )
        self.SendRawTransaction = channel.unary_unary(
                '/pactus.Transaction/SendRawTransaction',
                request_serializer=transaction__pb2.SendRawTransactionRequest.SerializeToString,
                response_deserializer=transaction__pb2.SendRawTransactionResponse.FromString,
                )


class TransactionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendRawTransaction(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TransactionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTransaction,
                    request_deserializer=transaction__pb2.TransactionRequest.FromString,
                    response_serializer=transaction__pb2.TransactionResponse.SerializeToString,
            ),
            'SendRawTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.SendRawTransaction,
                    request_deserializer=transaction__pb2.SendRawTransactionRequest.FromString,
                    response_serializer=transaction__pb2.SendRawTransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pactus.Transaction', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transaction(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Transaction/GetTransaction',
            transaction__pb2.TransactionRequest.SerializeToString,
            transaction__pb2.TransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendRawTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Transaction/SendRawTransaction',
            transaction__pb2.SendRawTransactionRequest.SerializeToString,
            transaction__pb2.SendRawTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
