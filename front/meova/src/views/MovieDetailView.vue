<template>
  <div v-if="movie" class="row movie-detail-box">
    <div class="movie-info col-6">
      <div class="movie-title">
        <b>{{ movie.title }}</b>
      </div>
      <div class="movie-overview">
        <p class="overview">
          {{ movie.overview }}
        </p>
      </div>
      <button class="btn runtime">{{ movie.runtime }}분</button>
      <button class="btn country">{{ movie.origin_country }}</button>
      <button class="btn genre" v-for="genre in movie.genres">
        {{ genre.name }}
      </button>

      <button class="btn withwho" v-for="keyword in movie.keywords">
        {{ keyword.name }}
      </button>
      <div class="tag-comment">
        <RouterLink
          class="nav-link" :to="{ name: 'TagCommentDetailView', params: { id: movie.id } }"
        >
          <div class="detail-category-title">
            <p>태그 코멘트</p>
          </div>
        </RouterLink>
        <template v-if="movie.tagcomment_set">
          <div
            v-for="tagcomment in movie.tagcomment_set.slice().reverse()"
            :key="tagcomment.id"
            class="tag-comment-content"
          >
          <i class="bi bi-chat-dots-fill me-2"></i>
            {{ tagcomment.content }}
            <span v-if="tagcomment.nickname" class="tag-comment-user">
              | {{ tagcomment.nickname }}
            </span>
            <span v-else class="tag-comment-user"> | {{ tagcomment.username }} </span>
          </div>
        </template>
        <template v-else>
          <p>아직 태그코멘트가 없어요!</p>
        </template>
      </div>
      <form @submit.prevent="createTag" class="tag-comment-input row" ref="form">
        <div class="col-9">
          <input
            type="text"
            placeholder="영화의 태그가 적합한지 평가해 주세요!"
            id="content"
            class="form-control"
            v-model="content"
          />
        </div>
        <button type="submit" class="tag-comment-btn btn btn-dark col-3">
          <i class="bi bi-pencil"></i>
        </button>
      </form>
    </div>
    
    <div class="poster-review col-6">
      <div class="rol">
        <img
          :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
          alt="movie-poster"
          class="movie-image col-12"
        />

          <RouterLink :to="{ name: 'CreateReview', params: { id: movie.id } }">
            <button class="review-btn mt-3 col-12 btn btn-warning">
              리뷰 작성
            </button>
          </RouterLink>
      </div>
    </div>

    <template v-if="movie.watchproviders.length > 0">
      <b>Provider</b>
      <div v-for="watchprovider in movie.watchproviders">
        {{ watchprovider }}
      </div>
    </template>

    <div class="director-box">
      <p class="detail-category-title">감독</p>
      <div class="director" v-for="director in movie.directors">
        <RouterLink
          class="nav-link" :to="{ name: 'DirectorDetailView', params: { id: director.id } }"
        >
          <p>{{ director.name }}</p>
        </RouterLink>
      </div>
    </div>

    <p class="detail-category-title">출연진</p>
    <template class="cast">
      <div v-for="credit in movie.credits">
        <RouterLink
          class="nav-link"
          :to="{ name: 'ActorDetailView', params: { id: credit.actor.id } }"
        >
          <img
            :src="
              'https://image.tmdb.org/t/p/original/' + credit.actor.profile_path
            "
            alt="actor-profile"
            class="profile-image"
          />
          <p class="character">{{ credit.character }}</p>
          <p class="actor">{{ credit.actor.name }}</p>
        </RouterLink>
      </div>
    </template>

    <p class="detail-category-title">리뷰</p>
    <template class="review">
      <div v-for="review in movie.review_set">
        <RouterLink
          class="nav-link"
          :to="{
            name: 'ReviewDetailView',
            params: { movieId: movie.id, reviewId: review.id },
          }"
        >
        <div class="review-item card">
          <div class="card-body">
            <h5 class="card-title">{{ review.title }}</h5>
            <p class="card-text">{{ review.content }}</p>
            <h6 class="card-subtitle mt-2 text-body-secondary">
              {{ review.nickname ? review.nickname : review.username }}
            </h6>
          </div>
        </div>
      </RouterLink>
      </div>
    </template>

  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, onUpdated, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useReviewStore } from "@/stores/review";
import { useUserStore } from "@/stores/user";
import { useRoute, RouterLink } from "vue-router";

const store = useMovieStore();
const reviewstore = useReviewStore();
const userStore = useUserStore();
const route = useRoute();
const movie = ref(null);
const movieId = Number(route.params["id"]);
const content = ref("");
const form = ref(null);


const createTag = function () {
  const tag = {
    content: content.value,
    id: movieId,
  };
  reviewstore.createTag(tag);
  form.value.reset();
  content.value = "";
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/movies/${movieId}/`,
  })
    .then((response) => {
      console.log(store.API_URL);
      console.log(response);
      movie.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
};

onUpdated(() => {});
console.log(store.API_URL);
onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/movies/${movieId}/`,
  })
    .then((response) => {
      console.log(store.API_URL);
      console.log(response);
      movie.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<style scoped>
.movie-title {
    font-size: 35px;
    margin-top: 10px;
    margin-bottom: 20px;
}
.movie-image {
  width: 100%;
  border-radius: 1%;
}

.movie-overview {
  margin-bottom: 20px;
}
.poster-review {
  padding-left: 50px;
  padding-bottom: 50px;
}
.profile-image {
  width: 200px;
  height: 200px;
  margin: 10px;
  object-fit: cover;
  border-radius: 100%;
}
.director {
  display: flex;
}
.cast {
  width: 100%;
  overflow: auto;
  display: flex;
}
.cast::-webkit-scrollbar {
    display: none;
}
.review {
  display: flex;
}

.movie-detail-box {
  margin-top: 50px;
}

.movie-info > button {
  margin-right: 3px;
  margin-bottom: 3px;
}
.detail-category-title {
  font-size: 20px;
  font-weight: 700;
}
.tag-comment {
  width: 100%;
  margin-top: 30px;
  max-height: 300px; /* 최대 높이 설정 */
  overflow: auto; /* 세로 스크롤 설정 */
  top: auto;
}

.tag-comment-content {
  margin-left: 3px;
  margin-bottom: 7px;
}

.tag-comment-user {
  margin-left: 5px;
  font-size: 13px;
  color: lightslategray;
}
.tag-comment-input {
  margin-top: 30px;
}
.tag-comment-btn {
  width: 13%;
}
.country {
  background-color: #CCD3CA;
  color: white;
}
.withwho {
  background-color: #B2C8DF;
  color: white;
}
.runtime {
  background-color: #eed3d9;
  color: white;
}
.genre {
  background-color: #F4D19B; 
  color: white;
}

.review-btn {
  color: white;
  font-size: 18px;
  font-weight: 700;
  height: 55px;
}

.director-box {
  margin-bottom: 30px;
}

.character {
  margin-top: 10px;
  text-align: center;
}
.actor {
  text-align: center;
  color: lightslategray;
}

.review {
  width: 100%;
  overflow: auto;
  display: flex;
}

.review::-webkit-scrollbar {
  display: none;
}

.review-item {
  height: 200px;
  width: 330px;
  margin-right: 10px;
}

.user-profile {
  height: 50px;
  width: 50px;
  border-radius: 100%;
}
</style>
