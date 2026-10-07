#!/usr/bin/env python3
import hashlib
import json
import os
import sys
import time

def sha256d(data: bytes) -> str:
    return hashlib.sha256(hashlib.sha256(data).digest()).hexdigest()

def main():
    worker = os.environ.get("ANCHOIN_CLONE_WORKER", "anchoin.clone")
    rounds = int(os.environ.get("ANCHOIN_CLONE_ROUNDS", "20"))
    if rounds < 1 or rounds > 100000:
        raise SystemExit("HOLD: ANCHOIN_CLONE_ROUNDS out of range")

    print(json.dumps({
        "mode":"SIMULATION",
        "device":"ANCHOIN_SOFTWARE_CLONE",
        "worker":worker,
        "claim_boundary":"NOT_REAL_BITCOIN_MINING",
        "tcge":"HOLD"
    }), flush=True)

    accepted = 0
    for nonce in range(rounds):
        payload = f"anchoin-clone|{worker}|{nonce}".encode()
        digest = sha256d(payload)
        simulated_share = digest.startswith("00")
        if simulated_share:
            accepted += 1
        print(json.dumps({
            "event":"simulated_hash",
            "nonce":nonce,
            "sha256d":digest,
            "simulated_share":simulated_share,
            "real_network_submission":False,
            "tcge":"HOLD"
        }), flush=True)
        time.sleep(0.01)

    print(json.dumps({
        "event":"clone_complete",
        "rounds":rounds,
        "simulated_shares":accepted,
        "real_btc_mined":0,
        "tcge":"HOLD"
    }), flush=True)
    return 0

if __name__=="__main__":
    sys.exit(main())
