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
          console.log(res.data.key);
          token.value = res.data.key;
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
          console.log("회원가입 성공");
          const password = password1;
          login({ username, password });
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
        })
        .catch((error) => {
          console.log(error);
        });
    };
    const userinfo = ref({});
    const settings = function () {
      axios({
        method: "get",
        url: `${BASE_URL}/user/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res);
          userinfo.value = res.data;
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
    };
  },
  { persist: true }
);
