import axios from 'axios'

const mapping_url = 'http://localhost:5555/config/role-mapping/'

function get_auth_header(token){
	return {'Authorization': 'Bearer ' + token}
}

const state= () =>  ({
	mapping:[],
})

const mutations = {
	updateMapping(state,mapping){
		state.mapping = mapping
	}
}

const actions = {	
	postMapping({rootState, dispatch, commit}, mapping){
		
		let token = rootState.misc.cloak.token
		let data = mapping

		let options = {
			url: mapping_url,
			method: 'POST',
			headers: get_auth_header(token),
			data: data
		}
		axios(options).then(r => {
			if(r.status > 205)
				throw 'Failed postMapping'
			dispatch('getMappings')	
      }).catch(e =>{
			commit('misc/updateFail', 'postMapping')
		})
	},
	getMappings({rootState, commit}){
		let token = rootState.misc.cloak.token
      let options = {
         url : mapping_url,
         method: 'GET',
			headers: get_auth_header(token),
      }

      axios(options).then(response =>{
			console.log(response.data)
			if(response.status > 205)
				throw 'Failed getMappings'
         commit('updateMapping', response.data.mapping)
      }).catch(e =>{
			commit('misc/updateFail', 'getMappings')
		})
   },
   deleteMapping({rootState, dispatch, commit}, id){
		
		let token = rootState.misc.cloak.token
		let options = {
			url: mapping_url + id,
			method: 'DELETE',
			headers: get_auth_header(token),
		}
		axios(options).then(r =>{
			if(r.status > 205)
				throw 'Failed deleteMapping'
         dispatch('getMappings')
      }).catch(e =>{
			commit('misc/updateFail', 'deleteMapping')
		})
   },
}

export default{
	namespaced: true,
	state,
	actions,
	mutations
}
