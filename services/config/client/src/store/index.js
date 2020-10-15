import Vue from 'vue'
import Vuex from 'vuex'
	
Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		cloak :''
	},
	mutations: {
		setCloak(state,cloak){
			state.cloak = cloak
		}
	},
	actions: {	
		logout({state}){
			state.cloak.logout()
		}
	},
	modules: {
	}
})
