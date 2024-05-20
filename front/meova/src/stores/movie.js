import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useMovieStore = defineStore(
  "movie",
  () => {
    const API_URL = "http://127.0.0.1:8000";

    const recommend_movies = ref([]);
    const popular_movies = ref([]);
    const release_movies = ref([]);
    const movies = ref([]);

    const search = function (q) {
      const { title, genre, keyword, runtime, country } = q;
      axios({
        method: "get",
        url: `${API_URL}/api/v1/meova/search/`,
        params: {
          title,
          genre,
          keyword,
          runtime,
          country,
        },
      }).then((res) => {
        console.log(res);
        movies.value = res.data;
      });
    };
    const getRecommendMovies = function () {
      console.log("추천알고리즘이없어요!");
    };

    const getPopularMovies = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/popular/`,
      })
        .then((response) => {
          console.log(response);
          popular_movies.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const getReleaseMovies = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/release/`,
      })
        .then((response) => {
          console.log(response);
          release_movies.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const isMain = ref(false);

    // const getMovie = function (movieId) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/${movieId}/`
    //   })
    //   .then(response => {
    //     console.log(response)
    //     movie.value = response.data
    //   })
    //   .catch(error => {
    //     console.log(error)
    //   })
    // }
    return {
      API_URL,
      isMain,
      getRecommendMovies,
      getPopularMovies,
      getReleaseMovies,
      recommend_movies,
      popular_movies,
      release_movies,
      search,
      movies,
    };
  },
  { persist: true }
);
