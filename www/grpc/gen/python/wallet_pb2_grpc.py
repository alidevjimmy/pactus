# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import wallet_pb2 as wallet__pb2


class WalletStub(object):
    """Define the Wallet service with various RPC methods for wallet management.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateWallet = channel.unary_unary(
                '/pactus.Wallet/CreateWallet',
                request_serializer=wallet__pb2.CreateWalletRequest.SerializeToString,
                response_deserializer=wallet__pb2.CreateWalletResponse.FromString,
                )
        self.RestoreWallet = channel.unary_unary(
                '/pactus.Wallet/RestoreWallet',
                request_serializer=wallet__pb2.RestoreWalletRequest.SerializeToString,
                response_deserializer=wallet__pb2.RestoreWalletResponse.FromString,
                )
        self.LoadWallet = channel.unary_unary(
                '/pactus.Wallet/LoadWallet',
                request_serializer=wallet__pb2.LoadWalletRequest.SerializeToString,
                response_deserializer=wallet__pb2.LoadWalletResponse.FromString,
                )
        self.UnloadWallet = channel.unary_unary(
                '/pactus.Wallet/UnloadWallet',
                request_serializer=wallet__pb2.UnloadWalletRequest.SerializeToString,
                response_deserializer=wallet__pb2.UnloadWalletResponse.FromString,
                )
        self.GetTotalBalance = channel.unary_unary(
                '/pactus.Wallet/GetTotalBalance',
                request_serializer=wallet__pb2.GetTotalBalanceRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetTotalBalanceResponse.FromString,
                )
        self.SignRawTransaction = channel.unary_unary(
                '/pactus.Wallet/SignRawTransaction',
                request_serializer=wallet__pb2.SignRawTransactionRequest.SerializeToString,
                response_deserializer=wallet__pb2.SignRawTransactionResponse.FromString,
                )
        self.GetValidatorAddress = channel.unary_unary(
                '/pactus.Wallet/GetValidatorAddress',
                request_serializer=wallet__pb2.GetValidatorAddressRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetValidatorAddressResponse.FromString,
                )
        self.GetNewAddress = channel.unary_unary(
                '/pactus.Wallet/GetNewAddress',
                request_serializer=wallet__pb2.GetNewAddressRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetNewAddressResponse.FromString,
                )
        self.GetAddressHistory = channel.unary_unary(
                '/pactus.Wallet/GetAddressHistory',
                request_serializer=wallet__pb2.GetAddressHistoryRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetAddressHistoryResponse.FromString,
                )
        self.SignMessage = channel.unary_unary(
                '/pactus.Wallet/SignMessage',
                request_serializer=wallet__pb2.SignMessageRequest.SerializeToString,
                response_deserializer=wallet__pb2.SignMessageResponse.FromString,
                )
        self.GetTotalStake = channel.unary_unary(
                '/pactus.Wallet/GetTotalStake',
                request_serializer=wallet__pb2.GetTotalStakeRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetTotalStakeResponse.FromString,
                )
        self.GetAddressInfo = channel.unary_unary(
                '/pactus.Wallet/GetAddressInfo',
                request_serializer=wallet__pb2.GetAddressInfoRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetAddressInfoResponse.FromString,
                )
        self.SetAddressLabel = channel.unary_unary(
                '/pactus.Wallet/SetAddressLabel',
                request_serializer=wallet__pb2.SetLabelRequest.SerializeToString,
                response_deserializer=wallet__pb2.SetLabelResponse.FromString,
                )
        self.ListWallet = channel.unary_unary(
                '/pactus.Wallet/ListWallet',
                request_serializer=wallet__pb2.ListWalletRequest.SerializeToString,
                response_deserializer=wallet__pb2.ListWalletResponse.FromString,
                )
        self.GetWalletInfo = channel.unary_unary(
                '/pactus.Wallet/GetWalletInfo',
                request_serializer=wallet__pb2.GetWalletInfoRequest.SerializeToString,
                response_deserializer=wallet__pb2.GetWalletInfoResponse.FromString,
                )
        self.ListAddress = channel.unary_unary(
                '/pactus.Wallet/ListAddress',
                request_serializer=wallet__pb2.ListAddressRequest.SerializeToString,
                response_deserializer=wallet__pb2.ListAddressResponse.FromString,
                )


class WalletServicer(object):
    """Define the Wallet service with various RPC methods for wallet management.
    """

    def CreateWallet(self, request, context):
        """CreateWallet creates a new wallet with the specified parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RestoreWallet(self, request, context):
        """RestoreWallet restores an existing wallet with the given mnemonic.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadWallet(self, request, context):
        """LoadWallet loads an existing wallet with the given name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnloadWallet(self, request, context):
        """UnloadWallet unloads a currently loaded wallet with the specified name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTotalBalance(self, request, context):
        """GetTotalBalance returns the total available balance of the wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignRawTransaction(self, request, context):
        """SignRawTransaction signs a raw transaction for a specified wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetValidatorAddress(self, request, context):
        """GetValidatorAddress retrieves the validator address associated with a
        public key.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNewAddress(self, request, context):
        """GetNewAddress generates a new address for the specified wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAddressHistory(self, request, context):
        """GetAddressHistory retrieves the transaction history of an address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SignMessage(self, request, context):
        """SignMessage signs an arbitrary message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTotalStake(self, request, context):
        """GetTotalStake return total stake of wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAddressInfo(self, request, context):
        """GetAddressInfo return address information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAddressLabel(self, request, context):
        """SetAddressLabel set label for given address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListWallet(self, request, context):
        """ListWallet return list wallet name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetWalletInfo(self, request, context):
        """GetWalletInfo return wallet information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAddress(self, request, context):
        """ListAddress return list address in wallet.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WalletServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWallet,
                    request_deserializer=wallet__pb2.CreateWalletRequest.FromString,
                    response_serializer=wallet__pb2.CreateWalletResponse.SerializeToString,
            ),
            'RestoreWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.RestoreWallet,
                    request_deserializer=wallet__pb2.RestoreWalletRequest.FromString,
                    response_serializer=wallet__pb2.RestoreWalletResponse.SerializeToString,
            ),
            'LoadWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadWallet,
                    request_deserializer=wallet__pb2.LoadWalletRequest.FromString,
                    response_serializer=wallet__pb2.LoadWalletResponse.SerializeToString,
            ),
            'UnloadWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.UnloadWallet,
                    request_deserializer=wallet__pb2.UnloadWalletRequest.FromString,
                    response_serializer=wallet__pb2.UnloadWalletResponse.SerializeToString,
            ),
            'GetTotalBalance': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTotalBalance,
                    request_deserializer=wallet__pb2.GetTotalBalanceRequest.FromString,
                    response_serializer=wallet__pb2.GetTotalBalanceResponse.SerializeToString,
            ),
            'SignRawTransaction': grpc.unary_unary_rpc_method_handler(
                    servicer.SignRawTransaction,
                    request_deserializer=wallet__pb2.SignRawTransactionRequest.FromString,
                    response_serializer=wallet__pb2.SignRawTransactionResponse.SerializeToString,
            ),
            'GetValidatorAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetValidatorAddress,
                    request_deserializer=wallet__pb2.GetValidatorAddressRequest.FromString,
                    response_serializer=wallet__pb2.GetValidatorAddressResponse.SerializeToString,
            ),
            'GetNewAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNewAddress,
                    request_deserializer=wallet__pb2.GetNewAddressRequest.FromString,
                    response_serializer=wallet__pb2.GetNewAddressResponse.SerializeToString,
            ),
            'GetAddressHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAddressHistory,
                    request_deserializer=wallet__pb2.GetAddressHistoryRequest.FromString,
                    response_serializer=wallet__pb2.GetAddressHistoryResponse.SerializeToString,
            ),
            'SignMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.SignMessage,
                    request_deserializer=wallet__pb2.SignMessageRequest.FromString,
                    response_serializer=wallet__pb2.SignMessageResponse.SerializeToString,
            ),
            'GetTotalStake': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTotalStake,
                    request_deserializer=wallet__pb2.GetTotalStakeRequest.FromString,
                    response_serializer=wallet__pb2.GetTotalStakeResponse.SerializeToString,
            ),
            'GetAddressInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAddressInfo,
                    request_deserializer=wallet__pb2.GetAddressInfoRequest.FromString,
                    response_serializer=wallet__pb2.GetAddressInfoResponse.SerializeToString,
            ),
            'SetAddressLabel': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAddressLabel,
                    request_deserializer=wallet__pb2.SetLabelRequest.FromString,
                    response_serializer=wallet__pb2.SetLabelResponse.SerializeToString,
            ),
            'ListWallet': grpc.unary_unary_rpc_method_handler(
                    servicer.ListWallet,
                    request_deserializer=wallet__pb2.ListWalletRequest.FromString,
                    response_serializer=wallet__pb2.ListWalletResponse.SerializeToString,
            ),
            'GetWalletInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetWalletInfo,
                    request_deserializer=wallet__pb2.GetWalletInfoRequest.FromString,
                    response_serializer=wallet__pb2.GetWalletInfoResponse.SerializeToString,
            ),
            'ListAddress': grpc.unary_unary_rpc_method_handler(
                    servicer.ListAddress,
                    request_deserializer=wallet__pb2.ListAddressRequest.FromString,
                    response_serializer=wallet__pb2.ListAddressResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pactus.Wallet', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Wallet(object):
    """Define the Wallet service with various RPC methods for wallet management.
    """

    @staticmethod
    def CreateWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/CreateWallet',
            wallet__pb2.CreateWalletRequest.SerializeToString,
            wallet__pb2.CreateWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RestoreWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/RestoreWallet',
            wallet__pb2.RestoreWalletRequest.SerializeToString,
            wallet__pb2.RestoreWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/LoadWallet',
            wallet__pb2.LoadWalletRequest.SerializeToString,
            wallet__pb2.LoadWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnloadWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/UnloadWallet',
            wallet__pb2.UnloadWalletRequest.SerializeToString,
            wallet__pb2.UnloadWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTotalBalance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetTotalBalance',
            wallet__pb2.GetTotalBalanceRequest.SerializeToString,
            wallet__pb2.GetTotalBalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignRawTransaction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/SignRawTransaction',
            wallet__pb2.SignRawTransactionRequest.SerializeToString,
            wallet__pb2.SignRawTransactionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetValidatorAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetValidatorAddress',
            wallet__pb2.GetValidatorAddressRequest.SerializeToString,
            wallet__pb2.GetValidatorAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNewAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetNewAddress',
            wallet__pb2.GetNewAddressRequest.SerializeToString,
            wallet__pb2.GetNewAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAddressHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetAddressHistory',
            wallet__pb2.GetAddressHistoryRequest.SerializeToString,
            wallet__pb2.GetAddressHistoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SignMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/SignMessage',
            wallet__pb2.SignMessageRequest.SerializeToString,
            wallet__pb2.SignMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTotalStake(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetTotalStake',
            wallet__pb2.GetTotalStakeRequest.SerializeToString,
            wallet__pb2.GetTotalStakeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetAddressInfo',
            wallet__pb2.GetAddressInfoRequest.SerializeToString,
            wallet__pb2.GetAddressInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAddressLabel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/SetAddressLabel',
            wallet__pb2.SetLabelRequest.SerializeToString,
            wallet__pb2.SetLabelResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListWallet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/ListWallet',
            wallet__pb2.ListWalletRequest.SerializeToString,
            wallet__pb2.ListWalletResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetWalletInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/GetWalletInfo',
            wallet__pb2.GetWalletInfoRequest.SerializeToString,
            wallet__pb2.GetWalletInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAddress(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/pactus.Wallet/ListAddress',
            wallet__pb2.ListAddressRequest.SerializeToString,
            wallet__pb2.ListAddressResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
