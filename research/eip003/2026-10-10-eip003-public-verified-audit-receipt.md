# EIP-003 public GitHub receipt — October 10, 2026

Owner attribution: Richard Stein (first-party statement). Research state: **0 · HOLD**; **DROP U**. Original REIK/TCGE kernel unchanged. No outside witness or scientific admission is claimed.

Repository `eternalimit/clarity`, branch `main`; append-only new files, no overwrite or original kernel modification:

1. Paper `research/eip003/2026-10-10-eip003-signed-rekor-significance-paper.md` — Git commit `8bd33b62d739ae71a8fdc9571480e020f3322d05`; Git blob SHA-1 `4d7b2cb544135d13f18e5303f8645fbcc5477902`. Exact published content matched a read-back from that commit and matched locally computed Git blob ID. Original local paper SHA-256 `0d5e94609e130e6c72fc65caf364d7c36349155b52e9e24ebfd33fe77358acdb`.
2. Complete reproduction appendix `research/eip003/2026-10-10-eip003-reproduction-appendix.md` — Git commit `076ee05b7ce4979fdd9224763b38bd9c060e3163`; Git blob SHA-1 `8d1c3392998c6ae11b8223d0c271ec2a32780889`. Exact published content matched read-back and local Git blob ID. Original local appendix SHA-256 `684261978800d8ac89663ea243d6dfcb429ab2014477f41f22ce02c2bc42b424`.

New local reproducible underlying artifacts (fenced unchanged in the reproduction appendix):
- `verify_eip003.py` SHA-256 `5c67d5f7a5ba97f2074da9f8d458e4ca54877a52bdd88278f0c494cc8f56c1a8`.
- `external_rekor_checkpoints.json` SHA-256 `7e462f32ec0486022715d9e9338edebbedd1949888d97e7edde0538ebd368f65`.
- `eip003_results.json` SHA-256 `ed16915a7049f442634bf001ca3ed98380d8e3d8a10756a9845dbeca41a7b305`.

Evidence: Rekor signed checkpoint API `https://rekor.sigstore.dev/api/v1/log`, two retrieved signed states per shard, six signatures verified with independently fetched **published key** from `sigstore/root-signing/targets/trusted_root.json`, Git blob `effb0a19e6a0b3f69b3f0a2c72b5c2a02a0ddeea`. Six publisher signature checks passed; 36/36 altered-source negative controls rejected; six wrong-log-key controls rejected. Tree `1193050959916656506` increased from 3,063,746,336 to 3,068,558,843 (difference 4,812,507); no Merkle consistency proof was acquired.

**HOLD boundaries:** Publisher key was not authenticated via complete TUF metadata chain; no independent outside cosigning witness, historical receipt timestamp, original raw HTTP transport archive, third-party independent corroboration, key-custody audit, leaf inclusion, same-shard Merkle consistency proof, or original-REIK scientific adoption evidence. Earlier EIP-002 hash-chain-only false admissions remain a recorded falsification; distinct Experiment 030/031 histories and Experiment 048/049 boundaries are preserved. Shared Gemini content was not authenticated. A public Git commit proves a versioned publication, not scientific correctness or cryptographic third-party attestation.
