<template>
    <div class="main">
        <div class="image d-flex justify-content-center mt-3 mb-4">
            <img class="shadow-lg p-3 mb-5 bg-body rounded" :src="require('@/assets/logo-novacproject.svg')"
                style="width: 250px;" />
        </div>
        <div class="mb-5 mt-5">
            <p class="fs-1 text-center fw-bold">Генератор заданий</p>
            <p class="text-center fs-3">Данный сервис сделан в рамках Проектной деятельности Московского Политеха</p>
        </div>
        <div class="mb-5 mt-5">
            <p class="fw-semibold fs-4 mt-4">В рамках проекта реализован следующий функционал:</p>
            <div class="mt-2 ms-3">
                <p class="fw-normal fs-5">Реализована регистрация студента и преподавателя</p>
                <p class="fw-normal fs-5">Реализована валидация вводимых данных</p>
                <p class="fw-normal fs-5">Реализована авторизация студента или преподавателя</p>
                <p class="fw-normal fs-5">Создан генератор заданий с четырьмя уровнями сложности</p>
                <p class="fw-normal fs-5">Реализована генерация заданий и вывод этих заданий</p>
            </div>
        </div>

        <div class="mb-5 mt-5">
            <p class="fw-semibold fs-4 mt-4">Будущая реализация предполагает:</p>
            <div class="mt-2 ms-3">
                <p class="fw-normal fs-5">Расширение уровней сложности до 6</p>
                <p class="fw-normal fs-5">Оптимизация непосредственно генератора для повышения качества валидности выражений</p>
                <p class="fw-normal fs-5">Добавление многопоточности для генерации выражений</p>
                <p class="fw-normal fs-5">Авторизация через социальные сети</p>

            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'Main'
}
</script>

<style scoped>

</style>