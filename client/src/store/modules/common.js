import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	passwordNoMatch: false,
	notFound: false,
	loginFlag: false,
};

const getters = {
	passwordNoMatch: state => state.passwordNoMatch,
	notFound: state => state.notFound,
	loginFlag: state => state.loginFlag,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signup';
		axios.post(path, payload)
			.then((res) => {
				router.push({ path: '/login' });
			})
			.catch(error => {
				console.log(error);
			})
	},

	login: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				if (res.data.login_flag) {
					commit('session/setUserObject', res.data.user, { root: true })
					commit('setLoginFlag', res.data.login_flag)
					router.push({ path: '/set_up' });
				}
				commit('setNoPasswordMatch', res.data.Password_no_match)
				commit('setNotFound', res.data.Not_found)
			})
			.catch(error => {
				console.log(error);
			})
	},

	logout: ({ commit, dispatch }) => {
		let passwordNoMatch = false
		let notFound = false
		let loginFlag = false
		let userObject = []
		dispatch('text/clearTextState', '', { root: true })
		commit('setLoginFlag', loginFlag)
		commit('setNoPasswordMatch', passwordNoMatch)
		commit('setNotFound', notFound)
		commit('session/setUserObject', userObject, { root: true })
	},

};

const mutations = {

	setLoginFlag(state, data) {
		state.loginFlag = data
	},

	setNoPasswordMatch(state, data) {
		state.passwordNoMatch = data
	},

	setNotFound(state, data) {
		state.notFound = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};