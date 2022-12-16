import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: '',
    user: {
      id: 0,
      email: ''
    },
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user.email = localStorage.getItem('email')
        state.user.id = localStorage.getItem('id')
        state.user.role = localStorage.getItem('role')
        state.user.email_verified = localStorage.getItem('email_verified')
      } else {
        state.token = ''
        state.isAuthenticated = false
        state.user.id = 0
        state.user.username = ''
        state.user.role = ''
        state.user.email_verified = ''
      }
    },
    setIsLoading(state, status) {
      state.isLoading = status
    },
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true
    },
    removeToken(state) {
      state.token = ''
      state.user.role = ''
      state.user.email_verified = ''
      state.isAuthenticated = false
    },
    setUser(state, user) {
      state.user = user
    },
  },
  actions: {
  },
  modules: {
  }
})
