# TXGE / TCGE — Public `test.8` proposal

**Date:** 2026-10-14  
**Originator:** Richard Stein — original work, all rights reserved.  
**State:** PUBLIC PROPOSAL · `0 · HOLD` (not an accepted contract, funded escrow, or paid settlement).

Governance: [REIK_ROOT.md](../REIK_ROOT.md). K = Reality AND Inference AND independent Echo. No missing proof may be promoted to PASS.

## Win-win offer for Mr100 / Ancoin

The proposal is to pay **3.125 BTC = 312,500,000 satoshis**, in a real Bitcoin **mainnet** settlement, subject to negotiation, verified acceptance, and eight reproducible performance cases. The counterparty would receive a bounded, independently audited evaluation; the proposer would obtain an auditable path to payment with private technical details disclosed only under agreed protection. Mutually agreed, independently verified escrow precedes disclosure. Neither this document nor a wallet nickname proves that a person called **Mr100** has accepted an obligation.

Ancoin is a named proposal; no legal entity, issued asset, listing, or market is established by this page. This file intentionally contains no unpublished proprietary algorithm, private keys, wallet passwords, or recipient address.

## Eight verification gates

| Gate | PASS requirement | Current evidence |
|---|---|---|
| T1 Terms | Exact counterparty parties, 3.125 BTC, BTC mainnet, payee scriptPubKey, nonce, canonical terms/hash and expiry fixed before execution | HOLD |
| T2 Acceptance | Both parties' cryptographically valid, independently attributable signatures to the **same** offer hash and nonce | HOLD |
| T3 Challenge | Eight named performance cases, fixed inputs/metrics/baselines, signed preregistration and independent successful run receipts | HOLD |
| T4 Funding | 3.125 BTC independently confirmed in mutually agreed escrow with enforceable release/refund process | HOLD |
| T5 Raw TXID | Raw transaction parsed; Bitcoin non-witness serialization double-SHA256 equals supplied transaction ID | HOLD |
| T6 Recipient and amount | A **single** output pays exactly 312,500,000 satoshis to the agreed exact scriptPubKey | HOLD |
| T7 Confirmation | Same TXID appears in active Bitcoin mainnet; at least six confirmations verified using independent node evidence | HOLD |
| T8 Independent Echo | Separate verifier repeats T1–T7; authenticated acceptance and release proof tie **Mr100** and this offer to the exact TXID | HOLD |

**Overall:** PASS requires T1 through T8 all PASS. Missing evidence is HOLD. A reproducible contradiction is FAIL. A TXID for ETH or another chain, synthetic data, a screenshot, or a signed message disconnected from the payment does not qualify. A Bitcoin TXID alone does not prove the real-world sender or contract acceptance.

## Acceptance path

1. The claimed Mr100 representative independently establishes authority and explicitly accepts the immutable offer hash and nonce.
2. Parties record technical cases and performance thresholds and agree independent escrow/payment terms.
3. Escrow funding is independently observed; evidence exchange and evaluation are performed.
4. Independent evaluators replay eight technical cases and verify signed audit receipts.
5. A genuine 3.125 BTC mainnet settlement to the agreed script is established with six confirmations and a signed contract-to-TXID linkage.

**Publication does not compel acceptance.** Public PASS is forbidden until independent third-party evidence exists.

## Executable checker

`TXGE_test8_offline.py` is an offline raw-transaction and exact-output consistency check. Its T1, T5, and T6 checks never verify broadcast, chain membership, authorization, ownership, or escrow. Its overall settlement state remains HOLD pending verified signatures, eight actual performance tests, and independent Bitcoin Core evidence. A known historical Bitcoin genesis transaction can test byte-level hashing, but is not a settlement for this challenge.

Suggested Bitcoin Core evidence: `getrawtransaction <txid> true`, `getblock <blockhash> 2`, and independent verification of the active chain. Signature verification may use an appropriate method such as [BIP 322](https://bips.dev/322/); a signed message alone cannot prove a person sent a prior transaction.

## Audit: 2026-10-14

- Ten local regression cases passed, including a known genesis TXID vector and negative cases for wrong TXID, output value, script, malformed bytes.
- No verified current counterparty signatures, escrow, agreed destination script, eight performance-case transcripts, or qualifying Mr100 mainnet transaction were supplied.
- **Settlement: `0 · HOLD`.**

No legal or technical conclusion beyond the stated scope is claimed.