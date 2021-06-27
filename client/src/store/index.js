import Vue from 'vue';
import Vuex from 'vuex';
import common from './modules/common';
import session from './modules/session';
import text from './modules/text';
import data from './modules/data';

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    common,
    session, 
    text,
    data
  },
})
