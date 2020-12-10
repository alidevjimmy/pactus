package genesis

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"time"

	"github.com/fxamacker/cbor/v2"
	"github.com/zarbchain/zarb-go/account"
	"github.com/zarbchain/zarb-go/crypto"
	"github.com/zarbchain/zarb-go/util"
	"github.com/zarbchain/zarb-go/validator"
)

// How many bytes to take from the front of the Genesis hash to append
// to the ChainName to form the ChainID. The idea is to avoid some classes
// of replay attack between chains with the same name.
const shortHashSuffixBytes = 3

// core types for a genesis definition

type genAccount struct {
	Address crypto.Address `cbor:"1,keyasint"`
	Balance int64          `cbor:"2,keyasint"`
}

type genValidator struct {
	PublicKey crypto.PublicKey `cbor:"1,keyasint"`
}

type params struct {
	BlockTimeInSecond int     `cbor:"1,keyasint"`
	MaximumPower      int     `cbor:"2,keyasint"`
	MaximumMemoLength int     `cbor:"3,keyasint"`
	FeeFraction       float64 `cbor:"4,keyasint"`
	MinimumFee        int64   `cbor:"5,keyasint"`
	TTL               int     `cbor:"6,keyasint"`
}

// Genesis is stored in the state database
type Genesis struct {
	data genesisData
}

type genesisData struct {
	ChainName   string         `cbor:"1,keyasint"`
	GenesisTime time.Time      `cbor:"2,keyasint"`
	Params      params         `cbor:"3,keyasint"`
	Accounts    []genAccount   `cbor:"4,keyasint"`
	Validators  []genValidator `cbor:"5,keyasint"`
}

func (gen *Genesis) Hash() crypto.Hash {
	bs, err := cbor.Marshal(gen.data)
	if err != nil {
		panic(fmt.Errorf("could not create hash of Genesis: %v", err))
	}
	return crypto.HashH(bs)
}

func (gen *Genesis) ChainName() string {
	return gen.data.ChainName
}

func (gen *Genesis) GenesisTime() time.Time {
	return gen.data.GenesisTime
}

func (gen *Genesis) BlockTime() time.Duration {
	return time.Duration(gen.data.Params.BlockTimeInSecond) * time.Second
}

func (gen *Genesis) MaximumPower() int {
	return gen.data.Params.MaximumPower
}

func (gen *Genesis) MaximumMemoLength() int {
	return gen.data.Params.MaximumMemoLength
}

func (gen *Genesis) FeeFraction() float64 {
	return gen.data.Params.FeeFraction
}

func (gen *Genesis) MinimumFee() int64 {
	return gen.data.Params.MinimumFee
}

func (gen *Genesis) TTL() int {
	return gen.data.Params.TTL
}

func (gen *Genesis) Accounts() []*account.Account {
	accs := make([]*account.Account, 0)
	for _, genAcc := range gen.data.Accounts {
		acc := account.NewAccount(genAcc.Address)
		acc.AddToBalance(genAcc.Balance)
		accs = append(accs, acc)
	}

	return accs
}

func (gen *Genesis) Validators() []*validator.Validator {
	vals := make([]*validator.Validator, 0, len(gen.data.Validators))
	for _, genVal := range gen.data.Validators {
		val := validator.NewValidator(genVal.PublicKey, 0)
		vals = append(vals, val)
	}

	return vals
}

func (gen Genesis) MarshalJSON() ([]byte, error) {
	return json.Marshal(&gen.data)
}

func (gen *Genesis) UnmarshalJSON(bs []byte) error {
	return json.Unmarshal(bs, &gen.data)
}

func makeGenesisAccount(acc *account.Account) genAccount {
	return genAccount{
		Address: acc.Address(),
		Balance: acc.Balance(),
	}
}

func makeGenesisValidator(val *validator.Validator) genValidator {
	return genValidator{
		PublicKey: val.PublicKey(),
	}
}

func MakeGenesis(chainName string, genesisTime time.Time,
	accounts []*account.Account,
	validators []*validator.Validator, blockTime int) *Genesis {

	genAccs := make([]genAccount, 0, len(accounts))
	for _, acc := range accounts {
		genAcc := makeGenesisAccount(acc)
		genAccs = append(genAccs, genAcc)
	}

	genVals := make([]genValidator, 0, len(validators))
	for _, val := range validators {
		genVal := makeGenesisValidator(val)
		genVals = append(genVals, genVal)
	}

	return &Genesis{
		data: genesisData{
			ChainName:   chainName,
			GenesisTime: genesisTime,
			Accounts:    genAccs,
			Validators:  genVals,
			Params: params{
				BlockTimeInSecond: blockTime,
				MaximumPower:      5,
				MaximumMemoLength: 1024,
				FeeFraction:       0.001,
				MinimumFee:        1000,
				TTL:               500,
			},
		},
	}
}

// LoadFromFile loads genesis object from a JSON file
func LoadFromFile(file string) (*Genesis, error) {
	dat, err := ioutil.ReadFile(file)
	if err != nil {
		return nil, err
	}
	var gen Genesis
	if err := json.Unmarshal(dat, &gen); err != nil {
		return nil, err
	}
	return &gen, nil
}

// SaveToFile saves the genesis info a JSON file
func (gen *Genesis) SaveToFile(file string) error {
	json, err := gen.MarshalJSON()
	if err != nil {
		return err
	}

	// write  dataContent to file
	if err := util.WriteFile(file, json); err != nil {
		return err
	}

	return nil
}
