<template>
  <div>
    <section v-if="store.profile_info" class="nato-font profile">
      <img
        v-if="store.profile_info.profile_photo"
        :src="store.profile_info.profile_photo"
        class="profile_img"
        alt="profile_img"
      />
      <img
        class="profile_img"
        src="@/assets/default_profile.png"
        v-else
        alt=""
      />
      <h1 v-if="store.profile_info.nickname">
        {{ store.profile_info.nickname }}
      </h1>
      <h1 v-else>{{ store.profile_info.username }}</h1>
      <p>{{ store.profile_info.bio }}</p>
      <div
        class="followinfo"
        v-if="store.profile_info.pk === store.userinfo.pk"
      >
        <button
          type="button"
          class="btn"
          data-bs-toggle="modal"
          data-bs-target="#ProfileFollowerListModal"
        >
          follower <b class="follow-cnt">{{ follower_count }}</b>
        </button>

        <!-- Modal -->
        <div
          class="modal fade modal-section"
          id="ProfileFollowerListModal"
          tabindex="-1"
          aria-labelledby="ProfileFollowerListModal"
          aria-hidden="true"
        >
          <ProfileFollowerListModal />
        </div>
        |<button
          type="button"
          class="btn"
          data-bs-toggle="modal"
          data-bs-target="#ProfileFollowingListModal"
        >
          following
          <b class="follow-cnt">{{ following_count }}</b>
        </button>
        <div
          class="modal fade modal-section"
          id="ProfileFollowingListModal"
          tabindex="-1"
          aria-labelledby="ProfileFollowerListModal"
          aria-hidden="true"
        >
          <ProfileFollowingListModal />
        </div>
      </div>
      <button v-if="store.profile_info.pk != store.userinfo.pk" @click="follow">
        <div v-if="isFollow">unfollow</div>
        <div v-else>follow</div>
      </button>
    </section>
    <Calendar :userid="store.profile_info.pk" />
    <UserReviewList :userid="store.profile_info.pk" />
    <UserFavoriteList :profile="store.profile_info" />
  </div>
</template>

<script setup>
import Calendar from "@/components/Calender.vue";
import ProfileFollowerListModal from "@/components/ProfileFollowerListModal.vue";
import ProfileFollowingListModal from "@/components/ProfileFollowingListModal.vue";
import UserReviewList from "@/components/UserReviewList.vue";
import UserFavoriteList from "@/components/UserFavoriteList.vue";
import { useUserStore } from "@/stores/user";
import { ref, onMounted, computed } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const store = useUserStore();

store.profile(route.params.username);
const isFollow = computed(() => {
  return store.profile_info.followers.includes(store.userinfo.pk);
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
onMounted(() => {
  store.settings();
});
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

.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}

.follow-cnt {
  margin-left: 3px;
}
</style>
