<template>
  <div>
    <form class="row g-3 mt-5" @submit.prevent="createReview">
      <h1 class="col-md-6 offset-3 mb-3"><b>리뷰생성</b></h1>
      <div class="col-md-6 offset-3">
        <label class="form-label" for="title">제목</label>

        <input type="text" class="form-control" id="title" v-model="title" />
      </div>
      <div class="col-md-6 offset-3">
        <label class="form-label" for="vote">별점</label>

        <input
          type="range"
          v-model="vote"
          class="form-range"
          min="0"
          max="5"
          step="0.5"
          id="vote"
        />
      </div>

      <div class="col-md-6 offset-3">
        <label for="content" class="form-label">내용</label>
        <textarea
          class="form-control"
          v-model="content"
          id="content"
          rows="3"
        ></textarea>
      </div>

      <div class="col-md-6 offset-3">
        <button type="submit" class="btn btn-dark">생성</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useReviewStore } from "@/stores/review";
import { ref } from "vue";
import { useRoute } from "vue-router";
import axios from "axios";
import { useUserStore } from "@/stores/user";
const vote = ref(5);
const title = ref("");
const content = ref("");
const store = useReviewStore();
const user = useUserStore();
const route = useRoute();
const createReview = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/movies/${route.params.id}/reviews/`,
    data: {
      vote: vote.value,
      title: title.value,
      content: content.value,
    },
    headers: {
      Authorization: `Token ${user.token}`,
    },
  })
    .then((res) => {
      console.log("성공");
      console.log(res);
    })
    .catch((error) => {
      console.log(error);
    });
};
</script>

<style scoped></style>
