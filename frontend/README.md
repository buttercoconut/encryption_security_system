# Encryption Security System Frontend

## Overview
This Vue 3 application provides a simple UI to interact with the backend encryption API. It allows users to generate a key, encrypt plaintext, and decrypt ciphertext.

## Project Structure
```
frontend/
├─ src/
│  ├─ components/
│  │  └─ EncryptionComponent.vue
│  ├─ views/
│  ├─ App.vue
│  └─ main.js
└─ README.md
```

## Getting Started
1. **Install dependencies**
   ```bash
   npm install
   ```
2. **Run the dev server**
   ```bash
   npm run dev
   ```
3. **Open** `http://localhost:5173` in your browser.

## Notes
- The frontend assumes the backend is running on `http://localhost:8000`.
- For production, configure the API base URL via environment variables.

---

© 2026 Encryption Security System
