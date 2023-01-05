<template>
  <div>
    <div class="container">
      <h1>Привет, это главная страница</h1>
      <div v-for="post in posts" :key="post.slug" class="blog">
        <div class="blog-title">{{ post.name}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/v1/themes/`);
    return {
      posts: data.results,
    }
  }
}
</script>

<style>

</style>
