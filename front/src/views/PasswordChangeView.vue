<template>
  <div class="login">
    <form class="row g-3 mt-5 login-form" @submit.prevent="changepassword">
      <h1 class="nato-font mb-3"><b>비밀번호 변경</b></h1>
      <div>
        <label class="nato-font form-label mt-3" for="nato-font password"
          >현재 비밀번호</label
        >

        <input
          type="password"
          class="form-control"
          id="password"
          v-model="old_password"
        />
      </div>
      <div>
        <label for="password1" class="nato-font form-label mt-3"
          >새로운 비밀번호</label
        >
        <input
          type="password"
          class="form-control"
          id="password1"
          v-model="new_password1"
        />
      </div>
      <div>
        <label for="password1" class="nato-font form-label mt-3"
          >새로운 비밀번호 확인</label
        >
        <input
          type="password"
          class="form-control"
          id="password2"
          v-model="new_password2"
        />
      </div>

      <div>
        <button type="submit" class="nato-font btn btn-dark">변경</button>
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

<style scoped>
.login {
  margin-top: 70px;
}
.login-form {
  margin: auto;
  width: 50%;
  max-width: 500px;
  min-width: 300px;
}

.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
</style>
<!-- 
<template>
  <div class="login">
    <form class="nato-font login-form" @submit.prevent="signup">
      <h1 class="nato-font"><b>회원가입</b></h1>
      <div>
        <label class="nato-font form-label mt-3" for="username">아이디</label>
        <input
          type="text"
          class="form-control"
          id="username"
          v-model="username"
        />
      </div>
      <div>
        <label for="password1" class="nato-font form-label mt-3"
          >비밀번호</label
        >
        <input
          type="password"
          class="form-control"
          id="password1"
          v-model="password1"
        />
      </div>
      <div>
        <label for="password2" class="nato-font form-label mt-3"
          >비밀번호 확인</label
        >
        <input
          type="password"
          class="form-control"
          id="password2"
          v-model="password2"
        />
      </div>
      <div>
        <button type="submit" class="nato-font btn btn-dark mt-3">
          회원가입
        </button>
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

.login {
  margin-top: 70px;
}
.login-form {
  margin: auto;
  width: 50%;
  max-width: 500px;
  min-width: 300px;
}
</style> -->
