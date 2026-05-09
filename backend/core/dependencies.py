"""Dependency injection utilities."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Dict

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# Dummy user for demonstration
fake_users_db = {
    "alice": {"username": "alice", "id": 1, "is_active": True},
}

def get_current_user(token: str = Depends(oauth2_scheme)) -> Dict:
    # In real implementation, decode JWT and fetch user
    user = fake_users_db.get("alice")
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
    return user
