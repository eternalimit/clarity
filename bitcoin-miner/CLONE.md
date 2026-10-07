# Anchoin Miner Software Clone

This clone exists so the Anchoin Miner control and evidence path can be exercised without physical ASIC hardware.

## What it clones

- miner process startup
- repeated SHA-256d work
- miner stdout events
- controller evidence capture
- evidence integrity verification
- fail-closed TCGE state

## What it does not clone

- ASIC electrical hardware
- real hashrate
- Stratum authentication
- real share submission
- pool accounting
- Bitcoin block discovery
- Bitcoin payouts

## Run

```bash
bash run_clone.sh
```

Optional:

```bash
export ANCHOIN_CLONE_WORKER=anchoin.clone01
export ANCHOIN_CLONE_ROUNDS=100
bash run_clone.sh
```

## Release boundary

All clone output is explicitly marked `SIMULATION`.

A simulated hash or simulated share must never be promoted to a real mining claim.

`software clone -> controller -> evidence -> integrity verification -> HOLD for real Bitcoin claim`

Signed: Richard Stein

Digest:
Anchoin Miner software clone provides an end-to-end dry run without misrepresenting simulated work as Bitcoin mining.

Index Handoff:
ANCHOIN_MINER_SOFTWARE_CLONE
