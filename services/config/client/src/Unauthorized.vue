<template>

	<v-app :dark='this.$vuetify.theme.dark = true'>
		<v-card loading 
			class="mx-auto my-12"
		>
			<v-card-title >Unauthorized</v-card-title>
			<v-card-text>You are not allowed to use this service and therefore being signed out</v-card-text>
		</v-card>
	</v-app>
</template>


<script>

import store from '@/store'

export default{
	components: {
	},
	created(){
		setTimeout(() =>{ store.dispatch('logout') }, 5000)
	}
}


</script>


