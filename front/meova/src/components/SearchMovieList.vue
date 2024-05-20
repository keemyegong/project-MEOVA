<template>
    <div>
        <div>
            <SearchMovieListItem 
                v-for="movie in movies"
                :key="movie.id"
                :movie="movie"
            />    
        </div>
    </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import SearchMovieListItem from '@/components/SearchMovieListItem.vue'

defineProps({
    movies: Array
})
const store = useMovieStore()

onMounted(() => {
  store.getPopularMovies()
})


</script>

<style scoped>
.movie-category-title {
    margin-top: 0px;
    margin-bottom: 50px;

    text-align: center;
    font-size: 50px;
    font-family: "Caprasimo", serif;
    font-weight: 400;
    font-style: normal;
}
</style>