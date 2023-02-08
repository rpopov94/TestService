<template>
    <div class="container">
      <h1>{{data.name}}</h1>
      <QTest :questions="data.questions"/>
    </div>
</template>

<script>
// import axios from "axios";
import QTest from "@/src/components/QTest";

export default {
  name: "id",
  components: {QTest},
  middleware: ["auth"],
  async asyncData({ $axios }) {
  const data = await $axios.$get(`/themes/${params.id}/`)
  return { data }
}
}
</script>

<style scoped>

</style>
