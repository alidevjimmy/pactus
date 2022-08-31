package payload

import (
	"io"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/zarbchain/zarb-go/crypto"
	"github.com/zarbchain/zarb-go/util"
	"github.com/zarbchain/zarb-go/util/errors"
)

func TestSendType(t *testing.T) {
	pld := SendPayload{}
	assert.Equal(t, pld.Type(), PayloadTypeSend)
}

func TestSendDecoding(t *testing.T) {
	tests := []struct {
		raw       []byte
		value     int64
		readErr   error
		sanityErr error
	}{
		{
			raw:       []byte{},
			value:     0,
			readErr:   io.EOF,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
				0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10,
				0x11, 0x12, 0x13, 0x14, // sender
			},
			value:     0,
			readErr:   io.EOF,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x00, // sender
				0x01, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, // receiver
			},
			value:     0,
			readErr:   io.EOF,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x00, // sender
				0x01, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, 0x25, // receiver
				0x80, 0x80, 0x80, // amount
			},
			value:     0,
			readErr:   io.EOF,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x02, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
				0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10,
				0x11, 0x12, 0x13, 0x14, 0x15, // sender
				0x01, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, 0x25, // receiver
				0x80, 0x80, 0x80, 0x01, // amount
			},
			value:     0x200000,
			readErr:   nil,
			sanityErr: errors.Error(errors.ErrInvalidAddress),
		},
		{
			raw: []byte{
				0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
				0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10,
				0x11, 0x12, 0x13, 0x14, 0x15, // sender
				0x02, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, 0x25, // receiver
				0x80, 0x80, 0x80, 0x01, // amount
			},
			value:     0x200000,
			readErr:   nil,
			sanityErr: errors.Error(errors.ErrInvalidAddress),
		},
		{
			raw: []byte{
				0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
				0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10,
				0x11, 0x12, 0x13, 0x14, 0x15, // sender
				0x01, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, 0x25, // receiver
				0x80, 0x80, 0x80, 0x01, // amount
			},
			value:     0x200000,
			readErr:   nil,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x00, // sender
				0x01, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18,
				0x19, 0x1A, 0x1B, 0x1C, 0x1D, 0x1E, 0x1F, 0x20,
				0x21, 0x12, 0x23, 0x24, 0x25, // receiver
				0x80, 0x80, 0x80, 0x01, // amount
			},
			value:     0x200000,
			readErr:   nil,
			sanityErr: nil,
		},
		{
			raw: []byte{
				0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08,
				0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10,
				0x11, 0x12, 0x13, 0x14, 0x15, // sender
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
				0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
				0x00, 0x00, 0x00, 0x00, 0x00, // receiver
				0x00, // amount
			},
			value:     0x0,
			readErr:   nil,
			sanityErr: nil,
		},
	}

	for n, test := range tests {
		pld := SendPayload{}
		r := util.NewFixedReader(len(test.raw), test.raw)
		err := pld.Decode(r)
		if test.readErr != nil {
			assert.Error(t, err)
		} else {
			assert.NoError(t, err)

			for i := 0; i < pld.SerializeSize(); i++ {
				w := util.NewFixedWriter(i)
				assert.Error(t, pld.Encode(w), "encode test %v failed", n)
			}
			w := util.NewFixedWriter(pld.SerializeSize())
			assert.NoError(t, pld.Encode(w))
			assert.Equal(t, len(w.Bytes()), pld.SerializeSize())
			assert.Equal(t, w.Bytes(), test.raw)

			// Sanity check
			if test.sanityErr != nil {
				assert.ErrorIs(t, pld.SanityCheck(), test.sanityErr)
			} else {
				assert.NoError(t, pld.SanityCheck())

				// Check signer
				if test.raw[0] != 0 {
					assert.Equal(t, pld.Signer().Bytes(), test.raw[:21])
				} else {
					assert.Equal(t, pld.Signer(), crypto.TreasuryAddress)
				}
				// Check amount
				assert.Equal(t, pld.Value(), test.value)
			}
		}
	}
}
