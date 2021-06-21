import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	loginUserObject: [],
	userCreated: false,
	token: null,
	passwordNoMatch: false,
	notFound: false,
	loginFlag: false,
	loginValues: {},
};

const getters = {
	loginUserObject: state => state.loginUserObject,
	userCreated: state => state.userCreated,
	token: state => state.token,
	passwordNoMatch: state => state.passwordNoMatch,
	notFound: state => state.notFound,
	loginFlag: state => state.loginFlag,
	loginValues: state => state.loginValues,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signup';
		axios.post(path, payload)
			.then((res) => {
				commit('setUserCreated', res.data);
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
				console.log(res.data)
				if (res.data.login_flag) {
					commit('setLoginFlag', res.data.login_flag)
					router.push({ path: '/set_up' });
				}
				commit('session/setUserObject', res.data.user, { root: true })
				commit('setNoPasswordMatch', res.data.Password_no_match)
				commit('setNotFound', res.data.Not_found)
				
			})
			.catch(error => {
				console.log(error);
			})
	},

	logout: ({ commit, dispatch }) => {
		dispatch('text/clearTextState', '', { root: true })
		let data = false
		commit('setLoginFlag', data)
	},

};

const mutations = {

	setloginUserObject(state, data) {
		state.loginUserObject = data
	},

	setUserCreated(state, data) {
		state.userCreated = data
	},

	set_token(state, token) {
		state.token = token
	},

	setLoginFlag(state, data) {
		state.loginFlag = data
	},

	setNoPasswordMatch(state, data) {
		state.passwordNoMatch = data
	},

	setNotFound(state, data) {
		state.notFound = state
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};