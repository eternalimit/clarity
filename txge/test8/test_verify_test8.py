"""Offline unit tests. All RPC replies are synthetic; none establishes BTC payment."""
import unittest
from unittest.mock import patch
import verify_test8 as v

ADDR = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
TXID = 'a' * 64
BH = 'b' * 64
TERMS = {
    'offer_id': 'TEST8', 'network': 'main', 'reference_valuation_sats': 312500000,
    'payment_sats': 312500000, 'recipient_address': ADDR,
    'mr100_signing_address': ADDR,
}

def evidence():
    return {'terms_sha256': v.canonical_sha(TERMS), 'mr100_message_signature': 'synthetic',
            'txid': TXID, 'blockhash': BH}

def pretend_rpc(cmd, *args):
    if args[0] == 'getblockchaininfo':
        return {'chain': 'main'}
    if args[0] == 'verifymessage':
        return True
    if args[0] == 'getrawtransaction':
        return {'txid': TXID, 'blockhash': BH, 'vout': [
            {'value': 3.125, 'scriptPubKey': {'address': ADDR}}]}
    if args[0] == 'getblock':
        return {'hash': BH, 'confirmations': 7, 'tx': [TXID]}
    return {'_rpc_error': 'unrecognized'}


class TestFailClosed(unittest.TestCase):
    def test_no_terms_no_pass(self):
        with patch.object(v, 'call_rpc', side_effect=pretend_rpc):
            r = v.check(TERMS, {**evidence(), 'terms_sha256': 'wrong'},
                        ['node-a'], ['node-b'], 6)
        self.assertEqual(r['overall'], 'HOLD')
        self.assertTrue(all(x['status'] == 'HOLD' for x in r['gates'].values()))

    def test_synthetic_ideal_case_still_requires_real_world_audit(self):
        with patch.object(v, 'call_rpc', side_effect=pretend_rpc):
            r = v.check(TERMS, evidence(), ['node-a'], ['node-b'], 6)
        self.assertTrue(all(x['status'] == 'PASS' for x in r['gates'].values()))
        self.assertEqual(r['overall'], 'HOLD')
        self.assertEqual(r['external_identity_audit'], 'REQUIRED')

    def test_missing_txid_holds(self):
        with patch.object(v, 'call_rpc', side_effect=pretend_rpc):
            r = v.check(TERMS, {**evidence(), 'txid': None},
                        ['node-a'], ['node-b'], 6)
        self.assertEqual(r['gates']['T3_mainnet_payment']['status'], 'HOLD')

    def test_second_node_cannot_be_identical_configuration(self):
        with patch.object(v, 'call_rpc', side_effect=pretend_rpc):
            r = v.check(TERMS, evidence(), ['node-a'], ['node-a'], 6)
        self.assertEqual(r['gates']['T4_independent_echo']['status'], 'HOLD')

    def test_underpayment_holds(self):
        def underpay(cmd, *args):
            result = pretend_rpc(cmd, *args)
            if args[0] == 'getrawtransaction':
                result['vout'][0]['value'] = 0.01
            return result
        with patch.object(v, 'call_rpc', side_effect=underpay):
            r = v.check(TERMS, evidence(), ['node-a'], ['node-b'], 6)
        self.assertEqual(r['gates']['T3_mainnet_payment']['status'], 'HOLD')

    def test_unconfirmed_holds(self):
        def unconfirmed(cmd, *args):
            result = pretend_rpc(cmd, *args)
            if args[0] == 'getblock':
                result['confirmations'] = 0
            return result
        with patch.object(v, 'call_rpc', side_effect=unconfirmed):
            r = v.check(TERMS, evidence(), ['node-a'], ['node-b'], 6)
        self.assertEqual(r['gates']['T3_mainnet_payment']['status'], 'HOLD')


if __name__ == '__main__':
    unittest.main()
