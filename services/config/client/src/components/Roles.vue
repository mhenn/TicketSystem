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
										:value="role"
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

				<v-list-group v-for="mapping in mappings"
					:key="mapping.id"
				>
					<template v-slot:activator>
						<div class="flex">
							<v-list-item-title v-text="mapping.name"> </v-list-item-title>
							<v-btn @click="deleteMapping(mapping.id)" icon>
								<v-icon>mdi-trash-can-outline</v-icon>
							</v-btn>
						</div>
					</template>

					<v-list v-for="child in mapping.children"
						:key="child"
					>
						<v-list-item v-text="child"></v-list-item>
					</v-list>

				</v-list-group>
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
			return store.state.queues.queues
		},
		roles(){
			return store.state.roles
		},
		mappings(){
			return store.state.mapping.mapping
		},
	},
	data(){
		return{
			queueName: '',
			selectedQueue: [],
			selectedRole: [],
		}
	},
	methods: {
		deleteMapping(id){
			store.dispatch('mapping/deleteMapping', id)
		},
		submitMapping(){
			this.selectedRole.forEach((role) => {	
					let mapping = {'id': role.id, 'name': role.name, 'children': this.selectedQueue}
					store.dispatch('mapping/postMapping',mapping)
			})
		},
		deleteItem(id){
			store.dispatch('queues/deleteQueue', id)		
		},
		addItem(){
			store.dispatch('queues/postQueue', this.queueName)	
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
