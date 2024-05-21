
<template>
  <div>
    <h1>Movie Recommendations</h1>
    <p v-if="recommendations">{{ recommendations }}</p>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import axios from 'axios';
import { useRouter, RouterLink } from "vue-router";
import { useMovieStore } from "@/stores/movie";
import { useUserStore } from "@/stores/user";
import { ref } from "vue";
const user = useUserStore();

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