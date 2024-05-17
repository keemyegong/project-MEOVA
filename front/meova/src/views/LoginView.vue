<template>
  <div>
    <form class="row g-3 mt-5" @submit.prevent="login">
      <h1 class="col-md-6 offset-3 mb-3"><b>로그인</b></h1>
      <div class="col-md-6 offset-3">
        <label class="form-label" for="username">아이디</label>

        <input
          type="text"
          class="form-control"
          id="username"
          v-model="username"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="password" class="form-label">비밀번호</label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="password"
        />
      </div>

      <div class="col-md-6 offset-3">
        <button type="submit" class="btn btn-dark">로그인</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref } from "vue";

const username = ref("");
const password = ref("");
const store = useUserStore();
const login = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.login(payload);
};
</script>

<style scoped></style>
