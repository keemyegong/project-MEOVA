<template>
  <div>
    <div v-if="result">
      <h3>오늘의 테마 : {{ theme }}</h3>
      <p></p>
      <div class="movie-item">
        <MovieListItem
          v-for="movie in recommendmovies"
          :key="movie.id"
          :movie="movie"
        />
      </div>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
import axios from "axios";
import { computed, onMounted, ref, watch } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieListItem from "./MovieListItem.vue";
const recommendations = computed(() => {
  return movieStore.recommendations;
});
const recommendmovies = computed(() => {
  console.log(movieStore.recommendmovies);
  return movieStore.recommendmovies;
});

const theme = ref("테마 없음");
const movieIds = ref([]);
const result = ref(null);
const movieStore = useMovieStore();
const extractThemeAndIds = () => {
  if (recommendations.value.message) {
    const themeMatch =
      recommendations.value.message.match(/"(.+?)"라는 컨셉으로/);
    theme.value = themeMatch ? themeMatch[1] : "테마 없음";

    const movieIdPattern = /\*\*.*?\((\d+)\)\*\*/g;
    let match;
    movieIds.value = [];
    while (
      (match = movieIdPattern.exec(recommendations.value.message)) !== null
    ) {
      movieIds.value.push(match[1]);
    }
    console.log(movieIds.value);
    result.value = {
      theme: theme.value,
      movieIds: movieIds.value,
    };

    // Fetch movie details for each movie ID
    movieStore.getRecommendMovieList(movieIds.value);
  }
};
console.log(movieIds);

onMounted(() => {
  movieStore.getRecommendMovies().then(() => {
    extractThemeAndIds();
  });
});

// Watch for changes in recommendations and extract theme and movie IDs
// watch(recommendations, (newVal) => {
//   if (newVal.message) {
//   }
// });
</script>
<style scoped>
.movie-item {
  width: 100%;
  margin-bottom: 150px;
  overflow: auto;
  display: flex;
}
</style>
