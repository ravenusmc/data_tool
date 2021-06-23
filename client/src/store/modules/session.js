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

	updateUserProfile: ({ commit }, { payload }) => {
		console.log(payload.id)
		const path = `http://localhost:5000/update_user_profile/${payload.id}`;
		axios.put(path, payload)
			.then((res) => {
				commit('setUserObject', res.data);
			})
			.catch(error => {
				console.log(error);
			})
	},

	deleteUser: ({ commit }, { payload }) => {
		const path = `http://localhost:5000/delete_user/${payload.id}`;
		axios.delete(path)
			.then(() => {
				let userObject = []
				let logoutFlag = false
				commit('setUserObject', userObject);
				commit('common/setLoginFlag', logoutFlag, { root: true })
				router.push({ path: '/' });
			})
			.catch(error => {
				console.log(error);
			})
	},

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