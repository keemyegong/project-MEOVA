
import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import SettingView from "@/views/SettingView.vue";
import PopularMovieView from '@/views/PopularMovieView.vue'
import ReleaseMovieView from '@/views/ReleaseMovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ActorDetailView from '@/views/ActorDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "main",
      component: MainView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignupView,
    },
    {
      path: "/settings",
      name: "settings",
      component: SettingView,
    },
    {
      path: '/movies/popular',
      name: 'PopularMovieView',
      component: PopularMovieView
    },
    {
      path: '/movies/release',
      name: 'ReleaseMovieView',
      component: ReleaseMovieView
    },
    {
      path: '/movies/:id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path: '/actors/:id',
      name: 'ActorDetailView',
      component: ActorDetailView
    },
  ]
})

export default router;
