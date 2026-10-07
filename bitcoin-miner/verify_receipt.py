#!/usr/bin/env python3
import argparse
import hashlib
import json
import re
import sys
import urllib.request

BLOCK_HASH_RE = re.compile(r"^[0-9a-fA-F]{64}$")

def fetch_json(url: str):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "clarity-tcge-bitcoin-verifier/1.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read().decode("utf-8"))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--block-hash", required=True)
    p.add_argument(
        "--echo-url",
        default="https://blockstream.info/api/block/"
    )
    args = p.parse_args()

    h = args.block_hash.lower()
    if not BLOCK_HASH_RE.fullmatch(h):
        raise SystemExit("HOLD: invalid 32-byte block hash")

    url = args.echo_url.rstrip("/") + "/" + h
    try:
        data = fetch_json(url)
    except Exception as exc:
        raise SystemExit(f"HOLD: Echo lookup failed: {exc}")

    returned_id = str(data.get("id", "")).lower()
    height = data.get("height")
    timestamp = data.get("timestamp")

    record = {
        "claim": "bitcoin_block_exists",
        "block_hash": h,
        "echo_source": url,
        "echo_returned_id": returned_id,
        "height": height,
        "timestamp": timestamp,
        "R": int(returned_id == h),
        "I": 1,
        "E": int(returned_id == h)
    }
    record["K"] = record["R"] & record["I"] & record["E"]
    record["status"] = "PASS" if record["K"] else "HOLD"
    canonical = json.dumps(record, sort_keys=True, separators=(",", ":")).encode()
    record["record_sha256"] = hashlib.sha256(canonical).hexdigest()

    print(json.dumps(record, indent=2, sort_keys=True))
    return 0 if record["K"] else 2

if __name__ == "__main__":
    sys.exit(main())
