<template>
	<div class="table">
		<table>
			<tr>
				<th>Contact</th>
				<th>Subject </th>
				<th>Status </th>
			</tr>
			<tr v-on:click="details" class="tdata"  v-for="field in fields" :key="field.Contact" >
				<td>{{ field.Contact }}</td>
				<td>{{ field.Subject }}</td>
				<td>{{ field.Status }}</td>
			</tr>
		</table>
	</div>
</template>

<script>


export default {
	name: 'CustomTable',
	props:{
		fields: Array,
	},
	methods:{
		details: function (e){	
			if(this.showTicket){
				this.showTicket = 0
			} else{
				this.showTicket = 1 
			}
			this.$emit('showTicket',this.showTicket)
		}
	}
}

</script>

<style scoped>

table{
	padding-bottom: 2em;
	font-family: "Roboto", sans-serif;
	text-transform: none;
	padding-top: 2em;
	color:#4a0500;
	width: 100%;
	border-spacing: 0;
	#border-collapse: collapse;
}

th{
	padding:0.5em;
	background-color: #4a0500;
	color:white;
}


.content{
margin-top: 60px;
}

.tdata{
	border-top: 1px solid;
}

.tdata:hover{
	background-color: #4a0500;
	color:white;
}
	


</style>
