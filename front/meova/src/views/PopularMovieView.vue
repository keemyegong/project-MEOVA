<template>
    <div>
        <div class="movie-category-title">
            Popular Movies
        </div>
        <div v-for="movie in store.popular_movies" :key="movie.id">
            <div class="movie-card mb-3">
                <div class="row g-0">
                    <div class="col-2">
                    <RouterLink :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                    <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image img-fluid rounded">
                    </RouterLink>
                    </div>
                    <div class="col-10">
                    <div class="ms-3 me-3 card-body">
                        <RouterLink class="nav-link" :to="{ name: 'MovieDetailView', params: { id: movie.id } }">
                            <p class="movie-title card-title">{{ movie.title }}</p>
                        </RouterLink>
                        <p class="overview card-text">{{ movie.overview }}</p>
                        <p class="movie-info card-text">
                            <button class="btn genre" v-for="genre in movie.genres">
                                {{ genre.name }}
                            </button>
                            <button class="btn runtime">{{ movie.runtime }}분</button>
                            <button class="btn country">{{ movie.origin_country }}</button>
                            <button class="btn withwho" v-for="keyword in movie.keywords.slice(0, 5)">
                                {{ keyword.name }}
                            </button>
                        </p>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

onMounted(() => {
  store.getPopularMovies()
})


</script>

<style scoped>
.movie-card {
    padding-bottom: 50px;
}
.movie-title {
    font-size: 25px;
    margin-top: 10px;
    margin-bottom: 10px;
}
.movie-image {
    height:95%;
}
.movie-category-title {
    margin-top: 0px;
    margin-bottom: 50px;

    text-align: center;
    font-size: 50px;
    font-family: "Caprasimo", serif;
    font-weight: 400;
    font-style: normal;
}
.overview {
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 보여줄 줄 수 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.movie-info > button {
  margin-right: 3px;
  margin-bottom: 3px;
}
.country {
  background-color: #CCD3CA;
  color: white;
}
.withwho {
  background-color: #B2C8DF;
  color: white;
}
.runtime {
  background-color: #eed3d9;
  color: white;
}
.genre {
  background-color: #F4D19B; 
  color: white;
}
</style>