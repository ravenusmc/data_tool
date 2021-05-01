import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	loginUserObject: [],
	userCreated: false,
};

const getters = {
	loginUserObject: state => state.loginUserObject,
	userCreated: state => state.userCreated,
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

};

const mutations = {

	setloginUserObject(state, data) {
		state.loginUserObject = data
	},

	setUserCreated(state, data) {
		state.userCreated = data 
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};