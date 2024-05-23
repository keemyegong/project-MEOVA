<template>
  <div class="actor-box" v-if="actor">
    <div class="movie-category-title">
      {{ actor.name }}
    </div>
    <img
      :src="'https://image.tmdb.org/t/p/original/' + actor.profile_path"
      alt="actor-profile"
      class="profile-image"
    />
    <SearchMovieListItem
      v-for="movie in actor.movies"
      :key="movie.id"
      :movie="movie"
    />
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useRoute, RouterLink } from "vue-router";
import SearchMovieListItem from "@/components/SearchMovieListItem.vue";

const store = useMovieStore();
const route = useRoute();
const actor = ref(null);

const actorId = route.params["id"];

axios({
  method: "get",
  url: `${store.API_URL}/api/v1/actors/${actorId}/`,
})
  .then((response) => {
    console.log(response);
    actor.value = response.data;
  })
  .catch((error) => {
    console.log(error);
  });
</script>

<style scoped>
.actor-box {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.profile-image {
  width: 300px;
  height: 300px;
  margin: 10px;
  margin-bottom: 100px;
  object-fit: cover;
  border-radius: 100%;
}

.movie-category-title {
  margin-top: 0px;
  margin-bottom: 50px;

  text-align: center;
  font-size: 50px;
  font-family: "Bagel Fat One", system-ui;
  font-weight: 400;
  font-style: normal;
}
</style>
