<template>
  <div class="encryption-box">
    <h2>Data Encryption / Decryption</h2>
    <textarea v-model="plainText" placeholder="Enter plain text" rows="4" class="form-control"></textarea>
    <button @click="encrypt" class="btn btn-primary mt-2">Encrypt</button>
    <textarea v-model="encryptedText" placeholder="Encrypted output" rows="4" class="form-control mt-2" readonly></textarea>
    <button @click="decrypt" class="btn btn-secondary mt-2">Decrypt</button>
    <textarea v-model="decryptedText" placeholder="Decrypted output" rows="4" class="form-control mt-2" readonly></textarea>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const plainText = ref('');
const encryptedText = ref('');
const decryptedText = ref('');

const apiBase = import.meta.env.VITE_API_BASE || 'http://localhost:8000';

const encrypt = async () => {
  try {
    const res = await axios.post(`${apiBase}/api/encrypt`, {
      data: plainText.value,
    });
    encryptedText.value = res.data.encrypted;
  } catch (e) {
    console.error(e);
    alert('Encryption failed');
  }
};

const decrypt = async () => {
  try {
    const res = await axios.post(`${apiBase}/api/decrypt`, {
      encrypted: encryptedText.value,
    });
    decryptedText.value = res.data.decrypted;
  } catch (e) {
    console.error(e);
    alert('Decryption failed');
  }
};
</script>

<style scoped>
.encryption-box {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
}
</style>
