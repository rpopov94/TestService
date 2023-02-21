<template>
  <v-app dark>
    <v-app-bar color="blue" :clipped-left="clipped" fixed app>    
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <div class="authentication-buttons">
        <div v-if="$auth.loggedIn">
          {{ $auth.user.email }}
          <v-btn icon to="/logout" class="logout-btn">
            <v-icon light @click="$auth.logout()">mdi-logout</v-icon>
          </v-btn>
        </div>
        <div v-else>
          <v-btn icon to="/login" class="login-btn">
            <v-icon>mdi-login</v-icon>
          </v-btn>
          <v-btn icon to="/register" class="register-btn">
            <v-icon>mdi-account-key-outline</v-icon>
          </v-btn>
        </div>
      </div>
    </v-app-bar>
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <v-footer :absolute="!fixed" app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: 'TestService',
    }
  },
}
</script>
