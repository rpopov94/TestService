<template>
    <ul>
        <li v-for="theme in all_themes" :key="theme.id">
            <nuxt-link :to="`themes/${theme.id}`" >{{ theme.name }}</nuxt-link>
        </li>
    </ul>
</template>

<script>

export default {
    async fetch({store}){
        await store.dispatch('fetchAllThemes')
    },
    computed: {
        all_themes() {
            return this.$store.getters.getAllThemes
        },
    },
}
</script>

