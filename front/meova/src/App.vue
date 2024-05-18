<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <RouterLink :to="{ name: 'main' }" class="navbar-brand">Main</RouterLink>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-if="store.isLogin">
          <li class="nav-item">
            <div class="nav-link" @click="store.logout">logout</div>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'settings' }" class="nav-link"
              >Settings</RouterLink
            >
          </li>
          <li v-if="store.userinfo" class="nav-item">
            <RouterLink
              :to="{
                name: 'profile',
                params: { username: store.userinfo.username },
              }"
              class="nav-link"
              >My profile</RouterLink
            >
          </li>
        </ul>
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0" v-else>
          <li class="nav-item">
            <RouterLink :to="{ name: 'login' }" class="nav-link"
              >Login</RouterLink
            >
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'signup' }" class="nav-link"
              >Signup</RouterLink
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useUserStore } from "./stores/user";
const store = useUserStore();
</script>

<style scoped></style>
