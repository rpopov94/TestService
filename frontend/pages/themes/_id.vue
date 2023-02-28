<template>
  <v-container>
    <v-card-title>{{theme.name}}</v-card-title>
    <QTest :questions="theme.questions" :id="Number(this.$route.params.id)"/>
  </v-container>
</template>

<script>
import QTest from "~/components/QTest.vue";

export default {
  middleware: ['auth'],
  created(){
    this.$store.dispatch('themes/fetchThemeById', this.$route.params.id)
  },
  computed: {
    validate({params}) {
      return /^\d+$/.test(params.id)
    },
    theme() {
      return this.$store.getters['themes/getThemeById']
    },
  }
}
</script>
