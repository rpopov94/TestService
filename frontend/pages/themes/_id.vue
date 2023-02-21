<template>
  <div>
    <h1>{{theme.name}}</h1>
    <QTest :questions="theme.questions"/>
  </div>

</template>

<script>
    import { mapState, mapGetters } from 'vuex'
    import QTest from "~/components/QTest.vue";
    export default{
        middleware: ['auth'],
        components: [
          'QTest'
        ],
        computed: {
            validate({params}){
                return /^\d+$/.test(params.id)
            },
            ...mapState([
                'themes'
            ]),
            ...mapGetters([
                'getThemeById'
            ]),
            theme () {
                return this.getThemeById(this.$route.params.id)
            }
        },
        // async fetch({ store }) {
        //     await store.dispatch('fetchThemeById', id)
        // }
    }
</script>
