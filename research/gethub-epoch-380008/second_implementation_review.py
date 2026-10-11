"""Read-only Ed25519 verification through libsodium, separate from OpenSSL.

A second local crypto backend is not a second independent operator or Echo.
No private keys are generated and no signing occurs.
"""
import ctypes
import ctypes.util


def verify_ed25519_with_libsodium(public_key: bytes, message: bytes,
                                  signature: bytes) -> bool:
    if not isinstance(public_key, bytes) or len(public_key) != 32:
        return False
    if not isinstance(signature, bytes) or len(signature) != 64:
        return False
    if not isinstance(message, bytes):
        return False
    name = ctypes.util.find_library("sodium")
    if not name:
        raise RuntimeError("libsodium not installed; independent-backend test unavailable")
    lib = ctypes.CDLL(name)
    lib.sodium_init.restype = ctypes.c_int
    if lib.sodium_init() < 0:
        raise RuntimeError("libsodium initialization failed")
    lib.crypto_sign_verify_detached.argtypes = [
        ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_void_p
    ]
    lib.crypto_sign_verify_detached.restype = ctypes.c_int
    sig = ctypes.create_string_buffer(signature)
    msg = ctypes.create_string_buffer(message or b"\x00")
    pk = ctypes.create_string_buffer(public_key)
    return lib.crypto_sign_verify_detached(sig, msg, len(message), pk) == 0
