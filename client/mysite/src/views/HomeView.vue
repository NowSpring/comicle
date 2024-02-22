<template>
  <HelloWorld />
  <a-button type="primary mx-4" @click.prevent="logOut">ログアウト</a-button>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import router from '@/router';
import EventService from "@/plugins/EventService.js";
// import TicketTable from "@/components/TicketTable.vue";
// import CreateModal from "@/components/CreateModal.vue";
import HelloWorld from "../components/HelloWorld.vue";


// const getTicketList = () => {
//   EventService.getTickets()
//     .then((response) => {
//       tickets.value = response.data;
//     })
//     .catch((error) => {
//       console.log("Error_home" + error);
//     });
// };

// onMounted(() => {
//   const token = localStorage.getItem('token');
//   if (token !== null) {
//     getTicketList(token);
//   }
// });

const logOut = () => {
  window.localStorage.removeItem('token');
  window.localStorage.removeItem('user_id');
  window.localStorage.removeItem('user_name');
  router.push({ name: 'login' });
};
</script>
