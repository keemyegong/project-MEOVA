
<template>
    <div>
        <h1>{{ director.name }}</h1>
        <hr>
        <h3>감독 영화</h3>
        <div v-for="movie in director.movies">
        <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
            <p>{{ movie.title }}</p>
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image">
            <p>{{ movie.overview }}</p>
        </RouterLink>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute, RouterLink } from 'vue-router'

const store = useMovieStore()
const route = useRoute()
const director = ref(null)

const directorId = route.params['id']

axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/directors/${directorId}/`
})
.then((response) => {
    console.log(response)
    director.value = response.data
})
.catch((error) => {
    console.log(error)
})
</script>

<style scoped>
.movie-image {
  width: 200px;
}
</style>