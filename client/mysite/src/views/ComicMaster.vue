<template>
  <TopBar></TopBar>
  <v-container>
    <ComicTable :data="comic_masters" :headers="headers">
      <template #[`item.title`]="{ item }">
        <router-link :to="{ name: 'comicversion', params: { id: item.id, title: item.title }}">
          {{ item.title }}
        </router-link>
      </template>
    </ComicTable>
  </v-container>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import EventService from "@/plugins/EventService.js";
import TopBar from '@/components/TopBar.vue';
import ComicTable from "@/components/ComicTable.vue";

const comic_masters = ref(null);

const headers = ref([
  {
    text: 'サムネイル予定',
    align: 'start',
    sortable: false,
    value: 'cover',
    width: 100,
  },
  {
    text: "タイトル",
    value: "title",
    width: 100,
  },
  {
    text: "作者",
    value: "author",
    width: 100,
  },
  {
    text: "年代",
    value: "era",
    width: 100,
  },
  {
    text: "出版社",
    value: "publisher",
    width: 100,
  },
  {
    text: "対象",
    value: "target",
    width: 100,
  },
  {
    text: "ジャンル",
    value: "genre",
    width: 100,
  },
]);

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
