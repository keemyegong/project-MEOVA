<template>
  <div v-if="movie">
    <h3>{{ movie.title }}</h3>
    <img
      :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
      alt="movie-poster"
      class="movie-image"
    />
    <p>{{ movie.overview }}</p>
    <b>러닝타임</b>
    <p>{{ movie.runtime }}분</p>
    <b>국가</b>
    <p>{{ movie.origin_country }}</p>
    <b>개봉일</b>
    <p>{{ movie.release_date }}</p>
    <b>장르</b>
    <div v-for="genre in movie.genres">
      <p>{{ genre.name }}</p>
    </div>
    <b>키워드</b>
    <div v-for="keyword in movie.keywords">
      <p>{{ keyword.name }}</p>
    </div>
    <RouterLink
      :to="{ name: 'TagCommentDetailView', params: { id: movie.id } }"
    >
      <b>태그 코멘트</b>
    </RouterLink>
    <template v-if="movie.tagcomment_set">
      <div v-for="tagcomment in movie.tagcomment_set" :key="tagcomment.id">
        {{ tagcomment.content }}
        <span v-if="tagcomment.nickname"> | {{ tagcomment.nickname }} </span>
        <span v-else> | {{ tagcomment.username }} </span>
      </div>
    </template>
    <template v-else>
      <p>아직 태그코멘트가 없어요!</p>
    </template>

    <form @submit.prevent="createTag" ref="form">
      <input
        type="text"
        placeholder="영화의 태그가 적합한지 평가해 주세요!"
        id="content"
        v-model="content"
      />
      <input type="submit" value="입력" />
    </form>
    <button>
      <RouterLink :to="{ name: 'CreateReview', params: { id: movie.id } }">
        리뷰 생성
      </RouterLink>
    </button>

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
        <RouterLink :to="{ name: 'main' }">
          <p>제목 | {{ review.title }}</p>
          <p>배우 | {{ review.content }}</p>
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
  width: 200px;
}
.profile-image {
  width: 200px;
}
.director {
  display: flex;
}
.cast {
  display: flex;
}
</style>
