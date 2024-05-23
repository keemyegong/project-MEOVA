import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import SearchView from "@/views/SearchView.vue";
import LoginView from "@/views/LoginView.vue";
import SignupView from "@/views/SignupView.vue";
import SettingView from "@/views/SettingView.vue";
import PasswordChangeView from "@/views/PasswordChangeView.vue";
import ProfileView from "@/views/ProfileView.vue";
import PopularMovieView from "@/views/PopularMovieView.vue";
import ReleaseMovieView from "@/views/ReleaseMovieView.vue";
import MovieDetailView from "@/views/MovieDetailView.vue";
import ReviewCreateView from "@/views/ReviewCreateView.vue";
import ActorDetailView from "@/views/ActorDetailView.vue";
import DirectorDetailView from "@/views/DirectorDetailView.vue";
import ReviewDetailView from "@/views/ReviewDetailView.vue";
import ReviewUpdateView from "@/views/ReviewUpdateView.vue";

const scrollBehavior = (to, from, savedPosition) => {
  return (
    savedPosition || {
      top: to.meta?.scrollTop || 0,
      left: 0,
    }
  );
};
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "main",
      component: MainView,
    },
    {
      path: "/search/",
      name: "search",
      component: SearchView,
      props: (route) => ({
        title: route.query.title,
        genre: route.query.genre,
        keyword: route.query.keyword,
      }),
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
      path: "/changepassword",
      name: "changepassword",
      component: PasswordChangeView,
    },
    {
      path: "/profile/:username",
      name: "profile",
      component: ProfileView,
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
  ],
  scrollBehavior,
});
import { useUserStore } from "@/stores/user";
import { useMovieStore } from "@/stores/movie";

router.beforeEach((to, from) => {
  const store = useUserStore();
  const movie = useMovieStore();

  if ((to.name === "login" || to.name === "signup") && store.isLogin) {
    return { name: "main" };
  }
  if (
    (to.name === "settings" ||
      to.name === "followerlist" ||
      to.name === "CreateReview" ||
      to.name === "ReviewUpdateView" ||
      to.name === "profile" ||
      to.name === "ReviewDetailView" ||
      to.name === "MovieDetailView" ||
      to.name === "changepassword") &&
    store.isLogin === false
  ) {
    return { name: "login" };
  }
  if (to.name === "main") {
    movie.isMain = true;
  } else {
    movie.isMain = false;
  }
  if (to.name === "settings") {
    store.profile(to.params.username);
    console.log();
  }
});
router.beforeEach((to, from, next) => {
  // console.log("window.scrollY:", window.scrollY);
  from.meta?.scrollTop && (from.meta.scrollTop = window.scrollY);
  // console.log("from:\t", from.name, "\t", from.meta);
  // console.log("to:\t\t", to.name, "\t", to.meta);
  return next();
});
export default router;
