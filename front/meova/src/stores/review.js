import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";
import { useUserStore } from "./user";

export const useReviewStore = defineStore("review", () => {
  const user = useUserStore();
  const router = useRouter();
  const BASE_URL = "http://127.0.0.1:8000/api/v1/movies";
  const API_URL = "http://127.0.0.1:8000/api/v1";
  const createReview = function (review) {
    const { id, vote, title, content } = review;
    axios({
      method: "post",
      url: `${BASE_URL}/${id}/reviews/`,
      data: {
        vote,
        title,
        content,
      },
      headers: {
        Authorization: `Token ${user.token}`,
      },
    })
      .then((res) => {
        console.log("성공");
        console.log(res.data);
        router.push({
          name: 'ReviewDetailView', params: {movieId: id, reviewId: res.data.id}
        })
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const createTag = function (tag) {
    const { id, content } = tag;
    axios({
      method: "post",
      url: `${BASE_URL}/${id}/tag-comments/`,
      data: {
        content,
      },
      headers: {
        Authorization: `Token ${user.token}`,
      },
    })
      .then((res) => {
        console.log("성공");
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const createComment = function (review) {
    const { id, content } = review;
    axios({
      method: "post",
      url: `${API_URL}/reviews/${id}/comments/`,
      data: {
        content,
      },
      headers: {
        Authorization: `Token ${user.token}`,
      },
    })
      .then((res) => {
        console.log("성공");
        console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return { createReview, createTag, createComment };
});
