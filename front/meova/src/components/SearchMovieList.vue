<template>
  <div>
    <div>
      <SearchMovieListItem
        v-for="movie in movielist"
        :key="movie.id"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script setup>
import { RouterLink, routeLocationKey, useRoute, useRouter } from "vue-router";
import { computed, onMounted, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import SearchMovieListItem from "@/components/SearchMovieListItem.vue";

const props = defineProps({
  movies: Array,
});
const movielist = computed(() => {
  return props.movies;
});

const route = useRoute();
const store = useMovieStore();
console.log(route.query);
store.search(route.query);
</script>

<style scoped>
.movie-category-title {
  margin-top: 0px;
  margin-bottom: 50px;

  text-align: center;
  font-size: 50px;
  font-family: "Caprasimo", serif;
  font-weight: 400;
  font-style: normal;
}
</style>
