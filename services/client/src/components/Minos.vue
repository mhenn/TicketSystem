<template>
	<div class="content Minos">
	<v-data-table
		class="table"
		:headers="headers"
      :items="items"
      >
			<template v-slot:item.id >
				<v-btn class="ma-2" outlined small fab  key="item.id" @click="switchDialog">
					<v-icon>mdi-pencil</v-icon>
				</v-btn> 		
			</template>
      
      </v-data-table>

	
		<Modal/>
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
			return store.state.tickets
		}
	},
	data() {
		return {
		headers:[
          {
            text: 'Edit',
            align: 'start',
            sortable: false,
            value: 'id',
          },
          { text: 'To', value: 'to' },
          { text: 'Subject', value: 'subject' },
          { text: 'Status', value: 'status' },
        ],	
		}
	},
	methods:{
		showDialog (){
			console.log(this)
		},
		showForm (){
			this.show = this.show ? 0 : 1
		},

		updateData (val){
			this.show = val
		},
		switchDialog(){
			store.commit('switch')
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

