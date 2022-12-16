<template>
  <h1 class="title mb-3">Верификация электронной почты</h1>
  <h5 v-if="message['message']"> {{message['message']}}</h5>
</template>
  
<script>
import { throwStatement } from '@babel/types';
import axios from 'axios'
export default {
  name: 'VerifyEmail',
  data() {
    return{
      message: []
    }
  },
  computed: {
    uid() {
      return this.$route.params.uid;
    },
    token() {
      return this.$route.params.token;
    }
  },
  methods: {
    async verifyEmailAccount() {
      try {
        const url_params = this.uid + '/' + this.token + '/'
        const response = await axios.get('/users/reg/success/' + url_params)
        this.message = response.data
      } catch (e) {
        this.message = 'Ошибка. Попробуйте еще раз!'
      }
    },
  },
  mounted() {
    this.verifyEmailAccount();
  }
};
</script>