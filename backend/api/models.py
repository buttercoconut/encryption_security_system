"""Pydantic models for API payloads."""

from pydantic import BaseModel, Field
from typing import Optional

class EncryptRequest(BaseModel):
    data: str = Field(..., description="Plaintext data to encrypt")
    key_id: Optional[str] = Field(None, description="Optional key identifier; if omitted, default key is used")

class EncryptResponse(BaseModel):
    ciphertext: str
    key_id: str

class DecryptRequest(BaseModel):
    ciphertext: str
    key_id: str

class DecryptResponse(BaseModel):
    plaintext: str

class KeyCreateRequest(BaseModel):
    key_name: str

class KeyCreateResponse(BaseModel):
    key_id: str
    key_name: str
