import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	textFile: {},
};

const getters = {
	textFile: state => state.textFile,
};

const actions = {

	handleFileUpload: ({ commit }, { payload }) => {
		console.log(payload)
		const path = 'http://localhost:5000/text_file_upload';
		axios.post(path, payload, {
			headers: {
					'Content-Type': 'multipart/form-data'
			}
		})
		.then((res) => {
			commit('setTextFile', res.data);
		})
		.catch(error => {
			console.log(error);
		})
	},

};

const mutations = {

	setTextFile(state, data) {
		state.textFile = data
	},

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};