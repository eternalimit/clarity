# TXGE / TCGE — public test.8: Mr100, Ancoin, and a real Bitcoin TXID

**Research originator / offer author (by declaration): Richard Stein. All rights reserved.**
**Status: PUBLIC PROPOSAL; NO ACCEPTANCE, BTC PAYMENT, TRANSACTION ID, OR MR100 IDENTITY PROVEN.**
**Date: 2026-10-14. Version: test.8 v0.1.**

This is a **public invitation to conduct a verifiable test**, not an assertion that the person/entity called "Mr100" has seen, accepted, or agreed to anything. It is not a payment demand, coin sale, binding contract, investment solicitation, escrow service, or authority to move anyone's BTC. **Ancoin** is the name provided for this offer; the existing `bitcoin-miner/` files use **Anchoin**. Neither label proves the existence, ownership, market, or legal status of an issued asset. The Bitcoin mining controller is a separate activity and cannot substitute for evidence of a payment.

## Win-win proposal

Mr100 may **voluntarily** consider a pre-agreed BTC transaction to a receiving address mutually validated by the actual parties, subject to agreed amount, fees, refund/dispute terms, legal review where appropriate, and independent verification. In exchange, Richard offers a transparent, reproducible audit package and the agreed consideration, if any, must be written into a separate executed agreement. No one is bound merely because this file is public. No address is supplied here, and no BTC should be sent based solely on this README.

The **3.125 BTC** (312,500,000 satoshi) figure is a **proposed reference valuation**, not evidence of an executable bid, sale price, funded escrow, debt, or obligation. The sample `payment_sats` equals that number *for demonstration only*; the parties must agree actual payment terms before constructing a binding test. Transaction fees are outside receiving-output `payment_sats`.

## Test cases 1–4 (TCGE / REIK)

| Test | Mechanically checkable event | Fail-closed condition |
|---|---|---|
| T1 — Terms | Canonical SHA-256 of fixed public terms matches independent evidence | Missing amount/address, digest mismatch, or no independently established **pre-transaction** publication |
| T2 — Acceptance | Exact `TXGE TEST8 ACCEPT\nOFFER_SHA256=<digest>` challenge signed by predesignated Bitcoin address | Invalid signature; no **independent public evidence** that the address is actually controlled/authorized by "Mr100" |
| T3 — Real transaction | A personally controlled fully validating Bitcoin **mainnet** node finds the TXID in its best chain with >=6 confirmations and matching output address/amount | A fabricated, testnet, unrelated, unconfirmed, wrong-address or underpaid transaction |
| T4 — Independent Echo | An independently operated full node observes identical TXID and block and matching payment with adequate confirmations | No second independently administered node, conflicting observations, or no verifiable operator identity |

**K = R AND I AND E. All four gates and external identity/chronology/operator audits are required before a human auditor can issue a final protocol PASS.** The script intentionally cannot infer a real-world pseudonymous actor's identity from signatures or blockchain data and therefore records `overall: HOLD` until that additional evidence is independently evaluated. T1 `PASS` in script means only correct *file digest and structure*, not attested prior publication; T2 `PASS` means *address signature validity*, not real-world identity.

**Key distinction:** A TXID proves only that a transaction has an identifier; a fully validated node plus confirmations supplies network evidence, whereas actual authorization and agreement require their own witnesses. A coinbase, any other person's payment, a pool share, or a published TXID alone is not a qualifying win.

## Reproducible procedure

