export const state = () => ({
    themes: {},
})

export const mutations = {
    allThemes (state, themes){
        state.themes = themes
    }
}
export const actions = {
    async get_all_themes({commit}){
        const {data} = await this.$axios.get('api/themes/')
        commit('allThemes', data)
    },
}

export const getters = {
    getAllThemes(store) {
        return store.themes
    }
}