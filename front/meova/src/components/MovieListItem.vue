<template>
    <div>
        <div class="movie-item">
        <b @click="goMovieDetail">{{ movie.title }}</b>
        <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image">
        <p>{{ movie.overview }}</p>
        </div>
    </div>
</template>
  
<script setup>
import { useRouter } from 'vue-router'
import { useMovieStore } from '@/stores/movie'

const props = defineProps({
    movie: Object
})

const store = useMovieStore()
const router = useRouter()
const goMovieDetail = function () {
    console.log(props.movie.id)
    router.push({ name: 'MovieDetailView', params: { 'id': props.movie.id}})
}


</script>

<style scoped>
.movie-item {
    width: 500px;
}

.movie-image {
    width: 40%;
}
</style>
  