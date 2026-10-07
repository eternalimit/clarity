#!/usr/bin/env python3
import os
import socket
import sys
from urllib.parse import urlparse

def hold(message):
    print("HOLD:", message)
    return 2

def main():
    host=os.environ.get("ANCHOIN_MINER_HOST","").strip()
    pool=os.environ.get("ANCHOIN_POOL_URL","").strip()

    if not host:
        return hold("ANCHOIN_MINER_HOST is not set")
    if not pool:
        return hold("ANCHOIN_POOL_URL is not set")

    parsed=urlparse(pool)
    if parsed.scheme not in ("stratum+tcp","stratum+ssl"):
        return hold("pool URL must use stratum+tcp or stratum+ssl")
    if not parsed.hostname or parsed.port is None:
        return hold("pool URL must include hostname and port")

    try:
        socket.getaddrinfo(host, None)
    except OSError as exc:
        return hold(f"miner host cannot be resolved: {exc}")

    try:
        with socket.create_connection((parsed.hostname, parsed.port), timeout=5):
            pass
    except OSError as exc:
        return hold(f"pool endpoint is unreachable: {exc}")

    print("PASS: miner host resolves and pool TCP endpoint is reachable")
    print("NOTE: connectivity is not proof of mining or accepted shares")
    return 0

if __name__=="__main__":
    sys.exit(main())
