
<template>
    <p @click="goMain">main</p>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'

const router = useRouter()
const goMain = function () {
    router.push({name:'MainView'})
}
</script>

<style scoped>
</style>
