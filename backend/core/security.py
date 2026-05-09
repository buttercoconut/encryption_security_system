"""Core security utilities: encryption, decryption, key generation."""

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Simple in-memory key store for demo purposes
_key_store = {}

# AES-256 GCM parameters
_KEY_SIZE = 32  # 256 bits
_NONCE_SIZE = 12


def generate_key() -> str:
    key = os.urandom(_KEY_SIZE)
    key_id = base64.urlsafe_b64encode(os.urandom(16)).decode("utf-8")
    _key_store[key_id] = key
    return key_id


def _get_key(key_id: str) -> bytes:
    key = _key_store.get(key_id)
    if not key:
        raise ValueError("Key not found")
    return key


def encrypt_data(plaintext: str, key_id: str) -> str:
    key = _get_key(key_id)
    nonce = os.urandom(_NONCE_SIZE)
    encryptor = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend()).encryptor()
    ct = encryptor.update(plaintext.encode("utf-8")) + encryptor.finalize()
    return base64.urlsafe_b64encode(nonce + encryptor.tag + ct).decode("utf-8")


def decrypt_data(ciphertext: str, key_id: str) -> str:
    key = _get_key(key_id)
    raw = base64.urlsafe_b64decode(ciphertext.encode("utf-8"))
    nonce = raw[:_NONCE_SIZE]
    tag = raw[_NONCE_SIZE:_NONCE_SIZE+16]
    ct = raw[_NONCE_SIZE+16:]
    decryptor = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend()).decryptor()
    plaintext = decryptor.update(ct) + decryptor.finalize()
    return plaintext.decode("utf-8")
