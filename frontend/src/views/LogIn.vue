<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title mb-3">Авторизация</h1>
                <form @submit.prevent="submitForm">
                    <div class="mb-3">
                        <label class="form-label">Электронная почта</label>
                        <input type="text" name="email" class="form-control" v-model="email">
                    </div>
                    
                    <div class="mb-3">
                        <label class="form-label">Пароль</label>
                        <input type="password" name="password" class="form-control" v-model="password">
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button type="submit" class="btn btn-primary">Войти</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'LogIn',
        data() {
            return {
                email: '',
                password: '',
                errors: [],
                message: [],
                didn: []
            }
        },
        methods: {
            
            async submitForm() {
                try {
                    const url_params = this.uid + '/' + this.token + '/'
                    const response = await axios.get('/users/reg/success/' + url_params)
                    this.message = response.data
                } catch (e) {
                    this.message = 'Ошибка. Попробуйте еще раз!'
                }

                this.$store.commit('setIsLoading', true)
                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')
                const formData = {
                    email: this.email,
                    password: this.password
                }
                await axios
                    .post('/users/login/', formData)
                    .then(response => {
                        const token = response.data.token
                        this.$store.commit('setToken', token)
                        axios.defaults.headers.common['Authorization'] = 'Token ' + token
                        localStorage.setItem('token', token)
                        // this.$router.push('/account')
                    })
                    .catch(error => {
                        if (error.message) {
                            this.errors.push(error)
                            this.errors.push('Неверный логин или пароль!')
                        }
                    })

                await axios
                    .get('/users/profile/', {
                            headers: {'Authorization': 'Token ' + this.$store.state.token}
                    })
                    .then(response => {
                        this.$store.commit('setUser', {
                            'id': response.data.id,
                            'role': response.data.role,
                            'email_verified': response.data.email_verified,
                        })
                        localStorage.setItem('id', response.data.id)
                        localStorage.setItem('role', response.data.role)
                        localStorage.setItem('email_verified', response.data.email_verified)
                        this.$router.push('/account')
                    })
                    .catch(error => {
                        if (error.message) {
                            console.log(error)
                        }
                    })
                this.$store.commit('setIsLoading', false)
            }
            // async getClient() {
            //     this.$store.commit('setIsLoading', true)
            //     await axios
            //         .get('/users/profile/', {
            //             headers: {'Authorization': 'Token ' + this.$store.state.token}

            //         })
            //         .then(response => {
            //             this.profile = response.data
            //         })
            //         .catch(error => {
            //             console.log(error)
            //         })

            //     this.$store.commit('setIsLoading', false)
            // }
        }
    }
</script>