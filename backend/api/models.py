"""Pydantic models for API payloads."""

from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    is_active: bool

# Additional models can be added here
