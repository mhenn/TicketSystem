import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
	
Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		dialog: false,
		tickets: []
	},
	mutations: {
		switch(state){
			state.dialog = state.dialog ? false : true
		},
		update(state, tickets){
			state.tickets = tickets
		},
		updateSingle(state,ticket){
			let i = state.tickets.findIndex((el) => {return el.id == ticket.id})
			if(i >= 0){
				state.tickets[i] = ticket	
			}
		}
	},
	actions: {
		getTickets({commit}){
			axios
			.get('http://localhost:5000/ticket')
			.then( response => (
				commit("update", response.data.tickets)
			))	
		}
	},
	modules: {
	}
})
