import axios from 'axios'

const mail_url = 'http://localhost:5555/config/mail-mapping/'

const state = () => ({
		mail: [],
	})


const mutations =  {
	updateMailMapping(state, mapping){
		state.mail = mapping
	}
}
	
const actions = {	
	postMailMapping({rootState, dispatch}, data){
		let token = rootState.misc.cloak.token	
		
		let options = {
			url: mail_url, 
			method: 'POST',
			headers: {
				'Authorization' : 'Bearer ' + token
			},
			data: data
		}
		axios(options).then(r =>{
			dispatch('getMailMappings')
		})
	},
	getMailMappings({rootState, commit}){
		
		let token = rootState.misc.cloak.token	

		let options = {
			url:  mail_url,
			method: 'GET',
			headers: {
				'Authorization' : 'Bearer ' + token
			}
		}

		axios(options).then(response =>{
			commit('updateMailMapping', response.data.mapping)
		})
	},
	deleteMailMapping({rootState, dispatch}, id){
		
		let token = rootState.misc.cloak.token	
		let options = {
			url : mail_url + id,
			method: 'DELETE',
			headers: {
				'Authorization' : 'Bearer ' + token
			}
		}

		axios(options).then(response =>{
			dispatch('getMailMappings')
		})
		
	}
}

export default {
	namespaced: true,
	state,
	actions,
	mutations
}
