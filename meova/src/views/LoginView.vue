<template>
  <div class="login">
    <form class="login-form" @submit.prevent="login">
      <h1 class="nato-font"><b>로그인</b></h1>
      <div>
        <label class="mt-3 form-label" for="username">
          <p>아이디</p></label>

        <input
          type="text"
          class="form-control"
          id="username"
          v-model="username"
        />
      </div>
      <div>
        <label for="password" class="mt-3 form-label">
          <p>비밀번호</p></label>
        <input
          type="password"
          class="form-control"
          id="password"
          v-model="password"
        />
      </div>

      <div>
        <button type="submit" class="nato-font btn btn-dark mt-3">로그인</button>
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

<style scoped>
  .nato-font {
    font-family: "Noto Sans KR", sans-serif;
    font-optical-sizing: auto;
    font-style: normal;
  }

  .login {
    margin-top: 70px;
  }
  .login-form {
    margin: auto;
    width: 50%;
    max-width: 500px;
    min-width: 300px;
  }

</style>
