<template>
	<div class="flex">
		<div>
			<v-select :items="items"
				v-model="sel"
				item-text="obj.name"
				item-disabled="obj.disabled"
				item-value="obj"
				multiple chips
			></v-select>
			<v-select v-model="updates" :items="updateSelection"
			multiple chips
			></v-select>

			<v-btn @click="submit">Submit</v-btn>
		</div>
				<v-divider class='space' vertical></v-divider>	
			
			<ListGroup title='Existing Mappings'>

				<v-list-group v-for="mapping in mail"
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

					<v-list v-for="child in mapping.actions"
						:key="child"
					>
						<v-list-item v-text="child"></v-list-item>
					</v-list>

				</v-list-group>
			</ListGroup>
	
	</div>
</template>

<script>

import store from '@/store'
import ListGroup from '@/components/ListGroup'
export default {
	name: 'Mail',
	computed: {
		mail(){
			let a = store.state.mail
			console.log('mail')
			console.log(a)
			return a
		},
		items(){
			let roles = store.state.roles
			let queues = store.state.queues			
			let items = [{obj:{name:'Roles', disabled: true}}]
			roles.forEach(role =>{
				items.push({obj:{name:role.name, mappingId: role.id, type: 'role'}})
			})

			items.push({obj:{name: 'Queues', disabled: true}})

			queues.forEach(queue =>{
				items.push({obj:{name:queue.title,mappingId:queue.id, type: 'queue'}})
			})				
			return items 
		},
		updateSelection(){
			return ['updated', 'created']
		}
	},
	data(){
		return{
			sel: [],
			updates: []
		}
	},
	methods: {
		submit(){
			this.sel.forEach(e =>{
				e['actions']= this.updates	
				store.dispatch('postMailMapping', e)
			})	
		
		},
		deleteMapping(id){
			console.log(id)
			store.dispatch('deleteMailMapping', id)
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

	.thick{
		width: 50vw;
	}
	.space{
		margin:1em;
	}
<
