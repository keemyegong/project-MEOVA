<template>
  <div>
    <div class="nato-font profile-header">
      <div class="profile-photo">
        <img
          :src="store.userinfo.profile_photo"
          v-if="store.userinfo.profile_photo"
          alt="Profile Photo"
        />
        <img
          src="@/assets/default_profile.png"
          v-else
          alt="Default Profile Photo"
        />
      </div>
      <div class="profile-info">
        <h3>
          <b>{{ store.userinfo.username }}</b>
        </h3>
        <button class="btn btn-dark btn-sm" @click="changepassword">
          비밀번호 바꾸기
        </button>
      </div>
    </div>
    <form class="nato-font row g-3 login-form" @submit.prevent="update">
      <div>
        <label class="mt-3 form-label" for="profile_photo">프로필 사진</label>
        <input
          type="file"
          class="form-control"
          id="profile_photo"
          @change="handleFileChange"
        />
      </div>
      <div>
        <label for="nickname" class="mt-3 form-label">닉네임</label>
        <input
          type="text"
          class="form-control"
          id="nickname"
          v-model="nickname"
        />
      </div>
      <div>
        <label for="email" class="mt-3 form-label">이메일</label>
        <input type="email" class="form-control" id="email" v-model="email" />
      </div>
      <div>
        <label for="bio" class="mt-3 form-label">소개글</label>
        <textarea
          class="form-control"
          v-model="bio"
          id="bio"
          rows="3"
        ></textarea>
      </div>
      <div>
        <button type="submit" class="btn btn-dark">프로필 업데이트</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const store = useUserStore();
onMounted(() => {
  store.settings();
});
const email = ref(store.userinfo.email);
const nickname = ref(store.userinfo.nickname);
const bio = ref(store.userinfo.bio);
const profile_photo = ref(null);
const handleFileChange = function (event) {
  profile_photo.value = event.target.files[0];
};
const update = function () {
  const payload = {
    email: email.value,
    nickname: nickname.value,
    bio: bio.value,
    profile_photo: profile_photo.value,
  };
  store.update(payload);
};
const router = useRouter();
const changepassword = function () {
  router.push({ name: "changepassword" });
};
</script>

<style scoped>
.profile-header {
  margin-top: 70px;
  display: flex;
  align-items: center;
  justify-content: center; /* 중앙 정렬 */
}

.profile-photo img {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 20px; /* 이미지와 프로필 정보 간의 간격 */
}

.profile-info {
  display: flex;
  flex-direction: column;
  align-items: center; /* 프로필 정보를 가운데 정렬 */
}

.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}

.login-form {
  margin: auto;
  width: 50%;
  max-width: 500px;
  min-width: 300px;
}
</style>
