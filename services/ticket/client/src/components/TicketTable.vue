<template>
	<v-data-table
		class="table"
		:headers="header"
		:items="items"
		>
			<template v-slot:item.id="{item}" >
				<v-btn class="ma-2" outlined small fab  key="item.id" @click="switchDialog(item.id)">
					<v-icon>mdi-pencil</v-icon>
				</v-btn> 		
			</template>
		</v-data-table>	
</template>

<script>
import store from '@/store'

export default {

	name: 'TicketTable',
	props: {
		items: Array,
		header: Array,
	},
	data() {
		return {
			delDialog: false,
		}
	},
	methods:{
		switchDialog(id){
			store.commit('switch')
			store.commit('changeSelectedTicket',id)
		},
	}
}

</script>

<style scoped>

</style>
