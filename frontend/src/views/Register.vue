<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title mb-3">Регистрация</h1>
                <form @submit.prevent="submitForm">
                    
                    <div class="form-floating mb-3">
                        <input type="email" name="email" class="form-control" id="email" placeholder="name@example.com" v-model="email">
                        <label for="email">Электронная почта</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input required type="text" name="last_name" class="form-control" placeholder="Иванов" id="last_name" v-model="last_name">
                        <label for="last_name">Фамилия</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input required type="text" name="first_name" class="form-control" placeholder="Иван" id="first_name" v-model="first_name">
                        <label for="first_name">Имя</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input required type="text" name="middle_name" class="form-control" placeholder="Иванович" id="middle_name" v-model="middle_name">
                        <label for="middle_name">Отчество</label>
                    </div>
                    <div class="form-floating mb-3">
                        <select id="floatingSelect" required class="form-select" name="groups" v-model="selectedGroup">
                            <option disabled selected>Выберите роль</option>
                            <option v-for="group in groups" :value="group">{{ group.name }}</option>
                        </select>
                        <label for="floatingSelect">Роль</label>
                    </div>
                    <div v-if="selectedGroup['id']===1" class="form-floating mb-3">
                        <input required type="text" name="student_group" class="form-control" placeholder="191-363" id="student_group" v-model="student_group">
                        <label for="student_group">Группа</label>
                    </div>
                    <div class="form-floating mb-3">
                        <input required type="password" name="password1" class="form-control" placeholder="******" id="password1" v-model="password1">
                        <label for="password1">Пароль</label>
                    </div>

                    <div class="form-floating mb-3">
                        <input required type="password" name="password2" class="form-control" placeholder="******" id="password2" v-model="password2">
                        <label for="password2">Повторите пароль</label>
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
import { toast } from 'bulma-toast'
export default {
    name: 'SignUp',
    data() {
        return {
            first_name: '',
            last_name: '',
            middle_name: '',
            student_group: '',
            email: '',
            password1: '',
            password2: '',
            groups: [
                {name: 'Студент', id:1},
                {name: 'Преподаватель', id:2}
            ],
            selectedGroup: {
                id: 0
            },
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)
            this.errors = []
            if (this.password1 === '') {
                this.errors.push('The password is too short')
            }
            if (this.email === '') {
                this.errors.push('The email is missing')
            }
            if (this.email.length > 254) {
                this.errors.push('Почта может не содержать более 254 символов')
            }
            if (this.first_name.length > 150) {
                this.errors.push('Имя может не содержать более 150 символов')
            }
            if (this.middle_name.length > 100) {
                this.errors.push('Отчество может не содержать более 100 символов')
            }
            if (this.student_group.length > 30) {
                this.errors.push('Группа может не содержать более 30 символов')
            }
            // if ( /^\d\d\d-\d\d\d$/.test(this.student_group) === false) {
            //     this.errors.push('Группа должна быть в формате 111-111, пример 191-363')
            // }
            if (this.password1 === '') {
                this.errors.push('The password is too short')
            }
            if (this.password1 !== this.password2) {
                this.errors.push('The password are not matching')
            }
            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                const formData = {
                    first_name: this.first_name,
                    last_name: this.last_name,
                    middle_name: this.middle_name,
                    student_group: this.student_group,
                    email: this.email,
                    password: this.password1,
                    groups: this.selectedGroup['name']
                }
                await axios
                    .post('/users/reg/', formData)
                    .then(response => {
                        toast({
                            message: 'Аккаунт был создан, проверьте свою почту',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                        this.$router.push('/login')
                    })
                    .catch(error => {
                        // if (error.response) {
                            
                        //     for (const property in error.response.data) {
                        //         this.errors.push(`${property}: ${error.response.data[property]}`)
                        //     }
                        // } else if (error.message) {
                        //     this.errors.push('Something went wrong. Please try again!')
                        // }
                        if (error.message) {
                            this.errors.push(error)
                            this.errors.push('Что-то пошло не так. Попробуйте еще раз!')
                        }
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
    }
}
</script>