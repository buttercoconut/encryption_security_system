# security.py
from cryptography.fernet import Fernet

# Simple key generation
def generate_key() -> bytes:
    return Fernet.generate_key()

# Encryption/Decryption helpers

def encrypt(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(token: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.decrypt(token)
