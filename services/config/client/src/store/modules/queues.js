import axios from 'axios'

const queue_url = 'http://localhost:5555/config/queues/'

function get_auth_header(token){
	return {'Authorization': 'Bearer ' + token}
}

const state = () => ({
	queues: [],
})

const getters = {}

const mutations = {
	updateQueues(state,queues){
		state.queues = queues
	},
}

const actions = {
	postQueue({rootState, dispatch, commit}, queueName ){	
		let token = rootState.misc.cloak.token
		let data = {'title' : queueName}

		let options = {
			url: queue_url,
			method: 'POST',
			headers: get_auth_header(token),
			data: data
		}
		axios(options).then(() => {
			dispatch('getQueues')
		}).catch(e =>{
			commit('misc/updateFail', 'postQueue')
		})
	},
	getQueues({rootState ,commit}){
		let token = rootState.misc.cloak.token
      let options = {
         url : queue_url,
         method: 'GET',
			headers: {
				'Authorization': 'Bearer ' + token
			},
      }
      axios(options).then(response =>{
			if(response.status > 205)
				throw "Failed getQueues"
			commit('updateQueues', response.data.queues)
      }).catch(e =>{
			
			commit('misc/updateFail', 'getQueue')
		})
   },
   deleteQueue({rootState, dispatch, commit}, id){
		let token = rootState.misc.cloak.token
		let options = {
			url: queue_url + id,
			method: 'DELETE',
			headers: get_auth_header(token),
		}
		axios(options).then(r =>{
			if(r.status > 205)
				throw "Failed Delete"
         dispatch('getQueues')
      }).catch(e =>{
			commit('misc/updateFail', 'deleteQueue')
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
