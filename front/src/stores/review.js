import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";
import { useUserStore } from "./user";
import moment from "moment";
export const useReviewStore = defineStore("review", () => {
  const user = useUserStore();
  const router = useRouter();
  const BASE_URL = "http://127.0.0.1:8000/api/v1/movies";
  const API_URL = "http://127.0.0.1:8000/api/v1";
  const changeToDate = (datetime) => {
    // 오늘 날짜
    let now = moment(new Date());
    // 오늘과의 시간 차이
    let duration = moment.duration(now.diff(datetime));
    // 변환
    // asSeconds 를 하면 오늘과의 시간차이를
    // 초단위로 float datatype 으로 보여준다 (3.82 이런식)
    let seconds = duration.asSeconds();
    let minute = duration.asMinutes();
    let hours = duration.asHours();
    let days = duration.asDays();
    let weeks = duration.asWeeks();
    let month = duration.asMonths();
    let year = duration.asYears();

    // 그래서 사용할 때는 parseInt 를 사용해 int 로 바꿔야 한다.
    if (minute < 1) {
      // 1분 미만이면 초 단위로 보여주고,
      return parseInt(seconds) + "초 전";
    } else if (hours < 1) {
      // 1시간 미만이면 분 단위로 보여주고
      return parseInt(minute) + "분 전";
    } else if (hours < 24) {
      // 하루 미만이면 시간으로 보여주고
      return parseInt(hours) + "시간 전";
    } else if (weeks < 1) {
      // 일주일 미만이면 일 단위로 보여주고
      return parseInt(days) + "일 전";
    } else if (month < 1) {
      // 한 달 미만이면 주 단위로 보여주고
      return parseInt(weeks) + "주 전";
    } else if (year < 1) {
      // 1년 미만이면 달 단위로 보여주고
      return parseInt(month) + "달 전";
    } else {
      // 1년 이상이면 넌 단위로 보여주고
      return parseInt(year) + "년 전";
    }
  };
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
        // console.log("성공");
        // console.log(res.data);
        router.push({
          name: "ReviewDetailView",
          params: { movieId: id, reviewId: res.data.id },
        });
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const updateReview = function (review) {
    const { id, vote, title, content } = review;
    axios({
      method: "put",
      url: `${API_URL}/reviews/${id}/`,
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
        // console.log("성공");
        router.push({
          name: "ReviewDetailView",
          params: { movieId: id, reviewId: id },
        });
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
        // console.log("성공");
        // console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const createComment = function (review) {
    const { id, content } = review;
    return axios({
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
        // console.log("성공");
        // console.log(res);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const review = ref(null);
  const userStore = useUserStore();
  const fetchReview = function (reviewId) {
    axios({
      method: "get",
      url: `${API_URL}/reviews/${reviewId}/`,
      headers: {
        Authorization: `Token ${userStore.token}`,
      },
    })
      .then((response) => {
        // console.log(response.data);
        review.value = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  };
  return {
    API_URL,
    createReview,
    updateReview,
    createTag,
    createComment,
    fetchReview,
    review,
    changeToDate,
  };
});
