import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex)

const state = {
	columns: {},
	showDataArea: false,
};

const getters = {
	columns: state => state.columns,
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
				commit('setColumns', res.data.column_names)
				commit('setShowDataArea', true)
			})
			.catch(error => {
				console.log(error);
			})
	},
};

const mutations = {

	setColumns(state, data) {
		state.columns = data
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