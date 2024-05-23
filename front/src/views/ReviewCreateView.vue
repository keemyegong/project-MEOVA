<template>
  <div class="review-create">
    <form class="nato-font create-form" @submit.prevent="createReview">
      <h1><b>영화는 어땠나요?</b></h1>
      <div>
        <label class="form-label mt-3" for="title">제목</label>

        <input type="text" class="form-control mt-3" id="title" v-model="title" />
      </div>
      <div>
        <label class="form-label mt-3" for="vote">별점</label>

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

      <div>
        <label for="content" class="form-label mt-3">내용</label>
        <textarea
          class="form-control"
          v-model="content"
          id="content"
          rows="3"
        ></textarea>
      </div>

      <div>
        <button type="submit" class="btn btn-dark mt-3">등록</button>
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

<style scoped>
.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
.review-create {
  margin-top: 70px;
}
.create-form {
  margin: auto;
  width: 50%;
  max-width: 500px;
  min-width: 300px;
}

</style>

