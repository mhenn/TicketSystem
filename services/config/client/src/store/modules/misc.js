import axios from 'axios'

const auth_url = 'http://localhost:8000/auth/admin/realms/Odonata/clients/64ce3a4f-c9a8-4105-a5b3-32522f1f1e88/roles'

const state = () =>  ({
	cloak :'',
	roles : [],
	userRoles:[],
	failed: []
})

const mutations = {
	selfUpdateUserRoles(state){

		let roles = state.cloak.tokenParsed.realm_access.roles
		let res = state.cloak.tokenParsed.resource_access
		for(let key in res){
			if(key){
				roles = [...roles, ...res[key].roles]
			}
		}

		state.userRoles = roles
	},
	setCloak(state,cloak){
		state.cloak = cloak
	},
	updateRoles(state,roles){
		state.roles = roles
	},
	updateFail(state, type){
		if(!state.failed.includes)	
			state.failed.push(type)
	},
	clearFailType(state, type){
		state.failed = state.failed.filter(e => {return e != type})
	},
	clearFail(state){
		state.failed = []
	}


}

const actions = {	
	logout({state}){
		rootState.cloak.logout()
	}
}

export default {
	namespaced: true,
	state,
	actions,
	mutations
}
