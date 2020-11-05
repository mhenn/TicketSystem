import {mapping_url, get_auth_header} from '@/store/utils.js'


const state= () =>  ({
	mapping:[],
})

const mutations = {
	updateMapping(state,mapping){
		state.mapping = mapping
	}
}

const actions = {	
	postMapping({state, dispatch}, mapping){
		
		let token = state.cloak.token
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
	getMappings({state, commit}){

		let token = state.cloak.token
      let options = {
         url : mapping_url,
         method: 'GET',
			headers: get_auth_header(token),
      }

      axios(options).then(response =>{
         //commit('/updateMapping', response.data.mapping)
      })
   },
   deleteMapping({state, dispatch }, id){
		
		let token = state.cloak.token
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
