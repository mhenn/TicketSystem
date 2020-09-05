<template>
	<div class="nav">
		<router-link class="ferryman" to="/" >Home</router-link> 
		<router-link class="ferryman" to="/settings" >Settings</router-link>
	</div>
</template>

<script>

export default {
  name: 'Navbar',
}

</script>

<style scoped>

.nav{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    margin: 0;
    height: 60px;
    z-index: 99;
    background-color: rgb(72, 5, 0);
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
}


h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
	position: relative;
	padding-bottom: 2px;
	font-weight: 700;
	font-family: "Roboto", sans-serif;
	text-transform: none;
	color: #fff;
	text-decoration: none;
	-webkit-transition: all 0.2s ease-in-out;
	transition: all 0.2s ease-in-out;
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
