<template>
	<div class="content Minos">
	<v-data-table
		class="table"
		:headers="headers"
      :items="items"
      >
		
			<template v-slot:item.id="">
				<v-btn class="ma-2" outlined small fab  key="item.id" v-on:click="showForm">
					<v-icon>mdi-pencil</v-icon>
				</v-btn> 
      </template>
      
      </v-data-table>

	
	
		<TicketForm v-if="show == 1" @showTicket="updateData"/>
	</div>
	


</template>

<script>

import TicketForm from '@/components/TicketForm'

export default {
	name: 'Minos',
	components: {
		TicketForm
	},
	data() {
		return {
			show: 0,
		items: [
			{ id:'1', contact: 'Admin', subject: 'Toast', status: 'Open'},
			{ id:'2', contact: 'Admin', subject: 'Toast', status: 'Open'},
			{ id:'3', contact: 'Admin', subject: 'Toast', status: 'Open'},
			{ id:'4', contact: 'Admin', subject: 'Toast', status: 'Open'},
			{ id:'5', contact: 'Admin', subject: 'Toast', status: 'Open'},
			],
		headers:[
          {
            text: 'Edit',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: 'Contact', value: 'contact' },
          { text: 'Subject', value: 'subject' },
          { text: 'Status', value: 'status' },
        ],	
		}
	},
	methods:{
		showForm (){
			this.show = this.show ? 0 : 1
		},

		updateData (val){
			this.show = val
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

.table{
	margin-top:3em;
	margin-bottom:3em;
}


thead{
	background-color: rgb(74,5,0);
}

th{
	color:white !important;
}

td{
	justify-content:center;
}

</style>

