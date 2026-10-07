# Anchoin Miner

Anchoin Miner is the local execution and evidence layer for the Bitcoin mining controller in this repository.

GitHub stores the control code and evidence logic. Real proof-of-work must be performed by legitimate external mining hardware or mining software.

## Main branch quick start

Clone and enter the repository:

```bash
git clone https://github.com/eternalimit/clarity.git
cd clarity
git checkout main
```

Configure the command that launches your legitimate miner on the local machine:

```bash
export BTC_MINER_COMMAND="/path/to/miner <your miner arguments>"
```

Do not place wallet private keys or seed phrases in this variable or repository.

Run the complete local control path:

```bash
bash run_all_8.sh
```

The launcher performs Python syntax checks, starts the existing external-miner controller, records SHA-256-bound evidence, and checks the stored evidence integrity.

## Verification

Evidence integrity:

```bash
python3 bitcoin-miner/check_evidence.py
```

Independent Bitcoin block lookup:

```bash
python3 bitcoin-miner/verify_receipt.py --block-hash <64-hex-block-hash>
```

A running miner, a successful process, or an accepted pool share is not by itself proof that a Bitcoin block was mined. The exact block claim remains HOLD until independently verified.

## State chain

`main -> run_all_8.sh -> controller.py -> external miner -> evidence -> check_evidence.py -> verify_receipt.py -> TCGE`

Signed: Richard Stein

Digest:
Anchoin Miner main execution path established with fail-closed verification.

Index Handoff:
ANCHOIN_MINER_MAIN
