<template>
	<div class="content Minos">
		<CustomTable v-bind:fields= "[
		{ Contact: 'Admin', Subject: 'Toast', Status: 'Open'},
		{ Contact: 'Admin', Subject: 'Toast', Status: 'Open'},
		{ Contact: 'Admin', Subject: 'Toast', Status: 'Open'},
		{ Contact: 'Admin', Subject: 'Toast', Status: 'Open'},
		{ Contact: 'Admin', Subject: 'Toast', Status: 'Open'},
		]" @showTicket="updateData"/>
	</div>
	
	<TicketForm v-if="show == 1" @showTicket="updateData"/>


</template>

<script>


import CustomTable from '@/components/CustomTable'
import TicketForm from '@/components/TicketForm'

export default {
	name: 'Minos',
	components: {
		CustomTable,
		TicketForm
	},
	data() {
		return {
			show: 0
		}
	},
	methods:{
		updateData (val){
			this.show = val
			console.log(val)
		}
	}
}

</script>

<style>
.content{
margin-top: 60px;
}

.Minos{
display: flex;
justify-content: center;

}
</style>

