
<template>
  <div v-if="review">
    <h1>{{ review.title }}</h1>
    <h2>평점 {{ review.vote }}</h2>
    <span v-if="review.nickname">
      작성자 | {{ review.nickname }}
    </span>
    <span v-else>
      작성자 | {{ review.username }}
    </span>
    <p>{{ review.content }}</p>
    <button @click="deleteReview(review.id)">삭제</button>

    <hr>

    <form @submit.prevent="createComment" ref="form">
      <input
        type="text"
        placeholder="댓글을 남겨 주세요!"
        id="content"
        v-model="content"
      />
      <input type="submit" value="입력" />
    </form>

    <div v-for="comment in review.reviewcomment_set">
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
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'
import { useReviewStore } from '@/stores/review'
import { useRoute, useRouter, RouterLink } from 'vue-router'

const userStore = useUserStore()
const movieStore = useMovieStore()
const reviewStore = useReviewStore()

const route = useRoute()
const router = useRouter()
const movieId = Number(route.params['movieId'])
const reviewId = Number(route.params['reviewId'])
const form = ref(null)
const movie = ref(null)
const review = ref(null)
const content = ref(null)

const fetchReview = function () {
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
}

onMounted(fetchReview)

const createComment = function () {
  const review = {
    content: content.value,
    id: reviewId,
  }
  reviewStore.createComment(review)
  form.value.reset()
  content.value = ""
  fetchReview()
  }

const deleteReview = (reviewId) => {
  axios({
  method: 'delete',
  url: `${movieStore.API_URL}/api/v1/reviews/${reviewId}/`,
  headers: {
      'Authorization': `Token ${userStore.token}`
  }
})
  .then(() => {
    router.push({
      name: 'MovieDetailView', params: {id : movieId}
    })
  })
  .catch((error) => {
      console.log(error)
  })
}
</script>

<style scoped>
</style>