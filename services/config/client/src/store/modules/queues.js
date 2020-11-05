

const state = () => ({
		queues: []
})

const getters = {}

const mutations = {
		updateQueues(state,queues){
			state.queues = queues
		},
}

const actions = {
	

}
	actions: {	
		postQueue({state, dispatch}, queueName ){
			
			let token = state.cloak.token
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
		getQueues({state,commit}){
			let token = state.cloak.token
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
      deleteQueue({state, dispatch}, id){
			let token = state.cloak.token
			let options = {
				url: 'http://localhost:5555/config/queues/' + id,
				method: 'DELETE',
				headers:{
            	Authorization: "Bearer " + token,
            }
			}
			axios(options).then(() =>{
            dispatch('getQueues')
         })
      },
	
