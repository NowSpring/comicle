<template>
  <h1>コミック一覧</h1>

  <v-data-table
    v-if="headers && datas"
    :headers="headers"
    :items="datas"
    :items-per-page="5"
    class="elevation-1 my-3 mx-auto"
    style="width:1000px;"
  >

    <template v-slot:item="{ item }">
      <tr
        :key="item.key"
        @click="clickRow(item)"
      >
        <td
          v-for="header in headers"
          :key="header.value"
        >
          <v-img 
            v-if="header.value === 'cover'"
            :src="item.cover" 
            :aspect-ratio="16/9" 
            height="9vw" 
            min-height="100px"
            width="16vw" 
            min-width="160px" 
            class="ma-0 pa-0"
          ></v-img>
          <span v-if="header.value === 'title'">
            {{ item.title }}
          </span>
          <span v-if="header.value === 'author'">
            {{ item.author }}
          </span>
          <span v-if="header.value === 'era'">
            {{ item.era }}
          </span>
          <span v-if="header.value === 'publisher'">
            {{ item.publisher }}
          </span>
          <span v-if="header.value === 'target'">
            {{ item.target }}
          </span>
          <span v-if="header.value === 'genre'">
            {{ item.genre }}
          </span>
          <span v-if="header.value === 'version_number'">
            {{ item.version_number }}
          </span>
          <span v-if="header.value === 'episode_number'">
            {{ item.episode_number }}
          </span>
        </td>
      </tr>
    </template>

  </v-data-table>
</template>

<script setup>

import { useRouter } from 'vue-router';
import { defineProps, toRefs, onMounted } from 'vue';

const router = useRouter();

const props = defineProps({
  datas: Array,
  headers: Array,
  linkname: String,
});

const { datas, headers, linkname } = toRefs(props);

const clickRow = (item) => {
  router.push({ name: linkname.value, params: { id: item.id }});
};

onMounted(() => {
  // console.log(headers.value); // headersの中身をコンソールに出力
});
</script>


