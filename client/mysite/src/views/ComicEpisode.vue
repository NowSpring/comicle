<template>
  <TopBar></TopBar>
  <v-container>
    {{ id }}
  </v-container>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import TopBar from '@/components/TopBar.vue';

const route = useRoute();

const id = computed(() => route.params.id);

</script>
