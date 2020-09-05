<template>
	<v-app class="Inferno">
		<Navbar/>
		<div class="content">
		<slot></slot>
		</div>
		<Footer/>
	</v-app>

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

<style>

.content{
	margin-top:60px;

}
</style>
