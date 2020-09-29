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
		updateTicketData(state, data){
			let field = data[0]
			let value = data[1]
			state.selectedTicket[field] = value
		}
	},
	actions: {
		getTickets({commit}){

			let token = window.localStorage['vue-token']	
			
			let options = {
				url :'http://localhost:5070/gateway/ticket/',
				method: 'GET',
				headers: {
					'Authorization' : 'Bearer ' + token
				}
			}

			axios(options).then(response =>{
				commit('update', response.data.tickets)	
			})
		},
		postSelected(context){
			let token = window.localStorage['vue-token']

			let options  = {
				url: 'http://localhost:5070/gateway/ticket/',
				method: 'POST',
				headers: {
					'Authorization': 'Bearer ' + token,
					'Content-Type': 'application/json;charset=UTF-8'
				},
				data: {
					ticket: context.state.selectedTicket
				}
			}

			axios(options).then(response =>{
				console.log(response)
			})
		
		},
		deleteSelected(context){
			let token = window.localStorage['vue-token']	
			axios
			.delete('http://localhost:5000/ticket/' + context.state.selectedTicket.id,{headers:{
				Authorization: "Bearer " + token,
				}}, )
			.then(() =>{
				context.dispatch('getTickets')
			})
		},
		putSelected(context){
			axios
			.put('http://localhost:5000/ticket/', context.state.selectedTicket)
			.then(() =>{
					context.dispatch('getTickets')
			})	
		}
	},
	modules: {
	}
})
