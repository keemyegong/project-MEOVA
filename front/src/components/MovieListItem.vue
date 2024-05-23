<template>
  <div>
    <div class="movie-item">
      <RouterLink
        class="nav-link"
        :to="{ name: 'MovieDetailView', params: { id: movie.id } }"
      >
        <img
          :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
          alt="movie-poster"
          class="movie-image"
        />
        <p class="movie-title">{{ movie.title }}</p>
      </RouterLink>
      <button class="btn p-0" @click="likeButton">
        <i class="bi bi-heart-fill" v-if="isLiked"></i>
        <i class="bi bi-heart" v-else></i>
      </button>
      <div class="overview-box">
        <p class="overview">{{ movie.overview }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter, RouterLink } from "vue-router";
import { useMovieStore } from "@/stores/movie";
import { useUserStore } from "@/stores/user";
import axios from "axios";
import { ref } from "vue";
const user = useUserStore();
const props = defineProps({
  movie: Object,
});
const isLiked = ref(props.movie.liked_users.includes(user.userinfo.pk));
const likeButton = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/movies/${props.movie.id}/like/`,
    headers: { Authorization: `Token ${user.token}` },
  })
    .then((res) => {
      isLiked.value = res.data.liked_users.includes(user.userinfo.pk);
    })
    .catch((error) => {
      console.log(error);
    });
};
const store = useMovieStore();
</script>

<style scoped>
.movie-item {
  width: 300px;
}
.movie-title {
  font-size: 25px;
  margin-top: 10px;
  margin-bottom: 10px;
}
.movie-image {
  height: 340px;
  width: 230px;
}

.overview-box {
  width: 250px;
}
.overview {
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 보여줄 줄 수 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.bi-heart-fill {
  color: red;
}
</style>
