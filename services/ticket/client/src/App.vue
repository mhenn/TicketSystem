<template>
	<router-view/>
</template>



<script>

import store from '@/store'


export default{
	created(){
		let roles = store.state.config.userRoles
		if(!roles.includes('Support')){
			store.dispatch('ticket/getTickets')
		}	else {
			store.dispatch('config/getMappings')
		}
		store.dispatch('config/getQueues')		
	},
	computed:{
		mappings(){
			return store.state.config.mappings
		}
	},
	watch:{
		mappings(value){
			if(value.length > 0){
				store.dispatch('ticket/getSupporterTickets')
			}
		}
	}
	
}

</script>

