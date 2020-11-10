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
			commit('updateQueues', r.data.queues)
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
}

export default {
	namespaced: true,
	state, 
	actions,
	mutations
}