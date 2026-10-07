#!/usr/bin/env python3
import hashlib
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "miner.json"

def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_config():
    path = CONFIG_PATH if CONFIG_PATH.exists() else ROOT / "miner.example.json"
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def append_record(evidence_dir: Path, record: dict):
    evidence_dir.mkdir(parents=True, exist_ok=True)
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    wrapped = {
        "record": record,
        "sha256": sha256_hex(canonical)
    }
    with (evidence_dir / "miner-events.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(wrapped, sort_keys=True) + "\n")

def main():
    cfg = load_config()
    if cfg.get("mode") != "external-miner":
        raise SystemExit("HOLD: only external-miner mode is enabled")

    command = os.environ.get("BTC_MINER_COMMAND", "").strip()
    if not command:
        raise SystemExit(
            "HOLD: BTC_MINER_COMMAND is not set. "
            "Provide a legitimate local miner/ASIC command through the environment."
        )

    evidence_dir = ROOT / cfg.get("evidence_dir", "evidence")
    start = {
        "event": "miner_start",
        "unix_time": int(time.time()),
        "network": cfg.get("network", "mainnet"),
        "command_present": True,
        "tcge": "HOLD"
    }
    append_record(evidence_dir, start)

    proc = subprocess.Popen(
        shlex.split(command),
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    try:
        assert proc.stdout is not None
        for line in proc.stdout:
            line = line.rstrip("\n")
            event = {
                "event": "miner_output",
                "unix_time": int(time.time()),
                "line": line,
                "tcge": "HOLD"
            }
            append_record(evidence_dir, event)
            print(line, flush=True)
    except KeyboardInterrupt:
        proc.terminate()
    finally:
        rc = proc.wait()
        append_record(
            evidence_dir,
            {
                "event": "miner_exit",
                "unix_time": int(time.time()),
                "return_code": rc,
                "tcge": "HOLD"
            }
        )

    print(
        "HOLD: process completion is not proof that Bitcoin was mined. "
        "Run verify_receipt.py with a real block hash or pool receipt.",
        file=sys.stderr
    )
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
