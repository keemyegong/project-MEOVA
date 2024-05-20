import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import SettingView from "@/views/SettingView.vue";
import ProfileView from "@/views/ProfileView.vue";
import ProfileFollowerListView from "@/views/ProfileFollowerListView.vue";
import PopularMovieView from "@/views/PopularMovieView.vue";
import ReleaseMovieView from "@/views/ReleaseMovieView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import ReviewCreateView from "@/views/ReviewCreateView.vue";
import ActorDetailView from "@/views/ActorDetailView.vue";
import DirectorDetailView from "@/views/DirectorDetailView.vue";
import TagCommentDetailView from "@/views/TagCommentDetailView.vue";
import ReviewDetailView from "@/views/ReviewDetailView.vue";
import ReviewUpdateView from "@/views/ReviewUpdateView.vue";

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
      path: "/profile/:username",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/profile/followerlist",
      name: "followerlist",
      component: ProfileFollowerListView,
    },
    {
      path: "/movies/popular",
      name: "PopularMovieView",
      component: PopularMovieView,
    },
    {
      path: "/movies/release",
      name: "ReleaseMovieView",
      component: ReleaseMovieView,
    },
    {
      path: "/movies/:id",
      name: "MovieDetailView",
      component: MovieDetailView,
    },
    {
      path: "/movies/:id/review/",
      name: "CreateReview",
      component: ReviewCreateView,
    },
    {
      path: "/movies/:movieId/reviews/:reviewId",
      name: "ReviewDetailView",
      component: ReviewDetailView,
    },
    {
      path: "/movies/reviews/:reviewId",
      name: "ReviewUpdateView",
      component: ReviewUpdateView,
    },
    {
      path: "/actors/:id",
      name: "ActorDetailView",
      component: ActorDetailView,
    },
    {
      path: "/directors/:id",
      name: "DirectorDetailView",
      component: DirectorDetailView,
    },
    {
      path: "/:id/tagcomments",
      name: "TagCommentDetailView",
      component: TagCommentDetailView,
    },
  ],
});
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";
router.beforeEach((to, from) => {
  const store = useUserStore();
  const movie = useMovieStore();
  if ((to.name === "login" || to.name === "signup") && store.isLogin) {
    return { name: "main" };
  }
  if (to.name === "settings" && store.isLogin === false) {
    return { name: "login" };
  }
  if (to.name === "main") {
    movie.isMain = true;
  } else {
    movie.isMain = false;
  }
});

export default router;
