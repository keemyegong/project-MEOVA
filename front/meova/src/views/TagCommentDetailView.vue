
<template>
    <div>
        <b>태그 코멘트</b>
        <template v-if="movie && movie.tagcomment_set">
            <div v-for="tagcomment in movie.tagcomment_set" :key="tagcomment.id">
                {{ tagcomment.content }}
                <span v-if="tagcomment.nickname">
                    | {{ tagcomment.nickname }}
                </span>
                <span v-else>
                    | {{ tagcomment.username }}
                </span>
                <button @click="deleteComment(tagcomment.id)">삭제</button>
            </div>
        </template>
        <template v-else>
            <p>아직 태그코멘트가 없어요!</p>
        </template>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useMovieStore } from '@/stores/movie'
import { useRoute, RouterLink } from 'vue-router'

const userStore = useUserStore()
const movieStore = useMovieStore()

const route = useRoute()
const movieId = Number(route.params['id'])
const movie = ref(null)

axios({
    method: 'get',
    url: `${movieStore.API_URL}/api/v1/movies/${movieId}/`
})
.then((response) => {
    movie.value = response.data
})
.catch((error) => {
    console.log(error)
})

const deleteComment = (tagcommentId) => {
    axios({
    method: 'delete',
    url: `${movieStore.API_URL}/api/v1/tag-comments/${tagcommentId}/`,
    headers: {
        'Authorization': `Token ${userStore.token}`
    }
})
    .then(() => {
        movie.value.tagcomment_set = movie.value.tagcomment_set.filter(tagcomment => tagcomment.id !== tagcommentId)
    })
    .catch((error) => {
        console.log(error)
    })
}
</script>

<style scoped>
</style>