# Encryption Security System Backend

## Overview
This repository contains a minimal FastAPI backend that demonstrates basic encryption, decryption, and key management using AES‑256 GCM. It is intended as a starting point for a more comprehensive security system.

## Project Structure
```
backend/
├─ api/
│  ├─ routes.py          # API endpoints
│  └─ models.py          # Pydantic models
├─ core/
│  ├─ config.py          # Application settings
│  ├─ dependencies.py    # Dependency injection helpers
│  └─ security.py        # Encryption utilities
├─ database/
│  └─ database.py        # SQLAlchemy session factory
└─ main.py               # FastAPI application entry point
```

## Getting Started
1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy cryptography pydantic
   ```
2. **Run the server**
   ```bash
   uvicorn backend.main:app --reload
   ```
3. **Test the API**
   - Generate a key: `POST /api/key/generate`
   - Encrypt: `POST /api/encrypt` with `{"plaintext": "Hello", "key_id": "<generated_key_id>"}`
   - Decrypt: `POST /api/decrypt` with `{"ciphertext": "<ciphertext>", "key_id": "<generated_key_id>"}`

## Notes
- This implementation uses an in‑memory key store for demonstration. In production, store keys securely (e.g., HSM, KMS).
- Authentication is mocked; replace `get_current_user` with real JWT validation.
- The database layer is prepared but not used in this minimal example.

---

© 2026 Encryption Security System
