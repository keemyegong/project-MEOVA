<template>
  <div v-if="movie" class="row">
    <div class="movie-info col-6">
      <h1 class="mb-3">
        <b>{{ movie.title }}</b>
      </h1>
      <p class="overview">{{ movie.overview }}</p>
      <button class="btn runtime">{{ movie.runtime }}분</button>
      <button class="btn country">{{ movie.origin_country }}</button>

      <button class="btn btn-light">{{ movie.release_date }}</button>

      <button class="btn genre" v-for="genre in movie.genres">
        {{ genre.name }}
      </button>

      <button class="btn withwho" v-for="keyword in movie.keywords">
        {{ keyword.name }}
      </button>
      <div class="tag-comment">
        <RouterLink
          :to="{ name: 'TagCommentDetailView', params: { id: movie.id } }"
        >
          <b>태그 코멘트</b>
        </RouterLink>
        <template v-if="movie.tagcomment_set">
          <div
            v-for="tagcomment in movie.tagcomment_set.slice().reverse()"
            :key="tagcomment.id"
          >
            {{ tagcomment.content }}
            <span v-if="tagcomment.nickname">
              | {{ tagcomment.nickname }}
            </span>
            <span v-else> | {{ tagcomment.username }} </span>
          </div>
        </template>
        <template v-else>
          <p>아직 태그코멘트가 없어요!</p>
        </template>
      </div>
      <form @submit.prevent="createTag" class="row" ref="form">
        <div class="col-9">
          <input
            type="text"
            placeholder="영화의 태그가 적합한지 평가해 주세요!"
            id="content"
            class="form-control"
            v-model="content"
          />
        </div>
        <input type="submit" class="btn btn-dark col-3" value="입력" />
      </form>
    </div>
    <div class="poster-review col-6">
      <div class="rol">
        <img
          :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
          alt="movie-poster"
          class="movie-image col-12"
        />
        <button class="mt-3 col-12 btn btn-warning">
          <RouterLink :to="{ name: 'CreateReview', params: { id: movie.id } }">
            리뷰 생성
          </RouterLink>
        </button>
      </div>
    </div>

    <template v-if="movie.watchproviders.length > 0">
      <b>Provider</b>
      <div v-for="watchprovider in movie.watchproviders">
        {{ watchprovider }}
      </div>
    </template>
    <hr />
    <b>감독</b>
    <div class="director" v-for="director in movie.directors">
      <RouterLink
        :to="{ name: 'DirectorDetailView', params: { id: director.id } }"
      >
        <p>{{ director.name }}</p>
      </RouterLink>
    </div>
    <hr />
    <b>출연진</b>
    <template class="cast">
      <div v-for="credit in movie.credits">
        <RouterLink
          :to="{ name: 'ActorDetailView', params: { id: credit.actor.id } }"
        >
          <img
            :src="
              'https://image.tmdb.org/t/p/original/' + credit.actor.profile_path
            "
            alt="actor-profile"
            class="profile-image"
          />
          <p>캐릭터 | {{ credit.character }}</p>
          <p>배우 | {{ credit.actor.name }}</p>
        </RouterLink>
      </div>
    </template>

    <template class="review">
      <div v-for="review in movie.review_set">
        <p>hhhhh</p>
        <RouterLink
          :to="{
            name: 'ReviewDetailView',
            params: { movieId: movie.id, reviewId: review.id },
          }"
        >
          <p>제목 | {{ review.title }}</p>
          <p>내용 | {{ review.content }}</p>
        </RouterLink>
      </div>
    </template>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, onUpdated, ref } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useRoute, RouterLink } from "vue-router";
import { useReviewStore } from "@/stores/review";

const store = useMovieStore();
const reviewstore = useReviewStore();
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
.movie-image {
  width: 100%;
}
.profile-image {
  width: 200px;
  height: 200px;
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
.review {
  display: flex;
}

.movie-info > button {
  margin-right: 3px;
  margin-bottom: 3px;
}
.overview {
  display: -webkit-box;
  -webkit-line-clamp: 3; /* 보여줄 줄 수 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
.tag-comment {
  width: 100%;
  max-height: 300px; /* 최대 높이 설정 */
  overflow: auto; /* 세로 스크롤 설정 */
  top: auto;
}
.country {
  background-color: #eed3d9;
  color: white;
}
.withwho {
  background-color: #ccd3ca;
  color: white;
}
.runtime {
  background-color: #ead7c7;
  color: white;
}
.genre {
  background-color: #b5c0d0;
  color: white;
}
</style>
