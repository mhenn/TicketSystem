<template>
	<div class="content Minos">

		<div >	
			<v-btn class='swole' dark @click="switchDialog(null)">New Ticket</v-btn>
			<v-data-table
				class="table"
				:headers="headers"
				:items="items"
				>
					<template v-slot:item.id="{item}" >
						<v-btn class="ma-2" outlined small fab  key="item.id" @click="switchDialog(item.id)">
							<v-icon>mdi-pencil</v-icon>
						</v-btn> 		
						<v-btn class="ma-2" outlined small fab  key="item.id + 1" @click="deleteDialog(item.id)">
							<v-icon>mdi-trash-can-outline</v-icon>
						</v-btn> 		
					</template>
				</v-data-table>	
		</div>
		<Modal/>

		<v-dialog
      v-model="delDialog"
      max-width="290"
    >
      <v-card>
        <v-card-title class="headline">Eintrag entfernen?</v-card-title>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="green darken-1"
            text
            @click="delDialog = false"
          >
            Nein
          </v-btn>

          <v-btn
            color="green darken-1"
            text
            @click="deleteTicket"
          >
            Ja
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


	</div>
	


</template>

<script>

import Modal from './Modal.vue'
import store from '@/store'

export default {

	name: 'Minos',
	components: {
		Modal
	},
	computed: {
		items() {
			return store.state.ticket.tickets
		}
	},
	data() {
		return {
		delDialog: false,
		headers:[
          { text: 'To', value: 'to' },
          { text: 'Subject', value: 'subject' },
          { text: 'Status', value: 'status' },
          {text: 'Edit', align: 'center',sortable: false,value: 'id'}
        ],	
		}
	},
	methods:{
		showDialog (){
			console.log(this)
		},
		updateData (val){
			this.show = val
		},
		deleteDialog(id){
			this.delDialog = true
			store.commit('ticket/changeSelectedTicket',  id)
		},
		deleteTicket(){
			store.dispatch('ticket/deleteSelected')
			this.delDialog = false
		},
		switchDialog(id){
			store.commit('misc/switch')
			store.commit('ticket/changeSelectedTicket',id)
		},
		
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
	margin-top:1em;
	margin-bottom:3em;
}

.swole{
	width: 100%;
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

