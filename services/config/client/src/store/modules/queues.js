import axios from 'axios'

const queue_url = 'http://localhost:5555/config/queues/'

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
	postQueue({rootState, dispatch}, queueName ){	
		let token = rootState.cloak.token
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
	getQueues({rootState ,commit}){
		console.log(rootState)
		console.log(commit)
		let token = rootState.cloak.token
      let options = {
         url : queue_url,
         method: 'GET',
			headers: {
				'Authorization': 'Bearer ' + token
			},
      }
      axios(options).then(response =>{
      	console.log(response)
			commit('updateQueues', response.data.queues)
      })
   },
   deleteQueue({rootState, dispatch}, id){
		let token = rootState.cloak.token
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
