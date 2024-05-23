<template>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title movie-category-title" id="exampleModalLabel">
          Tag Comments
        </h1>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="modal"
          aria-label="Close"
        ></button>
      </div>
      <div class="modal-body">
        <template v-if="movie && tags">
          <div v-for="tagcomment in tags" :key="tagcomment.id">
            <div class="tag-comment">
              <span class="tag-comment-content">
                <i class="bi bi-chat-dots-fill me-2"></i>
                {{ tagcomment.content }}
              </span>
              <span class="tag-comment-user">
                |
                {{
                  tagcomment.nickname
                    ? tagcomment.nickname
                    : tagcomment.username
                }}
              </span>
              <span class="tag-comment-user ms-5">
                {{ reviewStore.changeToDate(tagcomment.created_at) }}</span
              >
              <button
                v-if="isReviewOwner(tagcomment.user)"
                @click="deleteComment(tagcomment.id)"
                class="delete-btn btn btn-dark"
              >
                <p class="delete-btn-value">삭제</p>
              </button>
            </div>
          </div>
        </template>
        <template v-else>
          <p>아직 태그코멘트가 없어요!</p>
        </template>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-dark" data-bs-dismiss="modal">
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, computed, onMounted } from "vue";
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";
import { useRoute, RouterLink } from "vue-router";
import { storeToRefs } from "pinia";
import { useReviewStore } from "@/stores/review";

const userStore = useUserStore();
const movieStore = useMovieStore();
const reviewStore = useReviewStore();
const tags = computed(() => {
  return movieStore.movie.tagcomment_set;
});
const route = useRoute();
const movieId = Number(route.params["id"]);
const movie = computed(() => {
  return movieStore.movie;
});
// const fetchComment = function () {
//   axios({
//     method: "get",
//     url: `${movieStore.API_URL}/api/v1/movies/${movieId}/`,
//     headers: { Authorization: `Token ${userStore.token}` },
//   })
//     .then((response) => {
//       movie.value = response.data;
//     })
//     .catch((error) => {
//       console.log(error);
//     });
// };
onMounted(() => {
  // fetchComment()
  movieStore.getMovie(movieId);
});
const deleteComment = (tagcommentId) => {
  axios({
    method: "delete",
    url: `${movieStore.API_URL}/api/v1/tag-comments/${tagcommentId}/`,
    headers: {
      Authorization: `Token ${userStore.token}`,
    },
  })
    .then(() => {
      // movie.value.tagcomment_set = movie.value.tagcomment_set.filter(
      // //   (tagcomment) => tagcomment.id !== tagcommentId
      // );
      movieStore.getMovie(movieId);
    })
    .catch((error) => {
      console.log(error);
    });
};

const isReviewOwner = (user) => {
  return (
    movie.value.tagcomment_set &&
    userStore.userinfo &&
    user === userStore.userinfo.pk
  );
};
</script>

<style scoped>
.movie-category-title {
  margin-top: 0px;
  text-align: center;
  font-size: 50px;
  font-family: "Caprasimo", serif;
  font-weight: 400;
  font-style: normal;
}
.tag-comment {
  padding: 10px;
  margin: 10px;
  background-color: #f0f0f0;
  border-radius: 10px 10px 10px 10px;
}
.tag-comment-user {
  margin-left: 5px;
  font-size: 13px;
  color: lightslategray;
}
.tag-comment-content {
  margin: 10px;
}
.delete-btn-value {
  font-size: 11px;
}
.delete-btn {
  margin-left: 10px;
  width: 50px;
  height: 30px;
}
.modal-content {
  width: 700px;
}
</style>
