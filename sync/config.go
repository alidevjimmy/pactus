package sync

import (
	"time"

	"github.com/pactus-project/pactus/sync/firewall"
	"github.com/pactus-project/pactus/sync/peerset/peer/service"
	"github.com/pactus-project/pactus/util"
	"github.com/pactus-project/pactus/version"
)

type Config struct {
	Moniker        string           `toml:"moniker"`
	SessionTimeout time.Duration    `toml:"session_timeout"`
	Firewall       *firewall.Config `toml:"firewall"`

	// Private configs
	MaxSessions         int              `toml:"-"`
	BlockPerSession     uint32           `toml:"-"`
	BlockPerMessage     uint32           `toml:"-"`
	PruneWindow         uint32           `toml:"-"`
	LatestSupportingVer version.Version  `toml:"-"`
	Services            service.Services `toml:"-"`
}

func DefaultConfig() *Config {
	return &Config{
		SessionTimeout:  time.Second * 10,
		Services:        service.New(service.PrunedNode),
		MaxSessions:     8,
		BlockPerSession: 720,
		BlockPerMessage: 60,
		PruneWindow:     86_400, // Default retention blocks in prune mode
		Firewall:        firewall.DefaultConfig(),
		// v1.5.0 is the hard-fork for Ed25519 support.
		LatestSupportingVer: version.Version{
			Major: 1,
			Minor: 5,
			Patch: 0,
		},
	}
}

// BasicCheck performs basic checks on the configuration.
func (conf *Config) BasicCheck() error {
	return conf.Firewall.BasicCheck()
}

func (conf *Config) CacheSize() int {
	return util.LogScale(
		int(conf.BlockPerMessage * conf.BlockPerSession))
}
