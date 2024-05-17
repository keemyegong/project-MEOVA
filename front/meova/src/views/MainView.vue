
<template>
  <div>
    <h1>MAIN</h1>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from '@/components/MovieList.vue';
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const props = defineProps({
  movie: Object
})

const store = useMovieStore()

onMounted (() => {
  store.getRecommendMovies()
  store.getPopularMovies()
  store.getReleaseMovies()
})
</script>

<style scoped>
</style>