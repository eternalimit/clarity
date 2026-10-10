# EIP-003 — Complete Reproduction Appendix

This is a verbatim text container for the original local Python verifier, third-party-sourced checkpoint fixture reconstructed from public JSON, and executed audit result. Extract the fenced sections using the file paths below. Independent third-party witnessing, TUF trust-root signature-chain verification and Merkle consistency/inclusion proofs remain **HOLD**.

The original REIK/TCGE kernel was not accessed or modified. This appendix is not part of Experiment 048/049 and does not merge Experiment 030/031 lineages.

## `verify_eip003.py`
SHA-256 exact original text bytes: `5c67d5f7a5ba97f2074da9f8d458e4ca54877a52bdd88278f0c494cc8f56c1a8`

```python
#!/usr/bin/env python3
"""EIP-003: check externally published Rekor checkpoint signatures and negative controls.

This is an independent local checker implementation, not an external human witness.
It is NOT the original REIK/TCGE immutable kernel and does not alter any legacy artifact.
No network required. Dependencies: Python 3 and cryptography (tested 46.0.4).
Source fixture is explicitly a reconstruction from two externally retrieved JSON responses.
Do NOT treat the fixture as TUF root verification or as independent witness evidence.
"""
import base64
import hashlib
import json
from copy import deepcopy
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec

HERE = Path(__file__).resolve().parent
FIX = json.loads((HERE / 'external_rekor_checkpoints.json').read_text())


def raw_message(rec):
    return (f"rekor.sigstore.dev - {rec['treeID']}\n"
            f"{rec['treeSize']}\n{rec['rootB64']}\n").encode('utf-8')


def verify(rec, public_key_der):
    try:
        if base64.b64decode(rec['rootB64'], validate=True).hex() != rec['rootHash']:
            return False
        key_der = base64.b64decode(public_key_der, validate=True)
        key = serialization.load_der_public_key(key_der)
        if not isinstance(key, ec.EllipticCurvePublicKey) or key.curve.name != 'secp256r1':
            return False
        if not isinstance(rec['treeSize'], int) or rec['treeSize'] <= 0:
            return False
        signed = base64.b64decode(rec['signatureB64'], validate=True)
        if signed[:4] != hashlib.sha256(key_der).digest()[:4]:
            return False
        key.verify(signed[4:], raw_message(rec), ec.ECDSA(hashes.SHA256()))
        return True
    except (ValueError, TypeError, InvalidSignature, KeyError, OverflowError):
        return False


def flip_b64_byte(encoded, idx=-1):
    b = bytearray(base64.b64decode(encoded, validate=True))
    b[idx] ^= 1
    return base64.b64encode(b).decode('ascii')


def control(rec, what):
    r = deepcopy(rec)
    if what == 'altered_tree_id':
        r['treeID'] = str(int(r['treeID']) + 1)
    elif what == 'altered_tree_size':
        r['treeSize'] += 1
    elif what == 'forged_same_height_root':
        new = flip_b64_byte(r['rootB64'])
        r['rootB64'] = new
        r['rootHash'] = base64.b64decode(new).hex()
    elif what == 'altered_signature':
        r['signatureB64'] = flip_b64_byte(r['signatureB64'])
    elif what == 'root_metadata_mismatch':
        r['rootHash'] = '00' * 32
    elif what == 'altered_root_encoding':
        r['rootB64'] = flip_b64_byte(r['rootB64'])
    else:
        raise ValueError(what)
    return r


def main():
    entries = FIX['captures']
    keyb64 = FIX['publisher_key_b64_pkix_der']
    other = FIX['publisher_key_other_log_b64_pkix_der']
    controls = ('altered_tree_id', 'altered_tree_size', 'forged_same_height_root',
                'altered_signature', 'root_metadata_mismatch', 'altered_root_encoding')
    successes, negatives = [], []
    for r in entries:
        ok = verify(r, keyb64)
        successes.append(ok)
        if not ok:
            raise AssertionError(('published fixture signature mismatch', r['treeID'], r['order']))
        for c in controls:
            rejected = not verify(control(r, c), keyb64)
            negatives.append({'test': c, 'rejected': rejected})
            if not rejected:
                raise AssertionError(('failed to reject mutation', c))
        assert not verify(r, other), 'wrong-log key must not verify as Rekor P-256 signer'
    a = next(x for x in entries if x['order'] == 1 and x['shard'] == 'current')
    b = next(x for x in entries if x['order'] == 2 and x['shard'] == 'current')
    assert a['treeID'] == b['treeID']
    assert b['treeSize'] > a['treeSize']
    assert b['rootHash'] != a['rootHash']
    # A genuinely signed earlier same-tree note replayed as "latest" after recording B
    # is locally classified STALE.  A stale snapshot by itself is not proof of fraud.
    replayed_old_after_new = a['treeSize'] < b['treeSize']
    # Explicitly do NOT verify Merkle consistency, source archive chronology, TUF root,
    # cosignatures, log-entry inclusion or independent external source authenticity.
    result = {
        'experiment': 'EIP-003',
        'capture_source': FIX['retrieval_url'],
        'public_key_source': FIX['publisher_key_source_url'],
        'public_key_source_blob_sha1_prior_github_read': FIX['publisher_key_git_blob_sha1_observed'],
        'key_spki_der_sha256': hashlib.sha256(base64.b64decode(keyb64)).hexdigest(),
        'key_fingerprint_prefix_hex': hashlib.sha256(base64.b64decode(keyb64)).digest()[:4].hex(),
        'third_party_published_signed_checkpoint_captures': len(entries),
        'signature_verified': sum(successes),
        'signature_checks_total': len(entries),
        'negative_mutations_rejected': sum(x['rejected'] for x in negatives),
        'negative_mutations_total': len(negatives),
        'wrong_other_log_key_rejected': len(entries),
        'wrong_other_log_key_total': len(entries),
        'same_tree_two_capture_monotonic_size': b['treeSize'] > a['treeSize'],
        'same_tree_id': a['treeID'],
        'first_tree_size': a['treeSize'],
        'second_tree_size': b['treeSize'],
        'tree_size_difference': b['treeSize'] - a['treeSize'],
        'stale_return_detectable_relative_to_later_in_session_pinned_size': replayed_old_after_new,
        'same_tree_merkle_consistency_proof': 'NOT_ACQUIRED',
        'per_entry_inclusion_proof': 'NOT_ACQUIRED',
        'third_party_independent_witness_cosignatures': 0,
        'publisher_key_official_tuf_chain_verified': False,
        'independent_external_echo': 'HOLD',
        'scientific_claim_admission': '0 HOLD',
        'original_kernel_modified': False,
        'notes': [
            'Publisher-originating signed checkpoint messages, NOT independent witness attestations',
            'GitHub-published key is separately sourced, not cryptographically trusted as a TUF target',
            'Shard tree IDs are separate logs; different shards cannot be ordered by sizes',
            'Differences in inactive-shard signature bytes across captures do not imply new trees',
            'Checking six signatures does not establish the append-only relationship between snapshots',
            'Changing root with old signature is detected; no genuine conflicting signed fork was obtained',
            'Missing independent witness cannot be replaced by synthetic signing or metadata claims'
        ],
        'preserved_state': '0 HOLD; DROP U',
    }
    return result


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
```

