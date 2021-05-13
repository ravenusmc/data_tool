import Vue from 'vue';
import Vuex from 'vuex';
import common from './modules/common';
import text from './modules/text';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    common,
    text
  },
})
