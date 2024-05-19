<template>
  <div id="calendar-container">
    <h1>{{ nowM + 1 }}월</h1>
    <p v-for="movie in movies">
      {{ Date(movie.created_at) }}
    </p>
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
            :class="{ today: isToday(day.date) }"
          >
            <img src="" alt="" />
            {{ day }}
            {{ day.display }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";

export default {
  name: "CalendarComponent",
  setup() {
    const calendarRows = ref([]);
    const nowM = ref(new Date().getMonth());
    const store = useUserStore();
    const movies = ref([]);
    const fetchMovieReviews = async (userid) => {
      axios({
        method: "get",
        url: `http://127.0.0.1:8000/api/v1/${userid}/reviews/`,
        headers: { Authorization: `Token ${store.token}` },
      }).then((res) => {
        console.log(res);
        movies.value = res.data;
      });
    };

    const printCalendar = (y, m) => {
      const date = new Date();
      const nowY = date.getFullYear();
      const nowM = date.getMonth();
      const nowD = date.getDate();

      y = y !== undefined ? y : nowY;
      m = m !== undefined ? m - 1 : nowM;

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
        for (let k = 1; k <= 7; k++) {
          if ((i === 0 && k < theDay) || dNum > lastDate) {
            week.push({ date: null, display: " " });
          } else {
            const poster = ref([]);
            console.log(movies.value);
            for (const movie of movies.value) {
              if (
                Date(movie.created_at).getFullYear() === y &&
                Date(movie.created_at).getMonth() === m &&
                Date(movie.created_at).getDate() === dNum
              ) {
                poster.value.push(
                  `http://image.tmdb.org/t/p/w500${movie.movie.poster_path}`
                );
              }
            }
            week.push({
              date: new Date(y, m, dNum),
              display: dNum,
              poster: poster.value,
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
      printCalendar();
      fetchMovieReviews(1); // 예시로 userid 1을 사용
    });

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
}

th {
  background-color: #f4f4f4;
}

.today {
  background-color: #ffeb3b;
  font-weight: bold;
}

td {
  height: 100px;
  vertical-align: top;
}

h1 {
  margin-bottom: 20px;
}
</style>
