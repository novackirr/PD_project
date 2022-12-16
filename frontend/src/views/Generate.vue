<template>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-avatar@latest/dist/avatar.min.css" rel="stylesheet">
    <div class="Generate">
        <h1 class="title mb-3">Генератор заданий</h1>

        <div v-if="isEmail">
            {{isEmail}}
        </div>

        <div v-if="tasks.message === 'Извините для вас тест не сгенерирован!'">
            <p>На этой странице вы можете сгенерировать вариант</p>
            <div class="btn-group mb-3" role="group" aria-label="Basic example">
                <button type="button" @click="generateTask()" class="btn btn-primary">Сгенерировать вариант</button>
            </div>
        </div>

        <div v-if="tasks.message !== 'Извините для вас тест не сгенерирован!' && isEmail === ''">
            <p>Для вас уже доступен сгенерированный вариант</p>
        </div>

        <div v-if="tasks.message !== 'Извините для вас тест не сгенерирован!' && isEmail === ''" class="card">
            <div class="card-body">
                <h3 class="card-title">Сгенерированный вариант</h3>
                <div v-for="task in tasks.data">
                    <div class="card mt-4">
                        <div class="card-body">
                            <h5 class="card-subtitle mb-2 text-muted">Задание {{ task.task_number }}</h5>
                            <ul class="list-group list-group-flush">

                                <li class="list-group-item">
                                    <h5 class="card-title">Необходимо вычислить</h5>
                                    <div class="d-flex justify-content-center mt-5">
                                        <vue-mathjax :formula="'$$' + task.example + '$$'"></vue-mathjax>
                                    </div>
                                </li>
                                <li class="list-group-item">
                                    <h5 class="card-title">Ответ</h5>
                                    <div class="d-flex justify-content-center mt-5">
                                        <vue-mathjax :formula="'$$' + task.answer + '$$'"></vue-mathjax>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Main',
    data() {
        return {
            profile: [],
            tasks: [],
            tokeno: '',
            isGeneratedTasks: false,
            processGenerate: '',
            isEmail: ''
        }
    },
    mounted() {
        this.getTask()
    },
    methods: {
        async getTask() {
            this.$store.commit('setIsLoading', true)
            await axios
                .post('/test_generator/show_test/', {
                    headers: { 'Authorization': 'Token ' + this.$store.state.token }
                })
                .then(response => {
                    this.tasks = response.data
                    this.isGeneratedTasks = true
                })
                .catch(error => {
                    if (error.response){
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