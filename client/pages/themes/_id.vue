<template>
    <div class="container">
      <h1>{{data.name}}</h1>
      <QTest :questions="data.questions"/>
    </div>
</template>

<script>
import axios from "axios";
import QTest from "@/src/components/QTest";

export default {
  name: "id",
  components: {QTest},
  middleware: ["auth"],
  async asyncData({params}) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/themes/${params.id}/`);
    return {
      data
    }
  },
}
</script>

<style scoped>

</style>
