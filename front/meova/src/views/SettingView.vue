<template>
  <div>
    <div class="row g-3 mb-5 mt-5">
      <img
        class="col-1 offset-3"
        :src="store.userinfo.profile_photo"
        v-if="store.userinfo.profile_photo"
        alt=""
      />
      <img
        class="col-1 offset-3"
        src="@/assets/default_profile.png"
        v-else
        alt=""
      />
      <div class="col-3">
        <h3>
          <b>
            {{ store.userinfo.username }}
          </b>
        </h3>
        <button class="btn btn-dark btn-sm">비밀번호 바꾸기</button>
      </div>
    </div>
    <form class="row g-3" @submit.prevent="update">
      <div class="col-md-6 offset-3">
        <label class="form-label" for="profile_photo">프로필 사진</label>
        <input
          type="file"
          class="form-control"
          id="profile_photo"
          @change="handleFileChange"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="nickname" class="form-label">닉네임</label>
        <input
          type="text"
          class="form-control"
          id="nickname"
          v-model="nickname"
        />
      </div>
      <div class="col-md-6 offset-3">
        <label for="email" class="form-label">이메일</label>
        <input type="email" class="form-control" id="email" v-model="email" />
      </div>
      <div class="col-md-6 offset-3">
        <label for="bio" class="form-label">소개글</label>
        <textarea
          class="form-control"
          v-model="bio"
          id="bio"
          rows="3"
        ></textarea>
      </div>

      <div class="col-md-6 offset-3">
        <button type="submit" class="btn btn-dark">프로필 업데이트</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { onMounted, ref } from "vue";

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
</script>

<style scoped></style>
