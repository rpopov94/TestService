<template>
    <ul>
        <li v-for="theme in all_themes" :key="theme.id">
            <nuxt-link :to="`themes/${theme.id}`" :id="`${theme.id}`" >{{ theme.name }}</nuxt-link>
        </li>
    </ul>
</template>

<script>

export default {
  async fetch({store}){
    await store.dispatch('themes/get_all_themes')
  },
  computed: {
      all_themes() {
          return this.$store.getters['themes/getAllThemes'].results
      },
    },
}
</script>

