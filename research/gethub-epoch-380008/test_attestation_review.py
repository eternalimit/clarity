"""No live wallet, signature generation, RPC, or independent witness involved."""
from dataclasses import replace
import pytest
from attestation_review import (
    Challenge, Evidence, ReviewLedger, issue_review_challenge,
    challenge_siwe_text, verify_ed25519_reference_vector,
)

WALLET = "0x" + "a" * 40
NOW = 1700000000
DOMAIN = "review.example"
URI = "https://review.example/epoch/380008"

@pytest.fixture
def challenge():
    return issue_review_challenge(domain=DOMAIN, uri=URI, wallet=WALLET,
                                  chain_id=1, now=NOW)

@pytest.fixture
def evidence(challenge):
    return Evidence(challenge.nonce, WALLET, DOMAIN, URI, 1, True, True,
                    "test-public-key-1", "external-operator-fixture", "owner-fixture",
                    NOW, NOW + 120, 1, "a" * 64, "test-anchor-no-independent-proof")

@pytest.fixture
def ledger():
    return ReviewLedger(trusted_roots={"test-public-key-1": "test-anchor-no-independent-proof"})

def assess(ledger, challenge, evidence, now=NOW, **kwargs):
    policy=dict(expected_domain=DOMAIN, expected_uri=URI,
                expected_wallet=WALLET, expected_chain_id=1)
    policy.update(kwargs)
    return ledger.assess(challenge,evidence,now=now,**policy)


def test_local_policy_pass_still_holds(ledger, challenge, evidence):
    a=assess(ledger,challenge,evidence)
    assert a.local_policy_pass and a.status=="0 HOLD"
    assert "EXTERNAL_ECHO_MISSING" in a.reasons


def test_generated_nonce_is_randomized():
    a=issue_review_challenge(domain=DOMAIN,uri=URI,wallet=WALLET,chain_id=1,now=NOW)
    b=issue_review_challenge(domain=DOMAIN,uri=URI,wallet=WALLET,chain_id=1,now=NOW)
    assert a.nonce != b.nonce and len(a.nonce)==32


def test_siwe_proposal_text_is_unsigned(challenge):
    text=challenge_siwe_text(challenge)
    assert f"Nonce: {challenge.nonce}" in text and "Epoch 380008" in text
    assert "Chain ID: 1" in text and "Expiration Time:" in text


@pytest.mark.parametrize("field,value,reason",[
 ("signed_nonce","wrongnonce12345678","CHALLENGE_BINDING_MISMATCH"),
 ("claimed_wallet","0x"+"b"*40,"CHALLENGE_BINDING_MISMATCH"),
 ("claimed_domain","attack.example","CHALLENGE_BINDING_MISMATCH"),
 ("claimed_uri","https://attack.example/","CHALLENGE_BINDING_MISMATCH"),
 ("claimed_chain_id",8453,"CHALLENGE_BINDING_MISMATCH"),
 ("wallet_signature_checked_in_mock",False,"WALLET_SIGNATURE_UNVERIFIED"),
 ("witness_signature_checked_in_mock",False,"WITNESS_SIGNATURE_UNVERIFIED"),
 ("witness_key_id","unregistered","UNANCHORED_ROOT"),
 ("root_anchor","forged-anchor","UNANCHORED_ROOT"),
 ("witness_operator","owner-fixture","NONINDEPENDENT_OPERATOR"),
 ("witnessed_at",NOW+200,"WITNESS_NOT_FRESH"),
 ("witness_expires_at",NOW,"WITNESS_NOT_FRESH"),
 ("sequence",0,"INVALID_SEQUENCE"),
 ("checkpoint_sha256","notahash","INVALID_CHECKPOINT"),
])
def test_adversarial_evidence_rejected(ledger,challenge,evidence,field,value,reason):
    a=assess(ledger,challenge,replace(evidence,**{field:value}))
    assert not a.local_policy_pass and reason in a.reasons and a.status=="0 HOLD"


@pytest.mark.parametrize("field,value",[
 ("nonce","short"), ("epoch",380009), ("chain_id",True),
 ("issued_at",NOW+1000), ("expires_at",NOW+301),
 ("domain","other.example"), ("uri","https://review.example/\nattack"),
 ("wallet","0x123"),
])
def test_bad_challenge_rejected(ledger,challenge,evidence,field,value):
    a=assess(ledger,replace(challenge,**{field:value}),evidence)
    assert not a.local_policy_pass and a.status=="0 HOLD"


def test_expired_challenge(ledger,challenge,evidence):
    a=assess(ledger,challenge,evidence,now=NOW+300)
    assert "CHALLENGE_NOT_FRESH" in a.reasons


def test_nonce_replay(ledger,challenge,evidence):
    assert assess(ledger,challenge,evidence).local_policy_pass
    a=assess(ledger,challenge,evidence)
    assert not a.local_policy_pass and "NONCE_REPLAY" in a.reasons


