"""FastAPI application entry point."""

from fastapi import FastAPI
from .api.routes import router as api_router
from .database.database import Base, engine

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Encryption Security System API")
app.include_router(api_router)

# Simple token endpoint for demo (not secure)
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta
from .core.config import settings

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm):
    # In a real app verify username/password
    if form_data.username != "admin" or form_data.password != "admin":
        return {"error": "Invalid credentials"}
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": form_data.username, "exp": datetime.utcnow() + access_token_expires}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return {"access_token": encoded_jwt, "token_type": "bearer"}
