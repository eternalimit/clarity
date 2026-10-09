# Epoch 380008 signing binding

Root contract: [REIK_ROOT.md](REIK_ROOT.md).

Status: PREPARED; signing and deployment NOT EXECUTED.

Repository: eternalimit/clarity
Execution branch: vent
Exact source commit: 449eaa95ab60f40bc5cb0b52fd6810f8a71ba201
Source file: HANDOFF_380008_2026-10-08.md
Workflow: .github/workflows/clarity-handoff-protected-signing.yml

## Provenance

Adapted from eternalimit/chatgpt at commit 3653b3062eeb0d20d52d82a42719fd071fad7a8b, workflow blob ac3b5c60b2fe43d2138069391602cc24ab719fab.
This binding changes repository, execution branch, concurrency group, exact source guard and protection acknowledgement. The source commit is never rewritten.

## Protected configuration in this repository

Environment secrets are repository-specific; secrets in eternalimit/chatgpt are not automatically available here.

Configure environment gethub-signing restricted to vent, with an authorized reviewer and administrator bypass disabled where supported. Protect workflow changes.
Use the existing signing identity. Configure secrets GETHUB_GPG_PRIVATE_KEY and GETHUB_GPG_PASSPHRASE, and variables GETHUB_GPG_FINGERPRINT and GETHUB_SIGNING_EMAIL.
Register the matching public key with the signing account; its signing email must be verified.
Only after checking the protection and identity settings, set GETHUB_SIGNING_PROTECTION_CONFIRMED=clarity-vent-380008-v1.

Configure environment gethub-signing-public restricted to vent with independently authenticated public variables GETHUB_GPG_PUBLIC_KEY and GETHUB_GPG_FINGERPRINT. No signing secrets belong there.

## Manual execution prerequisite

GitHub requires a workflow_dispatch workflow to exist on the default branch before it can be dispatched. This binding is committed only on vent; main has not been changed. Publish the reviewed workflow on the default branch through the normal review process before dispatching it with ref vent and the exact target above.

The available connector cannot configure environments or secrets or dispatch a new workflow. No environment configuration or key existence has been verified.

## Receipt and verification

A successful run creates an append-only signed receipt commit parented to the exact source commit and pushes a unique gethub-signed-receipt archive branch.
A separate runner verifies the signature, expected fingerprint, exact source digest and parent relationship, plus GitHub's signature verification.
Preserve the source commit URL, receipt commit URL and Actions run URL for independent comparison.
Claim validation stays HOLD. Signing does not validate balances, wallet ownership, historical execution, email delivery or product-priority claims.
Website deployment remains unconfigured; no destination has been selected.
