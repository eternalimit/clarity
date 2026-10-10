#!/usr/bin/env python3
"""EIP-002: deterministic synthetic negative controls, NOT independent witnesses.
Python standard library; this is NOT the REIK/TCGE immutable kernel.
"""
import hashlib
import json

GENESIS = hashlib.sha256(b'EIP-002/synthetic/genesis/v1').hexdigest()


def sha(value):
    return hashlib.sha256(value).hexdigest()


def encode(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode('ascii')


def event(seq, seed, prev):
    body = {'seq': seq, 'source': sha(f'EIP002::{seed}::{seq}'.encode()), 'previous': prev}
    return dict(body, digest=sha(encode(body)))


def chain(seed, fork_after=None):
    out, prev = [], GENESIS
    for seq in range(1, 5):
        original = seed if fork_after is None or seq <= fork_after else seed + '::FORK'
        rec = event(seq, original, prev)
        out.append(rec)
        prev = rec['digest']
    return out


def local_replay(events):
    if len(events) != 4:
        return False
    prev = GENESIS
    for i, rec in enumerate(events, 1):
        if not isinstance(rec, dict) or set(rec) != {'seq', 'source', 'previous', 'digest'}:
            return False
        body = {k: rec[k] for k in ('seq', 'source', 'previous')}
        if rec['seq'] != i or rec['previous'] != prev or rec['digest'] != sha(encode(body)):
            return False
        prev = rec['digest']
    return True


def strict_decision(events, supplied_witness_claim=None):
    """No authenticated external witness material is available in this experiment.
    A self-asserted witness claim is never trusted as third-party Echo.
    """
    if not local_replay(events):
        return 'INVALID_LOCAL'
    return 'HOLD_NO_INDEPENDENT_ECHO'


def main():
    rows = []
    for i in range(64):
        original = chain(f'case-{i:02d}')
        changed = [dict(x) for x in original]
        changed[2]['source'] = sha(f'tamper::{i}'.encode())
        samples = (
            ('synthetic_baseline', original, None),
            ('stale_hash_mutation', changed, None),
            ('recomputed_forgery', chain(f'FAKE-case-{i:02d}'), 'three witnesses (unauthenticated text)'),
            ('same_height_fork', chain(f'case-{i:02d}', fork_after=2), 'trusted anchor (unauthenticated text)'),
        )
        for category, events, witness_claim in samples:
            local = local_replay(events)
            strict = strict_decision(events, witness_claim)
            rows.append({'case': i, 'category': category, 'local_chain_valid': local,
                         'hash_only_would_admit': local, 'strict_admission': strict})
            assert strict != 'VERIFIED'
            if category == 'stale_hash_mutation':
                assert not local and strict == 'INVALID_LOCAL'
            else:
                assert local and strict == 'HOLD_NO_INDEPENDENT_ECHO'
    from collections import Counter
    counts = {}
    for category in ('synthetic_baseline', 'stale_hash_mutation', 'recomputed_forgery', 'same_height_fork'):
        rs = [r for r in rows if r['category'] == category]
        counts[category] = {'n': len(rs), 'local_pass': sum(r['local_chain_valid'] for r in rs),
                            'hash_only_admit': sum(r['hash_only_would_admit'] for r in rs),
                            'strict_verified': sum(r['strict_admission'] == 'VERIFIED' for r in rs),
                            'strict_hold': sum(r['strict_admission'] == 'HOLD_NO_INDEPENDENT_ECHO' for r in rs),
                            'strict_invalid': sum(r['strict_admission'] == 'INVALID_LOCAL' for r in rs)}
    report = {
        'experiment': 'EIP-002', 'date': '2026-10-10', 'precommitted_design': '64 samples per category (256 trials)',
        'scope': 'synthetic negative-control gate only; NO real witnessed test or original kernel rehash',
        'cases': len(rows), 'classifications': counts,
        'unsafe_hash_only_false_admission_on_synthetic_attack_fixtures':
            sum(r['hash_only_would_admit'] for r in rows if r['category'] in ('recomputed_forgery', 'same_height_fork')),
        'unauthenticated_witness_claims_promoted': 0,
        'externally_authenticated_witnesses': 0,
        'authenticated_positive_trials': 0,
        'verified_knowledge_from_these_trials': 0,
        'independent_echo': 'NOT OBTAINED', 'original_kernel_modified': False,
        'target_64_of_64_external_witnessed_positive': 'NOT TESTABLE',
        'state': '0 HOLD; DROP U'
    }
    return report


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
