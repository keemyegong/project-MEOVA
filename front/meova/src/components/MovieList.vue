<template>
    <div>
        <h3>Recommend Movies</h3>
        <p>곧 추가될 예정이에요!</p>
        <hr>
        <RouterLink :to="{ name: 'PopularMovieView' }">
            <h3>Popular Movies</h3>
        </RouterLink>
        <MovieListItem
            v-for="movie in store.popular_movies"
            :key="movie.id"
            :movie="movie"
        />
        <hr>
        <RouterLink :to="{ name: 'ReleaseMovieView' }">
            <h3>Release Movies</h3>
        </RouterLink>
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
import { useRouter, RouterLink } from 'vue-router'

const store = useMovieStore()

</script>