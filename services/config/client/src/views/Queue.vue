<template>
	<Inferno>
		<QueueContent/>
	</Inferno>
</template>

<script>
	import Inferno from '@/components/Inferno'
	import QueueContent from '@/components/Queue'
export default {
	name: 'Queue',
	components: {
		QueueContent,
		Inferno
	}
}

</script>