## `external_rekor_checkpoints.json`
SHA-256 exact original text bytes: `7e462f32ec0486022715d9e9338edebbedd1949888d97e7edde0538ebd368f65`

```json
{
  "fixture_type": "EIP-003 reconstruction of third-party returned signed checkpoint text",
  "not_http_transport_raw_bytes": true,
  "retrieval_url": "https://rekor.sigstore.dev/api/v1/log",
  "publisher_key_source_url": "https://github.com/sigstore/root-signing/blob/main/targets/trusted_root.json",
  "publisher_key_git_blob_sha1_observed": "effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea",
  "publisher_key_b64_pkix_der": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE2G2Y+2tabdTV5BcGiBIx0a9fAFwrkBbmLSGtks4L3qX6yYY0zufBnhC8Ur/iy55GhWP/9A/bY2LhC30M9+RYtw==",
  "publisher_key_other_log_b64_pkix_der": "MCowBQYDK2VwAyEAt8rlp1knGwjfbcXAYPYAkn0XiLz1x8O4t0YkEhie244=",
  "captures": [
    {"order":1,"treeID":"3904496407287907110","treeSize":4163431,"rootHash":"4d006aa46efcb607dd51d900b1213754c50cc9251c3405c6c2561d9d6a2f3239","rootB64":"TQBqpG78tgfdUdkAsSE3VMUMySUcNAXGwlYdnWovMjk=","signatureB64":"wNI9ajBFAiA0PkKoUUuXpq+H78OcLiNgB7dvmVFTMSKKsnfOi7xXJwIhAKmmvCmTtyp3CE8culvIIkxANZm5M7XkoG8FUXIEpTXT","shard":"inactive"},
    {"order":1,"treeID":"2605736670972794746","treeSize":117740831,"rootHash":"2b9c578071e120aa84c9858783daa671565e4165f3a7dfa199aad81940299d8e","rootB64":"K5xXgHHhIKqEyYWHg9qmcVZeQWXzp9+hmarYGUApnY4=","signatureB64":"wNI9ajBGAiEAoXF/oEai0E9lpCqXs7+ZvAoT7lkU2mOw7FgG8ezeYWQCIQDqlyxyvM6Iw8++nj+/bYdnEHi4bs4pz0T6Q2aMLwdq8A==","shard":"inactive"},
    {"order":1,"treeID":"1193050959916656506","treeSize":3063746336,"rootHash":"78524a29457e2f48a9640276ebc60462f66dd3a797cc9eac1a20097534caffa4","rootB64":"eFJKKUV+L0ipZAJ268YEYvZt06eXzJ6sGiAJdTTK/6Q=","signatureB64":"wNI9ajBFAiBTWM2q58RfwlJ3Gp9M0piYbTNT+wSA2HFS2ti0HFUJBQIhAO5ihrPThnnucwBCw1bg4xCvvBVef9lVZuEi5xoz7p/Y","shard":"current"},
    {"order":2,"treeID":"3904496407287907110","treeSize":4163431,"rootHash":"4d006aa46efcb607dd51d900b1213754c50cc9251c3405c6c2561d9d6a2f3239","rootB64":"TQBqpG78tgfdUdkAsSE3VMUMySUcNAXGwlYdnWovMjk=","signatureB64":"wNI9ajBFAiB668IW0Wz9ZjzzM6qVqcX3Pb3QHpLthvhLtt6p0ZPq6QIhAJVxp3BvUZU9k88qkIvGpUlOlQaxXNgA8DBqTaJ2+GdK","shard":"inactive"},
    {"order":2,"treeID":"2605736670972794746","treeSize":117740831,"rootHash":"2b9c578071e120aa84c9858783daa671565e4165f3a7dfa199aad81940299d8e","rootB64":"K5xXgHHhIKqEyYWHg9qmcVZeQWXzp9+hmarYGUApnY4=","signatureB64":"wNI9ajBFAiEAmQYeuk5GoR3inVSj1LrqtHhhYNkI+0S3eYvv5ML4UgUCIAJo8vqJ06Jxid6cwyEAnp88MCiN2bazjWL8zpbT0b+B","shard":"inactive"},
    {"order":2,"treeID":"1193050959916656506","treeSize":3068558843,"rootHash":"21ee885dd58d425440d92812c212397008c28ed52ccd0747487a30c922f63132","rootB64":"Ie6IXdWNQlRA2SgSwhI5cAjCjtUszQdHSHowySL2MTI=","signatureB64":"wNI9ajBFAiEAlLnYQY1dt7RgrIvX6rUp+R8SHa0H0GtjlBiB9NiPj9wCIC2IcTewh1fSdmdJukNQz9X37pAu1xPDmgw1cagQi1l9","shard":"current"}
  ],
  "provenance_limits": "Two public endpoint results retrieved in session order, without raw HTTP transport-body capture, external archive timestamp, independent signature cosigning, independently authenticated TUF root, Merkle inclusion or consistency proof. Some checkpoint signatures may be nondeterministic although body remains unchanged."
}
```

