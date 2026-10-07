#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"

python3 -m py_compile bitcoin-miner/mock_asic.py
python3 -m py_compile bitcoin-miner/controller.py
python3 -m py_compile bitcoin-miner/check_evidence.py

export BTC_MINER_COMMAND="python3 mock_asic.py"

echo "Anchoin Miner software clone"
echo "SIMULATION ONLY: no real ASIC, pool submission, or Bitcoin reward."

bash run_all_8.sh
