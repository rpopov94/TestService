<template>
  <v-container class="bg-surface-variant">
    <v-row no-gutters v-for="theme in all_themes" :key="theme.id">
      <v-col>
        <template>
          <v-card
            class="mx-auto"
            max-width="400"
          >
            <v-img
              class="align-end text-white"
              height="200"
              :src="require(`@/assets/images/${theme.descriptor}.jpg`)"
              cover
            >
            </v-img>

            <v-card-subtitle class="pt-1">
              {{theme.name}}
            </v-card-subtitle>

            <v-card-actions>
              <v-btn color="orange">
                <nuxt-link :to="`themes/${theme.id}`" > Перейти </nuxt-link>
              </v-btn>
            </v-card-actions>
          </v-card>
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import {mapState} from "vuex";
export default {
  async fetch({store}){
    await store.dispatch('themes/fetchAllThemes')
  },
  computed: {
    all_themes() {
      return this.$store.getters['themes/getAllThemes']
    },
  },
}
</script>

