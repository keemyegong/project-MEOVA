<template>
    <div class="container">
      <FullCalendar :events="events" :eventContent="renderEventContent" />
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import FullCalendar from '@fullcalendar/vue3';
  import dayGridPlugin from '@fullcalendar/daygrid';
  import axios from 'axios';
  
  export default {
    components: {
      FullCalendar,
    },
    setup() {
      const events = ref([]);
  
      const fetchMovieReviews = async () => {
        try {
          // 여기에 실제 API 엔드포인트를 사용하십시오
          const response = await axios.get('/api/movie-reviews');
          events.value = response.data.map(review => ({
            title: review.movieTitle,
            start: review.date,
            extendedProps: {
              posterUrl: review.posterUrl,
            }
          }));
        } catch (error) {
          console.error('Error fetching movie reviews:', error);
        }
      };
  
      const renderEventContent = (eventInfo) => {
        return {
          html: `<div class="event-content">
                   <img src="${eventInfo.event.extendedProps.posterUrl}" alt="${eventInfo.event.title}" class="img-thumbnail" />
                   <p>${eventInfo.event.title}</p>
                 </div>`
        };
      };
  
      onMounted(fetchMovieReviews);
  
      return { events, renderEventContent };
    },
  };
  </script>
  
  <style>
  .event-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }
  
  .event-content img {
    width: 100px;
    height: auto;
    margin-bottom: 5px;
  }
  </style>