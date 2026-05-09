<template>
  <div class="encryption-component">
    <h2>Encryption Demo</h2>
    <div class="form-group">
      <label for="plaintext">Plaintext</label>
      <textarea id="plaintext" v-model="plaintext" rows="3"></textarea>
    </div>
    <div class="form-group">
      <label for="keyId">Key ID</label>
      <input id="keyId" v-model="keyId" type="text" placeholder="Generated key ID" />
    </div>
    <div class="buttons">
      <button @click="generateKey">Generate Key</button>
      <button @click="encrypt">Encrypt</button>
      <button @click="decrypt">Decrypt</button>
    </div>
    <div class="result" v-if="ciphertext">
      <h3>Ciphertext</h3>
      <pre>{{ ciphertext }}</pre>
    </div>
    <div class="result" v-if="decryptedText">
      <h3>Decrypted Text</h3>
      <pre>{{ decryptedText }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const plaintext = ref('');
const keyId = ref('');
const ciphertext = ref('');
const decryptedText = ref('');

const apiBase = 'http://localhost:8000/api';

async function generateKey() {
  try {
    const res = await axios.post(`${apiBase}/key/generate`);
    keyId.value = res.data.key_id;
    alert('Key generated: ' + keyId.value);
  } catch (e) {
    console.error(e);
    alert('Error generating key');
  }
}

async function encrypt() {
  try {
    const res = await axios.post(`${apiBase}/encrypt`, {
      plaintext: plaintext.value,
      key_id: keyId.value,
    });
    ciphertext.value = res.data.ciphertext;
    decryptedText.value = '';
  } catch (e) {
    console.error(e);
    alert('Encryption failed');
  }
}

async function decrypt() {
  try {
    const res = await axios.post(`${apiBase}/decrypt`, {
      ciphertext: ciphertext.value,
      key_id: keyId.value,
    });
    decryptedText.value = res.data.plaintext;
  } catch (e) {
    console.error(e);
    alert('Decryption failed');
  }
}
</script>

<style scoped>
.encryption-component {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
  font-family: Arial, sans-serif;
}
.form-group {
  margin-bottom: 1rem;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
textarea,
input {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
}
.buttons {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
button {
  padding: 0.5rem 1rem;
  font-size: 1rem;
}
.result {
  background: #f9f9f9;
  padding: 0.5rem;
  margin-top: 1rem;
}
pre {
  white-space: pre-wrap;
  word-break: break-all;
}
</style>
