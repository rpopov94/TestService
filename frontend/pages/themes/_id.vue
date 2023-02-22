<template>
  <v-container>
    <v-card-title>{{theme.name}}</v-card-title>
    <QTest :questions="theme.questions"/>
  </v-container>
</template>

<script>
import {mapState} from 'vuex'
import QTest from "~/components/QTest.vue";

export default {
  middleware: ['auth'],
  components: [
    QTest
  ],
  created(){
    this.$store.dispatch('fetchThemeById', this.$route.params.id)
  },
  computed: {
    validate({params}) {
      return /^\d+$/.test(params.id)
    },
    ...mapState(['theme'])
  }
}
</script>
