<template>
  <div v-if="reviewStore.review" >
    <div class="row review-box">
      <div class="col-6">
        <div class="user-info">
          <img
          v-if="reviewStore.review.profile_photo"
          :src="`http://127.0.0.1:8000${reviewStore.review.profile_photo}`"
          alt="user profile image"
          class="user-profile-img">
          <img
            class="comment-user-profile-im user-profile-img"
            src="@/assets/default_profile.png"
            v-else
            alt=""
          />
          <span class="user-name">{{ reviewStore.review.nickname ? reviewStore.review.nickname : reviewStore.review.username }}</span>
          <button class="update-btn btn btn-dark" @click="updateReview(reviewStore.review.id)">수정</button>
          <button class="delete-btn btn btn-dark" @click="deleteReview(reviewStore.review.id)"><i class="bi bi-trash3-fill"></i></button>

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
          <p class="review-title">{{ reviewStore.review.title }}</p>
          <p>{{ reviewStore.review.content }}</p>
        </div>
      </div>
      <div v-if="reviewStore.review.movie" class="col-6">
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

        <form @submit.prevent="createComment" class="row review" ref="form">
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



    <div
      v-for="comment in reviewStore.review.reviewcomment_set"
      :key="comment.id"
    >
      <img
      v-if="comment.profile_photo"
      :src="`http://127.0.0.1:8000${comment.profile_photo}`"
      alt="user profile image"
      class="comment-user-profile-img">
      <img
        class="comment-user-profile-img"
        src="@/assets/default_profile.png"
        v-else
        alt=""
      />
      <span class="comment-user-name">{{ comment.nickname ? comment.nickname : comment.username }}</span>
      <i class="bi bi-chat-dots-fill me-2"></i>
      <span class="comment-content">{{ comment.content }}</span>
      <button class="comment-delete-btn btn btn-dark" @click="deleteComment(comment.id)">
          <p class="comment-delete-btn-value">
            삭제
          </p>
      </button>
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
      reviewStore.review.value.reviewcomment_set = review.value.reviewcomment_set.filter(
        (comment) => comment.id !== commentId
      );
    })
    .catch((error) => {
      console.log(error);
    });
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
  font-size: 50px;
  font-weight: 800;
}
.poster-image {
  width: 93%;
  margin-left: 4%;
  border-radius: 1%;
}

/* 별점 */
.rate {
  text-align: center;
}
.rate-star {
  margin-right: 5px;
  font-size: 45px;
  color: #FDDE55;
}

.update-btn {
  width: 10%;
  height: 50px;
  margin-top: 15px;
  margin-left: auto;
}

.delete-btn {
  width: 10%;
  height: 50px;
  margin-top: 15px;
  margin-left: 10px;
}
.review {
  margin-top: 20px;
  margin-bottom: 40px;
}
.review-comment-btn {
  margin-left: 1%;
  width: 32%;
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
</style>
