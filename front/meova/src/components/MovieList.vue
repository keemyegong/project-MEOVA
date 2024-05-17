<template>
    <div>
        <h2>Movie List</h2>
        <h3>Recommend Movies</h3>
        <p>곧 추가될 예정이에요!</p>
        <hr>
        <h3 @click="goPopularMovies">Popular Movies</h3>
            <MovieListItem
                v-for="movie in store.popular_movies"
                :key="movie.id"
                :movie="movie"
            />
        <hr>
        <h3 @click="goReleaseMovies">Release Movies</h3>
            <MovieListItem
                v-for="movie in store.release_movies"
                :key="movie.id"
                :movie="movie"
            />
    </div>
  </template>
  
<script setup>
import { useMovieStore } from '@/stores/movie'
import MovieListItem from '@/components/MovieListItem.vue'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

const goPopularMovies = function () {
    router.push({ name: 'PopularMovieView'})
}

const goReleaseMovies = function () {
    router.push({ name: 'ReleaseMovieView'})
}
</script>
  