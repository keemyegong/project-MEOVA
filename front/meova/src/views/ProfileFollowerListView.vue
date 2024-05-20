<template>
  <div>
    <div v-for="follower in store.followerlist">
      <div class="follower-card">
        <img
          v-if="follower.profile_photo"
          :src="follower.profile_photo"
          class="profile_img"
          alt="profile_img"
        />
        <img
          class="profile_img"
          src="@/assets/default_profile.png"
          v-else
          alt=""
        />
        <div>
          <h3>{{ follower.username }}</h3>
          <h4>{{ follower.nickname }}</h4>
        </div>
        <button @click="toggleFollow(follower)">
          <div v-if="isFollowing(follower.pk)">unfollow</div>
          <div v-else>follow</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { onMounted, computed } from "vue";
const store = useUserStore();
const isFollowing = (followerPk) => {
  console.log(store.userinfo);
  return store.userinfo.followings.includes(followerPk);
};
const toggleFollow = async (follower) => {
  if (isFollowing(follower.pk)) {
    await store.follow(follower.username); // Unfollow 메소드가 필요함
  } else {
    await store.follow(follower.username);
  }
  await store.settings(); // Follow/Unfollow 후 사용자 정보를 다시 가져옵니다.
};
onMounted(() => {
  store.followers();
});
</script>

<style scoped>
.profile_img {
  height: 100px;
  width: 100px;
  border-radius: 50%;
}
.follower-card {
  display: flex;
  justify-content: space-between;
}
</style>