1. Before any transaction, parties confirm legal rights, roles, a Bitcoin mainnet receiving address, exact `payment_sats`, expiration, fee payer, terms of exchange, and independently documented Mr100 address-to-identity binding. Duplicate `terms.example.json` as `terms.json`, replace both example addresses. Do not publish private information or wallet secrets.
2. Compute the SHA-256 of the UTF-8 canonical compact JSON of `terms.json`, sorted keys, via `verify_test8.py` / `canonical_sha()`. Publicly timestamp and preserve that exact commitment **before** any signing or transaction. Once agreed, never silently edit terms: a change creates a new SHA-256 and requires a new signature and commitment.
3. Mr100 may demonstrate acceptance by signing **exactly** `TXGE TEST8 ACCEPT` followed by newline and `OFFER_SHA256=<full-64-lowercase-hex-hash>`, using a Bitcoin Core legacy `1...` address precommitted in the terms. Verify via `bitcoin-cli verifymessage`. For SegWit/Taproot, use an independently audited BIP-322 capable signer/verifier, not this v0.1 script. A valid signature shows address-key participation, **not** necessarily the legal identity of its signer or the source of the BTC payment.
4. Only an authorized account/wallet operator may choose to transmit actual BTC under a mutually accepted agreement. Record TXID, optional blockhash hint, and reference to the initial public terms commitment in a local `evidence.json`. The checker **never broadcasts** or initiates wallet transfers.
5. Run two **separately operated, independently synced Bitcoin Core mainnet nodes**, using `-txindex=1` for history lookups or provide a known blockhash. Capture node versions, operators, UTC times, and separate evidence receipts. Wait for a minimum of 6 best-chain confirmations (policy choice, not a Bitcoin consensus mandate).
6. An independent auditor checks publication chronology, legal/real-world identity-binding evidence, signatures, two genuinely independent node operators, the gross versus net payment rules, conflicts, and the manifest. Only then can a separate externally signed final PASS receipt be issued. Reorgs/reversals trigger reevaluation.

### Commands (read-only)

```bash
python3 -m unittest -v test_verify_test8.py
# From within this directory; examples are placeholders and will HOLD:
python3 verify_test8.py --terms terms.example.json --evidence evidence.example.json --output receipt.json

# After agreed and precommitted terms are written, a real tx is observed,
# and independent full nodes are accessible:
python3 verify_test8.py --terms terms.json --evidence evidence.json \
  --node-a 'bitcoin-cli -datadir=/path/to/independent-node-a -chain=main' \
  --node-b 'bitcoin-cli -datadir=/path/to/independent-node-b -chain=main' \
  --min-confirmations 6 --output receipt.json
```

`--node-a` and `--node-b` are *command vectors*, not shell pipelines. `bitcoin-cli` sends read-only RPC calls for this tool. Evidence may contain addresses and public signatures but **must not include** private keys, seed phrases, RPC passwords, cookies, or secrets.

### Audit limitations

- Script checks data supplied by configured RPC endpoints; it **does not** establish their operator independence, software integrity, or whether they are honest fully-validating nodes.
- Legacy message validation is only implemented for conventional Bitcoin `1...` P2PKH message signatures. See [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki) for other scripts. Never substitute a mock signature or unverifiable screenshot.
- Multiple outputs to the specified address are summed; script enforces receiving amount >= agreed payment. Exact-equality rules can be chosen in a future separately signed terms amendment. Transactions may have many unrelated outputs.
- No precommitted recipient/payment/identity, accepted offer, TXID, independent node responses, or third-party auditor has been supplied at publication. **Live test status: `0 · HOLD`.**
- The checker deliberately never returns overall PASS by itself. Its **T1–T4 mechanical checks are necessary but not sufficient** for the final independently witnessed finding.
- Automated offline unit tests create synthetic RPC replies and are **not evidence of a real Bitcoin transaction**.

## Sources and canonical control

- Canonical repository rule: [`REIK_ROOT.md`](../REIK_ROOT.md), `K=R AND I AND E`; absent independent evidence remains HOLD.
- Bitcoin Core RPC: [getrawtransaction](https://bitcoincore.org/en/doc/25.0.0/rpc/rawtransactions/getrawtransaction/) and [getblock](https://bitcoincore.org/en/doc/28.0.0/rpc/blockchain/getblock/).
- Signed message scope: [BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki).

**No funds have been handled or requested for transfer by this test artifact.**