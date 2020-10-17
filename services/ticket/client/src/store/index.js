/* eslint-disable */
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import fileDownload from 'js-file-download'
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
		return [ticket, content['timestamp']]
}


export default new Vuex.Store({
	state: {
		dialog: false,
		tickets: [],
		selectedTicket: {'to':'', 'subject':'', 'content':''},	
		files: [],
		emptyTicket: false,
		cloak : '',
		queues: []
	},
	mutations: {
		setCloak(state, cloak){
			state.cloak = cloak
		},
		updateQueues(state,queues){
			state.queues = queues
		},
		updateFiles(state, files){
			state.files = files
		},
		switch(state){
			state.dialog = state.dialog ? false : true
		},
		update(state, tickets){
			state.tickets = tickets
		},
		clearSelectedTicket(state){
			state.selectedTicket = {}
		},
		changeSelectedTicket(state, id){
			if(id != null){	
				state.selectedTicket = state.tickets.find( el => {return el.id == id}) 
				state.emptyTicket = false
			} else{
				state.emptyTicket = true
				state.selectedTicket = {'to':'', 'subject':'', 'content':''}	
			}	
		},
		updateTicketData(state, data){
			let field = data[0]
			let value = data[1]
			state.selectedTicket[field] = value
				
		}
	},
	actions: {

		getQueues({commit}){
			let token = window.localStorage['vue-token']		
		
			let options = {
				url: 'http://localhost:5070/gateway/queues/',
				method: 'get',
				headers: {
					'Authorization': 'Bearer ' + token,
				},
			}
			axios(options).then(r =>{
				commit('updateQueues', r.data.queues)
			
			})	

		},

		downloadFile({state}, [filename, messageId]){
				
			let token = window.localStorage['vue-token']		
			let id = state.selectedTicket.id
			let form = new FormData()
			form.append('uid', 'd2717165-4f26-477b-a992-bc31b2b085cd')
			messageId = messageId.replace(/\s/g,'')
			let options = {
				url: 'http://localhost:5070/gateway/ticket/' + id +'/message/'+messageId +'/file/'+filename,
				method: 'get',
				headers: {
					'Authorization': 'Bearer ' + token,
				},
				data: form
			}
			
			//window.open(options.url)
			axios(options).then(r => {
				if (r.status == 200){
					window.open(r.config.url)
				}
			})
		},
		postSelected({state, dispatch}){
	
			let form = new FormData()
			let file_list = []		
			state.files.forEach(file => file_list.push(file.file))
			file_list.forEach( file => form.append(file.name, file))
			
			
			let token = window.localStorage['vue-token']		
			let [ticket, messageId]  = defineContent(file_list, state)
			messageId = messageId.replace(/\s/g, '')
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
						let id = response.data.id
						let options_files = {
							url: 'http://localhost:5070/gateway/ticket/' + id + '/message/' + messageId  +'/files/',
							method: 'POST',
							headers: {
								'Authorization': 'Bearer ' + token,
								'accept' : 'application/json',
								'Content-Type': 'multipart/form-data'
							},
							data:form
						}

				
         		axios(options_files).then(response =>{
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
		putSelected({state, dispatch}){
	
			let form = new FormData()
			let file_list = []		
			state.files.forEach(file => file_list.push(file.file))
			file_list.forEach( file => form.append(file.name, file))
			
			
			let token = window.localStorage['vue-token']		
			let [ticket, messageId]  = defineContent(file_list, state)
			messageId = messageId.replace(/\s/g, '')
			let options_ticket = {
				url: 'http://localhost:5070/gateway/ticket/'+ ticket.id,
				method: 'put',
				headers: {
					'Authorization': 'Bearer ' + token,
				},
				data:{
					ticket:ticket
				}
			}
			
			axios(options_ticket).then(response =>{
				if(response.status == 200 && file_list.length > 0){
						let options_files = {
							url: 'http://localhost:5070/gateway/ticket/' + ticket.id + '/message/' + messageId  +'/files/',
							method: 'POST',
							headers: {
								'Authorization': 'Bearer ' + token,
								'accept' : 'application/json',
								'Content-Type': 'multipart/form-data'
							},
							data:form
						}

				
         		axios(options_files).then(response =>{
						dispatch('getTickets')
					})
				} else {
					dispatch('getTickets')
				}
			})	

		},
		logout(context){
			context.state.cloak.logout()
		}	
	},
	modules: {
	}
})
