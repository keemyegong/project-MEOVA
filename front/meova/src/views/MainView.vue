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
          <div class="nato-font col-9 offset-1">
            <div class="form-control form-control-lg">
              <button
                class="btn genre"
                v-for="genre in searchbar.genre.split(' ')"
                v-if="searchbar.genre"
              >
                {{ genre }}
              </button>
              <button
                class="btn runtime"
                v-for="runtime in searchbar.runtime.split(' ')"
                v-if="searchbar.runtime"
              >
                {{ runtime }}
              </button>
              <button
                class="btn withwho"
                v-for="keyword in searchbar.keyword.split(' ')"
                v-if="searchbar.keyword"
              >
                {{ keyword }}
              </button>
              <button
                class="btn country"
                v-for="country in searchbar.country.split(' ')"
                v-if="searchbar.country"
              >
                {{ country }}
              </button>

              <input
                type="text"
                class="search-input form-control"
                v-model="searchbar.title"
                placeholder="영화 뭐 볼까?"
                @focus="displaySearch"
              />
            </div>
          </div>
          <div class="col-2">
            <button
              type="submit"
              style="width: 80%"
              class="btn btn-lg btn-dark p-3"
            >
              <i class="bi bi-search"></i>
            </button>
          </div>
          <div v-if="showFilters" class="nato-font col-9 offset-1">
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
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '모험')"
                >
                  모험
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '판타지')"
                >
                  판타지
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '애니메이션')"
                >
                  애니메이션
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '드라마')"
                >
                  드라마
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '액션')"
                >
                  액션
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '코미디')"
                >
                  코미디
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '역사')"
                >
                  역사
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '스릴러')"
                >
                  스릴러
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '범죄')"
                >
                  범죄
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '다큐멘터리')"
                >
                  다큐멘터리
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', 'SF')"
                >
                  SF
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '미스터리')"
                >
                  미스터리
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '음악')"
                >
                  음악
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '가족')"
                >
                  가족
                </button>
                <button
                  type="button"
                  class="btn genre"
                  @click="addFilter('genre', '전쟁')"
                >
                  전쟁
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
                  @click="addFilter('keyword', 'family')"
                >
                  가족
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('keyword', 'friendship')"
                >
                  친구
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('keyword', 'love')"
                >
                  연인
                </button>
                <button
                  type="button"
                  class="btn withwho"
                  @click="addFilter('keyword', 'casual')"
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
    searchbar.value[type] += ` ${filter}`;
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
    keyword: searchbar.value.keyword,
    country: searchbar.value.country,
  });

  router.push({
    name: "search",
    query: {
      title: searchbar.value.title,
      genre: searchbar.value.genre,
      runtime: searchbar.value.runtime,
      country: searchbar.value.country,
      keyword: searchbar.value.keyword,
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
.search-bar-item > button {
  margin-bottom: 3px;
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
.search-input {
  width: auto;
  border: 0;
}
.search-input {
  flex-grow: 1;
  min-width: 100px; /* Optional: Minimum width for the input */
  margin: 5px;
}
.form-control {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
}

.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
