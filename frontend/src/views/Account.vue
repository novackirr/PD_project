<template>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-avatar@latest/dist/avatar.min.css" rel="stylesheet">
    <div class="Account">
        <!-- <div class="card" style="width: 18rem;"></div> -->
        <div>
            <div class="card">
                <div class="card-body">
                    <div class="d-flex justify-content-between mb-3">
                        <div>
                            <h4 class="card-title">{{ profile.role }}</h4>
                            <h5 class="card-subtitle mb-2 text-muted">{{ profile.last_name }} {{ profile.first_name }}</h5>
                        </div>
                        <div class="image">
                            <img v-if="profile.role==='Студент'" :src="require('@/assets/student.svg')" class="rounded-circle" style="width: 150px;" />
                            <img v-else :src="require('@/assets/teacher.svg')" class="rounded-circle" style="width: 150px;" />
                        </div>
                    </div>

                    <div class="mb-3">
                        <h5 class="card-title">
                            Контактная информация:
                        </h5>
                        <dl class="row">
                            <dt class="col-sm-3">Полное имя: </dt>
                            <dd class="col-sm-9">{{ profile.last_name }} {{ profile.first_name }} {{ profile.middle_name }}</dd>
                            <dt v-if="profile.student_group" class="col-sm-3">Группа: </dt>
                            <dd v-if="profile.student_group" class="col-sm-9">{{ profile.student_group }}</dd>
                            <dt class="col-sm-3">Почта: </dt>
                            <dd class="col-sm-9">{{ profile.email }}</dd>
                        </dl>
                        <button type="button" class="btn btn-outline-primary">Редактировать информацию</button>
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
            profile: []
        }
    },
    mounted() {
            this.getClient()
        },
        methods: {
            async deleteClient() {
                this.$store.commit('setIsLoading', true)
                const clientID = this.$route.params.id
                await axios
                    .post(`/api/v1/clients/delete_client/${clientID}/`)
                    .then(response => {
                        console.log(response.data)
                        this.$router.push('/dashboard/clients')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                this.$store.commit('setIsLoading', false)
            },
            async getClient() {
                this.$store.commit('setIsLoading', true)
                await axios
                    .get(`/users/profile`, {
                        headers: {'Authorization': 'Token ' + this.$store.state.token}

                    })
                    .then(response => {
                        this.profile = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                this.$store.commit('setIsLoading', false)
            }
        }
}
</script>

<style scoped>

</style>