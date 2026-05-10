"""Encryption utilities using Fernet (AES 128 in CBC mode)."""

import base64
import os
from cryptography.fernet import Fernet
from sqlalchemy.orm import Session
import uuid
from ..database.database import Key, Data

# In a real system keys would be stored securely (e.g., KMS). Here we keep them in DB.

def _get_key_bytes(key_id: str, db: Session) -> bytes:
    key_obj = db.query(Key).filter(Key.key_id == key_id).first()
    if not key_obj:
        raise ValueError(f"Key {key_id} not found")
    return base64.urlsafe_b64decode(key_obj.key_value)

def encrypt_data(plaintext: str, key_id: str, db: Session) -> str:
    key_bytes = _get_key_bytes(key_id, db)
    f = Fernet(base64.urlsafe_b64encode(key_bytes))
    return f.encrypt(plaintext.encode()).decode()

def decrypt_data(ciphertext: str, key_id: str, db: Session) -> str:
    key_bytes = _get_key_bytes(key_id, db)
    f = Fernet(base64.urlsafe_b64encode(key_bytes))
    return f.decrypt(ciphertext.encode()).decode()

def generate_key(key_name: str, db: Session) -> str:
    # Generate a 32-byte key for Fernet
    key_bytes = os.urandom(32)
    key_value = base64.urlsafe_b64encode(key_bytes).decode()
    key_obj = Key(key_id=str(uuid.uuid4()), key_name=key_name, key_value=key_value)
    db.add(key_obj)
    db.commit()
    db.refresh(key_obj)
    return key_obj.key_id
