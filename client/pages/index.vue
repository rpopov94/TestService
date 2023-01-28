<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col><h1>Тесты по темам</h1></b-col>
        <b-col v-show="$auth.loggedIn"><b-button class="modifybtn" to="#">Добавить тему</b-button></b-col>
      </b-row>
    </b-container>
    <div class="container">

      <div class="d-flex justify-content-start">
          <span v-for="post in posts" :key="post.id" class="blog">
            <ThemeCard :link="post.id" :name="post.name"/>
          </span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ThemeCard from "@/src/components/ThemeCard";

export default {
  components: {ThemeCard},
  // middleware: ["auth"],
  async asyncData(ctx) {
    const { data } = await axios.get(`http://127.0.0.1:8000/api/themes/`);
    return {
      posts: data.results,
    }
  }
}
</script>

<style>
.modifybtn{
  display: block;
  float: right;
  margin-top: 0.5em;
}
.bg-new {
  background-color: #fcfafa !important;
  color: black !important;
}

</style>
