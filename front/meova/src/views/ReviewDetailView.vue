<template>
  <div v-if="reviewStore.review">
    <div class="row review-box">
      <div class="col-7 user-box">
        <div class="m-1 user-info">
          <img
            v-if="reviewStore.review.profile_photo"
            :src="`${movieStore.API_URL}${reviewStore.review.profile_photo}`"
            alt="user profile image"
            class="user-profile-img"
          />
          <img
            class="comment-user-profile-img user-profile-img"
            src="@/assets/default_profile.png"
            v-else
            alt=""
          />
          <RouterLink
            class="nav-link"
            v-if="reviewStore.review"
            :to="{
              name: 'profile',
              params: { username: reviewStore.review.username },
            }"
          >
            <p class="user-name">
              {{
                reviewStore.review.nickname
                  ? reviewStore.review.nickname
                  : reviewStore.review.username
              }}
            </p>
          </RouterLink>
          <button class="like-btn btn" @click="likeButton">
            <i class="bi bi-heart-fill" v-if="isLiked"></i>
            <i class="bi bi-heart" v-else></i>
          </button>
        </div>
        <!-- 별점 -->
        <div class="rate">
          <div v-if="reviewStore.review.vote === '5.0'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
          </div>
          <div v-if="reviewStore.review.vote === '4.5'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-half"></i>
          </div>
          <div v-if="reviewStore.review.vote === '4.0'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '3.5'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-half"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '3.0'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '2.5'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-half"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '2.0'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '1.5'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star-half"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '1.0'">
            <i class="rate-star bi bi-star-fill"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '0.5'">
            <i class="rate-star bi bi-star-half"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
          <div v-if="reviewStore.review.vote === '0.0'">
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
            <i class="rate-star bi bi-star"></i>
          </div>
        </div>
        <div class="review">
          <div class="row">
            <p class="review-title col-8">{{ reviewStore.review.title }}</p>
            <div
              class="button-group col-4"
              v-if="isReviewOwner(reviewStore.review.user)"
            >
              <span class="comment-content">{{
                reviewStore.changeToDate(reviewStore.review.created_at)
              }}</span>
              <button
                class="update-btn btn btn-dark"
                @click="updateReview(reviewStore.review.id)"
              >
                <p class="update-txt">수정</p>
              </button>
              <button
                class="delete-btn btn btn-dark"
                @click="deleteReview(reviewStore.review.id)"
              >
                <i class="update-txt bi bi-trash3-fill"></i>
              </button>
            </div>
          </div>
          <p>{{ reviewStore.review.content }}</p>
        </div>
      </div>
      <div v-if="reviewStore.review.movie" class="poster-box col-5">
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
      <form
        @submit.prevent="createComment"
        class="nato-font row review"
        ref="form"
      >
        <input
          type="text"
          placeholder="댓글을 남겨 주세요!"
          id="content"
          v-model="content"
          class="col-8 review-comment-input"
        />
        <!-- <input class="btn btn-dark" type="submit" value="입력" /> -->
        <button type="submit" class="col-4 review-comment-btn btn btn-dark">
          <i class="bi bi-pencil"></i>
        </button>
      </form>
    </div>

    <div v-for="comment in comments" :key="comment.id" class="comment-box">
      <img
        v-if="comment.profile_photo"
        :src="`${movieStore.API_URL}${comment.profile_photo}`"
        alt="user profile image"
        class="comment-user-profile-img"
      />
      <img
        class="comment-user-profile-img"
        src="@/assets/default_profile.png"
        v-else
        alt=""
      />
      <span class="comment-user-name">{{
        comment.nickname ? comment.nickname : comment.username
      }}</span>
      <i class="bi bi-chat-dots-fill me-2"></i>
      <span class="comment-content">{{ comment.content }}</span>
      <button
        v-if="isReviewOwner(comment.user)"
        class="comment-delete-btn btn btn-dark"
        @click="deleteComment(comment.id)"
      >
        <p class="comment-delete-btn-value">삭제</p>
      </button>
      <span class="comment-content ms-1">{{
        reviewStore.changeToDate(comment.created_at)
      }}</span>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
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
// const comments = ref(null)
const content = ref(null);
const comments = computed(() => {
  return reviewStore.review.reviewcomment_set;
});
const fetchReview = function () {
  reviewStore.fetchReview(reviewId);
};

onMounted(fetchReview);

const createComment = function () {
  const review = {
    content: content.value,
    id: reviewId,
  };
  reviewStore.createComment(review).then(() => {
    fetchReview();
  });
  form.value.reset();
  content.value = "";
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
      // reviewStore.review.value.reviewcomment_set =
      //   review.value.reviewcomment_set.filter(
      //     (comment) => comment.id !== commentId
      //   );
      fetchReview();
    })
    .catch((error) => {
      console.log(error);
    });
};
const isReviewLoaded = computed(() => reviewStore.review !== null);

const isReviewOwner = (user) => {
  return (
    reviewStore.review && userStore.userinfo && user === userStore.userinfo.pk
  );
};

// 좋아요 여부를 확인하는 상태 변수
const isLiked = ref(false);

// 리뷰 데이터가 로드되면 isLiked 값 설정
if (isReviewLoaded.value) {
  isLiked.value = reviewStore.review.liked_users.includes(
    userStore.userinfo.pk
  );
}

// 비동기 함수로 likeButton 함수 정의
const likeButton = async function () {
  try {
    const response = await axios({
      method: "post",
      url: `${movieStore.API_URL}/api/v1/reviews/${reviewStore.review.id}/like/`,
      headers: { Authorization: `Token ${userStore.token}` },
    });
    isLiked.value = response.data.liked_users.includes(userStore.userinfo.pk);
  } catch (error) {
    console.log(error);
  }
};
</script>

<style scoped>
.review-title {
  font-size: 25px;
  font-weight: 700;
  margin-top: 10px;
}
.review-btn {
  margin-left: auto;
  color: rgb(170, 170, 170);
  font-size: 50px;
  font-weight: 800;
}
.review-comment-input {
  height: 50px;
}
.user-info {
  display: flex;
  align-items: center;
  margin-top: 50px;
  margin-bottom: 5px;
}
.user-profile-img {
  height: 80px;
  width: 80px;
  border-radius: 100%;
  margin-right: 20px;
}
.user-name {
  font-size: 2.3vw;
  font-weight: 700;
}
.button-group {
  display: flex;
  margin: auto;
}
.update-btn,
.delete-btn {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 80px;
  height: 40px;
  margin-left: 10px;
  font-size: 12px;
}
.update-txt {
  font-size: 90%;
  margin: 0;
}
.poster-box {
  padding: 0;
}
.poster-image {
  width: 93%;
  border-radius: 1%;
}

/* 별점 */
.rate {
  text-align: center;
  margin-top: 10px;
}
.rate-star {
  margin-right: 5px;
  font-size: 3vw;
  color: #fdde55;
}
.review {
  margin-top: 20px;
  margin-bottom: 40px;
}
.like-btn {
  font-size: 2.5vw;
  margin-left: auto;
}
.review-comment-btn {
  margin-left: 1%;
  width: 31%;
}
.comment-box {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
.comment-user-profile-img {
  padding: 3px;
  width: 53px;
  height: 53px;
  border-radius: 100%;
}
.comment-user-name {
  margin-left: 10px;
  margin-right: 10px;
  font-weight: 600;
}

.comment-delete-btn-value {
  font-size: 11px;
}
.comment-delete-btn {
  margin-left: 10px;
  width: 50px;
  height: 30px;
}
.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
