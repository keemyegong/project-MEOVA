<template>
  <div>
    <form class="row g-3 mt-5" @submit.prevent="changepassword">
      <h1 class="col-md-6 offset-3 mb-3"><b>비밀번호 변경</b></h1>
      <div class="col-md-6 offset-3">
        <label class="form-label" for="password">현재 비밀번호</label>

        <input
          type="password"
          class="form-control"
          id="password"
          v-model="old_password"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="password1" class="form-label">새로운 비밀번호</label>
        <input
          type="password"
          class="form-control"
          id="password1"
          v-model="new_password1"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="password1" class="form-label">새로운 비밀번호 확인</label>
        <input
          type="password"
          class="form-control"
          id="password2"
          v-model="new_password2"
        />
      </div>

      <div class="col-md-6 offset-3">
        <button type="submit" class="btn btn-dark">회원가입</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref } from "vue";

const old_password = ref("");
const new_password1 = ref("");
const new_password2 = ref("");
const store = useUserStore();
const changepassword = () => {
  const payload = {
    old_password: old_password.value,
    new_password1: new_password1.value,
    new_password2: new_password2.value,
  };
  store.changepassword(payload);
};
</script>
