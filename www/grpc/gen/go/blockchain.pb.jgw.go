// Code generated by protoc-gen-jsonrpc-gateway. DO NOT EDIT.
// source: blockchain.proto

/*
Package pactus is a reverse proxy.

It translates gRPC into JSON-RPC 2.0
*/
package pactus

import (
	"context"
	"encoding/json"

	"google.golang.org/protobuf/encoding/protojson"
)

type BlockchainJsonRpcService struct {
	client    	BlockchainClient
}

func NewBlockchainJsonRpcService(client BlockchainClient) BlockchainJsonRpcService {
	return BlockchainJsonRpcService {
		client: client,
	}
}

func (s *BlockchainJsonRpcService) Methods() map[string]func(ctx context.Context, params json.RawMessage) (interface{}, error) {
	return map[string]func(ctx context.Context, params json.RawMessage) (interface{}, error){

		"pactus.blockchain.get_block": func(ctx context.Context, params json.RawMessage) (interface{}, error) {
			in := new(GetBlockRequest)
			err := protojson.Unmarshal(params, in)
			if err != nil {
				return nil, err
			}
			return s.client.GetBlock(ctx, in)
		},

		"pactus.blockchain.get_block_hash": func(ctx context.Context, params json.RawMessage) (interface{}, error) {
			in := new(GetBlockHashRequest)
			err := protojson.Unmarshal(params, in)
			if err != nil {
				return nil, err
			}
			return s.client.GetBlockHash(ctx, in)
		},
	}
}
