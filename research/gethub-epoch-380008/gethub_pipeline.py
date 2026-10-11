"""Review-only GETHUB Epoch 380008 local keyed-integrity validator.

This checks configured values and produces an HMAC. It does NOT establish wallet
control, an external signature, blockchain transactions, or independent Echo.
"""
from __future__ import annotations

import hashlib
import hmac
import os
import re

EXPECTED_EPOCH = 380008
_WALLET_RE = re.compile(r"0x[0-9a-fA-F]{40}\Z")
_DOMAIN = b"GETHUB-PIPELINE-HMAC-SHA256-v1\x00"


class PipelineError(Exception):
    """Base type for expected fail-closed validator errors."""


class PipelineConfigurationError(PipelineError):
    """Required local configuration is absent or malformed."""


class PipelineInputError(PipelineError):
    """Unacceptable or noncanonical input."""


class PipelineAuthorizationError(PipelineError):
    """Local allowlist check did not pass."""


def _canonical_wallet(wallet: str) -> str:
    if not isinstance(wallet, str) or _WALLET_RE.fullmatch(wallet) is None:
        raise PipelineInputError("wallet must be a 20-byte 0x-prefixed hex address")
    return wallet.lower()


def _load_configuration() -> tuple[bytes, str]:
    raw_secret = os.environ.get("EPIENTER_STATE", "")
    secret = raw_secret.encode("utf-8")
    if len(secret) < 32:
        raise PipelineConfigurationError("EPIENTER_STATE must contain at least 32 UTF-8 bytes")
    configured_wallet = os.environ.get("GETHUB_AUTHORIZED_WALLET", "")
    try:
        canonical = _canonical_wallet(configured_wallet)
    except PipelineInputError as exc:
        raise PipelineConfigurationError("GETHUB_AUTHORIZED_WALLET is missing or malformed") from exc
    return secret, canonical


def automax_sync_node(coord_matrix: bytes, epoch: int, *, wallet: str) -> str:
    """Calculate a deterministic local HMAC; NOT an independent attestation."""
    if not isinstance(coord_matrix, bytes) or len(coord_matrix) == 0:
        raise PipelineInputError("coord_matrix must be nonempty bytes")
    if type(epoch) is not int or epoch != EXPECTED_EPOCH:
        raise PipelineInputError("epoch does not match the configured epoch")
    canonical = _canonical_wallet(wallet)
    secret, authorized = _load_configuration()
    if not hmac.compare_digest(canonical, authorized):
        raise PipelineAuthorizationError("wallet is not on the exact local allowlist")

    payload = (
        _DOMAIN
        + epoch.to_bytes(8, "big")
        + bytes.fromhex(canonical[2:])
        + len(coord_matrix).to_bytes(8, "big")
        + coord_matrix
    )
    return hmac.new(secret, payload, hashlib.sha256).hexdigest()


def verify_pipeline_sync(
    coord_matrix: bytes,
    epoch: int = EXPECTED_EPOCH,
    wallet: str = "",
) -> tuple[bool, str]:
    """Return fail-closed local integrity status with no secret contents in errors."""
    try:
        return True, automax_sync_node(coord_matrix, epoch, wallet=wallet)
    except PipelineError as exc:
        return False, f"HOLD: {exc}"
