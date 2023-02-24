export const state = () => ({
  themes: {},
  theme: {}
})

export const mutations = {
  clearListThemes(state) {
    state.themes = []
  },
  setThemes(state, themes) {
    state.themes = themes
  },
  setTheme(state, theme) {
    state.theme = theme
  }
}

export const actions = {
  async fetchAllThemes({ commit }) {
    commit('clearListThemes')
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
  getThemeById: (state) => {
    return state.theme
  }
}
