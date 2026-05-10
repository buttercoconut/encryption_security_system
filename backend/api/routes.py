"""FastAPI router for encryption endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..core.security import encrypt_data, decrypt_data, generate_key
from ..core.dependencies import get_current_user
from .models import (
    EncryptRequest,
    EncryptResponse,
    DecryptRequest,
    DecryptResponse,
    KeyCreateRequest,
    KeyCreateResponse,
)

router = APIRouter(prefix="/api", tags=["encryption"])

@router.post("/encrypt", response_model=EncryptResponse)
async def encrypt_endpoint(
    req: EncryptRequest,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    key_id = req.key_id or "default"
    try:
        ciphertext = encrypt_data(req.data, key_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return EncryptResponse(ciphertext=ciphertext, key_id=key_id)

@router.post("/decrypt", response_model=DecryptResponse)
async def decrypt_endpoint(
    req: DecryptRequest,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    try:
        plaintext = decrypt_data(req.ciphertext, req.key_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return DecryptResponse(plaintext=plaintext)

@router.post("/keys", response_model=KeyCreateResponse)
async def create_key(
    req: KeyCreateRequest,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user),
):
    key_id = generate_key(req.key_name, db)
    return KeyCreateResponse(key_id=key_id, key_name=req.key_name)
