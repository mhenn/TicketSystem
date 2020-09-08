import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		dialog: false,
		tickets: {}
	},
	mutations: {
		switch(state){
			state.dialog = state.dialog ? false : true
		}
	},
	actions: {
	},
	modules: {
	}
})
