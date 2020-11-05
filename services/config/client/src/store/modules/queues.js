import {queue_url} from '@/store/utils.js'
import axios from 'axios'

function get_auth_header(token){
	return {'Authorization': 'Bearer ' + token}
}

const state = () => ({
		queues: []
})

const getters = {}

const mutations = {
	updateQueues(state,queues){
		state.queues = queues
	},
}

const actions = {
	postQueue({rootState,state, dispatch}, queueName ){	
		let token = state.cloak.token
		let data = {'title' : queueName}

		let options = {
			url: queue_url,
			method: 'POST',
			headers: get_auth_header(token),
			data: data
		}
		axios(options).then(() => {
			dispatch('getQueues')
		})
	},
	getQueues({rootState, state,commit}){
		console.log('aasdfgfsadf')
		let token = rootState.cloak.token
		console.log('aasdfgfsadf')
      let options = {
         url : queue_url,
         method: 'GET',
			headers: {
				'Authorization': 'Bearer ' + token
			},
      }
		console.log('asdfff')
      axios(options).then(response =>{
			console.log('asdfff')
         commit('updateQueues', response.data.queues)
      })
   },
   deleteQueue({state, dispatch}, id){
		let token = state.cloak.token
		let options = {
			url: queue_url + id,
			method: 'DELETE',
			headers: get_auth_header(token),
		}
		axios(options).then(() =>{
         dispatch('getQueues')
      })
	}
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
}
