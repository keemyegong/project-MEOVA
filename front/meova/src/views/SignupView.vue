<template>
  <div>
    <form class="row g-3 mt-5" @submit.prevent="signup">
      <h1 class="nato-font col-md-6 offset-3 mb-3"><b>회원가입</b></h1>
      <div class="col-md-6 offset-3">
        <label class="nato-font form-label" for="username">아이디</label>

        <input
          type="text"
          class="form-control"
          id="username"
          v-model="username"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="password1" class="nato-font form-label">비밀번호</label>
        <input
          type="password"
          class="form-control"
          id="password1"
          v-model="password1"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="password1" class="nato-font form-label">비밀번호 확인</label>
        <input
          type="password"
          class="form-control"
          id="password2"
          v-model="password2"
        />
      </div>

      <div class="col-md-6 offset-3">
        <button type="submit" class="nato-font btn btn-dark">회원가입</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref } from "vue";

const username = ref("");
const password1 = ref("");
const password2 = ref("");
const store = useUserStore();
const signup = () => {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signup(payload);
};
</script>

<style scoped>
  .nato-font {
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
  }
</style>