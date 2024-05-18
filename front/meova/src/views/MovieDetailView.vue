<template>
    <div>
        <h3>{{ movie.title }}</h3>
        <img :src="'https://image.tmdb.org/t/p/original/' + movie.poster_path" alt="movie-poster" class="movie-image">
        <p>{{ movie.overview }}</p>
        <b>러닝타임</b>
        <p>{{ movie.runtime }}분</p>
        <b>국가</b>
        <p>{{ movie.origin_country }}</p>
        <b>개봉일</b>
        <p>{{ movie.release_date }}</p>
        <b>장르</b>
        <div v-for="genre in movie.genres">
            <p>{{ genre.name }}</p>
        </div>
        <b>키워드</b>
        <div v-for="keyword in movie.keywords">
            <p>{{ keyword.name }}</p>
        </div>
        <RouterLink :to="{ name: 'TagCommentDetailView', params: { id: movie.id } }">
            <b>태그 코멘트</b>
        </RouterLink>
        <template v-if="movie.tagcomment_set">
            <div v-for="tagcomment in movie.tagcomment_set" :key="tagcomment.id">
                {{ tagcomment.content }}
                <span v-if="tagcomment.nickname">
                    | {{ tagcomment.nickname }}
                </span>
                <span v-else>
                    | {{ tagcomment.username }}
                </span>
            </div>
        </template>
        <template v-else>
            <p>아직 태그코멘트가 없어요!</p>
        </template>

        <form>
            <input type="text">
            <input type="submit">
        </form>

        <template v-if="watchprovider in movie.watchproviders">
            <b>Provider</b>
            <div v-for="watchprovider in movie.watchproviders">
                {{ watchprovider }}
            </div>
        </template>
        <hr>
        <b>감독</b>
        <div v-for="director in movie.directors">
            <RouterLink :to="{ name: 'DirectorDetailView', params: { id: director.id } }">
                <p>{{ director.name }}</p>
            </RouterLink>
        </div>
        <hr>
        <b>출연진</b>
        <div v-for="credit in movie.credits">
            <RouterLink :to="{ name: 'ActorDetailView', params: { id: credit.actor.id } }">
                <img :src="'https://image.tmdb.org/t/p/original/' + credit.actor.profile_path" alt="actor-profile" class="profile-image">
                <p>캐릭터 | {{ credit.character }}</p>
                <p>배우 | {{ credit.actor.name }}</p>
            </RouterLink>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute, RouterLink } from 'vue-router'

const store = useMovieStore()
const route = useRoute()
const movie = ref(null)
const movieId = Number(route.params['id'])

    console.log(store.API_URL)
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/movies/${movieId}/`
    })
    .then((response) => {
        console.log(store.API_URL)
        console.log(response)
        movie.value = response.data
    })
    .catch((error) => {
        console.log(error)
    })
</script>

<style scoped>
.movie-image {
  width: 200px;
}
.profile-image {
  width: 200px;
}
</style>