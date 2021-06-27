import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	fileInformation: {},
	showDataArea: false,
};

const getters = {
	fileInformation: state => state.fileInformation,
	showDataArea: state => state.showDataArea,
};

const actions = {

	fetchFileInformation: ({ commit }, { formData }) => {
		const path = 'http://localhost:5000/fetch_File_Information';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
			.then((res) => {
				commit('setFileInformation', res.data)
				commit('setShowDataArea', true)
			})
			.catch(error => {
				console.log(error);
			})
	},

};

const mutations = {

	setFileInformation(state, data) {
		state.fileInformation = data
	},

	setShowDataArea(state, data) {
		state.showDataArea = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};