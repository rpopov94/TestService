<template>
  <h1>{{test.name}}</h1>
</template>

<script>
import axios from "axios";
export default {
  name: "_id",
  middleware: ["auth"],
  async asyncData({params}) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/themes/${params.id}/`);
    return {
      test: data,
    }
  }
}
</script>

<style scoped>



</style>
