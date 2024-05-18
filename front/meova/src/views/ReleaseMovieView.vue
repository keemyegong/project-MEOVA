<template>
    <div>
        <h2>Release Movies</h2>
        <div v-for="movie in store.release_movies" :key="movie.id">
            <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                <p>{{ movie.title }}</p>
                <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image">
            </RouterLink>
            <p>{{ movie.overview }}</p>
            <hr>
        </div>
    </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
  store.getReleaseMovies()
})

</script>

<style scoped>
    .movie-image {
        width: 40%;
    }
</style>