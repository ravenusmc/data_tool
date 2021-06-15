import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	userObject: [],
};

const getters = {
	userObject: state => state.userObject,
};

const actions = {

	// setUpUser: ({ commit }, { payload }) => {
	// 	const path = 'http://localhost:5000/signup';
	// 	axios.post(path, payload)
	// 		.then((res) => {
	// 			commit('setUserCreated', res.data);
	// 		})
	// 		.catch(error => {
	// 			console.log(error);
	// 		})
	// },

};

const mutations = {

	setUserObject(state, data) {
		state.userObject = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};