<template>
  <div v-if="movie" class="row movie-detail-box nato-font">
    <div class="movie-info col-12 col-md-6">
      <div class="movie-title">
        <b>{{ movie.title }}</b>
      </div>
      <div class="movie-overview">
        <p class="overview">
          {{ movie.overview }}
        </p>
      </div>
      <button class="btn runtime" @click="searchByRuntime(movie.runtime)">
        {{ movie.runtime }}분
      </button>
      <button
        class="btn country"
        @click="
          search({
            title: '',
            genre: '',
            keyword: '',
            runtime: '',
            country: movie.origin_country,
          })
        "
      >
        {{ movie.origin_country }}
      </button>
      <button
        class="btn genre"
        @click="
          search({
            title: '',
            genre: genre.name,
            keyword: '',
            runtime: '',
            country: '',
          })
        "
        v-for="genre in movie.genres"
      >
        {{ genre.name }}
      </button>

      <button
        class="btn withwho"
        @click="
          search({
            title: '',
            genre: '',
            keyword: keyword.name,
            runtime: '',
            country: '',
          })
        "
        v-for="keyword in movie.keywords"
      >
        {{ keyword.name }}
      </button>
      <div class="tag-comment">
        <!-- Button trigger modal -->
        <button
          type="button"
          class="btn detail-category-title"
          data-bs-toggle="modal"
          data-bs-target="#TagCommentDetailModal"
        >
          태그 코멘트
        </button>
        <template v-if="tags">
          <div
            v-for="tagcomment in tags.slice().reverse()"
            :key="tagcomment.id"
            class="tag-comment-content"
          >
            <i class="bi bi-chat-dots-fill me-2"></i>
            {{ tagcomment.content }}
            <span v-if="tagcomment.nickname" class="tag-comment-user">
              | {{ tagcomment.nickname }}
            </span>
            <span v-else class="tag-comment-user">
              | {{ tagcomment.username }}
            </span>
          </div>
        </template>
        <template v-else>
          <p>아직 태그코멘트가 없어요!</p>
        </template>
      </div>
      <form
        @submit.prevent="createTag"
        class="tag-comment-input row"
        ref="form"
      >
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

    <!-- Modal -->
    <div
      class="modal fade modal-section"
      id="TagCommentDetailModal"
      tabindex="-1"
      aria-labelledby="TagCommentDetailModal"
      aria-hidden="true"
    >
      <TagCommentDetailModal />
    </div>

    <div class="poster-review col-12 col-md-6">
      <div class="rol">
        <img
          :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
          alt="movie-poster"
          class="movie-image col-12"
        />
        <RouterLink
          :to="{
            name: 'ReviewDetailView',
            params: {
              movieId: movie.id,
              reviewId: movie.my_reviews[0] ? movie.my_reviews[0].id : null,
            },
          }"
          v-if="movie.my_reviews.length === 1"
        >
          <button class="review-btn mt-3 col-12 btn btn-warning">
            내 리뷰 보기
          </button>
        </RouterLink>
        <RouterLink
          :to="{ name: 'CreateReview', params: { id: movie.id } }"
          v-else
        >
          <button class="review-btn mt-3 col-12 btn btn-warning">
            리뷰 작성
          </button>
        </RouterLink>
      </div>
    </div>  
    
    <template v-if="movie.watchproviders.length > 0" class="director-box">
      <b style="display: flex" class="detail-category-title mt-3 mb-3">제공</b>

      <span v-for="watchprovider in movie.watchproviders" style="width: 7%">
        <img
          :src="
            'https://image.tmdb.org/t/p/original/' + watchprovider.logo_path
          "
          alt="actor-profile"
          style="width: 50px; border-radius: 50%"
        />
      </span>
    </template>
    
    <div class="director-box mt-5">
      <p class="detail-category-title">감독</p>
      <div class="director" v-for="director in movie.directors">
        <RouterLink
          class="nav-link"
          :to="{ name: 'DirectorDetailView', params: { id: director.id } }"
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
    <div v-if="movie.review_set" class="review">
      <div v-for="review in movie.review_set.slice().reverse()">
        <RouterLink
          class="nav-link"
          :to="{
            name: 'ReviewDetailView',
            params: { movieId: movie.id, reviewId: review.id },
          }"
        >
          <div class="review-item">
            <div class="card-body review-box">
              <h5 class="card-title">{{ review.title }}</h5>
              <p class="review-content card-text">{{ review.content }}</p>
              <div class="user-info">
                <img
                  v-if="review.profile_photo"
                  :src="`${store.API_URL}${review.profile_photo}`"
                  alt="user profile image"
                  class="user-profile-img"
                />
                <img
                  class="user-profile-img"
                  src="@/assets/default_profile.png"
                  v-else
                  alt=""
                />
                <span class="ms-2 card-subtitle mt-2 text-body-secondary">
                  {{ review.nickname ? review.nickname : review.username }}
                </span>
              </div>
            </div>
          </div>
        </RouterLink>
      </div>
      <div v-if="movie.review_set.length === 0">
        <p>아직 작성된 리뷰가 없어요! (⊙x⊙;)</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { computed, onMounted, onUpdated, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useReviewStore } from "@/stores/review";
import { useUserStore } from "@/stores/user";
import { useRoute, RouterLink, useRouter } from "vue-router";
import TagCommentDetailModal from "@/components/TagCommentDetailModal.vue";
const store = useMovieStore();
const reviewstore = useReviewStore();
const userStore = useUserStore();
const route = useRoute();
const router = useRouter();
// const movie = ref(null);
const movieId = Number(route.params["id"]);
const content = ref("");
const form = ref(null);
const movie = computed(() => {
  return store.movie;
});
const tags = computed(() => {
  return store.movie.tagcomment_set;
});
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
    headers: { Authorization: `Token ${userStore.token}` },
  })
    .then((response) => {
      console.log(store.API_URL);
      console.log(response);
      // movie.value = response.data;
      store.getMovie(movieId);
    })
    .catch((error) => {
      console.log(error);
    });
};

const search = function (q) {
  store.search(q);
  router.push({ name: "search", query: q });
};
const searchByRuntime = function (runtime) {
  let runtimeQuery;
  if (runtime <= 60) {
    runtimeQuery = "under_1_hour";
  } else if (runtime <= 120) {
    runtimeQuery = "under_2_hours";
  } else if (runtime <= 180) {
    runtimeQuery = "under_3_hours";
  } else {
    runtimeQuery = "over_3_hours";
  }
  search({
    title: "",
    genre: "",
    keyword: "",
    runtime: runtimeQuery,
    country: "",
  });
};

console.log(store.API_URL);

onMounted(() => {
  // axios({
  //   method: "get",
  //   url: `${store.API_URL}/api/v1/movies/${movieId}/`,
  //   headers: { Authorization: `Token ${userStore.token}` },
  // })
  //   .then((response) => {
  //     console.log(store.API_URL);
  //     console.log(response);
  //     movie.value = response.data;
  //   })
  //   .catch((error) => {
  //     console.log(error);
  //   });
  store.getMovie(movieId);
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
  background-color: #ccd3ca;
  color: white;
}
.withwho {
  background-color: #b2c8df;
  color: white;
}
.runtime {
  background-color: #eed3d9;
  color: white;
}
.genre {
  background-color: #f4d19b;
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
.user-info {
  margin-top: 50px;
  display: flex;
}
.user-profile-img {
  height: 50px;
  width: 50px;
  border-radius: 100%;
}
.modal-section {
  width: 100%;
}
.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
