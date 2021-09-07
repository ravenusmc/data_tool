import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueGoogleCharts from 'vue-google-charts'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faUserSecret, faHashtag, faPencilAlt, faCodeBranch, faNetworkWired } from '@fortawesome/free-solid-svg-icons'
import VTooltip from 'v-tooltip'

library.add(faUserSecret, faHashtag, faPencilAlt, faCodeBranch, faNetworkWired)

Vue.component('fa-icon', FontAwesomeIcon)

// Google charts plugin
Vue.use(VueGoogleCharts);
// Tooltips library 
Vue.use(VTooltip)
VTooltip.options.defaultTemplate = '<div class="tooltip-vue" role="tooltip"><div class="tooltip-vue-arrow"></div><div class="tooltip-vue-inner"></div></div>';
VTooltip.options.defaultArrowSelector = '.tooltip-vue-arrow, .tooltip-vue__arrow';
VTooltip.options.defaultInnerSelector = '.tooltip-vue-inner, .tooltip-vue__inner';
VTooltip.options.defaultLoadingClass = '.tooltip-vue-loading'
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
