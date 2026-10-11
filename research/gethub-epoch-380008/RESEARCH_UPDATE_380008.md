# Epoch 380008 — Research update: unsigned wallet challenge, witnessed freshness and falsification

**2026-10-10 | Richard Stein original project attribution | REVIEW ONLY / 0 · HOLD**

## Abstract

Continues `eternalimit/clarity` `review/gethub-epoch380008-validator-20261010` at
`1f87b593b4a8a6c32648950d7dff91773d71ef05`, without changing `vent`.
The original local 26 checks were reproduced. An additional read-only
attestation-policy module and independent local Ed25519 verification backend
were built with falsification tests. All simulated positive policy results
explicitly remain `0 HOLD`, because genuine Ethereum wallet signature recovery,
independent witness enrollment, external timestamp anchoring, and cross-machine
persistence have not occurred.

## Research question and hypothesis

Can a bounded GETHUB epoch validator reject address-prefix spoofing, stale or
replayed nonce attestations, root revocation, mismatched domains/chains,
rollback, conflicting checkpoints and self-witnessing, **without** claiming
production authorization from synthetic success?

**Hypothesis:** A domain-bound challenge and local review ledger can reject
those invalid conditions under explicit fixtures. Even if this succeeds,
external custody and independent Echo remain unresolved. A local hash or
signed fixture is not independent provenance.

## Original governance preserved

Original REIK/TCGE kernel **historical claimed SHA-256**:
`03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`.
This kernel is not included or rewritten and original bytes are not rehashed here.
Canonical repository root `REIK_ROOT.md`: **unchanged**.
`K = R AND I AND E`; E requires independently validated inference.
State rule: `0 HOLD`, `DROP U`, one forward branch, never silently promote claims.

FIDELITY (all eight): **Identity, Provenance, Chronology, Independence,
Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty.**
Experiment 030/280 and 030/282 are separate; Experiment 031/290, 031/294-A
and 031/294-B are separate historical branches. They are not merged here.

## Proposed protocol (no signature requests executed)

1. An independently trusted relying-party domain serves HTTPS and generates a
   random nonce per request. Bind an exact full wallet address, chain ID,
   domain, URI, epoch 380008, issued-at and expiration to the challenge.
   In the prototype the nonce is generated locally and the review message
   is displayed unsigned. `challenge_siwe_text()` is not a full ERC-4361
   conformant message parser.
2. A *future* human-approved wallet interaction would sign a properly
   canonicalized ERC-4361 SIWE message; Ethereum EOA verification must recover
   the signer according to ERC-191, and contract wallets require chain-specific
   ERC-1271 verification. Neither method is implemented or executed here.
3. The protected verifier must atomically record challenge issuance and
   consumption in durable storage, preventing replay across workers, restarts
   and regions. This prototype's `ReviewLedger` is process-local and is **not**
   suitable for production replay defense.
4. An independently administered Echo trust-root registry must document key
   custody, external anchoring (original bytes + timestamp), signer operator,
   enrollment authorization, rotation and revocation. This task does not
   enroll any real root or assert independent witness status.
5. A future signed witness receipt should bind canonical challenge hash,
   owner-independent identity, source checkpoint digest, counter, observed-at,
   not-before/expiry, signing key ID, and policy version. It must be verified
   against an *already independently authenticated* public trust root.
6. Independent observers must compare identical checkpoint identifiers at the
   same sequence for forks/non-equivocation and reject rollback. This local
   in-memory test only models those failure cases; durable multi-observer
   distribution and actual witness disagreement still need execution.
7. Two verification libraries were used on the *published RFC 8032 Ed25519
   test vector*: Python `cryptography` (OpenSSL) and a separate `libsodium`
   binding. No private key was generated; no signatures were created.
   These are separate cryptographic implementations on one local host,
   NOT independently administered Echo or Ethereum wallet signatures.

## Method and tests

Read back GitHub's four original review files and Git blob IDs. Compare source
byte hashes, run `python -B -m pytest -q -p no:cacheprovider` in a local
Python environment with `pytest`, `cryptography` and system `libsodium`.

- Original 26 tests: deterministic HMAC, exact wallet allowlist, fail-closed
  missing secret, malformed wallet/epoch, modified input.
- New review-only policy tests: randomized nonce, SIWE display draft, expired
  challenge, cross-origin/URI/chain substitution, consumed nonce replay,
  root/key mismatch and revocation, same-operator self-witness,
  witness freshness, monotonic sequence, conflicting checkpoints, malformed
  inputs, and fail-closed `0 HOLD` even on all-positive synthetic fixture.
- Published Ed25519 RFC 8032 TEST 1 empty-message verification and negative
  controls using two local backends. This test does not verify a live witness.

## Limitations and falsification priorities

No Ethereum message was signed or checked with Ethereum recover;
no wallet custody was demonstrated; no contract-wallet RPC was invoked;
no private key was requested; no protected GitHub Actions run, deployment,
merge, main/vent write, or chain transaction occurred. The prototype accepts
mock flags solely to test policy branches, but its status never becomes PASS.

**Critical remaining falsification tests:** cross-process nonce replay,
actual ERC-191 signature recovery on an externally presented challenge,
ERC-1271 state-change/revocation on a real chain and pinned block,
trust-root compromise and rollback, source-bounded external witness
independence, logged equivocation dissemination to a second operator,
second-host independently reproduced proof and source-byte hash.

## Standards and research references

- ERC-4361 Sign-In with Ethereum: https://eips.ethereum.org/EIPS/eip-4361
- ERC-191 Signed Data Standard: https://eips.ethereum.org/EIPS/eip-191
- ERC-1271 Contract Signature Validation: https://eips.ethereum.org/EIPS/eip-1271
- RFC 8032 EdDSA published vectors: https://www.rfc-editor.org/rfc/rfc8032.html

## Conclusion

The bounded local policy is testable and explicit; actual independent
attestation is still not evidenced. **R = local test results and repository
read-back; I = proposed challenge and witness gate; E = missing externally;
K = 0 HOLD externally.** `DROP U` preserves unresolved evidence as unresolved.
