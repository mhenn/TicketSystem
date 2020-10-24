<template>
  <div class="limbo">

	<Inferno>
		<Minos v-if="contains(roles(),'support')"   /> 
		<Support v-if="!contains(roles(),'support')"   /> 
	</Inferno>

  </div>
</template>

<script>

	import Inferno from '@/components/Inferno'
	import Minos from '@/components/Minos'
	import Support from '@/components/Support'
	import store from '@/store'

export default {
	name: 'Limbo',
	components: {
		Inferno,
		Minos,
		Support
	},
	methods:{	
		roles() {
			return JSON.stringify(store.state.cloak.tokenParsed.realm_access.roles)
		},
		contains(list,role){
			return list.includes(role)
		},
	}
}

</script>
