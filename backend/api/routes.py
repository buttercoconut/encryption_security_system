"""API routes for encryption operations."""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Dict

from ..core.security import encrypt_data, decrypt_data, generate_key
from ..core.dependencies import get_current_user

router = APIRouter()

class EncryptRequest(BaseModel):
    plaintext: str
    key_id: str

class DecryptRequest(BaseModel):
    ciphertext: str
    key_id: str

@router.post("/encrypt", status_code=status.HTTP_201_CREATED)
async def encrypt_endpoint(req: EncryptRequest, user: Dict = Depends(get_current_user)):
    try:
        ciphertext = encrypt_data(req.plaintext, req.key_id)
        return {"ciphertext": ciphertext}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/decrypt")
async def decrypt_endpoint(req: DecryptRequest, user: Dict = Depends(get_current_user)):
    try:
        plaintext = decrypt_data(req.ciphertext, req.key_id)
        return {"plaintext": plaintext}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/key/generate")
async def generate_key_endpoint(user: Dict = Depends(get_current_user)):
    key_id = generate_key()
    return {"key_id": key_id}
