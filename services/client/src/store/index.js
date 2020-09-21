import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
	
Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		dialog: false,
		tickets: [],
		selectedTicket: {},
	},
	mutations: {
		switch(state){
			state.dialog = state.dialog ? false : true
		},
		update(state, tickets){
			state.tickets = tickets
		},
		changeSelectedTicket(state, id){
			if(id != null){	
				state.selectedTicket = state.tickets.find( el => {return el.id == id}) 
				state.update = true
			} else{
				state.update = false
				state.selectedTicket = {}
			}	
		},
		updateTicketData(state, field, data){
			state.selectedTicket[field] = data
		}
	},
	actions: {
		getTickets({commit}){
			let token = window.localStorage['vue-token']	
			axios.get('http://localhost:5000/ticket/',
			{headers:{
				Authorization: "Bearer " + token,
				}}
			).then(function (response){
				console.log(response)
				commit('update', response.data.tickets)
			})
		},
		postSelected(context){
			let token = window.localStorage['vue-token']	
			axios
			.post('http://localhost:5000/ticket', {headers:{
				Authorization: "Bearer " + token,
				}}, context.state.selectedTicket)
			.then( () => {
				context.dispatch('getTickets')
			})			
		},
		deleteSelected(context){
			axios
			.delete('http://localhost:5000/ticket/' + context.state.selectedTicket.id)
			.then(() =>{
				context.dispatch('getTickets')
			})
		},
		putSelected(context){
			axios
			.put('http://localhost:5000/ticket', context.state.selectedTicket)
			.then(() =>{
					context.dispatch('getTickets')
			})	
		}
	},
	modules: {
	}
})
