<template>
  <h1>コミック一覧</h1>
  <v-data-table
    v-if="headers && data"
    :headers="headers"
    :items="data"
    :items-per-page="5"
    class="elevation-1 my-3 mx-auto"
    style="width:1000px;"
  >
    <template v-slot:item.cover="{ item }" >
      <v-img 
        :src="item.cover" 
        :aspect-ratio="16/9" 
        height="9vw" 
        min-height="100px"
        width="16vw" 
        min-width="160px" 
        class="ma-0 pa-0"
      ></v-img>
    </template>
  </v-data-table>
</template>

<script setup>
import { defineProps } from 'vue';

// propsを定義する
const { data, headers } = defineProps({
  data: Array,
  headers: Array,
});
</script>


