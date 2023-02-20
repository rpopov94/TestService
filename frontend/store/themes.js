export const state = () => ({
    themes: {},
})

export const mutations = {
    allThemes (state, themes){
        state.themes = themes
    },
    themebyid (state, theme) {
        state.themes.push_back(theme)
    }
}
export const actions = {
    async get_all_themes({commit}){
        const {data} = await this.$axios.get('api/themes/')
        commit('allThemes', data)
    },
    async get_theme_by_id({commit}, id){
        const {data} = await this.$axios.get(`api/themes/${id}/`)
        commit('themebyid', data)
    },
}

export const getters = {
    getAllThemes(store) {
        return store.themes
    },
    getThemeById: (store)  => (id) => {
        return store.themes.find(theme => theme.id === id)
    }
}