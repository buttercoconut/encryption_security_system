# Encryption Security System

## Overview

This repository contains a minimal implementation of an encryption‑based security system. The backend is a FastAPI application that exposes endpoints for encrypting, decrypting, and key generation. The frontend is a Vue 3 SPA that demonstrates the encryption flow.

## Directory Structure

```
backend/
├─ api/
│  ├─ routes.py
│  └─ models.py
├─ core/
│  ├─ config.py
│  ├─ dependencies.py
│  └─ security.py
├─ database/
│  └─ database.py
└─ main.py

frontend/
├─ src/
│  ├─ components/
│  │  └─ EncryptionComponent.vue
│  ├─ views/
│  ├─ App.vue
│  └─ main.js
```

## Running the Application

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be served on `http://localhost:5173` and will communicate with the backend at `http://localhost:8000`.

## Notes

- The encryption logic is intentionally simple and uses AES‑256 in CBC mode with PKCS7 padding.
- In a production system you would store keys securely (e.g., HSM, KMS) and use proper authentication/authorization.
- The current implementation generates a new key for each request; this is for demonstration only.

---

Happy coding!
