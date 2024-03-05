<template>
  <TopBar v-if="isParentRoute"></TopBar>
  <v-container  v-if="isParentRoute">
    <ComicTable :datas="comic_episodes" :headers="headers" :linkname="linkname">
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
const isParentRoute = computed(() => route.name === 'comicepisode');
const title_version_id = computed(() => route.params.id);

const comic_episodes = ref(null);

const headers = ref([
  {
    title: '',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: 100,
  },
  {
    title: "話数",
    value: "episode_number",
    sortable: true,
    width: 100,
  },
  {
    title: "",
    value: "review",
    width: 100,
  },
]);

const linkname =  'pdf';

const getComicEpisode = async () => {
  try {
    const response = await EventService.getComicEpisode(title_version_id.value);
    comic_episodes.value = response.data;
  } catch (error) {
    console.log("Error_home" + error);
  }
};

onMounted(() => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    getComicEpisode(token);
  }
});

</script>