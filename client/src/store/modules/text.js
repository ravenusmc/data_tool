import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

const state = {
	textFile: {},
	showSentimentResults: false,
	initalValue: 1,
	sentence: '',
	sentenceSentiment: 0,
	textLength: 0,
};

const getters = {
	textFile: state => state.textFile,
	showSentimentResults: state => state.showSentimentResults,
	initalValue: state => state.initalValue,
	sentence: state => state.sentence,
	sentenceSentiment: state => state.sentenceSentiment,
	textLength: state => state.textLength,
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
				commit('setTextFile', res.data);
				commit('setShowSentimentResults', true);
				commit('setSentence', res.data.sentence_and_sentiment_list[0].sentence)
				commit('setSentenceSentiment', res.data.sentence_and_sentiment_list[0].sentiment)
				commit('setTextLength', res.data.sentence_and_sentiment_list.length)
			})
			.catch(error => {
				console.log(error);
			})
	},

	changeSentenceAndSentiment: ({ commit, getters }, { payload }) => {
		// console.log(getters.textFile.sentence_and_sentiment_list.length)
		commit('setSentence', getters.textFile.sentence_and_sentiment_list[payload.value].sentence)
		commit('setSentenceSentiment', getters.textFile.sentence_and_sentiment_list[payload.value].sentiment)
		commit('setInitalValue', payload.value)
	},

};

const mutations = {

	setTextFile(state, data) {
		state.textFile = data
	},

	setShowSentimentResults(state, data) {
		state.showSentimentResults = data
	},

	setInitalValue(state, data) {
		state.initalValue = data
	},

	setSentence(state, data) {
		state.sentence = data
	},

	setSentenceSentiment(state, data) {
		state.sentenceSentiment = data
	},

	setTextLength(state, data) {
		state.textLength = data
	}

};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};