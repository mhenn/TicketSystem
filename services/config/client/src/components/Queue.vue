<template>
	<div>
		<div class='flex'>	
			<v-text-field v-model="queueName" label='New Entry' dense solo ></v-text-field>
			<v-btn @click='addItem' icon>
				<v-icon>mdi-plus</v-icon>
			</v-btn>
		</div>

		<v-list  class="thick">
			<v-item
				v-for="queue in queues"
				:key='queue.title'
			>
			<div class='flex'>
				<v-list-item-content >
					<v-list-item-title v-text='queue.title'></v-list-item-title>	
				</v-list-item-content>
					<v-btn @click='deleteItem(queue.id)' icon>
						<v-icon>mdi-trash-can-outline</v-icon>
					</v-btn>
			</div>
			</v-item>
		</v-list>
	</div>
</template>

<script>

import store from '@/store'

export default {
	name: 'QueueContent',
	computed: {
		queues(){
			return store.state.queues.queues
		}
	},
	data(){
		return{
			queueName: ''
		}
	},
	methods: {
		deleteItem(id){
			store.dispatch('queues/deleteQueue', id)		
		},
		addItem(){
			store.dispatch('queues/postQueue', this.queueName)	
		}
	},
	components: {
		store
	}
	
}

</script>

<style>
	.flex{
		display:flex;
	}

	.thick{
		width: 50vw;
	}
</style>
