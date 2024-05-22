<template>
    <div class="nato-font">
      <p class="favorite-item-title">
        Favorite Reviews
      </p>
      <div class="favorite" v-if="profile.liked_reviews">
          <div v-for="review in profile.liked_reviews.slice().reverse()"
              :key="review.id">
              <div class="favorite-item">
                  <div class="card-body favorite-box">
                  <p class="favorite-content card-text">{{ review.title }}</p>
                      <RouterLink
                      class="nav-link"
                      :to="{
                          name: 'ReviewDetailView',
                          params: { movieId: review.movie.id, reviewId: review.id},
                      }">
                          <div class="movie-info">
                            <img
                              v-if="review.profile_photo"
                              :src="review.profile_photo"
                              class="profile-img"
                              alt="profile_img"
                            />
                            <img
                              class="profile-img"
                              src="@/assets/default_profile.png"
                              v-else
                              alt=""
                            />
                              <p class="movie-title ms-3 card-subtitle mt-2 text-body-secondary">
                                  {{ review.content }}
                              </p>
                              
                          </div>
                      </RouterLink>
                  </div>
              </div>
          </div>
          <div v-if="profile.liked_reviews.length === 0">
            <p class="ms-4">아직 좋아한 리뷰가 없어요! (⊙_⊙;)</p>
          </div>
        </div>
      </div>
  </template>
    
  <script setup>
  import axios from "axios";
  import { ref, onMounted } from "vue";
  import { useUserStore } from "@/stores/user";
  import { useReviewStore } from "@/stores/review";
  import { useRoute } from "vue-router";
  
  const reviewStore = useReviewStore();
  const userStore = useUserStore();
  const route = useRoute(); 
  
  const props = defineProps({
    'profile': Object,
  });

  console.log(props.profile)

  </script>
    
  <style scoped>
  .favorite {
    display: flex;
  }
  .favorite-item-title {
    margin-top: 5%;
    margin-left: 2%;
    font-size: 40px;
    font-family: "Caprasimo", serif;
    font-weight: 400;
    font-style: normal;
  }
  .favorite-item {
    height: 200px;
    width: 330px;
    margin-right: 10px;
    padding: 10px;
    margin: 10px;
    border-radius: 10px 10px 10px 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  .favorite-box {
    padding: 10px;
  }
  .favorite-content {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .movie-info {
    margin-top: 50px;
    display: flex;
  }
  .movie-title {
      font-weight: 700;
  }
  .profile-img {
    height: 50px;
    width: 50px;
    border-radius: 100%;
  }
  .nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}
  </style>
    