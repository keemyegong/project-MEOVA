<template>
  <div v-if="reviewStore.review">
    <h1>{{ reviewStore.review.title }}</h1>
    <div v-if="reviewStore.review.movie">
      <RouterLink
        :to="{
          name: 'MovieDetailView',
          params: { id: reviewStore.review.movie.id },
        }"
      >
        <img
          :src="
            'https://image.tmdb.org/t/p/original/' +
            reviewStore.review.movie.poster_path
          "
          alt="movie-poster"
          class="poster-image"
        />
      </RouterLink>
    </div>
    <h2>평점 {{ reviewStore.review.vote }}</h2>
    <span v-if="reviewStore.review.nickname">
      작성자 | {{ reviewStore.review.nickname }}
    </span>
    <span v-else> 작성자 | {{ reviewStore.review.username }} </span>
    <p>{{ reviewStore.review.content }}</p>
    <button @click="updateReview(reviewStore.review.id)">수정</button>
    <button @click="deleteReview(reviewStore.review.id)">삭제</button>
    <hr />

    <form @submit.prevent="createComment" ref="form">
      <input
        type="text"
        placeholder="댓글을 남겨 주세요!"
        id="content"
        v-model="content"
      />
      <input type="submit" value="입력" />
    </form>

    <div
      v-for="comment in reviewStore.review.reviewcomment_set"
      :key="comment.id"
    >
      <span>{{ comment.content }}</span>
      <span v-if="comment.nickname"> | {{ comment.nickname }} </span>
      <span v-else> | {{ comment.username }} </span>
      <button @click="deleteComment(comment.id)">삭제</button>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";
import { useReviewStore } from "@/stores/review";
import { useRoute, useRouter, RouterLink } from "vue-router";

const userStore = useUserStore();
const movieStore = useMovieStore();
const reviewStore = useReviewStore();

const route = useRoute();
const router = useRouter();
const movieId = Number(route.params["movieId"]);
const reviewId = Number(route.params["reviewId"]);
const form = ref(null);
const movie = ref(null);

const content = ref(null);

const fetchReview = function () {
  reviewStore.fetchReview(reviewId);
};

onMounted(fetchReview);

const createComment = function () {
  const review = {
    content: content.value,
    id: reviewId,
  };
  reviewStore.createComment(review);
  form.value.reset();
  content.value = "";
  fetchReview();
};

const updateReview = (reviewId) => {
  router.push({
    name: "ReviewUpdateView",
    params: { id: reviewId },
  });
};

const deleteReview = (reviewId) => {
  axios({
    method: "delete",
    url: `${movieStore.API_URL}/api/v1/reviews/${reviewId}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(() => {
      router.push({
        name: "MovieDetailView",
        params: { id: movieId },
      });
    })
    .catch((error) => {
      console.log(error);
    });
};

const deleteComment = (commentId) => {
  axios({
    method: "delete",
    url: `${movieStore.API_URL}/api/v1/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(() => {
      review.value.reviewcomment_set = review.value.reviewcomment_set.filter(
        (comment) => comment.id !== commentId
      );
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped>
.poster-image {
  width: 200px;
}
</style>
