<template>
	<div class="Footer">
		<div class="flex">
			<router-link class="ferryman" to="/legal" >Impressum</router-link> 
			<router-link class="ferryman" to="/privacy" >Datenschutz</router-link> 
		</div>
	
	</div>
</template>

<script>

export default {
  name: 'Footer',
}

</script>

<style scoped>
	
.Footer{
	display:flex;
	background-color: rgb(72,5,0);
	height: 60px;
	left: 0;
	width: 100%;
	position: fixed;
	align-items:center;
	justify-content:center;
}

a{
	position: relative;
	padding-bottom: 2px;
	font-weight: 700;
	font-family: "Roboto", sans-serif;
	text-transform: none;
	color: #fff;
	text-decoration: none;
	-webkit-transition: all 0.2s ease-in-out;
	transition: all 0.2s ease-in-out;
	margin-left:2em;
}

a:after{
	content: "";
	position: absolute;
	right: 0;
	bottom: 0;
	left: 0;
	background-color: #fff;
	-webkit-transform: scaleX(0);
	transform: scaleX(0);
	height: 2px;
	-webkit-transition: all 0.2s ease-in-out;
	transition: all 0.2s ease-in-out;
}

a:hover:after{
	transform: scaleX(1);
	background-color: red;
}

</style>
