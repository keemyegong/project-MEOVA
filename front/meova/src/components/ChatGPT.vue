<template>
  <div>
    <h1>Movie Recommendations</h1>
    <p v-if="recommendations">{{ recommendations }}</p>
    <p v-else>Loading...</p>
  </div>
</template>

<script setup></script>
