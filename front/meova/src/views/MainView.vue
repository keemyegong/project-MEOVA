<template>
  <div>
    <div class="main">
      <div class="main-search">
        <img
          class="col-12"
          :src="store.API_URL + '/static/main_logo.gif'"
          alt="logo"
        />
        <form class="row g-2">
          <div class="col-9 offset-1">
            <input
              type="text"
              class="form-control form-control-lg"
              v-model="searchbar"
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
                <button>장르</button>
                <button type="button" @click="addFilter('공포')">공포</button>
              </div>
              <div class="search-bar-item">
                <button>러닝타임</button>
                <button type="button" @click="addFilter('1시간이내')">
                  1시간이내
                </button>
                <button type="button" @click="addFilter('2시간이내')">
                  2시간이내
                </button>
                <button type="button" @click="addFilter('3시간이내')">
                  3시간이내
                </button>
                <button type="button" @click="addFilter('3시간이상')">
                  3시간이상
                </button>
              </div>
              <div class="search-bar-item">
                <button>누구랑</button>
                <button type="button" @click="addFilter('가족')">가족</button>
                <button type="button" @click="addFilter('친구')">친구</button>
                <button type="button" @click="addFilter('연인')">연인</button>
                <button type="button" @click="addFilter('직장동료')">
                  직장동료
                </button>
              </div>
              <div class="search-bar-item">
                <button>국가</button>
                <button type="button" @click="addFilter('미국')">미국</button>
                <button type="button" @click="addFilter('한국')">한국</button>
                <button type="button" @click="addFilter('일본')">일본</button>
                <button type="button" @click="addFilter('그외')">그외</button>
              </div>
            </section>
          </div>
        </form>
      </div>
    </div>
    <MovieList />
  </div>
</template>

<script setup>
import MovieList from "@/components/MovieList.vue";
import { onMounted, ref } from "vue";
import { useMovieStore } from "@/stores/movie";

const props = defineProps({
  movie: Object,
});

const store = useMovieStore();

const searchbar = ref("");
const showFilters = ref(false);

const displaySearch = () => {
  showFilters.value = true;
};

const addFilter = (filter) => {
  if (searchbar.value) {
    searchbar.value += ` ${filter}`;
  } else {
    searchbar.value = filter;
  }
};

const search = () => {
  // 검색 로직 추가
  console.log("검색어:", searchbar.value);
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
  padding: 1px;
  align-items: center;
}
.country {
  background-color: #eed3d9;
  color: white;
}
.withwho {
  background-color: #ccd3ca;
  color: white;
}
.runtime {
  background-color: #ead7c7;
  color: white;
}
.genre {
  background-color: #b5c0d0;
  color: white;
}
</style>
