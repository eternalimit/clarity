# Anchoin Miner Physical Connection

## Connection chain

`Controller host -> Ethernet/LAN -> ASIC/miner -> Stratum pool -> Bitcoin network -> receipt -> Echo -> TCGE`

## 1. Physical layer

1. Connect the ASIC/miner to its manufacturer-rated power source.
2. Connect the miner's Ethernet port to your LAN/router.
3. Keep the controller computer on a network that can reach the miner.
4. Find the miner's LAN hostname or IP from the router or miner management interface.

Follow the miner manufacturer's electrical, cooling, and installation requirements. Do not improvise mains-power wiring.

## 2. Pool layer

Obtain these values from the mining pool you choose:

- Stratum endpoint and port
- Worker/account name
- Worker password only if the pool requires one

Never store wallet private keys or seed phrases in this repository.

## 3. Anchoin environment

Example placeholders:

```bash
export ANCHOIN_MINER_HOST="192.0.2.10"
export ANCHOIN_POOL_URL="stratum+tcp://pool.example:3333"
```

Run the network preflight:

```bash
python3 bitcoin-miner/physical_preflight.py
```

PASS means only that the configured miner host resolves and the pool TCP endpoint can be reached. It does not prove the ASIC is hashing or that the pool accepted work.

## 4. Execution adapter

Set the existing controller interface to the legitimate miner software command installed on the controller/miner host:

```bash
export BTC_MINER_COMMAND="/path/to/miner --url $ANCHOIN_POOL_URL --user <worker>"
bash run_all_8.sh
```

Use the exact command-line syntax documented by your miner software or manufacturer. Do not guess flags.

## 5. Proof boundary

Required progression:

`physical connection -> miner running -> pool connection -> accepted share/block evidence -> independent network/pool Echo -> TCGE`

Physical connectivity alone remains HOLD for the claim that Bitcoin was mined.

Signed: Richard Stein

Digest:
Physical miner connection contract created without embedding credentials or claiming unobserved hardware execution.

Index Handoff:
ANCHOIN_MINER_PHYSICAL_CONNECT
