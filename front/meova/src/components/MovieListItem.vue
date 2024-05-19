<template>
  <div>
    <div class="movie-item">
      <RouterLink
        class="nav-link"
        :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
      >
        <img
          :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
          alt="movie-poster"
          class="movie-image"
        />
        <p class="movie-title">{{ movie.title }}</p>
      </RouterLink>
      <div class="overview-box">
        <p class="overview">{{ movie.overview }}</p>
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
  width: 300px;
}
.movie-title {
  font-size: 25px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.movie-image {
  height: 340px;
  width: 230px;
}

.overview-box {
  width: 250px;
}
.overview {
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 보여줄 줄 수 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

</style>
