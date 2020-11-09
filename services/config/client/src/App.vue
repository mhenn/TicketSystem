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
		store.dispatch('mapping/getMappings')
		store.dispatch('mail/getMailMappings')
	}
}

</script>

