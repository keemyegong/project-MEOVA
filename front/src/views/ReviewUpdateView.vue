<template>
  <div class="review-create nato-font">
    <form class="nato-font create-form" @submit.prevent="updateReview">
      <h1><b>리뷰를 수정해 주세요!</b></h1>
      <div>
        <label class="form-label mt-3" for="title">제목</label>

        <input type="text" class="form-control" id="title" v-model="title" />
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
        <button type="submit" class="btn btn-dark">수정</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useReviewStore } from "@/stores/review";

// Store와 router 사용 설정
const store = useReviewStore();
const route = useRoute();
const router = useRouter();

// 라우트에서 reviewId 가져오기
const reviewId = Number(route.params.reviewId);

// 컴포넌트 상태 변수 정의
const title = ref(store.review.title);
const vote = ref(store.review.vote);
const content = ref(store.review.content);

// 초기 리뷰 데이터를 가져오기 위한 함수
const fetchReview = async () => {
  await store.fetchReview(reviewId);

  // Store에 데이터가 정상적으로 로드되었는지 확인
  if (store.review) {
    title.value = store.review.title || "";
    vote.value = store.review.vote || 0;
    content.value = store.review.content || "";
  }
};
// 컴포넌트가 마운트될 때 리뷰 데이터 가져오기

// 리뷰 업데이트 함수
const updateReview = async () => {
  const updatedReview = {
    id: reviewId,
    title: title.value,
    vote: vote.value,
    content: content.value,
  };
  try {
    const res = await store.updateReview(updatedReview);
    console.log("성공", res.data);
    router.push({
      name: "ReviewDetailView",
      params: { reviewId: res.data.id },
    });
  } catch (error) {
    console.error(error);
  }
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
