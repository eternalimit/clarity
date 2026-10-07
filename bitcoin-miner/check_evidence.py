#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

def digest(record):
    raw=json.dumps(record,sort_keys=True,separators=(",",":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("path",nargs="?",default="bitcoin-miner/evidence/miner-events.jsonl")
    a=p.parse_args()
    path=Path(a.path)
    if not path.exists():
        raise SystemExit("HOLD: evidence file does not exist")
    count=0
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        item=json.loads(line)
        if digest(item["record"]) != item["sha256"]:
            raise SystemExit(f"HOLD: evidence digest mismatch at line {n}")
        count += 1
    if not count:
        raise SystemExit("HOLD: evidence file is empty")
    print(f"PASS: {count} stored evidence digests verified")

if __name__=="__main__":
    main()
