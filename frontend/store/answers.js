export const state = () => ({
  answers: []
})
export const mutations = {
  resetdata(state){
    state.answers = []
  },
  setData(state, answers) {
    state.answers = answers

  }
}
export const actions = {
  async fetchAnswers({commit}, id){
    commit('resetdata')
    try{
      const {questions} = await this.$axios.$get(`api/answers/${id}/`)
      const data = questions.map(question => question.answer)
      commit('setData', data)
    }catch (error){
      // commit('setData', error)
    }

  }
}
export const getters = {
  getAnswers(store){
    return store.answers
  }
}