## `eip003_results.json`
SHA-256 exact original text bytes: `ed16915a7049f442634bf001ca3ed98380d8e3d8a10756a9845dbeca41a7b305`

```json
{
  "capture_source": "https://rekor.sigstore.dev/api/v1/log",
  "experiment": "EIP-003",
  "first_tree_size": 3063746336,
  "independent_external_echo": "HOLD",
  "key_fingerprint_prefix_hex": "c0d23d6a",
  "key_spki_der_sha256": "c0d23d6ad406973f9559f3ba2d1ca01f84147d8ffc5b8445c224f98b9591801d",
  "negative_mutations_rejected": 36,
  "negative_mutations_total": 36,
  "notes": [
    "Publisher-originating signed checkpoint messages, NOT independent witness attestations",
    "GitHub-published key is separately sourced, not cryptographically trusted as a TUF target",
    "Shard tree IDs are separate logs; different shards cannot be ordered by sizes",
    "Differences in inactive-shard signature bytes across captures do not imply new trees",
    "Checking six signatures does not establish the append-only relationship between snapshots",
    "Changing root with old signature is detected; no genuine conflicting signed fork was obtained",
    "Missing independent witness cannot be replaced by synthetic signing or metadata claims"
  ],
  "original_kernel_modified": false,
  "per_entry_inclusion_proof": "NOT_ACQUIRED",
  "preserved_state": "0 HOLD; DROP U",
  "public_key_source": "https://github.com/sigstore/root-signing/blob/main/targets/trusted_root.json",
  "public_key_source_blob_sha1_prior_github_read": "effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea",
  "publisher_key_official_tuf_chain_verified": false,
  "same_tree_id": "1193050959916656506",
  "same_tree_merkle_consistency_proof": "NOT_ACQUIRED",
  "same_tree_two_capture_monotonic_size": true,
  "scientific_claim_admission": "0 HOLD",
  "second_tree_size": 3068558843,
  "signature_checks_total": 6,
  "signature_verified": 6,
  "stale_return_detectable_relative_to_later_in_session_pinned_size": true,
  "third_party_independent_witness_cosignatures": 0,
  "third_party_published_signed_checkpoint_captures": 6,
  "tree_size_difference": 4812507,
  "wrong_other_log_key_rejected": 6,
  "wrong_other_log_key_total": 6
}
```

## Offline replay

Run `python3 verify_eip003.py > eip003_results.json` from a directory containing the Python and fixture files. Python 3 and `cryptography` 46.0.4 were used. Recomputed result must match the stated SHA-256 only when the same script and fixture bytes are used. Trust root was separately obtained from sigstore/root-signing Git blob `effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea`; exact downloaded TUF metadata signatures were **not** validated.
