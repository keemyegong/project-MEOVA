import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import PopularMovieView from '@/views/PopularMovieView.vue'
import ReleaseMovieView from '@/views/ReleaseMovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ActorDetailView from '@/views/ActorDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
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

export default router
