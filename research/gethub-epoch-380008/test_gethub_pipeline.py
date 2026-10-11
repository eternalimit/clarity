"""Purely local negative controls for the review-only validator."""
import hmac
import pytest
from gethub_pipeline import (
    EXPECTED_EPOCH,
    PipelineAuthorizationError,
    PipelineInputError,
    automax_sync_node,
    verify_pipeline_sync,
)

WALLET = "0x" + "a261" + ("1" * 36)
SPOOF = "0x" + "a261" + ("2" * 36)
OTHER = "0x" + ("b" * 40)


@pytest.fixture(autouse=True)
def configured_env(monkeypatch):
    monkeypatch.setenv("EPIENTER_STATE", "test-only-key-material-" + "s" * 40)
    monkeypatch.setenv("GETHUB_AUTHORIZED_WALLET", WALLET)


def test_success_local_digest():
    ok, result = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, WALLET)
    assert ok and len(result) == 64
    assert all(c in "0123456789abcdef" for c in result)


def test_repeatable_digest():
    a = automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=WALLET)
    b = automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=WALLET)
    assert hmac.compare_digest(a, b)


def test_payload_tampering_changes_digest():
    a = automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=WALLET)
    b = automax_sync_node(b"coordinateX", EXPECTED_EPOCH, wallet=WALLET)
    assert a != b


@pytest.mark.parametrize("wallet", [SPOOF, OTHER, WALLET[:-1] + "0"])
def test_not_authorized_even_if_prefix_matches(wallet):
    ok, reason = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, wallet)
    assert not ok and reason.startswith("HOLD:")


@pytest.mark.parametrize("wallet", ["0xa261", "0x" + "g" * 40, "abcd", "", None])
def test_malformed_wallet(wallet):
    ok, reason = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, wallet)
    assert not ok and reason.startswith("HOLD:")


def test_case_insensitive_exact_address():
    ok, _ = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, WALLET.upper().replace("0X", "0x"))
    assert ok


@pytest.mark.parametrize("epoch", [1, 380009, True, "380008", -1])
def test_epoch_fail_closed(epoch):
    ok, reason = verify_pipeline_sync(b"coordinates", epoch, WALLET)
    assert not ok and reason.startswith("HOLD:")


@pytest.mark.parametrize("matrix", [b"", None, "coordinates", bytearray(b"x")])
def test_invalid_input_types(matrix):
    ok, reason = verify_pipeline_sync(matrix, EXPECTED_EPOCH, WALLET)
    assert not ok and reason.startswith("HOLD:")


def test_missing_secret(monkeypatch):
    monkeypatch.delenv("EPIENTER_STATE")
    ok, reason = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, WALLET)
    assert not ok and "EPIENTER_STATE" in reason


def test_short_secret(monkeypatch):
    monkeypatch.setenv("EPIENTER_STATE", "short")
    ok, _ = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, WALLET)
    assert not ok


def test_missing_allowlist(monkeypatch):
    monkeypatch.delenv("GETHUB_AUTHORIZED_WALLET")
    ok, reason = verify_pipeline_sync(b"coordinates", EXPECTED_EPOCH, WALLET)
    assert not ok and "GETHUB_AUTHORIZED_WALLET" in reason


def test_secret_change_changes_digest(monkeypatch):
    first = automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=WALLET)
    monkeypatch.setenv("EPIENTER_STATE", "different-test-key-" + "k" * 40)
    second = automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=WALLET)
    assert first != second


def test_exception_types():
    with pytest.raises(PipelineInputError):
        automax_sync_node(b"", EXPECTED_EPOCH, wallet=WALLET)
    with pytest.raises(PipelineAuthorizationError):
        automax_sync_node(b"coordinates", EXPECTED_EPOCH, wallet=SPOOF)
