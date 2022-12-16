<template>
    <h1 class="mb-3">Информация о студентах</h1>
    <!-- <div class="card">
        <div class="card-body">
            <h4 class="card-title">Студенты без сгенерированного варианта</h4>
            <div class="card">
                <div class="card-body">

                    {{ user.id }}
                    {{ user.email }}
                    {{ user.first_name }} {{ user.middle_name }} {{ user.last_name }}
                    {{ user.student_group }}

                    <div v-for="user in usersWithoutOption" :key="user.id">
                        <div class="card" style="width: 18rem;">
                            <div class="card-body">
                                <h5 class="card-title">Card title</h5>
                                <h6 class="card-subtitle mb-2 text-muted">Card subtitle</h6>
                                <p class="card-text">Some quick example text to build on the card title and make up the
                                    bulk
                                    of the card's content.</p>
                                <a href="#" class="card-link">Card link</a>
                                <a href="#" class="card-link">Another link</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div>{{ usersWithoutOption }}</div>

        </div>
    </div> -->
    <div v-if="usersWithoutOption.length" class="card-body">
        <h3 class="card-title">Студенты без сгенерированного варианта</h3>
        <div v-for="user in usersWithoutOption" :key="user.id">
            <div class="card mt-4">
                <div class="card-body">
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                            <h5 class="card-subtitle mb-2 text-muted">
                                {{ user.first_name }} {{ user.last_name }} {{ user.middle_name }}
                            </h5>
                        </li>

                        <li class="list-group-item">
                            <dl class="row mb-0">
                                <dt class="col-sm-3">Группа: </dt>
                                <dd class="col-sm-9">{{ user.student_group }}</dd>
                                <dt class="col-sm-3">Почта: </dt>
                                <dd class="col-sm-9">{{ user.email }}</dd>
                            </dl>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div v-if="usersWithOption.length" class="card-body mt-3">
        <h3 class="card-title">Студенты, приславшие ответы на задания</h3>
        <div v-for="userWithOption in usersWithOption" :key="userWithOption.id">
            <div class="card mt-4">
                <div class="card-body">
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">
                            <h5 class="card-subtitle mb-2 text-muted">
                                {{ userWithOption.user__first_name }} {{ userWithOption.user__last_name }} {{ userWithOption.user__middle_name }}
                            </h5>
                        </li>

                        <li class="list-group-item">
                            <dl class="row mb-0">
                                <dt class="col-sm-3">Группа: </dt>
                                <dd class="col-sm-9">{{ userWithOption.user__student_group }}</dd>
                                <dt class="col-sm-3">Почта: </dt>
                                <dd class="col-sm-9">{{ userWithOption.user__email }}</dd>
                            </dl>
                            <a class="fs-5" :href="'http://192.168.1.3:8000/test_generator/media/' + userWithOption.decision">Решение</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import axios from 'axios'
export default {
    name: 'StudentsDo',
    data() {
        return {
            profile: [],
            usersWithoutOption: [],
            usersWithOption: [],
            tokeno: '',
            isGeneratedTasks: false,
            processGenerate: '',
            isEmail: ''
        }
    },
    mounted() {
        this.getUserListWithoutOption(),
        this.getUserListWithOption()
    },
    methods: {
        async getUserListWithOption() {
            this.$store.commit('setIsLoading', true)
            await axios
                .post('/users/user_list_with_option/', {
                    headers: { 'Authorization': 'Token ' + this.$store.state.token }
                })
                .then(response => {
                    this.usersWithOption = response.data.data
                })
                .catch(error => {
                    if (error.response) {
                        this.isEmail = error.response.data.detail
                    }
                    console.log(error)
                    this.isGeneratedTasks = false
                })
            this.$store.commit('setIsLoading', false)
        },
        
        async getUserListWithoutOption() {
            this.$store.commit('setIsLoading', true)
            await axios
                .post('/users/user_list_without_option/', {
                    headers: { 'Authorization': 'Token ' + this.$store.state.token }
                })
                .then(response => {
                    this.usersWithoutOption = response.data.data
                })
                .catch(error => {
                    if (error.response) {
                        this.isEmail = error.response.data.detail
                    }
                    console.log(error)
                    this.isGeneratedTasks = false
                })
            this.$store.commit('setIsLoading', false)
        },
        async generateTask() {
            this.$store.commit('setIsLoading', true)
            this.processGenerate = 'Генерируется вариант'

            await axios
                .post('/test_generator/generate/', {
                    headers: { 'Authorization': 'Token ' + this.$store.state.token }
                })
                .then(response => {
                    this.profile = response.data
                    this.processGenerate = 'Вариант сгенерирован'
                    this.$router.push('/account')
                })
                .catch(error => {
                    console.log(error)
                    this.processGenerate = 'Ошибка'
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>

<style scoped>

</style>