<template>
    <div>StudentsDo</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'StudentsDo',
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
    // mounted() {
    //     this.getTask()
    // },
    // methods: {
    //     async getTask() {
    //         this.$store.commit('setIsLoading', true)
    //         await axios
    //             .post('/test_generator/show_test/', {
    //                 headers: { 'Authorization': 'Token ' + this.$store.state.token }
    //             })
    //             .then(response => {
    //                 this.tasks = response.data
    //                 this.isGeneratedTasks = true
    //             })
    //             .catch(error => {
    //                 if (error.response){
    //                     this.isEmail = error.response.data.detail
    //                 }
    //                 console.log(error)
    //                 this.isGeneratedTasks = false
    //             })
    //         this.$store.commit('setIsLoading', false)
    //     },
    //     async generateTask() {
    //         this.$store.commit('setIsLoading', true)
    //         this.processGenerate = 'Генерируется вариант'

    //         await axios
    //             .post('/test_generator/generate/', {
    //                 headers: { 'Authorization': 'Token ' + this.$store.state.token }
    //             })
    //             .then(response => {
    //                 this.profile = response.data
    //                 this.processGenerate = 'Вариант сгенерирован'
    //                 this.$router.push('/account')
    //             })
    //             .catch(error => {
    //                 console.log(error)
    //                 this.processGenerate = 'Ошибка'
    //             })

    //         this.$store.commit('setIsLoading', false)
    //     }
    // }
}
</script>

<style scoped>

</style>