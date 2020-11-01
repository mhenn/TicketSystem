<template>
  <div class="limbo">

	<Inferno>
		<Minos v-if="!contains(roles(),'Support')"   /> 
		<Support v-if="contains(roles(),'Support')"   /> 
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
			return store.state.userRoles 
		},
		contains(list,role){
			return list.includes(role)
		},
	}
}

</script>
