
<template>
    <div>
        <div class="movie-category-title">
            {{ director.name }}
        </div>
        <div>
            <SearchMovieListItem
                v-for="movie in director.movies"
                :key="movie.id"
                :movie="movie"
            />
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute, RouterLink } from 'vue-router'
import SearchMovieListItem from '@/components/SearchMovieListItem.vue'

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
.movie-category-title {
    margin-top: 0px;
    margin-bottom: 50px;

    text-align: center;
    font-size: 50px;
    font-family: "Bagel Fat One", system-ui;
    font-weight: 400;
    font-style: normal;
}
</style>