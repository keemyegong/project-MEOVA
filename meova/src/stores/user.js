import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";
export const useUserStore = defineStore(
  "user",
  () => {
    const router = useRouter();
    const token = ref(null);
    const BASE_URL = "http://127.0.0.1:8000/accounts";
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });

    const userinfo = ref({});
    const settings = function () {
      return axios({
        method: "get",
        url: `${BASE_URL}/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          // console.log(res);
          userinfo.value = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const login = function (payload) {
      const { username, password } = payload;
      axios({
        method: "post",
        url: `${BASE_URL}/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          // console.log(res.data.key);
          token.value = res.data.key;
          settings();
          router.push({ name: "main" });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const signup = function (payload) {
      const { username, password1, password2 } = payload;
      axios({
        method: "post",
        url: `${BASE_URL}/signup/`,
        data: {
          username,
          password1,
          password2,
        },
      })
        .then((res) => {
          // console.log("회원가입 성공");
          const password = password1;
          login({ username, password });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const changepassword = function (payload) {
      const { old_password, new_password1, new_password2 } = payload;
      axios({
        method: "post",
        url: `${BASE_URL}/password/change/`,
        data: {
          old_password,
          new_password1,
          new_password2,
        },
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log("비밀번호 변경 성공");
          router.push({ name: "settings" });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const logout = function () {
      axios({
        method: "post",
        url: `${BASE_URL}/logout/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          token.value = null;
          router.push({ name: "main" });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const update = function (payload) {
      const { email, bio, nickname, profile_photo } = payload;
      axios({
        method: "put",
        url: `${BASE_URL}/update/`,
        data: {
          email,
          bio,
          nickname,
          profile_photo,
        },
        headers: {
          Authorization: `Token ${token.value}`,
          "Content-Type": "multipart/form-data",
        },
      })
        .then((res) => {
          console.log(res);
          userinfo.value = res.data;
          router.push({
            name: "profile",
            params: { username: res.data.username },
          });
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const profile_info = ref({});
    const profile = function (username) {
      axios({
        method: "get",
        url: `${BASE_URL}/profile/${username}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res);
          profile_info.value = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const follow = function (username) {
      return axios({
        method: "post",
        url: `${BASE_URL}/profile/${username}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          // console.log("팔로우 요청 받음 ! 받은 사람 정보 : ", res);
          if (profile_info.pk !== userinfo.pk) {
            profile_info.value.followers = res.data.followers;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const followerlist = ref([]);
    const followers = function () {
      axios({
        method: "get",
        url: `${BASE_URL}/followers/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          // console.log(res);
          followerlist.value = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const followinglist = ref([]);
    const followings = function () {
      axios({
        method: "get",
        url: `${BASE_URL}/followings/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          // console.log(res);
          followinglist.value = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    };
    return {
      token,
      isLogin,
      login,
      signup,
      logout,
      settings,
      userinfo,
      update,
      profile,
      profile_info,
      follow,
      followers,
      followerlist,
      followings,
      followinglist,
      changepassword,
    };
  },
  { persist: true }
);
