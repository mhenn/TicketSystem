<template>
	<v-container fluid class="modal">
		<div v-on:click="close" class="close" ></div>
		<v-sheet class="form pa-12">
		<v-row>
		<v-col
			cols="12"	
			md="4"
			>
			<v-form>
		    <v-textarea
      label="Message"
    ></v-textarea>
		</v-form>
		</v-col>
		</v-row>
		</v-sheet>
	</v-container>
	


</template>

<script>

	import { required, max } from 'vee-validate/dist/rules'
	import { extend,  ValidationProvider  } from 'vee-validate'
	import FileDrop from '@/components/FileDrop'	
	
	extend('required', {
		...required,
		message: '{_field_} can not be empty',
	})
  extend('max', {
    ...max,
    message: '{_field_} may not be greater than {length} characters',
  })

export default {
	name: 'TicketForm',
	data: () => ({


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
	margin: 80px;
	margin: 5rem;
	background-color: #fff;
	padding: 48px 64px;
	padding: 3rem 4rem;
}
</style>

