<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title mb-3">Sign up</h1>
            
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label class="form-label">Никнейм</label>
                        <input type="text" name="username" class="form-control" v-model="username">
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Электронная почта</label>
                        <input type="email" name="email" class="form-control" v-model="email">
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Пароль</label>
                        <input type="password" name="password1" class="form-control" v-model="password1">
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Повторите пароль</label>
                        <input type="password" name="password2" class="form-control" v-model="password2">
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import {toast} from 'bulma-toast'
    export default {
        name: 'SignUp',
        data() {
            return {
                username: '',
                email: '',
                password1: '',
                password2: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                
                this.errors = []
                if (this.username === '') {
                    this.errors.push('The username is missing')
                }
                if (this.email === '') {
                    this.errors.push('The email is missing')
                }
                if (this.password1 === '') {
                    this.errors.push('The password is too short')
                }
                if (this.password1 !== this.password2) {
                    this.errors.push('The password are not matching')
                }
                if (!this.errors.length) {
                    this.$store.commit('setIsLoading', true)
                    const formData = {
                        username: this.username,
                        email: this.email,
                        password: this.password1
                    }
                    await axios
                        .post('/api/v1/users/', formData)
                        .then(response => {
                            toast({
                                message: 'Account was created, please log in',
                                type: 'is-success',
                                dismissible: true,
                                pauseOnHover: true,
                                duration: 2000,
                                position: 'bottom-right',
                            })
                            this.$router.push('/login')
                        })
                        .catch(error => {
                            if (error.response) {
                                for (const property in error.response.data) {
                                    this.errors.push(`${property}: ${error.response.data[property]}`)
                                }
                            } else if (error.message) {
                                this.errors.push('Something went wrong. Please try again!')
                            }
                        })
                    
                    this.$store.commit('setIsLoading', false)
                }
            }
        }
    }
</script>