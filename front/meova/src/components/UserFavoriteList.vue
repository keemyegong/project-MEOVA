<template>
    <div class="nato-font">
      <p class="favorite-item-title">
        My Favorite
      </p>
      <div class="favorite">
          <div v-for="movie in profile.liked_movies"
              :key="movie.id">
              <div class="favorite-item">
                  <div class="card-body favorite-box">
                  <p class="favorite-content card-text">{{ movie.content }}</p>
                      <RouterLink
                      class="nav-link"
                      :to="{
                          name: 'MovieDetailView',
                          params: { id: movie.id },
                      }">
                          <div class="movie-info">
                              <img
                              :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path"
                              alt="movie poster image"
                              class="poster-img"
                              />
                              <p class="movie-title ms-3 card-subtitle mt-2 text-body-secondary">
                                  {{ movie.title }}
                              </p>
                              
                          </div>
                      </RouterLink>
                  </div>
              </div>
          </div>
          <div v-if="profile.liked_movies.length === 0">
            <p class="ms-4">아직 좋아한 영화가 없어요! (⊙_⊙;)</p>
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
    margin-top: 10%;
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
  .poster-img {
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
    