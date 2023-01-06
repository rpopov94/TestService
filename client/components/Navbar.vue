<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
    <nuxt-link class="navbar-brand" to="/">
      TS
    </nuxt-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse"
            data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <span class="navbar-nav mr-auto"></span>
      <span class="navbar-text mr-2">{{user?.username}}</span>
      <nuxt-link class="btn btn-outline-light mr-2" to="/signout">Выход</nuxt-link>
      <nuxt-link class="btn btn-outline-light mr-2" to="/signin">Вход</nuxt-link>
      <nuxt-link class="btn btn-outline-light mr-2" to="/signup">Регистрация</nuxt-link>
    </div>
  </nav>
</template>

<script>
export default {
  computed: {
    loggedIn() {
      return this.$auth.loggedIn
    },
    user() {
      return this.$auth.user
    }
  }
}
</script>

<style scoped>

</style>
