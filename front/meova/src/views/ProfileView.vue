<template>
  <div>{{ store.profile_info }}</div>
</template>

<script setup>
import { useUserStore } from "@/stores/user";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const store = useUserStore();

onMounted(() => {
  store.profile(route.params.username);
});
</script>

<style scoped></style>
