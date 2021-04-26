import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	loginUserObject: [],
};

const getters = {
	loginUserObject: state => state.loginUserObject,
};

const actions = {

	setUpUser: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/signup';
		axios.post(path, payload)
			.then((res) => {
				console.log(res.data);
				// for (let i = 1; i < res.data.length; i++) {
				// 	let date = new Date(res.data[i][0], 0, 1)
				// 	res.data[i][0] = date
				// }
				// commit('setEvaCountData', res.data);
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