<template>
  <div id="calendar-container" class="nato-font">
    <h1>{{ nowM + 1 }}월</h1>
    <table>
      <thead>
        <tr>
          <th scope="col">MON</th>
          <th scope="col">TUE</th>
          <th scope="col">WED</th>
          <th scope="col">THU</th>
          <th scope="col">FRI</th>
          <th scope="col">SAT</th>
          <th scope="col">SUN</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(week, index) in calendarRows" :key="index">
          <td
            v-for="day in week"
            :key="day.date"
            :class="{ today: isToday(day.date), 'has-poster': day.poster.length === 1}"
            class="calendar-cell"
          >
            <img
              class="posterimg"
              v-for="poster in day.poster"
              :key="poster"
              :src="poster"
              alt="poster"
            />
            {{ day.display }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, watch, onMounted } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import { useReviewStore } from "@/stores/review";
import { useRoute } from "vue-router";

export default {
  name: "CalendarComponent",
  setup() {
    const calendarRows = ref([]);
    const nowM = ref(new Date().getMonth());
    const store = useUserStore();
    const reviewStore = useReviewStore();
    const movies = ref([]);
    const route = useRoute();
    const fetchMovieReviews = async (userid) => {
      try {
        const res = await axios.get(
          `http://127.0.0.1:8000/api/v1/${userid}/reviews/`,
          {
            headers: { Authorization: `Token ${store.token}` },
          }
        );
        movies.value = res.data;
        console.log(movies);
        printCalendar(); // 데이터가 로드된 후에 캘린더를 출력합니다.
      } catch (error) {
        console.error("Error fetching movie reviews:", error);
      }
    };

    const printCalendar = (y, m) => {
      const date = new Date();
      const nowY = date.getFullYear();
      const nowM = date.getMonth();
      const nowD = date.getDate();

      y = y !== undefined ? y : nowY;
      m = m !== undefined ? m : nowM;

      const theDate = new Date(y, m, 1);
      const theDay = theDate.getDay();

      const last = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

      if ((y % 4 === 0 && y % 100 !== 0) || y % 400 === 0) last[1] = 29;

      const lastDate = last[m];
      const row = Math.ceil((theDay + lastDate) / 7);

      const calendar = [];
      let dNum = 1;

      for (let i = 0; i < row; i++) {
        const week = [];
        for (let k = 0; k < 7; k++) {
          if ((i === 0 && k < theDay) || dNum > lastDate) {
            week.push({ date: null, display: " ", poster: [] });
          } else {
            const posters = [];
            for (const movie of movies.value) {
              const movieDate = new Date(movie.created_at);
              if (
                movieDate.getFullYear() === y &&
                movieDate.getMonth() === m &&
                movieDate.getDate() === dNum &&
                posters.length === 0
              ) {
                posters.push(
                  `http://image.tmdb.org/t/p/w500${movie.movie.poster_path}`
                )
                ;
              }
            }
            week.push({
              date: new Date(y, m, dNum),
              display: dNum,
              poster: posters,
            });
            dNum++;
          }
        }
        calendar.push(week);
      }
      calendarRows.value = calendar;
    };

    const isToday = (date) => {
      if (!date) return false;
      const today = new Date();
      return (
        date.getFullYear() === today.getFullYear() &&
        date.getMonth() === today.getMonth() &&
        date.getDate() === today.getDate()
      );
    };

    onMounted(() => {
      console.log(store.profile_info.pk);
      fetchMovieReviews(store.profile_info.pk); // 예시로 userid 1을 사용
    });
    watch(
      () => store.profile_info.pk,
      (pk) => {
        fetchMovieReviews(pk); // 사용자 ID가 변경될 때마다 데이터를 다시 가져옵니다.
      }
    );
    return {
      calendarRows,
      isToday,
      nowM,
      movies,
    };
  },
};
</script>

<style scoped>
.calendar-cell {
  position: relative; /* Establish a positioning context */
  width: 100px; /* Adjust width and height as needed */
  height: 140px;
}

#calendar-container {
  width: 100%;
  margin: 30px auto;
  max-width: 800px;
  text-align: center;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  width: 14.28%;
  padding: 10px;
  text-align: center;
  border: 1px solid #ddd;
  font-weight: 150;
}

th {
  color: whitesmoke;
  background-color: rgb(108, 108, 108);
}

.today {
  background-color: rgba(211, 211, 211, 0.313);
  font-weight: bold;
}

td {
  height: 100px;
  vertical-align: top;
}

h1 {
  margin-bottom: 20px;
}
.posterimg {
  position: absolute;
  height: 100%;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  opacity: 0.8;
  object-fit: cover;
}
.has-poster {
  color: white;
  font-weight: 700;
}
.nato-font {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}

</style>
