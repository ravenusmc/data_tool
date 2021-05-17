import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import router from '../../router';

Vue.use(Vuex)

const state = {
	textFile: {},
	showSentimentResults: false,
};

const getters = {
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults
};

const actions = {

	handleFileUpload: ({ commit }, { formData }) => {
		// console.log(payload)
		const path = 'http://localhost:5000/text_file_upload';
		axios.post(path, formData, {
			headers: {
				'Content-Type': 'multipart/form-data'
			}
		})
		.then((res) => {
			console.log(res.data)
			commit('setTextFile', res.data);
			commit('setShowSentimentResults', true);
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

	setShowSentimentResults(state, data) {
		state.showSentimentResults = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};