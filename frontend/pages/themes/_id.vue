<template>
  <div>
    <h1>{{themes}}</h1>
<!--    <QTest :questions="theme.questions"/>-->
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
            ...mapState({
              themes: state => state.themes
            })
        },
    }
</script>
