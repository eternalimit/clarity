#!/usr/bin/env python3
"""TXGE test.8 OFFLINE Bitcoin TXID/output consistency checker.

No wallet, network, or chain verification. A PASS is never a payment confirmation.
Copyright (c) 2026 Richard Stein. All rights reserved for original material.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SATOSHIS = 312_500_000
HEX_RE = re.compile(r"^[0-9a-fA-F]+$")

class ParseError(ValueError):
    pass


def decode_varint(raw, pos):
    if pos >= len(raw):
        raise ParseError('truncated varint')
    prefix = raw[pos]
    pos += 1
    if prefix < 0xfd:
        value = prefix
    else:
        size = {0xfd: 2, 0xfe: 4, 0xff: 8}[prefix]
        if pos + size > len(raw):
            raise ParseError('truncated varint payload')
        value = int.from_bytes(raw[pos:pos + size], 'little')
        if (prefix == 0xfd and value < 0xfd) or (prefix == 0xfe and value <= 0xffff) or (prefix == 0xff and value <= 0xffffffff):
            raise ParseError('non-canonical varint')
        pos += size
    return value, pos


def take(raw, pos, count):
    if count < 0 or pos + count > len(raw):
        raise ParseError('truncated transaction')
    return raw[pos:pos + count], pos + count


def parse_tx(raw):
    if len(raw) < 10:
        raise ParseError('transaction too short')
    version = raw[:4]
    pos = 4
    segwit = raw[pos] == 0 and pos + 1 < len(raw) and raw[pos + 1] != 0
    if segwit:
        if raw[pos + 1] != 1:
            raise ParseError('unsupported witness flag')
        pos += 2
    begin_inputs = pos
    ni, pos = decode_varint(raw, pos)
    if ni == 0 or ni > 100_000:
        raise ParseError('invalid input count')
    for _ in range(ni):
        _, pos = take(raw, pos, 36)
        l, pos = decode_varint(raw, pos)
        _, pos = take(raw, pos, l + 4)
    begin_outputs = pos
    no, pos = decode_varint(raw, pos)
    if no == 0 or no > 100_000:
        raise ParseError('invalid output count')
    outputs = []
    for idx in range(no):
        amount_bytes, pos = take(raw, pos, 8)
        amt = int.from_bytes(amount_bytes, 'little')
        if amt > 21_000_000 * 100_000_000:
            raise ParseError('output exceeds Bitcoin max supply')
        slen, pos = decode_varint(raw, pos)
        script, pos = take(raw, pos, slen)
        outputs.append({'vout': idx, 'value_sats': amt, 'script_hex': script.hex()})
    end_outputs = pos
    if segwit:
        for _ in range(ni):
            items, pos = decode_varint(raw, pos)
            if items > 100_000:
                raise ParseError('unreasonable witness stack')
            for _ in range(items):
                l, pos = decode_varint(raw, pos)
                _, pos = take(raw, pos, l)
    locktime, pos = take(raw, pos, 4)
    if pos != len(raw):
        raise ParseError('trailing bytes')
    stripped = version + raw[begin_inputs:begin_outputs] + raw[begin_outputs:end_outputs] + locktime
    txid = hashlib.sha256(hashlib.sha256(stripped).digest()).digest()[::-1].hex()
    return txid, outputs, segwit


def audit(data):
    results = []
    def result(gate, status, reason):
        results.append({'gate': gate, 'status': status, 'reason': reason})

    if not isinstance(data, dict):
        raise ParseError('receipt must be a JSON object')
    if data.get('schema') != 'txge.test8.offline.v1':
        result('FORMAT', 'FAIL', 'unknown schema')
    else:
        result('FORMAT', 'PASS', 'known offline receipt schema')

    if data.get('network') != 'bitcoin-mainnet':
        result('T1', 'FAIL', 'explicit bitcoin-mainnet identifier required')
    elif data.get('amount_sats') != SATOSHIS or isinstance(data.get('amount_sats'), bool):
        result('T1', 'FAIL', 'amount must be integer 312500000 sats')
    elif not isinstance(data.get('offer_nonce'), str) or len(data['offer_nonce']) < 12:
        result('T1', 'HOLD', 'offer nonce of at least 12 characters required')
    elif not isinstance(data.get('payee_scriptpubkey_hex'), str) or not data['payee_scriptpubkey_hex']:
        result('T1', 'HOLD', 'a mutually agreed exact payee script is required')
    else:
        result('T1', 'PASS', 'proposed label, amount, nonce and script are present; this is NOT a signed agreement or chain proof')

    script = data.get('payee_scriptpubkey_hex')
    if not isinstance(script, str) or len(script) < 2 or len(script) % 2 or not HEX_RE.fullmatch(script):
        result('T6', 'HOLD', 'agreed payee script missing or malformed')
        script = None
    else:
        script = script.lower()

    claimed = data.get('claimed_txid')
    raw_hex = data.get('raw_transaction_hex')
    try:
        if not isinstance(claimed, str) or len(claimed) != 64 or not HEX_RE.fullmatch(claimed):
            raise ParseError('missing or invalid 64-character claimed TXID')
        if not isinstance(raw_hex, str) or len(raw_hex) % 2 or not HEX_RE.fullmatch(raw_hex):
            raise ParseError('raw transaction hex missing or malformed')
        computed, outputs, segwit = parse_tx(bytes.fromhex(raw_hex))
        if claimed.lower() != computed:
            result('T5', 'FAIL', f'TXID mismatch: computed {computed}, claimed {claimed.lower()}')
        else:
            result('T5', 'PASS', f'TXID independently computed from bytes: {computed}; witness={segwit}')
        if script:
            matching = [x['vout'] for x in outputs if x['value_sats'] == SATOSHIS and x['script_hex'] == script]
            result('T6', 'PASS' if matching else 'FAIL', f'exact output vout indices: {matching}' if matching else 'no single exact 3.125 BTC output to agreed script')
    except (ParseError, ValueError) as e:
        result('T5', 'FAIL', str(e))
        if script:
            result('T6', 'HOLD', 'transaction not parsed')

    for gate, reason in [
        ('T2', 'Mr100 and proposer acceptance signatures need independent cryptographic and identity verification'),
        ('T3', 'eight preregistered reproducible performance tests and independent run receipts not supplied'),
        ('T4', 'independent mainnet escrow funding is not checkable offline'),
        ('T7', 'active-mainnet block inclusion and six confirmations require live independent nodes'),
        ('T8', 'independent Echo, authority attribution and contract-to-TXID linkage require outside evidence'),
    ]:
        result(gate, 'HOLD', reason)
    result('OVERALL', 'HOLD', 'offline consistency cannot establish Mr100 acceptance, eight technical wins or on-chain payment')
    return {'protocol': 'TXGE/test.8', 'scope': 'offline-only/no-wallet/no-network', 'results': results}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('receipt', type=Path, help='offline receipt JSON')
    args = parser.parse_args(argv)
    try:
        payload = json.loads(args.receipt.read_text(encoding='utf-8'))
        out = audit(payload)
    except (OSError, json.JSONDecodeError, ParseError) as e:
        out = {'protocol': 'TXGE/test.8', 'results': [{'gate':'FORMAT','status':'FAIL','reason':str(e)}], 'overall':'HOLD'}
    print(json.dumps(out, indent=2))
    return 0 if all(x['status'] != 'FAIL' for x in out['results']) else 1

if __name__ == '__main__':
    sys.exit(main())
