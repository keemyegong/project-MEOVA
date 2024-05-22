import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useUserStore } from "./user";

export const useMovieStore = defineStore(
  "movie",
  () => {
    const API_URL = "http://127.0.0.1:8000";
    const userStore = useUserStore()
    const recommend_movies = ref([]);
    const popular_movies = ref([]);
    const release_movies = ref([]);
    const movies = ref([]);
    const movie = ref(null)

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
        // console.log(res);
        movies.value = res.data;
      });
    };
    const recommendations = ref({});
    const recommendmovies = ref([]);
    const getRecommendMovies = function () {
      return axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/recommended/`,
      }).then((res) => {
        recommendations.value = res.data[res.data.length - 1];
      });
    };
    const getRecommendMovieList = function (ids) {
      recommendmovies.value = [];
      for (const pk of ids) {
        axios({
          method: "get",
          url: `${API_URL}/api/v1/movies/recommended/${pk}/`,
        }).then((res) => {
          recommendmovies.value.push(res.data);
        });
      }
    };

    const getPopularMovies = function () {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/popular/`,
      })
        .then((response) => {
          // console.log(response);
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
          // console.log(response);
          release_movies.value = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const isMain = ref(false);

    const getMovie = function (movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/`,
        headers: { Authorization: `Token ${userStore.token}` },
      })
      .then(response => {
        console.log(response)
        movie.value = response.data
      })
      .catch(error => {
        console.log(error)
      })

    }
    return {
      API_URL,
      isMain,
      getRecommendMovies,
      recommendations,
      getPopularMovies,
      getReleaseMovies,
      recommend_movies,
      popular_movies,
      release_movies,
      search,
      movie,
      movies,
      getRecommendMovieList,
      recommendmovies,
      getMovie
    };
  },
  { persist: true }
);
