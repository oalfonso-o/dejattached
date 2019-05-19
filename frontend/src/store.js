import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex);

const state = {
  auth_status: '',
  token: localStorage.getItem('token') || '',
  user : {},
  numbers: [1, 2, 3]
};

const mutations = {
  ADD_NUMBER(state, payload) {
    state.numbers.push(payload);
  },
  AUTH_REQUEST(state){
    state.auth_status = 'loading'
  },
  AUTH_SUCCESS(state, token, user){
    state.auth_status = 'success'
    state.token = token
    state.user = user
  },
  AUTH_ERROR(state){
    state.auth_status = 'error'
  },
  LOGOUT(state){
    state.auth_status = ''
    state.token = ''
  },
};

const actions = {
  addNumber(context, number) {
    context.commit('ADD_NUMBER', number);
  },
  login({commit}, login_data){
    return new Promise((resolve, reject) => {
      commit('AUTH_REQUEST')
      axios({url: 'http://127.0.0.1:8000/api/login', data: login_data, method: 'POST' })
      .then(resp => {
        const token = resp.data.token
        const user = resp.data.user
        localStorage.setItem('token', token)
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        commit('AUTH_SUCCESS', token, user)
        resolve(resp)
      })
      .catch(err => {
        commit('AUTH_ERROR')
        localStorage.removeItem('token')
        reject(err)
      })
    })
  },
  register({commit}, register_data){
    return new Promise((resolve, reject) => {
      commit('AUTH_REQUEST')
      axios({url: 'http://127.0.0.1:8000/api/register', data: register_data, method: 'POST' })
      .then(resp => {
        const token = resp.data.token
        const user = resp.data.user
        localStorage.setItem('token', token)
        axios.defaults.headers.common['Authorization'] = 'Token ' + token
        commit('AUTH_SUCCESS', token, user)
        resolve(resp)
      })
      .catch(err => {
        commit('AUTH_ERROR', err)
        localStorage.removeItem('token')
        reject(err)
      })
    })
  },
  logout({commit}){
    return new Promise((resolve) => {
      commit('LOGOUT')
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
      resolve()
    })
  }
};

const getters = {
  getNumbers: state => state.numbers,
  isLoggedIn: state => !!state.token,
  authStatus: state => state.status,
};

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
});