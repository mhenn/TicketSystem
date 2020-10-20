<template>
	<router-view/>
</template>


<script>

import store from '@/store'

export default{
	created(){
		store.dispatch('getQueues')
		store.dispatch('getMappings')
	}
}

</script>

