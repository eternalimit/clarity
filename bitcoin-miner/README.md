# Bitcoin Miner Control Plane

This module is for **real Bitcoin mining orchestration and evidence capture**.

It does not claim that GitHub itself mines Bitcoin. GitHub stores code, configuration, logs, and verification records. Actual proof-of-work must be performed by mining hardware/software outside GitHub.

## Architecture

Gethub / GitHub
-> CONFIG
-> MINER PROCESS
-> STRATUM POOL or BITCOIN NODE
-> HASH WORK
-> SHARE / BLOCK RECEIPT
-> ECHO VERIFY
-> TCGE

## TCGE rule

R = direct mining/network evidence
I = claim that a share or block was found
E = independent verification from a second source

K = R AND I AND E

Without a valid network receipt and independent verification: HOLD.

## Requirements

- Python 3.11+
- A legitimate Bitcoin mining program or ASIC controller
- Your own pool URL / worker credentials, or your own Bitcoin Core node
- Never commit wallet private keys, seed phrases, API secrets, or pool passwords

## Configuration

Copy:

```
cp miner.example.json miner.json
```

Set your external miner command using environment variables. Example:

```
export BTC_MINER_COMMAND="/path/to/your/miner --url stratum+tcp://POOL:PORT --user WORKER --pass x"
python3 controller.py
```

The controller launches the configured external miner, timestamps stdout/stderr, computes SHA-256 digests of evidence records, and writes JSONL receipts under `evidence/`.

## Important

This repository must never report "BTC mined" merely because:
- a local hash was computed,
- a simulated nonce matched a toy target,
- a process exited successfully,
- a pool connection was opened.

A Bitcoin block is considered validated only when a real block hash is independently confirmed on the Bitcoin network.

Signed: Richard Stein

Digest:
GitHub controls -> external miner works -> receipt -> independent Echo -> PASS/HOLD

Index Handoff:
BITCOIN_MINER_CONTROL_PLANE
