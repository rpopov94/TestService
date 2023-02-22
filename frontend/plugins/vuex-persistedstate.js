// plugins/vuex-persistedstate.js
import createPersistedState from 'vuex-persistedstate'

export default ({ store }) => {
  createPersistedState()(store)
}
