<template>
	<div class="Inferno">
		<Navbar/>
		<h1>{{ msg }}</h1>
		<slot></slot>
		<Footer/>
	</div>

</template>


<script>
	import Navbar from '@/components/Navbar'
	import Footer from '@/components/Footer'


	export default {
		name: "Inferno",
		components: {
			Navbar,
			Footer
		}
	}


</script>
