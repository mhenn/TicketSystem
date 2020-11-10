/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import ticket from './modules/ticket'
import config from './modules/config'
import misc from './modules/misc'
Vue.use(Vuex)

export default new Vuex.Store({
	modules: {
		ticket,
		config,
		misc
	}
})
