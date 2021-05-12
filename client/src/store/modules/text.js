import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	textFile: '',
};

const getters = {
	textFile: state => state.textFile,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signup';
		axios.post(path, payload)
			.then((res) => {
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

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};