<template>
  <v-card class="mx-auto" max-width="1000" tile>
    <v-img height="200" src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg"></v-img>
    <v-row style="margin:2.5%;position:absolute; top: 130px">
      <v-list-item>
       <v-list-item-avatar size="100">
          <img
            src="https://www.w3schools.com/howto/img_avatar.png"
            alt="John"
          >
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title" style="margin-top:20px;">{{ $auth.user.first_name}} {{$auth.user.last_name}}</v-list-item-title>
          <v-list-item-subtitle>{{$auth.user.bio}}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-row>
  </v-card>
</template>

<script>

</script>
