package vote

import (
	"fmt"

	"github.com/fxamacker/cbor/v2"
)

type CPValue int8

const (
	CPValueNo      = CPValue(0)
	CPValueYes     = CPValue(1)
	CPValueAbstain = CPValue(2)
)

func (v CPValue) String() string {
	switch v {
	case CPValueNo:
		return "no"
	case CPValueYes:
		return "yes"
	case CPValueAbstain:
		return "abstain"
	default:
		return fmt.Sprintf("unknown: %d", v)
	}
}

type cpVote struct {
	Round int16
	Value CPValue
	Just  Just
}

func (v *cpVote) BasicCheck() error {
	if v.Round < 0 {
		return BasicCheckError{
			Reason: "invalid CP round",
		}
	}
	if v.Value < CPValueNo ||
		v.Value > CPValueAbstain {
		// Invalid values
		return BasicCheckError{
			Reason: "invalid CP value",
		}
	}

	return v.Just.BasicCheck()
}

type _cpVote struct {
	Round    int16    `cbor:"1,keyasint"`
	Value    CPValue  `cbor:"2,keyasint"`
	JustType JustType `cbor:"3,keyasint"`
	JustData []byte   `cbor:"4,keyasint"`
}

type _JustMainVoteConflict struct {
	Just0Type JustType `cbor:"1,keyasint"`
	Just0Data []byte   `cbor:"2,keyasint"`
	Just1Type JustType `cbor:"3,keyasint"`
	Just1Data []byte   `cbor:"4,keyasint"`
}

// MarshalCBOR encodes the cpVote into CBOR format.
func (v *cpVote) MarshalCBOR() ([]byte, error) {
	justData := []byte{}
	if v.Just.Type() == JustTypeMainVoteConflict {
		conflictJust := v.Just.(*JustMainVoteConflict)
		data0, err := cbor.Marshal(conflictJust.JustNo)
		if err != nil {
			return nil, err
		}
		data1, err := cbor.Marshal(conflictJust.JustYes)
		if err != nil {
			return nil, err
		}

		_conflictingJust := _JustMainVoteConflict{
			Just0Type: conflictJust.JustNo.Type(),
			Just0Data: data0,
			Just1Type: conflictJust.JustYes.Type(),
			Just1Data: data1,
		}
		data, err := cbor.Marshal(_conflictingJust)
		if err != nil {
			return nil, err
		}
		justData = append(justData, data...)
	} else {
		data, err := cbor.Marshal(v.Just)
		if err != nil {
			return nil, err
		}
		justData = append(justData, data...)
	}

	msg := &_cpVote{
		Round:    v.Round,
		Value:    v.Value,
		JustType: v.Just.Type(),
		JustData: justData,
	}

	return cbor.Marshal(msg)
}

// UnmarshalCBOR decodes the cpVote from CBOR format.
func (v *cpVote) UnmarshalCBOR(bs []byte) error {
	var _cp _cpVote
	err := cbor.Unmarshal(bs, &_cp)
	if err != nil {
		return err
	}

	var just Just
	if _cp.JustType == JustTypeMainVoteConflict {
		_conflictingJust := &_JustMainVoteConflict{}
		err := cbor.Unmarshal(_cp.JustData, _conflictingJust)
		if err != nil {
			return err
		}

		just0 := makeJust(_conflictingJust.Just0Type)
		err = cbor.Unmarshal(_conflictingJust.Just0Data, just0)
		if err != nil {
			return err
		}

		just1 := makeJust(_conflictingJust.Just1Type)
		err = cbor.Unmarshal(_conflictingJust.Just1Data, just1)
		if err != nil {
			return err
		}

		just = &JustMainVoteConflict{
			JustNo:  just0,
			JustYes: just1,
		}
	} else {
		just = makeJust(_cp.JustType)
		err := cbor.Unmarshal(_cp.JustData, just)
		if err != nil {
			return err
		}
	}

	v.Round = _cp.Round
	v.Value = _cp.Value
	v.Just = just

	return nil
}
