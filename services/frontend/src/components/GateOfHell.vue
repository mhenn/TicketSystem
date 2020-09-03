<template>
	<div class="Entry">
		<h1>{{ msg }}</h1>
		<router-link to="/Home">{{ btnmsg }}</router-link> 
	</div>
</template>

<script>
export default {
	name: 'GateOfHell',
	props:{
		msg: String,
		btnmsg: String
	}
}
</script>
