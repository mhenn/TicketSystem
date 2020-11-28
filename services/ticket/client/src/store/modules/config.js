/*eslint-disable*/
import axios from 'axios'

const state = () => ({
		cloak : '',
		queues: [],
		mappings: [],
		userRoles: [],
		userName : '',
})

const mutations = {
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
}
const actions = {
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
			if(r.status > 205)
				throw 'getQueues failed'
			commit('updateQueues', r.data.queues)
		}).catch(e =>{
			commit('misc/updateFail', 'getQueues',{root:true})
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
			if(response.status > 205)
				throw "getMappings failed"
			commit('updateMapping', response.data.mapping)	
		}).catch(e =>{
			commit('misc/updateFail', 'getMappings',{root:true})
		})
	},

	logout(context){
		context.state.cloak.logout()
	},
}

export default {
	namespaced: true,
	state, 
	actions,
	mutations
}
