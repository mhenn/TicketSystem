<template>
	<router-view/>
</template>


<script>

import store from '@/store'
import {mapActions} from 'vuex'

export default{
	created(){
		console.log(store)
		//this.getQueues()
		store.dispatch('queues/getQueues')
		store.dispatch('getMappings')
		store.dispatch('getMailMappings')
	}
}

</script>

