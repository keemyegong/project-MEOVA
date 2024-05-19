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
import { useRoute, useRouter } from "vue-router";
const vote = ref(5);
const title = ref("");
const content = ref("");
const store = useReviewStore();
const route = useRoute();
const router = useRouter()
const movieId = Number(route.params['id'])
const createReview = function () {
  const review = {
    vote: vote.value,
    title: title.value,
    content: content.value,
    id: route.params.id,
  };
  store.createReview(review);
};
</script>

<style scoped></style>

