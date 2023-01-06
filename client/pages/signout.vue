<template>
  <div class="container message">
    <div class="text">
      Вы вышли из системы, здесь Вы можете снова
      <nuxt-link to="/signin"><i>войти</i></nuxt-link>
    </div>

  </div>
</template>

<script>
export default {
  async created() {
    await this.$auth.logout()
  }
}
</script>
<style>
  .message {
    display: flex;
    height: 100%;
  }
  .text{
    align-self: center;
  }
</style>
