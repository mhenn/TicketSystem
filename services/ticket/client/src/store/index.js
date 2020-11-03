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
		queues: [],
		mappings: [],
		userRoles: [],
		userName : '',
	},
	mutations: {
		async updateUserName(state, info){
			info = await info
			state.userName = info.preferred_username
		},
		setCloak(state, cloak){
			state.cloak = cloak
		},
		selfUpdateRoles(state){

			let roles = state.cloak.tokenParsed.realm_access.roles
			let res = state.cloak.tokenParsed.resource_access
			for(let key in res){
				if(key){
					roles = [...roles, ...res[key].roles]	
				}
			}

			state.userRoles = roles
		},
		updateQueues(state,queues){
			state.queues = queues
		},
		updateMapping(state, mapping){
			state.mappings = mapping
		},
		updateFiles(state, files){
			state.files = files
		},
		clearFiles(state){
			state.files = []
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

		getQueues({state,commit}){
			let token = state.cloak.token
		
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
				
			let token = state.cloak.token
			let id = state.selectedTicket.id
			messageId = messageId.replace(/\s/g,'')
			let options = {
				url: 'http://localhost:5070/gateway/ticket/' + id +'/message/'+messageId +'/file/'+filename,
				method: 'GET',
				responseType: 'blob',
				headers: {
					'Authorization': 'Bearer ' + token,
					'Accept': '*/*'
				}
			}
			axios(options).then(r => {
				let url = window.url || window.webkitURL
				let downloadUrl = url.createObjectURL(r.data)
				window.open(downloadUrl)
			})
		},
		postSelected({state, dispatch}){
	
			let form = new FormData()
			let file_list = []		
			state.files.forEach(file => file_list.push(file.file))
			file_list.forEach( file => form.append(file.name, file))
			
			
			let token = state.cloak.token
			let [ticket, messageId]  = defineContent(file_list, state)
			ticket.sender = state.userName
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
		getTickets({state,commit}){

			let token = state.cloak.token
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
			deleteSelected({state, dispatch}){
			let token = state.cloak.token	
			axios
			.delete('http://localhost:5000/ticket/' + context.state.selectedTicket.id,{headers:{
				Authorization: "Bearer " + token,
				}}, )
			.then(() =>{
				dispatch('getTickets')
			})
		},
		putSelected({state, dispatch}){
	
			let form = new FormData()
			let file_list = []		
			state.files.forEach(file => file_list.push(file.file))
			file_list.forEach( file => form.append(file.name, file))
			
			
			let token = state.cloak.token	
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
		getMappings({state, commit}){
			let token = state.cloak.token
			let options = {
				url :'http://localhost:5070/gateway/config/role-mapping/',
				method: 'GET',
				headers: {
					'Authorization' : 'Bearer ' + token
				}
			}

			axios(options).then(response =>{
				commit('updateMapping', response.data.mapping)	
			})	
		},
		logout(context){
			context.state.cloak.logout()
		},
		getSupporterTickets({state,commit}){

			let token = state.cloak.token	
			let topics = []
			state.mappings.forEach(m =>{
				m.children.forEach(c =>{
					topics.push(c)
				})
			})
			let data = {'topics': [... new Set(topics)]}
			let options = {
				url :'http://localhost:5070/gateway/supporter/ticket/',
				method: 'POST',
				headers: {
					'Authorization' : 'Bearer ' + token
				},
				data: data
			}

			axios(options).then(response =>{
				commit('update', response.data.tickets)	
			})
		},
	},
	modules: {
	}
})
