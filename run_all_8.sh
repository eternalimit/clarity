#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

echo "Anchoin Miner preflight"

python3 -m py_compile bitcoin-miner/controller.py
python3 -m py_compile bitcoin-miner/check_evidence.py
python3 -m py_compile bitcoin-miner/verify_receipt.py

if [ -z "${BTC_MINER_COMMAND:-}" ]; then
  echo "HOLD: BTC_MINER_COMMAND is not set."
  echo "Set it to the legitimate miner command on the machine connected to your ASIC or mining software."
  exit 2
fi

echo "Controller ready. Starting external miner..."
set +e
python3 bitcoin-miner/controller.py
rc=$?
set -e

if [ -f bitcoin-miner/evidence/miner-events.jsonl ]; then
  echo "Checking evidence integrity..."
  python3 bitcoin-miner/check_evidence.py
else
  echo "HOLD: no evidence file was produced."
fi

echo "TCGE HOLD: mining process output is not proof that a Bitcoin block was mined."
echo "Use verify_receipt.py with a real block hash for independent network verification."

exit "$rc"
