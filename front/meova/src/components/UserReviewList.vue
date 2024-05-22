<template>
  <div class="nato-font">
    <p class="review-item-title">
      {{ userStore.profile_info.nickname ? userStore.profile_info.nickname : userStore.profile_info.username }}`s Reviews
    </p>
    <div v-if="reviews " class="review">
        <div v-for="review in reviews"
            :key="review.id">
            <div class="review-item">
                <div class="card-body review-box">
                <h5 class="card-title">{{ review.title }}</h5>
                <p class="review-content card-text">{{ review.content }}</p>
                    <RouterLink
                    class="nav-link"
                    :to="{
                        name: 'ReviewDetailView',
                        params: { movieId: review.movie.id, reviewId: review.id },
                    }">
                        <div class="movie-info">
                            <img
                            :src="'https://image.tmdb.org/t/p/original/' + review.movie.poster_path"
                            alt="movie poster image"
                            class="poster-img"
                            />
                            <span class="movie-title ms-3 card-subtitle mt-2 text-body-secondary">
                                {{ review.movie.title }}
                            </span>
                        </div>
                    </RouterLink>
                </div>
            </div>
        </div>
        <div v-if="reviews.length === 0">
            <p class="ms-4">아직 작성된 리뷰가 없어요! (T_T)</p>
        </div>
      </div>
    </div>
</template>
  
<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useReviewStore } from "@/stores/review";
import { useRoute } from "vue-router";

const reviewStore = useReviewStore();
const userStore = useUserStore();
const route = useRoute();
const reviews = ref(null);


const props = defineProps({
  userid: Number
});
onMounted(() => {
axios({
  method: "get",
  url: `${reviewStore.API_URL}/${props.userid}/reviews/`,
  headers: { Authorization: `Token ${userStore.token}` },
})
  .then((response) => {
    reviews.value = response.data;
    console.log(response)
  })
  .catch((error) => {
    console.log(error);
  });
})
</script>
  
<style scoped>
.review {
  display: flex;
}
.review-item-title {
  margin-top: 10%;
  margin-left: 2%;
  font-size: 40px;
  font-family: "Caprasimo", serif;
  font-weight: 400;
  font-style: normal;
}
.review-item {
  height: 200px;
  width: 330px;
  margin-right: 10px;
  padding: 10px;
  margin: 10px;
  border-radius: 10px 10px 10px 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.review-box {
  padding: 10px;
}
.review-content {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.movie-info {
  margin-top: 50px;
  display: flex;
}
.movie-title {
    font-weight: 700;
}
.poster-img {
  height: 50px;
  width: 50px;
  border-radius: 100%;
}
.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
  