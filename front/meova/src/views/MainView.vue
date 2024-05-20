<template>
  <div>
    <div class="main">
      <div class="main-search">
        <img
          class="col-12"
          :src="store.API_URL + '/static/main_logo.gif'"
          alt="logo"
        />
        <form class="row g-2" @submit.prevent="search">
          <div class="col-9 offset-1">
            <input
              type="text"
              class="form-control form-control-lg"
              v-model="searchbar.title"
              placeholder="영화 뭐 볼까?"
              @focus="displaySearch"
            />
          </div>
          <div class="col-2">
            <button
              type="submit"
              style="width: 80%"
              class="btn btn-lg btn-dark"
            >
              <i class="bi bi-search"></i>
            </button>
          </div>
          <div v-if="showFilters" class="col-9 offset-1">
            <section class="search-bar">
              <div class="search-bar-item">
                <button class="btn disabled">장르</button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '공포')"
                >
                  공포
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '로맨스')"
                >
                  로맨스
                </button>
              </div>
              <div class="search-bar-item">
                <button class="btn disabled">러닝타임</button>
                <button
                  type="button"
                  class="btn runtime"
                  @click="addFilter('runtime', 'under_1_hour')"
                >
                  1시간이내
                </button>
                <button
                  type="button"
                  class="btn runtime"
                  @click="addFilter('runtime', 'under_2_hours')"
                >
                  2시간이내
                </button>
                <button
                  type="button"
                  class="btn runtime"
                  @click="addFilter('runtime', 'under_3_hours')"
                >
                  3시간이내
                </button>
                <button
                  type="button"
                  class="btn runtime"
                  @click="addFilter('runtime', 'over_3_hours')"
                >
                  3시간이상
                </button>
              </div>
              <div class="search-bar-item">
                <button class="btn disabled">누구랑</button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('가족')"
                >
                  가족
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('친구')"
                >
                  친구
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('연인')"
                >
                  연인
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('직장동료')"
                >
                  직장동료
                </button>
              </div>
              <div class="search-bar-item">
                <button class="btn disabled">국가</button>
                <button
                  type="button"
                  class="btn country"
                  @click="addFilter('country', 'US')"
                >
                  미국
                </button>
                <button
                  type="button"
                  class="btn country"
                  @click="addFilter('country', 'KR')"
                >
                  한국
                </button>
                <button
                  type="button"
                  class="btn country"
                  @click="addFilter('country', 'JP')"
                >
                  일본
                </button>
                <button
                  type="button"
                  class="btn country"
                  @click="addFilter('그외')"
                >
                  그외
                </button>
              </div>
            </section>
          </div>
        </form>
      </div>
    </div>
    <MovieList />
    <SearchMovieList />
  </div>
</template>

<script setup>
import MovieList from "@/components/MovieList.vue";
import SearchMovieList from "@/components/SearchMovieList.vue";
import { onMounted, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useRouter } from "vue-router";

const props = defineProps({
  movie: Object,
});

const store = useMovieStore();

const searchbar = ref({
  title: "",
  genre: "",
  keyword: "",
  runtime: "",
  country: "",
});
const showFilters = ref(false);

const displaySearch = () => {
  showFilters.value = true;
};
const addFilter = (type, filter) => {
  if (searchbar.value[type]) {
    searchbar.value[type] += `+${filter}`;
  } else {
    searchbar.value[type] = filter;
  }
};

const router = useRouter();
const search = () => {
  store.search({
    title: searchbar.value.title,
    genre: searchbar.value.genre,
    runtime: searchbar.value.runtime,
    country: searchbar.value.country,
    withwho: searchbar.value.withwho,
  });

  router.push({
    name: "search",
    query: {
      title: searchbar.value.title,
      genre: searchbar.value.genre,
      runtime: searchbar.value.runtime,
      country: searchbar.value.country,
      withwho: searchbar.value.withwho,
    },
  });
};

onMounted(() => {
  store.getRecommendMovies();
  store.getPopularMovies();
  store.getReleaseMovies();
});
</script>

<style scoped>
.main-search {
  height: 80vh;
  display: flex;
  flex-direction: column;
  margin-top: 20vh;
  align-items: center;
}
.main-search > form {
  width: 100%;
}
.main-search > img {
  width: 80%;
}
.search-bar {
  padding: 10px;
  border: 1px solid #e0e0e0;
}
.search-bar-item {
  display: flex;
  flex-wrap: wrap;
  padding: 3px;
  align-items: center;
}
.country {
  background-color: #ccd3ca;
  color: white;
  margin-right: 5px;
}
.withwho {
  background-color: #b2c8df;
  color: white;
  margin-right: 5px;
}
.runtime {
  background-color: #eed3d9;
  color: white;
  margin-right: 5px;
}
.genre {
  background-color: #f4d19b;
  color: white;
  margin-right: 5px;
}

.disabled {
  border: none;
}
</style>
