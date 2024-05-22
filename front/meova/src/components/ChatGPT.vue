<template>
  <div>
    <div v-if="result">
      <div class="movie-info">
        <span>챗GPT가</span>
        <span class="display-6">❝</span>
          <span class="theme">
            {{ theme }}
          </span>
            <span class="display-6">❞</span>
        <span>테마에 맞춰 오늘의 영화 3개를 추천해요!</span>
      </div>
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
      recommendations.value.message.match(/"(.+?)"이라는 컨셉으로/) ||
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

// then으로 대체
// watch(recommendations, (newVal) => {
//   if (newVal.message) {
//   }
// });
</script>
<style scoped>
.movie-item {
  justify-content: center;
  width: 100%;
  margin-bottom: 150px;
  overflow: auto;
  display: flex;
}
.movie-category-title {
  margin-top: 0px;
  text-align: center;
  font-size: 30px;
  font-family: "Bagel Fat One", system-ui;
  font-weight: 400;
  font-style: normal;
}
.movie-info {
  text-align: center;
  font-size: 15px;
  font-weight: 300;
  color: gray;
  margin-bottom: 20px;
}

.theme {
  color: rgb(122, 122, 122);
  margin-left: 7px;
  margin-right: 7px;
  font-size:30px;
  font-family: "Grandiflora One", cursive;
  font-weight: 1000;
  font-style: normal;
  background-color: rgba(197, 197, 197, 0.253);
}
</style>
