<template>
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title movie-category-title" id="exampleModalLabel">
          Followings
        </h1>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="modal"
          aria-label="Close"
        ></button>
      </div>
      <div class="modal-body">
        <template v-if="followings.length !== 0">
          <div v-for="following in followings" :key="following.pk">
            <div class="follower-card">
              <span class="follower-card-content">
                <img
                  v-if="following.profile_photo"
                  :src="following.profile_photo"
                  class="profile_img"
                  alt="profile_img"
                />
                <img
                  class="profile_img"
                  src="@/assets/default_profile.png"
                  v-else
                  alt=""
                />
              </span>
              <span class="follower-card-user">
                |
                {{
                  following.nickname ? following.nickname : following.username
                }}
              </span>
              <!-- <button
                @click="toggleFollow(follower)"
                class="delete-btn btn btn-dark"
              >
                <div class="delete-btn-value">unfollow</div>
              </button> -->
            </div>
          </div>
        </template>
        <template v-else>
          <p>아직 팔로우 중인 사용자가 없어요!</p>
        </template>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-dark" data-bs-dismiss="modal">
          Close
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { onMounted, computed } from "vue";
const store = useUserStore();
const followings = computed(() => {
  return store.followinglist;
});

onMounted(() => {
  store.followings();
});
</script>

<style scoped>
.profile_img {
  height: 60px;
  width: 60px;
  border-radius: 50%;
}

.movie-category-title {
  margin-top: 0px;
  font-size: 50px;
  font-family: "Caprasimo", serif;
  font-weight: 400;
  font-style: normal;
}
.follower-card {
  padding: 10px;
  margin: 10px;
  background-color: #f0f0f0;
  border-radius: 10px 10px 10px 10px;
}
.follower-card-user {
  margin-left: 5px;
  font-size: 13px;
  color: lightslategray;
}
.follower-card-content {
  margin: 10px;
}
.delete-btn-value {
  font-size: 11px;
}
.delete-btn {
  margin-left: 10px;
  width: 50px;
  height: 30px;
}
.modal-content {
  width: 100%;
}
</style>
