<template>
    <div class="info">
        <h1 class="mb-3">Информация о сайте</h1>
        <ul class="list-group list-group-flush">
            <li class="fs-5 list-group-item">
                <p class="fs-3 fw-semibold">
                    Данный сайт создан для генерации математических выражений
                </p>
                <p class="fw-normal mt-2">
                    Преподаватель создает варианты задания для решения математических выражений.
                </p>
                <p class="fw-normal mt-2">
                    Студент решает задачи, которые были предложены преподавателем.
                </p>
            </li>
            <li class="fs-5 list-group-item">
                <p class="fs-3 fw-semibold">
                    Используемые технологии:
                </p>
                <p class="fw-normal mt-2">
                    Django
                </p>
                <p class="fw-normal mt-2">
                    Django REST Framework
                </p>
                <p class="fw-normal mt-2">
                    Vue.js
                </p>
                <p class="fw-normal mt-2">
                    Bootstrap 5
                </p>
                <p class="fw-normal mt-2">
                    MySQL
                </p>
                <p class="fw-normal mt-2">
                    Python
                </p>
                <p class="fw-normal mt-2">
                    JavaScript
                </p>
                <p class="fw-normal mt-2">
                    SymPy
                </p>
            </li>

            <li class="fs-5 list-group-item">
                <p class="fs-3 fw-semibold">
                    Если у вас возникли проблемы при работе с сайтом, обратитесь по адресу:
                </p>
                <p class="font-monospace mt-2">
                    help@pdproject.com
                </p>
            </li>
            <li class="fs-5 list-group-item">
                <p class="fs-3 fw-semibold">
                    Тест работы LaTeX
                </p>
            </li>
        </ul>
        <div class="form-floating mt-3">
            <textarea class="form-control" placeholder="Formula" id="floatingTextarea" v-model="formula" cols="30" rows="10"></textarea>
            <label for="floatingTextarea">Formula</label>
        </div>
        <div class="d-flex justify-content-center mt-5">
            <vue-mathjax :formula="formula"></vue-mathjax>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Info',
    data() {
        return {
            formula: '$$x = {-b \\pm \\sqrt{b^2-4ac} \\over 2a}.$$',
        }
    }
}
</script>

<style scoped>

</style>