export const state = () => ({
    themes: {}
  })

export const mutations = {
  setThemes(state, themes) {
    state.themes = themes
  },
  setTheme(state, theme) {
    state.themes.push(theme)
  }
}

export const actions = {
    async fetchAllThemes({ commit }) {
        try {
            const { data } = await this.$axios.get('api/themes/')
            commit('setThemes', data.results)
        } catch (error) {
            // console.error(error)
        }
    },
    async fetchThemeById({ commit }, id) {
        try {
            const { data } = await this.$axios.get(`api/themes/${id}/`)
            commit('setTheme', data)
        } catch (error) {
            // console.error(error)
        }
    }
}

export const getters = {
    getAllThemes: (state) => {
        return state.themes
    },
    getThemeById: (state) => (id) => {
        for(let i = 0; state.themes.length; i++){
            if (state.themes[i].id == id){
                return state.themes[i]
            }
        }
        return undefined
    }
}
