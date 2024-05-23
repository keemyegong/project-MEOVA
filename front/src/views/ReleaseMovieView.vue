<template>
    <div>
        <div class="movie-category-title">
            Release Movies
        </div>
        <SearchMovieList
            :movies="store.release_movies"
        />
    </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie'
import SearchMovieList from '@/components/SearchMovieList.vue';

const store = useMovieStore()

onMounted(() => {
  store.getReleaseMovies()
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