def test_revocation_before_accept(ledger,challenge,evidence):
    ledger.revoke(evidence.witness_key_id)
    a=assess(ledger,challenge,evidence)
    assert not a.local_policy_pass and "REVOKED_ROOT" in a.reasons


def test_revocation_after_local_accept(ledger,challenge,evidence):
    assert assess(ledger,challenge,evidence).local_policy_pass
    ledger.revoke(evidence.witness_key_id)
    c2=issue_review_challenge(domain=DOMAIN,uri=URI,wallet=WALLET,chain_id=1,now=NOW)
    a=assess(ledger,c2,replace(evidence,signed_nonce=c2.nonce,sequence=2))
    assert "REVOKED_ROOT" in a.reasons


def test_rollback_sequence(ledger,challenge,evidence):
    assert assess(ledger,challenge,evidence).local_policy_pass
    c2=issue_review_challenge(domain=DOMAIN,uri=URI,wallet=WALLET,chain_id=1,now=NOW)
    a=assess(ledger,c2,replace(evidence,signed_nonce=c2.nonce,sequence=1))
    assert "ROLLBACK_OR_REPLAY" in a.reasons


def test_conflicting_checkpoint_detected(ledger,challenge,evidence):
    assert assess(ledger,challenge,evidence).local_policy_pass
    c2=issue_review_challenge(domain=DOMAIN,uri=URI,wallet=WALLET,chain_id=1,now=NOW)
    forged=replace(evidence,signed_nonce=c2.nonce,checkpoint_sha256="b"*64)
    a=assess(ledger,c2,forged)
    assert "EQUIVOCATION" in a.reasons


def test_policy_origin_binding(ledger,challenge,evidence):
    a=assess(ledger,challenge,evidence,expected_domain="another.example")
    assert "ORIGIN_MISMATCH" in a.reasons


def test_policy_wallet_chain_binding(ledger,challenge,evidence):
    a=assess(ledger,challenge,evidence,expected_chain_id=10)
    assert "SUBJECT_MISMATCH" in a.reasons


# RFC 8032 Section 7.1, TEST 1, empty message; independently published
# test vector. Verification only. No key creation or signing.
RFC8032_PK=bytes.fromhex("d75a980182b10ab7d54bfed3c964073a0ee172f3daa62325af021a68f707511a")
RFC8032_SIG=bytes.fromhex(
    "e5564300c360ac729086e2cc806e828a84877f1eb8e5d974d873e06522490155"
    "5fb8821590a33bacc61e39701cf9b46bd25bf5f0595bbe24655141438e7a100b"
)


def test_rfc8032_published_vector_verifies():
    assert verify_ed25519_reference_vector(RFC8032_PK,b"",RFC8032_SIG)


def test_rfc8032_message_tamper_rejected():
    assert not verify_ed25519_reference_vector(RFC8032_PK,b"x",RFC8032_SIG)


def test_rfc8032_signature_tamper_rejected():
    sig=bytearray(RFC8032_SIG);sig[0]^=1
    assert not verify_ed25519_reference_vector(RFC8032_PK,b"",bytes(sig))


def test_rfc8032_key_tamper_rejected():
    pk=bytearray(RFC8032_PK);pk[0]^=1
    assert not verify_ed25519_reference_vector(bytes(pk),b"",RFC8032_SIG)


def test_not_real_world_echo_even_with_mock_flags(ledger,challenge,evidence):
    local=assess(ledger,challenge,evidence)
    assert local.local_policy_pass and local.status=="0 HOLD"
    assert "SYNTHETIC_POLICY_ONLY" in local.reasons


def test_second_backend_rfc8032_agrees_on_valid_vector():
    from second_implementation_review import verify_ed25519_with_libsodium
    assert verify_ed25519_with_libsodium(RFC8032_PK, b"", RFC8032_SIG)
    assert verify_ed25519_reference_vector(RFC8032_PK,b"",RFC8032_SIG)


def test_second_backend_rfc8032_agrees_on_tampering():
    from second_implementation_review import verify_ed25519_with_libsodium
    assert not verify_ed25519_with_libsodium(RFC8032_PK,b"changed",RFC8032_SIG)
    assert not verify_ed25519_reference_vector(RFC8032_PK,b"changed",RFC8032_SIG)


@pytest.mark.parametrize("field,value",[
    ("claimed_wallet",None), ("claimed_domain",42),
    ("claimed_chain_id","1"), ("witness_operator",None),
    ("root_anchor",None), ("wallet_signature_checked_in_mock",1),
])
def test_bad_evidence_types_fail_closed(ledger,challenge,evidence,field,value):
    a=assess(ledger,challenge,replace(evidence,**{field:value}))
    assert not a.local_policy_pass and a.status=="0 HOLD"
