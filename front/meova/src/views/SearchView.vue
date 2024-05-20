<template>
  <div>
    <div class="movie-category-title">{{ route.params.q }}</div>

    <SearchMovieList :movies="store.movies" />
  </div>
</template>

<script setup>
import { RouterLink, useRoute, useRouter } from "vue-router";
import { ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import SearchMovieList from "@/components/SearchMovieList.vue";
const store = useMovieStore();

const route = useRoute();
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
  height: 95%;
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
  background-color: #ccd3ca;
  color: white;
}
.withwho {
  background-color: #b2c8df;
  color: white;
}
.runtime {
  background-color: #eed3d9;
  color: white;
}
.genre {
  background-color: #f4d19b;
  color: white;
}
</style>
