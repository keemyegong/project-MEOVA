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
        <button @click="follow(follower.username, follower.pk)">
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
const follow = function (username) {
  store.follow(username);
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
