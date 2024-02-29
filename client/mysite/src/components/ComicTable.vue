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
    <template #[`item.cover`]="{ item }" >
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
import { defineProps, toRefs } from 'vue';

const props = defineProps({
  data: Array,
  headers: Array,
});

const { data, headers } = toRefs(props);
</script>


