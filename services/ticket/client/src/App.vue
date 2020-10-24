<template>
	<router-view/>
</template>



<script>

import store from '@/store'


export default{
	created(){
		let roles  = JSON.stringify(store.state.cloak.tokenParsed.realm_access.roles)
		if(roles.includes('support')){
			store.dispatch('getTickets')
		}	else {
			store.dispatch('getMappings')
		//	store.dispatch('getSupporterTickets')
		}
		store.dispatch('getQueues')		
	},
	computed:{
		mappings(){
			return store.state.mappings
		}
	},
	watch:{
		mappings(value){
			if(value.length > 0){
				store.dispatch('getSupporterTickets')
			}
		}
	}
	
}

</script>

