<template>
	<div class="modal">
	<div v-on:click="close" class="close" ></div>
	<div class="form"></div>
	</div>
	


</template>

<script>



export default {
	name: 'TicketForm',
	data() {
		return {
			show: 0
		}
	},
	methods:{
		close(){
			this.$emit('showTicket', 0)
		},
	}
}

</script>

<style>

.modal{
	background-color: rgba(24, 26, 27, 0.6);
	position: fixed;
	top: 0;
	left: 0;
	height: 100vh;
	width: 100vw;
	background-color: rgba(0, 0, 0, .6);
	z-index: 999;
	overflow: auto;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
}

.close{
	position: fixed;
	top: 32px;
	top: 2rem;
	right: 32px;
	right: 2rem;
	height: 40px;
	height: 2.5rem;
	width: 40px;
	width: 2.5rem;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-pack: center;
	-ms-flex-pack: center;
	justify-content: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-transition: all 0.2s ease-in-out;
	transition: all 0.2s ease-in-out;
	border: 4px solid #fff;
    border-top-color: rgb(255, 255, 255);
    border-right-color: rgb(255, 255, 255);
    border-bottom-color: rgb(255, 255, 255);
    border-left-color: rgb(255, 255, 255);
	border-radius: 50%;
}

.close::before{
	position: absolute;
	content: "";
	height: 24px;
	height: 1.5rem;
	width: 4px;
	width: 0.25rem;
	background-color: #fff;
	transform: rotate(45deg);	
	transition: all 0.2s ease-in-out;
}

.close::after{
position: absolute;
	content: "";
	height: 24px;
	height: 1.5rem;
	width: 4px;
	width: 0.25rem;
	background-color: #fff;
	transition: all 0.2s ease-in-out;
	transform: rotate(-45deg);
}

.close:hover:before{
	transform: rotate(135deg);
}

.close:hover:after{
	transform: rotate(45deg);
}

.form{
	width: 60vw;
	height: 75vh;
	margin: 80px;
	margin: 5rem;
	background-color: #fff;
	display: -webkit-box;
	display: -ms-flexbox;
	display: flex;
	-webkit-box-orient: vertical;
	-webkit-box-direction: normal;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 48px 64px;
	padding: 3rem 4rem;
}
</style>

