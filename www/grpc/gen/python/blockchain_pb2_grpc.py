# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import blockchain_pb2 as blockchain__pb2


class BlockchainStub(object):
    """Blockchain service defines RPC methods for interacting with the blockchain.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBlock = channel.unary_unary(
                '/pactus.Blockchain/GetBlock',
                request_serializer=blockchain__pb2.GetBlockRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetBlockResponse.FromString,
                )
        self.GetBlockHash = channel.unary_unary(
                '/pactus.Blockchain/GetBlockHash',
                request_serializer=blockchain__pb2.GetBlockHashRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetBlockHashResponse.FromString,
                )
        self.GetBlockHeight = channel.unary_unary(
                '/pactus.Blockchain/GetBlockHeight',
                request_serializer=blockchain__pb2.GetBlockHeightRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetBlockHeightResponse.FromString,
                )
        self.GetBlockchainInfo = channel.unary_unary(
                '/pactus.Blockchain/GetBlockchainInfo',
                request_serializer=blockchain__pb2.GetBlockchainInfoRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetBlockchainInfoResponse.FromString,
                )
        self.GetConsensusInfo = channel.unary_unary(
                '/pactus.Blockchain/GetConsensusInfo',
                request_serializer=blockchain__pb2.GetConsensusInfoRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetConsensusInfoResponse.FromString,
                )
        self.GetAccount = channel.unary_unary(
                '/pactus.Blockchain/GetAccount',
                request_serializer=blockchain__pb2.GetAccountRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetAccountResponse.FromString,
                )
        self.GetValidator = channel.unary_unary(
                '/pactus.Blockchain/GetValidator',
                request_serializer=blockchain__pb2.GetValidatorRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetValidatorResponse.FromString,
                )
        self.GetValidatorByNumber = channel.unary_unary(
                '/pactus.Blockchain/GetValidatorByNumber',
                request_serializer=blockchain__pb2.GetValidatorByNumberRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetValidatorResponse.FromString,
                )
        self.GetValidatorAddresses = channel.unary_unary(
                '/pactus.Blockchain/GetValidatorAddresses',
                request_serializer=blockchain__pb2.GetValidatorAddressesRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetValidatorAddressesResponse.FromString,
                )
        self.GetPublicKey = channel.unary_unary(
                '/pactus.Blockchain/GetPublicKey',
                request_serializer=blockchain__pb2.GetPublicKeyRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetPublicKeyResponse.FromString,
                )
        self.GetTxPoolContent = channel.unary_unary(
                '/pactus.Blockchain/GetTxPoolContent',
                request_serializer=blockchain__pb2.GetTxPoolContentRequest.SerializeToString,
                response_deserializer=blockchain__pb2.GetTxPoolContentResponse.FromString,
                )


class BlockchainServicer(object):
    """Blockchain service defines RPC methods for interacting with the blockchain.
    """

    def GetBlock(self, request, context):
        """GetBlock retrieves information about a block based on the provided request
        parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockHash(self, request, context):
        """GetBlockHash retrieves the hash of a block at the specified height.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockHeight(self, request, context):
        """GetBlockHeight retrieves the height of a block with the specified hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockchainInfo(self, request, context):
        """GetBlockchainInfo retrieves general information about the blockchain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetConsensusInfo(self, request, context):
        """GetConsensusInfo retrieves information about the consensus instances.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccount(self, request, context):
        """GetAccount retrieves information about an account based on the provided
        address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidator(self, request, context):
        """GetValidator retrieves information about a validator based on the provided
        address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidatorByNumber(self, request, context):
        """GetValidatorByNumber retrieves information about a validator based on the
        provided number.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidatorAddresses(self, request, context):
        """GetValidatorAddresses retrieves a list of all validator addresses.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPublicKey(self, request, context):
        """GetPublicKey retrieves the public key of an account based on the provided
        address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTxPoolContent(self, request, context):
        """GetTxPoolContent retrieves current transactions on the TXPool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BlockchainServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlock,
                    request_deserializer=blockchain__pb2.GetBlockRequest.FromString,
                    response_serializer=blockchain__pb2.GetBlockResponse.SerializeToString,
            ),
            'GetBlockHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockHash,
                    request_deserializer=blockchain__pb2.GetBlockHashRequest.FromString,
                    response_serializer=blockchain__pb2.GetBlockHashResponse.SerializeToString,
            ),
            'GetBlockHeight': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockHeight,
                    request_deserializer=blockchain__pb2.GetBlockHeightRequest.FromString,
                    response_serializer=blockchain__pb2.GetBlockHeightResponse.SerializeToString,
            ),
            'GetBlockchainInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockchainInfo,
                    request_deserializer=blockchain__pb2.GetBlockchainInfoRequest.FromString,
                    response_serializer=blockchain__pb2.GetBlockchainInfoResponse.SerializeToString,
            ),
            'GetConsensusInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConsensusInfo,
                    request_deserializer=blockchain__pb2.GetConsensusInfoRequest.FromString,
                    response_serializer=blockchain__pb2.GetConsensusInfoResponse.SerializeToString,
            ),
            'GetAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccount,
                    request_deserializer=blockchain__pb2.GetAccountRequest.FromString,
                    response_serializer=blockchain__pb2.GetAccountResponse.SerializeToString,
            ),
            'GetValidator': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidator,
                    request_deserializer=blockchain__pb2.GetValidatorRequest.FromString,
                    response_serializer=blockchain__pb2.GetValidatorResponse.SerializeToString,
            ),
            'GetValidatorByNumber': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidatorByNumber,
                    request_deserializer=blockchain__pb2.GetValidatorByNumberRequest.FromString,
                    response_serializer=blockchain__pb2.GetValidatorResponse.SerializeToString,
            ),
            'GetValidatorAddresses': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidatorAddresses,
                    request_deserializer=blockchain__pb2.GetValidatorAddressesRequest.FromString,
                    response_serializer=blockchain__pb2.GetValidatorAddressesResponse.SerializeToString,
            ),
            'GetPublicKey': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPublicKey,
                    request_deserializer=blockchain__pb2.GetPublicKeyRequest.FromString,
                    response_serializer=blockchain__pb2.GetPublicKeyResponse.SerializeToString,
            ),
            'GetTxPoolContent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTxPoolContent,
                    request_deserializer=blockchain__pb2.GetTxPoolContentRequest.FromString,
                    response_serializer=blockchain__pb2.GetTxPoolContentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pactus.Blockchain', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Blockchain(object):
    """Blockchain service defines RPC methods for interacting with the blockchain.
    """

    @staticmethod
    def GetBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetBlock',
            blockchain__pb2.GetBlockRequest.SerializeToString,
            blockchain__pb2.GetBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetBlockHash',
            blockchain__pb2.GetBlockHashRequest.SerializeToString,
            blockchain__pb2.GetBlockHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockHeight(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetBlockHeight',
            blockchain__pb2.GetBlockHeightRequest.SerializeToString,
            blockchain__pb2.GetBlockHeightResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockchainInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetBlockchainInfo',
            blockchain__pb2.GetBlockchainInfoRequest.SerializeToString,
            blockchain__pb2.GetBlockchainInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetConsensusInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetConsensusInfo',
            blockchain__pb2.GetConsensusInfoRequest.SerializeToString,
            blockchain__pb2.GetConsensusInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetAccount',
            blockchain__pb2.GetAccountRequest.SerializeToString,
            blockchain__pb2.GetAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidator(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetValidator',
            blockchain__pb2.GetValidatorRequest.SerializeToString,
            blockchain__pb2.GetValidatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidatorByNumber(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetValidatorByNumber',
            blockchain__pb2.GetValidatorByNumberRequest.SerializeToString,
            blockchain__pb2.GetValidatorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidatorAddresses(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetValidatorAddresses',
            blockchain__pb2.GetValidatorAddressesRequest.SerializeToString,
            blockchain__pb2.GetValidatorAddressesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPublicKey(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetPublicKey',
            blockchain__pb2.GetPublicKeyRequest.SerializeToString,
            blockchain__pb2.GetPublicKeyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTxPoolContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Blockchain/GetTxPoolContent',
            blockchain__pb2.GetTxPoolContentRequest.SerializeToString,
            blockchain__pb2.GetTxPoolContentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
