<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="items"
      @click:row="clickRow"
    >
      <template #[`item.action`]="{ item }">
        <v-btn @click.stop="clickEdit(item)">編集</v-btn>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>

export default {
  name: 'DataTable',

  computed: {
    headers: () => [
      { text: 'id', value: 'id' },
      { text: 'name', value: 'name' },
      { text: 'point', value: 'point' },
      { text: 'action', value: 'action' }
    ],

    items: () => [
      { id: 1, name: 'AAA', point: 100 },
      { id: 2, name: 'BBB', point: 50 },
      { id: 3, name: 'CCC', point: 25 }
    ]
  },

  methods: {
    clickRow (row) {
      console.log('clickRow', row)
    },

    clickEdit (item) {
      console.log('clickEdit', item)
    }
  }
}
</script>

