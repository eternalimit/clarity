# GETHUB Epoch 380008 — Review-only validation module

**Author/project attribution:** Richard Stein. This safety hardening is an
AI-assisted proposed derivative of the user-supplied three-file sequence,
not verified historical source bytes or a deployed production service.

**Status:** LOCAL TESTS ONLY / `0 · HOLD` on external authorization, signing,
independent Echo, blockchain events, and production execution.

## Source and integration

Repository root contract: [`../../REIK_ROOT.md`](../../REIK_ROOT.md).
This self-contained, review-only example deliberately does **not** change
`REIK_ROOT.md`, original kernels, the `vent` branch, or existing GitHub Actions.
It does not install or trigger `.github/workflows/pipeline-sync.yml`.

The user-supplied sequence described `gethub_pipeline.py`,
`test_gethub_pipeline.py`, and `.github/workflows/pipeline-sync.yml`, but a
read of `vent` did not find them at those root paths. Therefore these files
are a **new proposal** and must not be represented as recovered originals.

## Local execution

Python 3.11 or later. Install pytest in an isolated environment and run:

```bash
python -m pip install pytest
python -m pytest -q test_gethub_pipeline.py
```

The tests inject synthetic values with `monkeypatch`, not live keys or wallet
ownership. No secret is printed or committed. Never use the test key in an
actual deployment.

## Security model and limits

1. Epoch must be exactly integer `380008`.
2. Caller address and configured `GETHUB_AUTHORIZED_WALLET` must be
   well-formed 20-byte EVM-style hex addresses and **exactly match**
   after case normalization. An exact address is still **not proof of
   custody/control**.
3. `EPIENTER_STATE` must be configured with at least 32 UTF-8 bytes;
   missing or short values yield `HOLD`. This length check is **not**
   proof of cryptographic randomness or adequate entropy.
4. HMAC-SHA-256 binds a domain separator, epoch, canonical address,
   and length-prefixed coordinate bytes to the local secret.
   **HMAC is not a signature or independent witness.**
5. Validator errors fail closed with `False, "HOLD: ..."`, never echoing
   secrets. Passing local tests does not imply production certification.
6. No network, chain calls, signing, asset transfers, or CI deployment
   are performed by this module.

## External evidence still required

Before any protected workflow is enabled: authorized human review,
verified secrets/environment protection, approved wallet custody
challenge/signature, independent trust-root attestation (Echo), signed
receipt with independently reproducible read-back, and branch/action
permissions review. Maintain distinct original research lineages;
do not promote unresolved claims or timestamps.

## Research receipt

- R: GitHub `vent` tree, root contract and user-supplied sequence inspected.
- I: Prefix-only matching and plain SHA-256 are insufficient evidence of
  authorization and independently anchored attestation.
- E: Local synthetic negative controls only; independent Echo missing.
- K: HOLD on external authorization.
- Scope: review-only code and tests, no workflow installation.
