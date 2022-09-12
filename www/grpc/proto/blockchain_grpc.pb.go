// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             (unknown)
// source: blockchain.proto

package pactus

import (
	context "context"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// BlockchainClient is the client API for Blockchain service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type BlockchainClient interface {
	GetBlock(ctx context.Context, in *BlockRequest, opts ...grpc.CallOption) (*BlockResponse, error)
	GetBlockHash(ctx context.Context, in *BlockHashRequest, opts ...grpc.CallOption) (*BlockHashResponse, error)
	GetAccount(ctx context.Context, in *AccountRequest, opts ...grpc.CallOption) (*AccountResponse, error)
	GetValidators(ctx context.Context, in *ValidatorsRequest, opts ...grpc.CallOption) (*ValidatorsResponse, error)
	GetValidator(ctx context.Context, in *ValidatorRequest, opts ...grpc.CallOption) (*ValidatorResponse, error)
	GetValidatorByNumber(ctx context.Context, in *ValidatorByNumberRequest, opts ...grpc.CallOption) (*ValidatorResponse, error)
	GetBlockchainInfo(ctx context.Context, in *BlockchainInfoRequest, opts ...grpc.CallOption) (*BlockchainInfoResponse, error)
}

type blockchainClient struct {
	cc grpc.ClientConnInterface
}

func NewBlockchainClient(cc grpc.ClientConnInterface) BlockchainClient {
	return &blockchainClient{cc}
}

func (c *blockchainClient) GetBlock(ctx context.Context, in *BlockRequest, opts ...grpc.CallOption) (*BlockResponse, error) {
	out := new(BlockResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetBlock", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetBlockHash(ctx context.Context, in *BlockHashRequest, opts ...grpc.CallOption) (*BlockHashResponse, error) {
	out := new(BlockHashResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetBlockHash", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetAccount(ctx context.Context, in *AccountRequest, opts ...grpc.CallOption) (*AccountResponse, error) {
	out := new(AccountResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetAccount", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetValidators(ctx context.Context, in *ValidatorsRequest, opts ...grpc.CallOption) (*ValidatorsResponse, error) {
	out := new(ValidatorsResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetValidators", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetValidator(ctx context.Context, in *ValidatorRequest, opts ...grpc.CallOption) (*ValidatorResponse, error) {
	out := new(ValidatorResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetValidator", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetValidatorByNumber(ctx context.Context, in *ValidatorByNumberRequest, opts ...grpc.CallOption) (*ValidatorResponse, error) {
	out := new(ValidatorResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetValidatorByNumber", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *blockchainClient) GetBlockchainInfo(ctx context.Context, in *BlockchainInfoRequest, opts ...grpc.CallOption) (*BlockchainInfoResponse, error) {
	out := new(BlockchainInfoResponse)
	err := c.cc.Invoke(ctx, "/pactus.Blockchain/GetBlockchainInfo", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// BlockchainServer is the server API for Blockchain service.
// All implementations should embed UnimplementedBlockchainServer
// for forward compatibility
type BlockchainServer interface {
	GetBlock(context.Context, *BlockRequest) (*BlockResponse, error)
	GetBlockHash(context.Context, *BlockHashRequest) (*BlockHashResponse, error)
	GetAccount(context.Context, *AccountRequest) (*AccountResponse, error)
	GetValidators(context.Context, *ValidatorsRequest) (*ValidatorsResponse, error)
	GetValidator(context.Context, *ValidatorRequest) (*ValidatorResponse, error)
	GetValidatorByNumber(context.Context, *ValidatorByNumberRequest) (*ValidatorResponse, error)
	GetBlockchainInfo(context.Context, *BlockchainInfoRequest) (*BlockchainInfoResponse, error)
}

// UnimplementedBlockchainServer should be embedded to have forward compatible implementations.
type UnimplementedBlockchainServer struct {
}

func (UnimplementedBlockchainServer) GetBlock(context.Context, *BlockRequest) (*BlockResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetBlock not implemented")
}
func (UnimplementedBlockchainServer) GetBlockHash(context.Context, *BlockHashRequest) (*BlockHashResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetBlockHash not implemented")
}
func (UnimplementedBlockchainServer) GetAccount(context.Context, *AccountRequest) (*AccountResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetAccount not implemented")
}
func (UnimplementedBlockchainServer) GetValidators(context.Context, *ValidatorsRequest) (*ValidatorsResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetValidators not implemented")
}
func (UnimplementedBlockchainServer) GetValidator(context.Context, *ValidatorRequest) (*ValidatorResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetValidator not implemented")
}
func (UnimplementedBlockchainServer) GetValidatorByNumber(context.Context, *ValidatorByNumberRequest) (*ValidatorResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetValidatorByNumber not implemented")
}
func (UnimplementedBlockchainServer) GetBlockchainInfo(context.Context, *BlockchainInfoRequest) (*BlockchainInfoResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetBlockchainInfo not implemented")
}

// UnsafeBlockchainServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to BlockchainServer will
// result in compilation errors.
type UnsafeBlockchainServer interface {
	mustEmbedUnimplementedBlockchainServer()
}

func RegisterBlockchainServer(s grpc.ServiceRegistrar, srv BlockchainServer) {
	s.RegisterService(&Blockchain_ServiceDesc, srv)
}

func _Blockchain_GetBlock_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BlockRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetBlock(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetBlock",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetBlock(ctx, req.(*BlockRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetBlockHash_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BlockHashRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetBlockHash(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetBlockHash",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetBlockHash(ctx, req.(*BlockHashRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetAccount_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(AccountRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetAccount(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetAccount",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetAccount(ctx, req.(*AccountRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetValidators_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ValidatorsRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetValidators(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetValidators",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetValidators(ctx, req.(*ValidatorsRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetValidator_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ValidatorRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetValidator(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetValidator",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetValidator(ctx, req.(*ValidatorRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetValidatorByNumber_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ValidatorByNumberRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetValidatorByNumber(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetValidatorByNumber",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetValidatorByNumber(ctx, req.(*ValidatorByNumberRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Blockchain_GetBlockchainInfo_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(BlockchainInfoRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(BlockchainServer).GetBlockchainInfo(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/pactus.Blockchain/GetBlockchainInfo",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(BlockchainServer).GetBlockchainInfo(ctx, req.(*BlockchainInfoRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Blockchain_ServiceDesc is the grpc.ServiceDesc for Blockchain service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Blockchain_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "pactus.Blockchain",
	HandlerType: (*BlockchainServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetBlock",
			Handler:    _Blockchain_GetBlock_Handler,
		},
		{
			MethodName: "GetBlockHash",
			Handler:    _Blockchain_GetBlockHash_Handler,
		},
		{
			MethodName: "GetAccount",
			Handler:    _Blockchain_GetAccount_Handler,
		},
		{
			MethodName: "GetValidators",
			Handler:    _Blockchain_GetValidators_Handler,
		},
		{
			MethodName: "GetValidator",
			Handler:    _Blockchain_GetValidator_Handler,
		},
		{
			MethodName: "GetValidatorByNumber",
			Handler:    _Blockchain_GetValidatorByNumber_Handler,
		},
		{
			MethodName: "GetBlockchainInfo",
			Handler:    _Blockchain_GetBlockchainInfo_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "blockchain.proto",
}