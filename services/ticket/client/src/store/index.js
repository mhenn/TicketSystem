import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
	
Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		dialog: false,
		tickets: [],
		selectedTicket: {},	
		files: [],
		emptyTicket: false
	},
	mutations: {
		updateFiles(state, files){
			console.log(files)
			state.files = files
			console.log('reeee')
			console.log(state.files)
		},
		switch(state){
			state.dialog = state.dialog ? false : true
		},
		update(state, tickets){
			state.tickets = tickets
		},
		changeSelectedTicket(state, id){
			if(id != null){	
				state.selectedTicket = state.tickets.find( el => {return el.id == id}) 
				state.emptyTicket = false
			} else{
				state.emptyTicket = true
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
		
		withFiles({state}){
			const form = new FormData()
			form.append('file', state.files[0])
			console.log(state.files[0])
			form.append('rat', 'house')
			let options = {
            url: 'http://localhost:5000/ticket/upload/',
            method: 'POST',
				headers: {
					'accept' : 'application/json',
					'Content-Type': 'multipart/form-data'
				},
            form:form
         }

         axios(options).then(response =>{
				console.log(response)
			})
		}, 
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
			let ticket = context.state.selectedTicket
			let content = {
				'timestamp': new Date().toUTCString(),
				'message':ticket.content,
				'appendices' : null
			}
			delete context.state.selectedTicket.content
			ticket['messages'] = [content]	
			
			let options  = {
				url: 'http://localhost:5070/gateway/ticket/',
				method: 'POST',
				headers: {
					'Authorization': 'Bearer ' + token,
					'Content-Type': 'application/json;charset=UTF-8'
				},
				data: {
					ticket: ticket 
				}
			}

			axios(options).then(response =>{
				console.log(response)
				context.dispatch('getTickets')
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

			let token = window.localStorage['vue-token']
			let ticket = context.state.selectedTicket
			let content = {
				'timestamp': new Date().toUTCString(),
				'message':ticket.content,
				'appendices' : null
			}
			let messages_reverse = ticket.messages.reverse()
			messages_reverse.push(content)
			ticket.messages = messages_reverse.reverse()

			delete context.state.selectedTicket.content
			
			let options  = {
				url: 'http://localhost:5070/gateway/ticket/'+ ticket.id,
				method: 'PUT',
				headers: {
					'Authorization': 'Bearer ' + token,
					'Content-Type': 'application/json;charset=UTF-8'
				},
				data: {
					ticket: ticket 
				}
			}

			axios(options).then(response =>{
				console.log(response)
				context.dispatch('getTickets')
			})
		}
	},
	modules: {
	}
})
