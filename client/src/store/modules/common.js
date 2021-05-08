import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	loginUserObject: [],
	userCreated: false,
	token: null, 
	passwordNoMatch: false,
	loginValues: {},
};

const getters = {
	loginUserObject: state => state.loginUserObject,
	userCreated: state => state.userCreated,
	token: state => state.token, 
	passwordNoMatch: state => state.passwordNoMatch, 
	loginValues: state => state.loginValues,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signup';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data);
				commit('setUserCreated', res.data);
			})
			.catch(error => {
				console.log(error);
			})
	},

	login: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/login';
		axios.post(path, payload)
			.then((res) => {
				commit('setNoPasswordMatch', res.data.Password_no_match);
			})
			.catch(error => {
				console.log(error);
			})
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

	setNoPasswordMatch(state, data) {
		state.passwordNoMatch = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};