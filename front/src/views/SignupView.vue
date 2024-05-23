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
        <p v-if="errors.username" class="error">{{ errors.username }}</p>
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
        <p v-if="errors.password1" class="error">{{ errors.password1 }}</p>
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
        <p v-if="errors.password2" class="error">{{ errors.password2 }}</p>
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
const errors = ref({
  username: "",
  password1: "",
  password2: "",
});
const store = useUserStore();

const validate = () => {
  let isValid = true;

  // 아이디 유효성 검사
  if (!username.value) {
    errors.value.username = "아이디를 입력하세요.";
    isValid = false;
  } else {
    errors.value.username = "";
  }

  // 비밀번호 유효성 검사
  if (!password1.value) {
    errors.value.password1 = "비밀번호를 입력하세요.";
    isValid = false;
  } else if (password1.value.length < 6) {
    errors.value.password1 = "비밀번호는 최소 6자 이상이어야 합니다.";
    isValid = false;
  } else {
    errors.value.password1 = "";
  }

  // 비밀번호 확인 유효성 검사
  if (!password2.value) {
    errors.value.password2 = "비밀번호 확인을 입력하세요.";
    isValid = false;
  } else if (password1.value !== password2.value) {
    errors.value.password2 = "비밀번호가 일치하지 않습니다.";
    isValid = false;
  } else {
    errors.value.password2 = "";
  }

  return isValid;
};

const signup = () => {
  if (validate()) {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
    };
    store.signup(payload);
  }
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

.error {
  margin-top: 1%;
  color: red;
  font-size: 0.9em;
}
</style>
