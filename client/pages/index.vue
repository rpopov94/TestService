<template>
  <div>
    <div class="container">
      <h1>Привет, это главная страница</h1>
      <div class="d-flex justify-content-start">
          <span v-for="post in posts" :key="post.id" class="blog">
                <nuxt-link :to="`/themes/${post.id}`" class="mr-1 badge badge-info">{{ post.name }}</nuxt-link>
          </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  middleware: ["auth"],
    async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/themes/`);
    // this.$router.push('/')
    return {
      posts: data.results,
    }
  }
}
</script>

<style>

</style>
