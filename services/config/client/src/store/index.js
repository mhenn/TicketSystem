import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		cloak :'',
		queues: [],
		roles: []
	},
	mutations: {

		setCloak(state,cloak){
			state.cloak = cloak
		},
		updateRoles(state,roles){
			console.log(roles)
			state.roles = roles
		},
		updateQueues(state,queues){
			console.log(queues)
			state.queues = queues
		}
	},
	actions: {	
		logout({state}){
			state.cloak.logout()
		},
		postQueue({dispatch}, queueName ){
			
			let token = window.localStorage['vue-token']
			let data = {'title' : queueName}

			let options = {
				url: 'http://localhost:5555/config/queues/',
				method: 'POST',
				headers: {
					'Authorization' : 'Bearer ' + token
				},
				data: data
			}
			axios(options).then(() => {
				dispatch('getQueues')
			})

		},
		getQueues({commit}){

         let token = window.localStorage['vue-token']
         let options = {
            url :'http://localhost:5555/config/queues/',
            method: 'GET',
            headers: {
               'Authorization' : 'Bearer ' + token
            }
         }

         axios(options).then(response =>{
            commit('updateQueues', response.data.queues)
         })
      },
      deleteQueue(context, id){
         let token = window.localStorage['vue-token']
			let options = {
				url: 'http://localhost:5555/config/queues/' + id,
				method: 'DELETE',
				headers:{
            	Authorization: "Bearer " + token,
            }
			}
			axios(options).then(() =>{
            context.dispatch('getQueues')
         })
      },
		getRoles(context){
			let token = window.localStorage['vue-token']

			let options = {
				url: 'http://localhost:8000/auth/admin/realms/Odonata/clients/64ce3a4f-c9a8-4105-a5b3-32522f1f1e88/roles',
				method: 'GET',
				headers:{
					Authorization: "Bearer " + token
				}
			}
			axios(options).then(r =>{ console.log(r)})
		},
	},
	modules: {
	}
})
