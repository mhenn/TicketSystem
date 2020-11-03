<template>
	<router-view/>
</template>



<script>

import store from '@/store'


export default{
	created(){
		let roles = store.state.userRoles
		if(!roles.includes('Support')){
			store.dispatch('getTickets')
		}	else {
			store.dispatch('getMappings')
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

