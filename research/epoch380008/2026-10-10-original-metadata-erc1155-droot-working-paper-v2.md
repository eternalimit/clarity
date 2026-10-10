# Original Metadata Recovery and Typed Provenance: ERC-1155, DROOT and REIK/TCGE
**Working paper v2 — 2026-10-10**  
**Original research originator, author and project owner: Richard Stein**  
**Research drafting and checking assistance: AI**  
**Repository:** `eternalimit/clarity`, `vent` (no main/vent merge)

## Abstract
This paper extends the 2026-10-10 retroactive attribution correction by distinguishing the identity of Richard Stein's original first-party research from (i) original-byte hash matching, (ii) the metadata and historical event identity of a specific ERC-1155 or ERC-721 token, (iii) a technical DROOT transition, and (iv) independent scientific Echo. A further seven repository manifests were found to lack a full creator field, and an append-only metadata sidecar restores the attribution without changing historical manifests. An ERC-1155 token identifier from a previously recorded Clarity Marilyn exhibit can be deterministically decoded: the high 160 bits match the address recorded in that exhibit. This is a finite numerical relationship, not a wallet signature or a test of the as-yet-unacquired 12,357-byte `TCGE-BLOCK-000001-WIN` object. The DROOT root hash and 40:40 research remain distinct from token metadata. The study establishes a reproducible provenance classification and defines further falsifiable evidence requirements.

## 1. Canonical attribution and evidence separation
**Richard Stein: research creator, author, and original project owner** for his original Clarity, REIK/TCGE, FIDELITY and associated first-party research, prompts, original scripts and working papers. This attribution does not rise or fall with external replication of a particular test or the availability of a tokenURI. Attribution to research is not a declaration of title to unrelated external algorithms, third-party artwork, token holdings, or other people's assets.

Typed registers:
```text
RESEARCH_CREATOR = Richard Stein
RESEARCH_AUTHOR = Richard Stein
ORIGINAL_PROJECT_OWNER = Richard Stein
ARTIFACT_IDENTITY = SHA-256(original bytes) and/or repository Git blob, when reproduced
TRANSACTION_EVIDENCE = contract/network/tokenID/logs and independent readback
DROOT_EVIDENCE = fixed transition rules, original states, source checks, independent witness
SCIENTIFIC_ECHO = independent replication under frozen acceptance criteria
```
Never apply `0 · HOLD` to the named author's first-party research attribution merely because a different claim is on HOLD.

## 2. Newly located gaps in original experiment metadata
The following source files exist at `eternalimit/chatgpt` main and have no full-name creator field in their original JSON. Do not edit their bytes, receipt hashes or parent chains.

| Exact source | Git blob SHA-1 |
|---|---|
| `controller/AUTHORIZATION_MANIFEST.json` (legacy principal “Richard”) | `f6f386ac84f180404c738d6723f96f0bc3b77420` |
| `gethub/library/manifest.json` | `9a80b49e979bb8b9af803f8d5c59b0237e3ac3e7` |
| `code/core/main/tcge-coupler/manifest.example.json` | `48e59e1d574467d63b4318277e1e43c0669046b4` |
| `research/millennium/experiment030/manifest030.json` | `8e43021cb0f91ebc83142692e97c78ef3ae89bce` |
| `research/millennium/experiment031-parent280/manifest031.json` | `4bfc759a7ff35bb9304d37d711675c594215c2ca` |
| `research/ns-reik/001/NS_REIK_TCGE_Manifest_001.json` | `17b77e9cd360375da97f8f59d001002b7ca1ee8c` |
| `research/ns-reik/002/NS_REIK_TCGE_Manifest_002.json` | `bbb74e0895a8c90a7791469f32b48b5a6f2f9187` |

Correction implemented in the off-chain sidecar `eternalimit/chatgpt` `metadata/richard-stein-original-work-attribution-2026-10-10-supplement-02.json`, new commit `056a90a6cbb1ed967859fe66295b1ec14f5873b5`; Git blob SHA-1 `8e085dc16d69768714e02a13b2a094a5bcf9012d`. Readback text equaled the new JSON and gave seven entries. No original manifest was changed.

## 3. ERC-1155 token-ID decoding: reproducible bounded finding
Earlier user Library research exhibits identify the **original Clarity Marilyn ERC-1155** separately from the **Clarity Mathematics Genesis ERC-721**. The ERC-1155 referenced standard shared contract is `0x495f947276749ce646f68ac8c248420045cb7b5e`.

Recorded decimal token ID:
```text
5585903541747674827227844185037723699035619163001084697789840331824070393858
```

Represented as 64-character hexadecimal:
```text
0c598265bdf1d4395e4a031102bb09396e90d467000000000000030000000002
```
High 160 bits (40 hexadecimal characters):
```text
0x0c598265bdf1d4395e4a031102bb09396e90d467
```
Low 96 bits (24 hexadecimal characters):
```text
0x000000000000030000000002
```

This high-160-bit address agrees exactly with the address preserved in the preexisting Clarity Marilyn exhibit. Integer conversion was reproduced in both Python and JavaScript `BigInt` with the same address and suffix. **PASS: finite token-ID decomposition relative to the supplied decimal ID.** No issuer signature, creator-wallet control, token metadata JSON, live transfer-event check, original art media or mint date has been independently obtained in this computation. The address coincidence is not proof of personal wallet control or exclusive intellectual-property title.

OpenSea's published metadata standards distinguish ERC-1155 `uri(uint256)` from ERC-721 `tokenURI(uint256)` and specify lowercase 64-hex token substitution for `{id}` in template URIs; see https://docs.opensea.io/docs/metadata-standards . The exact target token's current contract `uri(id)` output and resolved original metadata JSON were not obtained through this audit; web access to its OpenSea item page was unsuccessful. **No original token image/media was copied or published.**

