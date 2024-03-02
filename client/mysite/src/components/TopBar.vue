<template>
  <v-app-bar
    app
    clippedLeft
    :height="60"
    color="primary"
  >

    <v-btn
      icon
      :to="{ name: 'comicmaster' }"
    >
      <v-icon x-large>
        mdi-book-open-variant
      </v-icon>
    </v-btn>

    <v-spacer></v-spacer>

    <v-btn
      text
      :to="{ name: 'comicmaster' }" 
    >
      <span>{{ user_name }}</span>
      <v-icon>mdi-account</v-icon>
    </v-btn>

    <v-btn
      text
      @click="logOut"
    >
      <span class="mr-2">
        Logout
      </span>
      <v-icon>
        mdi-open-in-new
      </v-icon>
    </v-btn>

  </v-app-bar>
  
</template>

<script setup>
import { ref, onMounted } from 'vue';
import router from '@/router';

const user_name = ref('');

onMounted(() => {
  user_name.value = window.localStorage.getItem("user_name");
}) 

const logOut = () => {
  window.localStorage.removeItem('token');
  window.localStorage.removeItem('user_id');
  window.localStorage.removeItem('user_name');
  router.push({ name: 'login' });
};
</script>
