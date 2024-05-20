<template>
  <div>
    <!-- 수정 -->
    <div class="movie-card mb-3">
      <div class="row g-0">
        <div class="col-2">
          <div>
            <RouterLink
              :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
            >
              <img
                :src="
                  'https://image.tmdb.org/t/p/original/' + movie.poster_path
                "
                alt="movie-poster"
                class="movie-image img-fluid rounded"
              />
            </RouterLink>
          </div>
        </div>
        <div class="col-10">
          <div class="ms-3 me-3 card-body">
            <RouterLink
              class="nav-link"
              :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
            >
              <p class="movie-title card-title">{{ movie.title }}</p>
            </RouterLink>
            <p class="overview card-text">{{ movie.overview }}</p>
            <p class="movie-info card-text">
              <button
                @click="
                  search({
                    title: '',
                    genre: genre.name,
                    keyword: '',
                    runtime: '',
                    country: '',
                  })
                "
                class="btn genre"
                v-for="genre in movie.genres"
              >
                {{ genre.name }}
              </button>
              <button
                class="btn runtime"
                @click="searchByRuntime(movie.runtime)"
              >
                {{ movie.runtime }}분
              </button>
              <button
                class="btn country"
                @click="
                  search({
                    title: '',
                    genre: '',
                    keyword: '',
                    runtime: '',
                    country: movie.origin_country,
                  })
                "
              >
                {{ movie.origin_country }}
              </button>
              <button
                class="btn withwho"
                @click="
                  search({
                    title: '',
                    genre: '',
                    keyword: keyword.name,
                    runtime: '',
                    country: '',
                  })
                "
                v-for="keyword in movie.keywords.slice(0, 5)"
              >
                {{ keyword.name }}
              </button>
            </p>
          </div>
        </div>
      </div>
    </div>
    <!-- 수정 끝 -->
  </div>
</template>

<script setup>
const props = defineProps({
  movie: Object,
});

import { useMovieStore } from "@/stores/movie";
import { useRouter, RouterLink } from "vue-router";

const store = useMovieStore();
const router = useRouter();
const search = function (q) {
  store.search(q);
  router.push({ name: "search", query: q });
};
const searchByRuntime = function (runtime) {
  let runtimeQuery;
  if (runtime <= 60) {
    runtimeQuery = "under_1_hour";
  } else if (runtime <= 120) {
    runtimeQuery = "under_2_hours";
  } else if (runtime <= 180) {
    runtimeQuery = "under_3_hours";
  } else {
    runtimeQuery = "over_3_hours";
  }
  search({
    title: "",
    genre: "",
    keyword: "",
    runtime: runtimeQuery,
    country: "",
  });
};
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