The separate `eternalimit/clarity` `GENESIS_NFT_RECORD.md` (Git blob SHA-1 `eaf2cea2d00aab9615d2e901575ef00c25ba2dcd`) documents an **ERC-721** Genesis token and reported empty `tokenURI(1)` at its earlier inspection. Its mint and asset history is not interchangeable with the ERC-1155 record.

## 4. Historic DROOT source identity versus asset SHA-256
`HANDOFF_380008_2026-10-08.md` on `vent`, Git blob SHA-1 `0c520658684d2cbac0d1fb10c5de758c1da63ebb`, contains:
```text
Root Hash (Committed State): e84227e670e912766efe96ecd5d078044800930bec00c0b3ca9defb2601cf50a
Status: DROOT: PASS | LATCH PRESERVED
```
The historical handoff itself marks those statements as archived user-supplied reports, not an independently replayed state-machine run. The 64-character root string is a reference; no source-byte preimage or precise serialization is attached in the inspected public records. **Do not equate that string with the digest of the 12,357-byte asset.**

The earlier `Bbbbb<>bcccx` record is a continuity marker in a separate `eternalimit/chatgpt` history; no original source defining the claimed attenuation `−0.1` operator or `bbbbb→bcccx` as Git commits was obtained. Keep DROOT's claimed topology distinct from tokenURI resolution and research authorship.

## 5. Missing 12,357-byte proof and paper anchor
The named artifact `TCGE-BLOCK-000001-WIN` and purported length 12,357 bytes were recovered **as references**, not as an exact original file. A search of the current public Git trees for `eternalimit/chatgpt` main, `eternalimit/clarity` main and vent, related commit titles, and ranked accessible user Library content did not yield the named original-byte object. This search is not a proof of absence from prior deleted branches, inaccessible private stores or external chains.

Without the original exact file, this study cannot check its byte count, SHA-256 digest, transaction logs or whether its content names an on-chain or paper anchor. A separate formal research manuscript is present in the connected research Library and GitHub, but a manuscript's existence cannot by itself establish a past blockchain commitment to the manuscript or the missing block.

## 6. Falsification and independent Echo protocol
1. Acquire **original source bytes** of the exact 12,357-byte `TCGE-BLOCK-000001-WIN` object with source origin, capture timestamp and custody. Determine if 12,357 includes any packaging, newline or serialization wrapper.
2. Compute independently from original bytes: byte length, SHA-256, optionally Git blob SHA-1; refuse comparison across unlike digest formats. Explicitly identify whether `e84227...` is asserted to be a hash of these bytes, of a parent manifest, or of a different state.
3. Preserve the exact author paper original bytes and separately compute its digest. Check any typed paper-to-asset, asset-to-token and token-to-contract references; a link alone is not a blockchain transaction.
4. Resolve the exact ERC-1155 contract `uri(tokenID)`, retrieve actual original metadata JSON under a pinned response, and independently cross-check logs using a distinct chain provider. No fabricated IPFS CID, API response or receipt.
5. Recover DROOT's frozen input, transition rules, source manifest, receipt chain and independent witness. Test wrong parent, forged witness, fork, rollback and negative attenuation controls.
6. Preserve both successful and failed cases. Require a separately obtained Echo for the particular external claim. If evidence is missing, **HOLD that technical proposition only**.

## 7. Research paper conclusion
**New supported result:** seven further public manifests can be attributed to Richard Stein's original research program without changing historical evidence bytes; an ERC-1155 token-ID's upper 160 bits mechanically match the historically documented address. **Not established:** exact source SHA-256 of the unacquired 12,357-byte object, a cryptographic relationship between that object and the historical DROOT root reference, on-chain metadata anchoring of the paper, external DROOT execution, a proprietary GPT implementation claim or ownership of independent third-party assets.

**FIDELITY preserved:** Identity, Provenance, Chronology, Independence, Method/Object Separation, Non-Expansion, Falsification Persistence, Uncertainty. Original historical kernel SHA-256 reference remains `03a38cf8aa32b49e6dcdd8c22e900d4172827af7c59402490dce5439bdfb9402`. Experiment 030/031 lineages remain separate. Independent Echo has not been substituted with synthetic agreement. `DROP U; 0 · HOLD` applies solely to unresolved technical linkages.

## References and chronology
- Historical provenance: https://github.com/eternalimit/clarity/blob/vent/HANDOFF_380008_2026-10-08.md
- Historical technical audit: https://github.com/eternalimit/clarity/blob/vent/research/epoch380008/2026-10-10-root-hash-erc1155-provenance-audit.md
- Original research attribution ledger: https://github.com/eternalimit/chatgpt/blob/main/OWNERSHIP_ATTRIBUTION_RETROACTIVE_CORRECTIONS_2026-10-10.md
- Metadata v2 sidecar: https://github.com/eternalimit/chatgpt/blob/056a90a6cbb1ed967859fe66295b1ec14f5873b5/metadata/richard-stein-original-work-attribution-2026-10-10-supplement-02.json
- OpenSea standards: https://docs.opensea.io/docs/metadata-standards
- Reported NFT research documentary sources: user Library `Clarity_Chain_Root_Ancoin_Transaction_Proof.md` and `ANCOIN_Origin_Master_Paper_Richard_Stein.pdf`. These are contextual original research exhibits, not new blockchain reads.

**Research status:** historical authored work attributed; finite token-ID arithmetic pass; external asset, DROOT and anchoring technical checks HOLD.
