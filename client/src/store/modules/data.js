import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	passwordNoMatch: false,
};

const getters = {
	passwordNoMatch: state => state.passwordNoMatch,
};

const actions = {

	fetchFileInformation: ({ commit }, { formData }) => {
		console.log(formData)
		const path = 'http://localhost:5000/fetch_File_Information';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
			.then((res) => {
				console.log(res.data)
				// router.push({ path: '/login' });
			})
			.catch(error => {
				console.log(error);
			})
	},

};

const mutations = {

	setLoginFlag(state, data) {
		state.loginFlag = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};