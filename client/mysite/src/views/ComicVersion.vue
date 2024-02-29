<template>
  <TopBar></TopBar>
  <v-container>
    {{ props.title }}
  </v-container>
</template>


<script setup>
import { defineProps } from 'vue';
import TopBar from '@/components/TopBar.vue';

const props = defineProps({
  id: Number,
  title: String
});
</script>