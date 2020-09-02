<template>
  <div class="limbo">

	<Inferno>
		<Minos/>
	</Inferno>

  </div>
</template>

<script>

	import Inferno from '@/components/Inferno'
	import Minos from '@/components/Minos'

export default {
	name: 'Limbo',
	components: {
		Inferno,
		Minos
	}
}

</script>
