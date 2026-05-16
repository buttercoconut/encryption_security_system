<template>
  <div>
    <h2>Encrypt Data</h2>
    <input v-model="plainText" placeholder="Enter text" />
    <button @click="encrypt">Encrypt</button>
    <p>Encrypted: {{ encrypted }}</p>

    <h2>Decrypt Data</h2>
    <input v-model="cipherText" placeholder="Enter encrypted text" />
    <button @click="decrypt">Decrypt</button>
    <p>Decrypted: {{ decrypted }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      plainText: '',
      encrypted: '',
      cipherText: '',
      decrypted: ''
    }
  },
  methods: {
    async encrypt() {
      const res = await axios.post('http://localhost:8000/encrypt', {
        encrypted_payload: this.plainText
      })
      this.encrypted = res.data.encrypted_payload
    },
    async decrypt() {
      const res = await axios.post('http://localhost:8000/decrypt', {
        encrypted_payload: this.cipherText
      })
      this.decrypted = res.data.decrypted_payload
    }
  }
}
</script>
