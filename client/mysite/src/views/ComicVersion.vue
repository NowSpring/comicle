<template>
  <TopBar v-if="isParentRoute"></TopBar>
  <v-container  v-if="isParentRoute">
    <ComicTable :datas="comic_versions" :headers="headers" :linkname="linkname">
    </ComicTable>
  </v-container>
  <router-view></router-view>
</template>


<script setup>
import { useRoute } from 'vue-router';
import { ref, computed, onMounted } from 'vue';
import EventService from "@/plugins/EventService.js";
import TopBar from '@/components/TopBar.vue';
import ComicTable from "@/components/ComicTable.vue";

const route = useRoute();
const isParentRoute = computed(() => route.name === 'comicversion');
const title_id = computed(() => route.params.id);

const comic_versions = ref(null);

const headers = ref([
  {
    title: '',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: 100,
  },
  {
    title: "巻数",
    value: "version_number",
    sortable: true,
    width: 100,
  },
]);

const linkname =  'comicepisode';

const getComicVersion = async () => {
  try {
    const response = await EventService.getComicVersion(title_id.value);
    comic_versions.value = response.data;
  } catch (error) {
    console.log("Error_home" + error);
  }
};

onMounted(() => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    getComicVersion(token);
  }
});

</script>