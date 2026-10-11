"""REVIEW ONLY: proposed Epoch 380008 wallet and Echo *policy* gates.

No signing, EVM recovery, Ethereum RPC, network access, trusted key enrollment,
production replay storage, or independent Echo. Mock verification flags are never
interpreted as real authorization. All external decisions remain 0 HOLD.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
import secrets

EXPECTED_EPOCH = 380008
NONCE_RE = re.compile(r"[A-Za-z0-9]{16,128}\Z")
ADDRESS_RE = re.compile(r"0x[0-9a-fA-F]{40}\Z")
HASH_RE = re.compile(r"[0-9a-f]{64}\Z")
MAX_TTL_SECONDS = 300
MAX_CLOCK_SKEW_SECONDS = 30


@dataclass(frozen=True)
class Challenge:
    domain: str
    uri: str
    wallet: str
    chain_id: int
    epoch: int
    nonce: str
    issued_at: int
    expires_at: int


def issue_review_challenge(*, domain: str, uri: str, wallet: str,
                           chain_id: int, now: int) -> Challenge:
    """Create only an unsigned nonce challenge. Never contact a wallet."""
    return Challenge(domain, uri, wallet, chain_id, EXPECTED_EPOCH,
                     secrets.token_hex(16), now, now + MAX_TTL_SECONDS)


def challenge_siwe_text(challenge: Challenge) -> str:
    """Display *proposed* SIWE message; NOT a full ERC-4361 parser/verifier."""
    from datetime import datetime, timezone
    def stamp(t: int) -> str:
        return datetime.fromtimestamp(t, tz=timezone.utc).isoformat().replace("+00:00", "Z")
    if not _well_formed_challenge(challenge):
        raise ValueError("invalid unsigned challenge")
    return (
        f"{challenge.domain} wants you to sign in with your Ethereum account:\n"
        f"{challenge.wallet}\n\n"
        f"GETHUB Epoch {EXPECTED_EPOCH} review-only proof of address control.\n\n"
        f"URI: {challenge.uri}\nVersion: 1\nChain ID: {challenge.chain_id}\n"
        f"Nonce: {challenge.nonce}\nIssued At: {stamp(challenge.issued_at)}\n"
        f"Expiration Time: {stamp(challenge.expires_at)}"
    )


def _well_formed_challenge(c: Challenge) -> bool:
    return (
        isinstance(c.domain, str) and bool(re.fullmatch(r"[a-z0-9.-]+(?::[0-9]{1,5})?", c.domain))
        and isinstance(c.uri, str) and c.uri.startswith("https://" + c.domain + "/")
        and "\n" not in c.uri and "\r" not in c.uri
        and isinstance(c.wallet, str) and ADDRESS_RE.fullmatch(c.wallet) is not None
        and type(c.chain_id) is int and c.chain_id > 0
        and type(c.epoch) is int and c.epoch == EXPECTED_EPOCH
        and isinstance(c.nonce, str) and NONCE_RE.fullmatch(c.nonce) is not None
        and type(c.issued_at) is int and type(c.expires_at) is int
        and 0 < c.expires_at - c.issued_at <= MAX_TTL_SECONDS
    )


@dataclass(frozen=True)
class Evidence:
    """External evidence PLACEHOLDERS; booleans mean *mocked* verification only."""
    signed_nonce: str
    claimed_wallet: str
    claimed_domain: str
    claimed_uri: str
    claimed_chain_id: int
    wallet_signature_checked_in_mock: bool
    witness_signature_checked_in_mock: bool
    witness_key_id: str
    witness_operator: str
    subject_operator: str
    witnessed_at: int
    witness_expires_at: int
    sequence: int
    checkpoint_sha256: str
    root_anchor: str


@dataclass(frozen=True)
class Assessment:
    local_policy_pass: bool
    status: str
    reasons: tuple[str, ...]


class ReviewLedger:
    """Ephemeral test-only replay, revocation and fork bookkeeping.

    Do not use this process-local data structure in an API, CI approval gate,
    multi-worker service, or production authenticator.
    """
    def __init__(self, *, trusted_roots: dict[str, str]) -> None:
        self.trusted_roots = dict(trusted_roots)  # key-id -> externally anchored ref (fixture)
        self.revoked: set[str] = set()
        self.consumed: set[str] = set()
        self.highest_sequence: dict[str, int] = {}
        self.checkpoints: dict[tuple[str, int], str] = {}

    def revoke(self, key_id: str) -> None:
        self.revoked.add(key_id)

    def assess(self, c: Challenge, e: Evidence, *, now: int,
               expected_domain: str, expected_uri: str, expected_wallet: str,
               expected_chain_id: int) -> Assessment:
        reasons: list[str] = []
        if (type(now) is not int or not isinstance(c, Challenge)
                or not isinstance(e, Evidence) or not _well_formed_challenge(c)):
            return Assessment(False, "0 HOLD", ("BAD_CHALLENGE",))
        if (not isinstance(e.claimed_wallet, str) or not isinstance(e.claimed_domain, str)
                or not isinstance(e.claimed_uri, str)
                or type(e.claimed_chain_id) is not int or not isinstance(e.signed_nonce, str)
                or not isinstance(e.witness_key_id, str)
                or not isinstance(e.witness_operator, str)
                or not isinstance(e.subject_operator, str)
                or not isinstance(e.root_anchor, str)
                or type(e.wallet_signature_checked_in_mock) is not bool
                or type(e.witness_signature_checked_in_mock) is not bool):
            return Assessment(False, "0 HOLD", ("BAD_CHALLENGE",))
        if now < c.issued_at - MAX_CLOCK_SKEW_SECONDS or now >= c.expires_at:
            reasons.append("CHALLENGE_NOT_FRESH")
        if c.nonce in self.consumed:
            reasons.append("NONCE_REPLAY")
        if c.domain != expected_domain or c.uri != expected_uri:
            reasons.append("ORIGIN_MISMATCH")
        if c.wallet.lower() != expected_wallet.lower() or c.chain_id != expected_chain_id:
            reasons.append("SUBJECT_MISMATCH")
        if (e.signed_nonce != c.nonce or e.claimed_wallet.lower() != c.wallet.lower()
                or e.claimed_domain != c.domain or e.claimed_uri != c.uri
                or e.claimed_chain_id != c.chain_id):
            reasons.append("CHALLENGE_BINDING_MISMATCH")
        if not e.wallet_signature_checked_in_mock:
            reasons.append("WALLET_SIGNATURE_UNVERIFIED")
        if not e.witness_signature_checked_in_mock:
            reasons.append("WITNESS_SIGNATURE_UNVERIFIED")
        if (e.witness_key_id not in self.trusted_roots
                or self.trusted_roots.get(e.witness_key_id) != e.root_anchor
                or not e.root_anchor):
            reasons.append("UNANCHORED_ROOT")
        if e.witness_key_id in self.revoked:
            reasons.append("REVOKED_ROOT")
        if not e.witness_operator or e.witness_operator == e.subject_operator:
            reasons.append("NONINDEPENDENT_OPERATOR")
        if (type(e.witnessed_at) is not int or type(e.witness_expires_at) is not int
                or e.witnessed_at > now + MAX_CLOCK_SKEW_SECONDS
                or e.witnessed_at < c.issued_at - MAX_CLOCK_SKEW_SECONDS
                or not e.witnessed_at < e.witness_expires_at
                or now >= e.witness_expires_at):
            reasons.append("WITNESS_NOT_FRESH")
        if type(e.sequence) is not int or e.sequence < 1:
            reasons.append("INVALID_SEQUENCE")
        if not isinstance(e.checkpoint_sha256, str) or HASH_RE.fullmatch(e.checkpoint_sha256) is None:
            reasons.append("INVALID_CHECKPOINT")
        key = (e.witness_key_id, e.sequence)
        old = self.checkpoints.get(key)
        if old is not None and old != e.checkpoint_sha256:
            reasons.append("EQUIVOCATION")
        last = self.highest_sequence.get(e.witness_key_id, 0)
        if type(e.sequence) is int and e.sequence <= last:
            reasons.append("ROLLBACK_OR_REPLAY")
        if reasons:
            return Assessment(False, "0 HOLD", tuple(dict.fromkeys(reasons)))
        # Only mock local accept; never claim wallet or Echo verified.
        self.consumed.add(c.nonce)
        self.highest_sequence[e.witness_key_id] = e.sequence
        self.checkpoints[key] = e.checkpoint_sha256
        return Assessment(True, "0 HOLD", ("SYNTHETIC_POLICY_ONLY", "EXTERNAL_ECHO_MISSING"))


def verify_ed25519_reference_vector(public_key: bytes, message: bytes,
                                    signature: bytes) -> bool:
    """Verification-only crypto primitive; published RFC8032 vectors, no signing.

    Uses a local installed verifier, NOT an independently administered Echo.
    """
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        Ed25519PublicKey.from_public_bytes(public_key).verify(signature, message)
        return True
    except (ValueError, TypeError, ImportError):
        return False
    except Exception as ex:
        # cryptography raises InvalidSignature, grouped defensively for reviewer
        if ex.__class__.__name__ == "InvalidSignature":
            return False
        raise
