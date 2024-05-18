import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";
import { useUserStore } from "./user";

export const useReviewStore = defineStore("review", () => {
  const user = useUserStore();
  const router = useRouter();
  const BASE_URL = "http://127.0.0.1:8000/api/v1/movies";

  return {};
});
