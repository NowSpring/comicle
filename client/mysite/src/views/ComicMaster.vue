<template>
  <TopBar v-if="isParentRoute"></TopBar>
  <v-container  v-if="isParentRoute">
    <ComicTable :datas="comic_masters" :headers="headers" :linkname="linkname">
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
const isParentRoute = computed(() => route.name === 'comicmaster');

const comic_masters = ref(null);

const headers = ref([
  {
    title: '',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: 100,
  },
  {
    title: "タイトル",
    value: "title",
    sortable: true,
    width: 100,
  },
  {
    title: "作者",
    value: "author",
    sortable: true,
    width: 100,
  },
  {
    title: "年代",
    value: "era",
    sortable: true,
    width: 100,
  },
  {
    title: "出版社",
    value: "publisher",
    sortable: true,
    width: 100,
  },
  {
    title: "対象",
    value: "target",
    sortable: true,
    width: 100,
  },
  {
    title: "ジャンル",
    value: "genre",
    sortable: true,
    width: 100,
  },
]);

const linkname =  'comicversion';

const getComicMaster = async () => {
  try {
    const response = await EventService.getComicMaster();
    comic_masters.value = response.data;
    // console.log("comic_masters.value:", comic_masters.value);
  } catch (error) {
    console.log("Error_home" + error);
  }
};

onMounted(() => {
  const token = localStorage.getItem('token');
  if (token !== null) {
    getComicMaster(token);
  }
});

</script>
