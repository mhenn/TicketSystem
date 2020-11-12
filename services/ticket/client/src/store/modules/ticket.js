import axios from 'axios'

const base_url = 'http://localhost:5070/gateway/ticket/'

function defineContent( file_list ,state){
			console.log(state)	
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


const state = () => ({
	tickets: [],
	selectedTicket: {'to':'', 'subject':'', 'content':''},	
	files: [],
	emptyTicket: false,
})

const mutations =  {
	updateFiles(state, files){
		state.files = files
	},
	clearFiles(state){
		state.files = []
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
			console.log(id)
			console.log(state.selectedTicket)
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
}

const actions = {
	downloadFile({rootState}, [filename, messageId]){
			
		let token = rootState.config.cloak.token
		let id = rootState.ticket.selectedTicket.id
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
	postSelected({rootState, dispatch}){
	
		let form = new FormData()
		let file_list = []		
		rootState.ticket.files.forEach(file => file_list.push(file.file))
		file_list.forEach( file => form.append(file.name, file))
		
		
		let token = rootState.config.cloak.token
		let [ticket, messageId]  = defineContent(file_list, rootState.ticket)
		ticket.sender = rootState.config.userName
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
						url: base_url + id + '/message/' + messageId  +'/files/',
						method: 'POST',
						headers: {
							'Authorization': 'Bearer ' + token,
							'accept' : 'application/json',
							'Content-Type': 'multipart/form-data'
						},
						data:form
					}
			
				axios(options_files).then(() =>{
					dispatch('getTickets')
				})
			} else {
				dispatch('getTickets')
			}
		})	

	}, 
	getTickets({rootState,commit}){
	
		let token = rootState.config.cloak.token
		let options = {
			url : base_url,
			method: 'GET',
			headers: {
				'Authorization' : 'Bearer ' + token
			}
		}

		axios(options).then(response =>{
			console.log(response.data.tickets)
			commit('update', response.data.tickets)	
		})
	},
	deleteSelected({rootState,  dispatch}){
		let token = rootState.config.cloak.token	
		axios
		.delete('http://localhost:5000/ticket/' + rootState.ticket.selectedTicket.id,{headers:{
			Authorization: "Bearer " + token,
			}}, )
		.then(() =>{
			dispatch('getTickets')
		})
	},
	putSelected({rootState, dispatch}){
	
		let form = new FormData()
		let file_list = []		
		rootState.ticket.files.forEach(file => file_list.push(file.file))
		file_list.forEach( file => form.append(file.name, file))
			
		let token = rootState.config.cloak.token	
		let [ticket, messageId]  = defineContent(file_list, rootState.ticket)
		messageId = messageId.replace(/\s/g, '')
		
		let options_ticket = {
			url: base_url + ticket.id,
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
						url: base_url + ticket.id + '/message/' + messageId  +'/files/',
						method: 'POST',
						headers: {
							'Authorization': 'Bearer ' + token,
							'accept' : 'application/json',
							'Content-Type': 'multipart/form-data'
						},
						data:form
					}

			
				axios(options_files).then(() =>{
					dispatch('getTickets')
				})
			} else {
				dispatch('getTickets')
			}
		})	

	},
	getSupporterTickets({rootState,commit}){

		let token = rootState.config.cloak.token	
		let topics = []
		rootState.config.mappings.forEach(m =>{
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
}

export default{
	namespaced: true,
	state,
	actions,
	mutations,
	base_url
}
