/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
//import {serialize} from 'object-to-formdata'
Vue.use(Vuex)


function defineContent( file_list ,state){
			var ticket = state.selectedTicket 
			var file_names = []
			file_list.forEach(file => file_names.push(file.name))		
	
			let content = {
				'timestamp': new Date().toUTCString(),
				'message':ticket.content,
				'appendices' : file_names
			}

			delete state.selectedTicket.content
			if ('messages' in ticket){
				let messages_reverse = ticket.messages.reverse()
				messages_reverse.push(content)
				ticket.messages = messages_reverse.reverse()
			} else{
				ticket['messages'] = [content]	
			}
		return ticket
}


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
			state.files = files
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
		
		postSelected({state, dispatch}){
	
			let form = new FormData()
			let file_list = []		
			state.files.forEach(file => file_list.push(file.file))
			file_list.forEach( file => form.append(file.name, file))
			
			
			let token = window.localStorage['vue-token']		
			let ticket = defineContent(file_list, state)

			let options_ticket = {
				url: 'http://localhost:5070/gateway/ticket/',
				method: 'post',
				headers: {
					'Authorization': 'Bearer ' + token,
					'Content-Type': 'application/json' 
				},
				data: ticket
			}
			
			axios(options_ticket).then(response =>{
				if(response.status == 200 && file_list.length > 0){
						console.log(response)	
						id = response.data.id
						let options_files = {
							url: 'http://localhost:5000/ticket/' + id + '/files/',
							method: 'POST',
							headers: {
								'accept' : 'application/json',
								'Content-Type': 'multipart/form-data'
							},
							data:form
						}

				
         		axios(options_files).then(response =>{
						console.log(response)
						dispatch('getTickets')
					})
				} else {
					dispatch('getTickets')
				}
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
