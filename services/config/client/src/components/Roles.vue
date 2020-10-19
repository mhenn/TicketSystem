<template>
	<div>
		<v-card-title center>Role <> Queue Mapping</v-card-title>
		<div class='flex'>	
			<div class="col--flex">
				<div class='flex'>	
					<v-card>
						<v-list>
							<v-list-item
								v-for="role in roles"
								:key="role.name"
							>
								<v-list-item-content>
									<v-checkbox
										v-model="selectedRole"
										:label="role.name"
										:value="role.name"
									></v-checkbox>	
								</v-list-item-content>
							</v-list-item>
						</v-list>

					</v-card>

					<v-card>
						<v-list>
							<v-list-item
								v-for="queue in queues"
								:key="queue.title"
							>
								<v-list-item-content>
									<v-checkbox
										v-model="selectedQueue"
										:label="queue.title"
										:value="queue.title"
									></v-checkbox>	
								</v-list-item-content>
							</v-list-item>
						</v-list>
					</v-card>	
				</div>
				<v-btn @click="submitMapping">Submit</v-btn>
			</div>

			<v-divider class='space' vertical></v-divider>	
			<ListGroup title='Existing Mappings'>
				<v-treeview></v-treeview>
			</ListGroup>
		</div>
	</div>
</template>

<script>

import store from '@/store'
import ListGroup from '@/components/ListGroup'


export default {
	name: 'QueueContent',
	computed: {
		queues(){
			return store.state.queues
		},
		roles(){
			return store.state.roles
		}
	},
	data(){
		return{
			queueName: '',
			selectedQueue: [],
			selectedRole: [],
		}
	},
	methods: {
		submitMapping(){
			console.log(this.selectedQueue)
			console.log(this.selectedRole)
		},
		deleteItem(id){
			store.dispatch('deleteQueue', id)		
		},
		addItem(){
			store.dispatch('postQueue', this.queueName)	
		}
	},
	components: {
		store,
		ListGroup
	}
	
}

</script>

<style scoped>
	.flex{
		display:flex;
	}
	.col--flex{
		display: flex;
		flex-direction: column;
	}

	.v-messages{
		display:none;
	}
	.v-card{
		margin: 1em;
	}
	.space{
		margin:1em;
	}

</style>
