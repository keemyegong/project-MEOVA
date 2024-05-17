<template>
  <div>
    <form @submit.prevent="signup">
      <label for="username">아이디 : </label>
      <input type="text" id="username" v-model="username" />
      <label for="password1">비밀번호 : </label>
      <input type="password" id="password1" v-model="password1" />
      <label for="password2">비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2" />
      <input type="submit" value="회원가입" />
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
