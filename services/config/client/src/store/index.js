import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import queues from './modules/queues'
import mapping from './modules/mapping'
import mail from './modules/mail'

Vue.use(Vuex)

export default new Vuex.Store({
	modules:{
		queues,
		mapping,
		mail
	},
	state: {
		cloak :'',
		roles : [],
		userRoles:[],
	},
	mutations: {
		selfUpdateUserRoles(state){

         let roles = state.cloak.tokenParsed.realm_access.roles
         let res = state.cloak.tokenParsed.resource_access
         console.log(roles)
         console.log(res)
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
	},
	actions: {	
		logout({state}){
			state.cloak.logout()
		},
			getRoles({state }){
			let token = state.cloak.token

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
})
