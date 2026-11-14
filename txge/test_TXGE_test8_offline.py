"""Offline parser and settlement-consistency regression tests.
Synthetic fixture TXIDs are not Bitcoin mainnet evidence.
"""
import hashlib
import unittest
from TXGE_test8_offline import parse_tx, audit, ParseError, SATOSHIS

SCRIPT = bytes.fromhex('0014' + 'ab'*20)  # synthetic segwit keyhash script; not a known recipient

def make_tx(segwit=False, amt=SATOSHIS, script=SCRIPT, witness=b'\x01\x01\x01'):
    version = bytes.fromhex('02000000')
    vins = b'\x01' + bytes.fromhex('11'*32) + bytes.fromhex('00000000') + b'\x00' + bytes.fromhex('ffffffff')
    vouts = b'\x01' + amt.to_bytes(8,'little') + bytes([len(script)]) + script
    locktime = bytes(4)
    if segwit:
        return version + bytes.fromhex('0001') + vins + vouts + witness + locktime
    return version + vins + vouts + locktime

def receipt(raw, **changes):
    txid,_,_=parse_tx(raw)
    d={'schema':'txge.test8.offline.v1','network':'bitcoin-mainnet','amount_sats':SATOSHIS,
       'payee_scriptpubkey_hex':SCRIPT.hex(),'offer_nonce':'synthetic-nonce-123',
       'claimed_txid':txid,'raw_transaction_hex':raw.hex()}
    d.update(changes)
    return d

def status(r, name):
    return next(x['status'] for x in r['results'] if x['gate']==name)

class TestTXGE(unittest.TestCase):
    def test_legacy_parser_and_outputs(self):
        raw=make_tx()
        claimed,outputs,witness=parse_tx(raw)
        self.assertEqual(len(claimed),64)
        self.assertEqual(outputs[0]['value_sats'],SATOSHIS)
        self.assertFalse(witness)
        x=audit(receipt(raw))
        self.assertEqual(status(x,'T5'),'PASS')
        self.assertEqual(status(x,'T6'),'PASS')
        self.assertEqual(status(x,'OVERALL'),'HOLD')

    def test_segwit_parser_strip_witness(self):
        a=make_tx(segwit=True, witness=bytes.fromhex('010101'))
        b=make_tx(segwit=True, witness=bytes.fromhex('010102'))
        self.assertEqual(parse_tx(a)[0],parse_tx(b)[0]) # txid excludes witness
        self.assertTrue(parse_tx(a)[2]); self.assertEqual(status(audit(receipt(a)),'T5'),'PASS')

    def test_wrong_txid_is_fail(self):
        x=audit(receipt(make_tx(), claimed_txid='00'*32))
        self.assertEqual(status(x,'T5'),'FAIL')

    def test_wrong_payment_is_fail(self):
        x=audit(receipt(make_tx(amt=SATOSHIS-1)))
        self.assertEqual(status(x,'T6'),'FAIL')

    def test_wrong_recipient_script_is_fail(self):
        x=audit(receipt(make_tx(script=bytes.fromhex('0014'+'cd'*20))))
        self.assertEqual(status(x,'T6'),'FAIL')

    def test_trailing_bytes_detected(self):
        with self.assertRaises(ParseError):parse_tx(make_tx()+b'\x00')

    def test_missing_nonce_holds_terms(self):
        x=audit(receipt(make_tx(), offer_nonce=''))
        self.assertEqual(status(x,'T1'),'HOLD')

    def test_invalid_segwit_witness(self):
        raw=make_tx(segwit=True, witness=bytes.fromhex('010208'))
        with self.assertRaises(ParseError):parse_tx(raw)

    def test_known_genesis_txid_vector(self):
        # Known historical Bitcoin genesis coinbase vector; NOT a spendable payment.
        raw_hex = ('01000000' + '01' + '00'*32 + 'ffffffff' + '4d'
            + '04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'
            + 'ffffffff' + '01' + '00f2052a01000000' + '43'
            + '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
            + '00000000')
        txid,outputs,segwit = parse_tx(bytes.fromhex(raw_hex))
        self.assertEqual(txid, '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(outputs[0]['value_sats'],5_000_000_000)
        self.assertFalse(segwit)

    def test_no_synthetic_case_yields_overall_pass(self):
        x=audit(receipt(make_tx()))
        self.assertTrue(all(g['status']=='HOLD' for g in x['results'] if g['gate'] in ['T2','T3','T4','T7','T8','OVERALL']))

if __name__=='__main__':unittest.main()
