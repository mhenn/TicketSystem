import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
	state: {
		cloak :'',
		queues: [],
		roles : [],
		mapping:[],
		mail: []
	},
	mutations: {

		setCloak(state,cloak){
			state.cloak = cloak
		},
		updateRoles(state,roles){
			state.roles = roles
		},
		updateQueues(state,queues){
			state.queues = queues
		},
		updateMapping(state,mapping){
			console.log(mapping)
			state.mapping = mapping
		},
		updateMailMapping(state, mapping){
			state.mapping = mapping
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
		//MAPPING
		postMapping({dispatch}, mapping){
			


			let token = window.localStorage['vue-token']
			let data = mapping

			let options = {
				url: 'http://localhost:5555/config/role-mapping/',
				method: 'POST',
				headers: {
					'Authorization' : 'Bearer ' + token
				},
				data: data
			}
			axios(options).then(() => {
				dispatch('getMappings')
			})

		},
		getMappings({commit}){

         let token = window.localStorage['vue-token']
         let options = {
            url :'http://localhost:5555/config/role-mapping/',
            method: 'GET',
            headers: {
               'Authorization' : 'Bearer ' + token
            }
         }

         axios(options).then(response =>{
            commit('updateMapping', response.data.mapping)
         })
      },
      deleteMapping(context, id){
         let token = window.localStorage['vue-token']
			let options = {
				url: 'http://localhost:5555/config/role-mapping/' + id,
				method: 'DELETE',
				headers:{
            	Authorization: "Bearer " + token,
            }
			}
			axios(options).then(() =>{
            context.dispatch('getMappings')
         })
      },
		postMailMapping(context, data){
			let token = window.localStorage['vue-token']
			let options = {
				url: 'http://localhost:5555/config/mail-mapping/',
				method: 'POST',
				headers: {
					'Authorization' : 'Bearer ' + token
				},
				data: data
			}
			axios(options).then(r =>{
				console.log(r)
			})
		},
		getMailMappings({commit}){

         let token = window.localStorage['vue-token']
         let options = {
            url :'http://localhost:5555/config/mail-mapping/',
            method: 'GET',
            headers: {
               'Authorization' : 'Bearer ' + token
            }
         }

         axios(options).then(response =>{
				console.log(response.data)
            commit('updateMailMapping', response.data.mapping)
         })
      },
 
	},
	modules: {
	}
})
