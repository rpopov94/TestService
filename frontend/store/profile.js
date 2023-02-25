export const state = () => ({
  user: {}
})

export const mutations = {
  resetdata(state) {
    state.user = {}
  },
  setData(state, user) {
    state.user = user
  },
}

export const actions = {
  async fetchUser({commit}, id){
    commit('resetdata')
    try{
      const {data} = await this.$axios.$get(`accounts/users/${id}/`)
      commit('setData', data)
    }catch (error){
      // commit('setData', error)
    }
  }
}

export const getters = {
  getUser:(state) => {
    return state.profile
  }
}
