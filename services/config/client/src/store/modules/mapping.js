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
	postMapping({rootState, dispatch}, mapping){
		
		let token = rootState.cloak.token
		let data = mapping

		let options = {
			url: mapping_url,
			method: 'POST',
			headers: get_auth_header(token),
			data: data
		}
		axios(options).then(() => {
			dispatch('getMappings')
		})
	},
	getMappings({rootState, commit}){

		let token = rootState.cloak.token
      let options = {
         url : mapping_url,
         method: 'GET',
			headers: get_auth_header(token),
      }

      axios(options).then(response =>{
         commit('updateMapping', response.data.mapping)
      })
   },
   deleteMapping({rootState, dispatch }, id){
		
		let token = rootState.cloak.token
		let options = {
			url: mapping_url + id,
			method: 'DELETE',
			headers: get_auth_header(token),
		}
		axios(options).then(() =>{
         dispatch('getMappings')
      })
   },
}

export default{
	namespaced: true,
	state,
	actions,
	mutations
}
