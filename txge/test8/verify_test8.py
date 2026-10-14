#!/usr/bin/env python3
"""TXGE Test 8: fail-closed Bitcoin mainnet receipt checker. Read-only.

Requires Bitcoin Core bitcoin-cli. Never signs or broadcasts a transaction.
Independent identity binding and pretransaction commitment need a human audit.
"""
import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re
import shlex
import subprocess
import sys

HEX64 = re.compile(r"^[a-fA-F0-9]{64}$")


def canonical_sha(data):
    return hashlib.sha256(json.dumps(data, ensure_ascii=False, sort_keys=True,
                    separators=(",", ":")).encode("utf-8")).hexdigest()


def gate(condition, detail):
    return {"status": "PASS" if condition else "HOLD", "detail": detail}


def call_rpc(command, *args):
    try:
        result = subprocess.run(command + list(args), check=True, capture_output=True,
                                text=True, timeout=35)
        return json.loads(result.stdout)
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired, ValueError) as exc:
        return {"_rpc_error": str(exc)[:220]}


def check_node(cmd, txid, addr, sats, blockhint, minimum):
    info = call_rpc(cmd, "getblockchaininfo")
    if not isinstance(info, dict) or info.get("chain") != "main":
        return gate(False, "Bitcoin Core mainnet chain was not independently verified"), None
    args = ["getrawtransaction", txid, "true"]
    if blockhint:
        args.append(blockhint)
    tx = call_rpc(cmd, *args)
    if not isinstance(tx, dict) or tx.get("txid") != txid:
        return gate(False, "Mainnet transaction not found or TXID mismatch"), None
    bh = tx.get("blockhash")
    if not isinstance(bh, str) or not HEX64.fullmatch(bh):
        return gate(False, "TXID not recorded in a Bitcoin mainnet block"), None
    block = call_rpc(cmd, "getblock", bh, "1")
    if (not isinstance(block, dict) or block.get("hash") != bh or
            not isinstance(block.get("confirmations"), int) or
            block["confirmations"] < minimum or
            txid not in block.get("tx", [])):
        return gate(False, "Transaction lacks required best-chain confirmations"), None
    paid = 0
    for output in tx.get("vout", []):
        script = output.get("scriptPubKey", {})
        addresses = script.get("addresses", [])
        if script.get("address") == addr or addr in addresses:
            try:
                value = Decimal(str(output["value"])) * Decimal(100000000)
                if value != value.to_integral_value():
                    return gate(False, "Nonintegral satoshi value"), None
                paid += int(value)
            except (KeyError, ValueError, InvalidOperation):
                return gate(False, "Malformed payment output"), None
    if paid < sats:
        return gate(False, "Matching outputs pay less than agreed amount"), None
    return gate(True, "Best-chain Bitcoin mainnet output and confirmations verified"), {
        "txid": txid, "blockhash": bh, "confirmations": block["confirmations"],
        "recipient_sats": paid,
    }


