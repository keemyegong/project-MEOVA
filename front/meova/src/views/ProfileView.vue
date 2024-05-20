<template>
  <div>
    <section v-if="store.profile_info" class="profile">
      <img :src="store.profile_info.profile_photo" class="profile_img" alt="" />
      <h1 v-if="store.profile_info.nickname">
        {{ store.profile_info.nickname }}
      </h1>
      <h1 v-else>{{ store.profile_info.username }}</h1>
      <p>{{ store.profile_info.bio }}</p>
      <button>
        follower <b>{{ follower_count }}</b></button
      >|<button>
        following
        <b>{{ following_count }}</b>
      </button>
      <button v-if="store.profile_info.pk != store.userinfo.pk" @click="follow">
        {{ store.userinfo }}
        <div v-if="isFollow">unfollow</div>
        <div v-else>follow</div>
      </button>
    </section>
    <Calendar :userid="store.profile_info.pk" />
  </div>
</template>

<script setup>
import Calendar from "@/components/Calender.vue";
import { useUserStore } from "@/stores/user";
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const store = useUserStore();

store.profile(route.params.username);
const isFollow = computed(() => {
  return store.profile_info.followers.includes(store.userinfo);
});
const follower_count = computed(() => {
  return store.profile_info.followers.length;
});
const following_count = computed(() => {
  return store.profile_info.followings.length;
});
const follow = function () {
  store.follow(route.params.username);
};
</script>

<style scoped>
.profile_img {
  margin-top: 50px;
  border-radius: 50%;
  width: 200px;
  height: 200px;
}
.profile {
  text-align: center;
}
.profile > h1 {
  margin-top: 30px;
  font-size: 45px;
}
.profile > button {
  border: 0cap;
  background-color: white;
}
</style>
