
<template>
  <div>
    <h1>{{ review.title }}</h1>
    <h2>평점 {{ review.vote }}</h2>
    <span v-if="review.nickname">
      작성자 | {{ review.nickname }}
    </span>
    <span v-else>
      작성자 | {{ review.username }}
    </span>
    <p>{{ review.content }}</p>

    <hr>

    <div v-for="comment in review.comments">
      <span>{{ comment.content }}</span>
      <span v-if="comment.nickname">
      | {{ comment.nickname }}
      </span>
      <span v-else>
      | {{ comment.username }}
    </span>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'
import { useReviewStore } from '@/stores/review'
import { useRoute, RouterLink } from 'vue-router'

const userStore = useUserStore()
const movieStore = useMovieStore()
const reviewStore = useReviewStore()

const route = useRoute()
const movieId = Number(route.params['movieId'])
const reviewId = Number(route.params['reviewId'])

const movie = ref(null)
const review = ref(null)

axios({
  method: 'get',
  url: `${movieStore.API_URL}/api/v1/reviews/${reviewId}/`,
    headers: {
      'Authorization': `Token ${userStore.token}`
  }
})
.then((response) => {
  console.log(response.data)
  review.value = response.data
})
.catch((error) => {
  console.log(error)
})

// const deleteReview = (reviewId) => {
//   axios({
//   method: 'delete',
//   url: `${movieStore.API_URL}/api/v1/movies/${movieId}/reviews/${reviewId}/`,
//   headers: {
//       'Authorization': `Token ${userStore.token}`
//   }
// })
//   .then(() => {
//   })
//   .catch((error) => {
//       console.log(error)
//   })
// }
</script>

<style scoped>
</style>