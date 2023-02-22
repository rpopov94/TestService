<template>
  <div>
    <h1>{{theme.name}}</h1>
    <QTest :questions="theme.questions"/>
  </div>

</template>

<script>
import {mapState, mapActions} from 'vuex'
import QTest from "~/components/QTest.vue";

export default {
  middleware: ['auth'],
  components: [
    'QTest'
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