def check(terms, evidence, node_a, node_b, minimum):
    commitment = canonical_sha(terms)
    out = {"test": "TXGE-TEST8", "terms_sha256": commitment, "gates": {},
           "overall": "HOLD", "external_identity_audit": "REQUIRED",
           "public_precommit_chronology_audit": "REQUIRED"}
    required = ["offer_id", "network", "reference_valuation_sats", "payment_sats",
                "recipient_address", "mr100_signing_address"]
    valid = (all(k in terms for k in required) and terms.get("network") == "main" and
             type(terms.get("reference_valuation_sats")) is int and
             terms["reference_valuation_sats"] == 312500000 and
             type(terms.get("payment_sats")) is int and terms["payment_sats"] > 0 and
             isinstance(terms.get("recipient_address"), str) and
             len(terms["recipient_address"]) >= 26 and
             isinstance(terms.get("mr100_signing_address"), str) and
             terms["mr100_signing_address"].startswith("1") and
             evidence.get("terms_sha256") == commitment)
    out["gates"]["T1_terms"] = gate(valid, "Fixed terms and digest match; public precommit chronology still requires external audit")
    if not valid:
        for name in ("T2_acceptance", "T3_mainnet_payment", "T4_independent_echo"):
            out["gates"][name] = gate(False, "Blocked by missing or inconsistent terms")
        return out
    challenge = "TXGE TEST8 ACCEPT\nOFFER_SHA256=" + commitment
    signature = evidence.get("mr100_message_signature")
    sig_valid = False
    if isinstance(signature, str) and signature and node_a:
        sig_valid = call_rpc(node_a, "verifymessage", terms["mr100_signing_address"],
                             signature, challenge) is True
    out["gates"]["T2_acceptance"] = gate(sig_valid,
        "Bitcoin legacy-address message signature verified; binding to Mr100 must be audited externally"
        if sig_valid else "No valid legacy-address acceptance signature for exact terms")
    txid = evidence.get("txid")
    if not isinstance(txid, str) or not HEX64.fullmatch(txid) or not node_a:
        out["gates"]["T3_mainnet_payment"] = gate(False, "No valid 64-character TXID or first Bitcoin Core node")
        out["gates"]["T4_independent_echo"] = gate(False, "No independently verified transaction")
        return out
    txid = txid.lower()
    hint = evidence.get("blockhash")
    if hint is not None and (not isinstance(hint, str) or not HEX64.fullmatch(hint)):
        out["gates"]["T3_mainnet_payment"] = gate(False, "Invalid blockhash hint")
        out["gates"]["T4_independent_echo"] = gate(False, "No valid mainnet receipt")
        return out
    g3, witness_a = check_node(node_a, txid, terms["recipient_address"],
                               terms["payment_sats"], hint, minimum)
    out["gates"]["T3_mainnet_payment"] = g3
    if witness_a:
        out["bitcoin_witness_a"] = witness_a
    if not witness_a or not node_b or node_a == node_b:
        out["gates"]["T4_independent_echo"] = gate(False, "Second distinct Bitcoin Core node and first valid witness required")
        return out
    g4, witness_b = check_node(node_b, txid, terms["recipient_address"],
                               terms["payment_sats"], hint, minimum)
    matching = bool(witness_b and witness_b["blockhash"] == witness_a["blockhash"])
    out["gates"]["T4_independent_echo"] = gate(g4["status"] == "PASS" and matching,
         "Second node agrees on canonical transaction and block; independence of node operators must be audited"
         if matching else "Independent chain verification failed or disagreed")
    if witness_b:
        out["bitcoin_witness_b"] = witness_b
    # Deliberately never auto-PASS the overall protocol: on-chain data and wallet
    # signatures do not attest the real-world identity of an aliased party.
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--terms", required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--node-a", default="bitcoin-cli -chain=main", help="bitcoin-cli command for primary node")
    p.add_argument("--node-b", default="", help="bitcoin-cli command for separately operated echo node")
    p.add_argument("--min-confirmations", type=int, default=6)
    p.add_argument("--output", help="optional JSON receipt path")
    a = p.parse_args()
    if a.min_confirmations < 1:
        p.error("confirmations must be >= 1")
    try:
        terms = json.loads(Path(a.terms).read_text(encoding="utf-8"))
        evidence = json.loads(Path(a.evidence).read_text(encoding="utf-8"))
        result = check(terms, evidence, shlex.split(a.node_a) if a.node_a else [],
                       shlex.split(a.node_b) if a.node_b else [], a.min_confirmations)
    except (OSError, ValueError, TypeError) as exc:
        result = {"test": "TXGE-TEST8", "overall": "HOLD", "error": str(exc)[:200]}
    formatted = json.dumps(result, indent=2, sort_keys=True) + "\n"
    print(formatted, end="")
    if a.output:
        Path(a.output).write_text(formatted, encoding="utf-8")
    return 0 if result.get("overall") == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())