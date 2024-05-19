<template>
    <div>
        <RouterLink class="nav-link" :to="{ name: 'PopularMovieView' }">
            <div class="movie-category-title">
                Popular Movies
            </div>
        </RouterLink>
        <div class="movie-item">
        <MovieListItem
            v-for="movie in store.popular_movies"
            :key="movie.id"
            :movie="movie"
        />
        </div>

        <RouterLink class="nav-link" :to="{ name: 'ReleaseMovieView' }">
            <div class="movie-category-title">
                Release Movies
            </div>
        </RouterLink>
        <div class="movie-item">
        <MovieListItem
            v-for="movie in store.release_movies"
            :key="movie.id"
            :movie="movie"
        />
        </div>
        <RouterLink class="nav-link" :to="{ name: 'PopularMovieView' }">
            <div class="movie-category-title">
                Recommended Movies
            </div>
        </RouterLink>
        <p>곧 추가될 예정이에요!</p>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import MovieListItem from '@/components/MovieListItem.vue'
import { useRouter, RouterLink } from 'vue-router'

const store = useMovieStore()

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

.movie-item {
    width: 100%;
    margin-bottom: 150px;
    overflow: auto;
    display: flex;
}

.movie-item::-webkit-scrollbar {
    display: none;
}
</style>