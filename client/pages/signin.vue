<template>
  <div>
    <div class="container">
      <div class="text-center">
        <form class="form-signin" @submit.prevent="userLogin">
          <h1 class="h3 mb-3 mt-3 font-weight-normal">Пожалуйста укажите логин и пароль</h1>
          <label for="inputUsername" class="sr-only">Имя пользователя</label>
          <input id="inputUsername" class="form-control" placeholder="Имя пользователя" required="" v-model="login.username">
          <label for="inputPassword" class="sr-only">Пароль</label>
          <input type="password" id="inputPassword" class="form-control mt-2" placeholder="Пароль" required="" v-model="login.password">
          <button class="btn mt-2 btn-lg btn-primary btn-block" type="submit">Войти</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  layout: "post_detail",
  data() {
    return {
      login: {
        username: 'admin',
        password: 'password'
      },
    }
  },
  methods: {
    async userLogin() {
        let response = await this.$auth.loginWith('local', { data: this.login })
        this.$router.push('/')
    }
  }
}
</script>

<style scoped>

.text-center{
  display: flex;
  justify-content: center;
  align-items: center;
}
.btn-primary{
  color: #fff;
  background-color: #7b688e;
  border-color: #2b2a2a;
}

</style>
