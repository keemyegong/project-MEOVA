<template>
    <div>
        <div class="movie-item">
        <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
            <p>{{ movie.title }}</p>
            <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image">
        </RouterLink>
        <p>{{ movie.overview }}</p>
        </div>
    </div>
</template>

<script setup>
import { useRouter, RouterLink } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const props = defineProps({
    movie: Object
})

const store = useMovieStore()
</script>

<style scoped>
.movie-item {
    width: 500px;
}

.movie-image {
    width: 40%;
}
</style>
