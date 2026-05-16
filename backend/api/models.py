# models.py
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

class Key(BaseModel):
    id: int
    key_value: str

class Data(BaseModel):
    id: int
    user_id: int
    encrypted_payload: str

class EncryptionPolicy(BaseModel):
    id: int
    algorithm: str
    key_id: int
