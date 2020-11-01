
<template>
	<div class="content Minos">

	<v-tabs
		fixed-tabs
		slider-color="red"
		dark>
		<v-tab>Open</v-tab>
		<v-tab>Inquiry</v-tab>
		<v-tab>Closed</v-tab>
		
		<v-tab-item
			v-for="item in items"
			:key="item.name" 
		>
			<TicketTable :items='item.data' :header='headers' />
		</v-tab-item>
		
	</v-tabs>
	<Modal />

	</div>
	


</template>

<script>

import Modal from '@/components/Modal'
import TicketTable from '@/components/TicketTable'
import store from '@/store'


export default {

	name: 'Minos',
	components: {
		Modal,
		TicketTable
	},
	computed: {
			items() {
				
			let tickets = store.state.tickets
			let open = tickets.filter(e => e.status == 'open')
			let inquiry = tickets.filter(e => e.status == 'inquiry')
			let closed = tickets.filter(e => e.status == 'closed')
			let ret = [
				{'name': 'open', 'data': open},
				{'name': 'inquiry', 'data': inquiry},
				{'name': 'closed', 'data' :closed}		
			]
			return ret
		}
	},
	data() {
		return {
			delDialog: false,
			headers:[
				{ text: 'Query', value: 'to' },
				{ text: 'Name', value: 'sender'},
				{ text: 'Subject', value: 'subject' },
				{ text: 'Status', value: 'status' },
				{text: 'Edit', align: 'center',sortable: false,value: 'id'}
			],	
		}
	},
}

</script>

<style scoped>
.content{
margin-top: 60px;
}

.Minos{
display: flex;
justify-content: center;

}

.table{
	margin-top:1em;
	margin-bottom:3em;
}


thead{
	background-color: #1E1E1E;
}


th{
	color:white !important;
}

td{
	justify-content:center;
}

</style>

