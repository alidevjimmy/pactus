package sortition

import (
	"math/big"

	"github.com/zarbchain/zarb-go/crypto"
	"github.com/zarbchain/zarb-go/crypto/bls"
	"github.com/zarbchain/zarb-go/crypto/hash"
	"github.com/zarbchain/zarb-go/util"
)

// evaluate returns a random number between 0 and max with the proof.
func evaluate(seed VerifiableSeed, signer crypto.Signer, max uint64) (index uint64, proof Proof) {
	signData := append(seed[:], signer.PublicKey().Bytes()...)
	sig := signer.SignData(signData)

	proof, _ = ProofFromBytes(sig.Bytes())
	index = getIndex(proof, max)

	return index, proof
}

// verify ensures the proof is valid.
func verify(seed VerifiableSeed, publicKey crypto.PublicKey, proof Proof, max uint64) (index uint64, result bool) {
	proofSig, err := bls.SignatureFromBytes(proof[:])
	if err != nil {
		return 0, false
	}

	// Verify signature (proof)
	signData := append(seed[:], publicKey.Bytes()...)
	if err := publicKey.Verify(signData, proofSig); err != nil {
		return 0, false
	}

	index = getIndex(proof, max)

	return index, true
}

func getIndex(proof Proof, max uint64) uint64 {
	h := hash.CalcHash(proof[:])

	rnd64 := util.SliceToUint64(h.Bytes())

	// construct the numerator and denominator for normalizing the proof uint
	bigRnd := &big.Int{}
	bigMax := &big.Int{}
	denominator := &big.Int{}
	numerator := &big.Int{}

	bigRnd.SetUint64(rnd64)
	bigMax.SetUint64(max)
	denominator.SetUint64(util.MaxUint64)

	numerator = numerator.Mul(bigRnd, bigMax)

	// divide numerator and denominator to get the election ratio for this block height
	index := big.NewInt(0)
	index = index.Div(numerator, denominator)

	return index.Uint64()
}
