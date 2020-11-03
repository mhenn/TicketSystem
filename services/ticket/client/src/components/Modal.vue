<template>
  <v-row  justify="center">
    <v-dialog   v-model="dialog" persistent max-width="600px">
            <v-card >
		<ValidationObserver ref="form"> 
			<form @submit.prevent='onSubmit'>
			<v-card-text>
          <v-container class="swole">
            <v-row>
              <v-col cols="12"  >
			<ValidationSelect :readonly="!emptyTicket" rules="required" v-model='to' :items="selection" label="Contact"/> 
			<ValidationTextfield :readonly="!emptyTicket" rules="required|max:50" v-model="subject" label="Subject"/>
			<ValidationSelect :readonly="state == 'closed'" v-if="contains(roles(),'Support')" rules="required" v-model='state' :items="stateSelection" label="State"/> 
              </v-col>
              <v-col cols="12" >
			<ValidationTextarea rules="required" v-model="content" label="Message"/>
		<Upload />			

<v-list v-if="!emptyTicket" >
      <v-list-group
        v-for="item in messages"
        :key="item.timestamp"
        v-model="item.active"
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.timestamp"></v-list-item-title>
          </v-list-item-content>
        </template>
			<v-list-item-content> 
				<v-textarea
		readonly
      label="Message"
		:solo="true"
		:value="item.message"
    ></v-textarea>

	<v-list>
		<v-list-group  
		v-for="file in item['appendices']"
		:key='file'>
			<template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title >Appendices</v-list-item-title>
          </v-list-item-content>
        </template>

			<v-btn @click='download(file, item.timestamp)'>{{ file }}</v-btn>
		</v-list-group>
	
	</v-list>


			</v-list-item-content>
      </v-list-group>
    </v-list>


              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" text @click="clear">Clear</v-btn>
			<v-spacer></v-spacer>
			<v-spacer></v-spacer>
          <v-btn color="grey darken-1" text @click="switchDialog">Close</v-btn>
          <v-btn v-if='!newTicket' color="grey darken-1" text type='submit'>Submit</v-btn>
          <v-btn v-if='newTicket && state != "closed"' color="grey darken-1" text @click="updateTicket">Update</v-btn>
        </v-card-actions>

		</form>
		</ValidationObserver>
      </v-card>
		
    </v-dialog>
  </v-row>
</template>

<script>


	import { required, max } from 'vee-validate/dist/rules'
	import { extend, ValidationObserver  } from 'vee-validate'
	import store from '@/store'	
	import ValidationSelect from './inputs/ValidationSelect'
	import ValidationTextfield from  './inputs/ValidationTextfield'
	import ValidationTextarea from  './inputs/ValidationTextarea'
//	import axios from 'axios'
	import Upload from '@/components/FileUpload'
	extend('required', {
		...required,
		message: '{_field_} can not be empty',
	})
  extend('max', {
		...max,
		message: '{_field_} may not be greater than {length} characters',
  })

  export default {
		name: "Modal",
		computed: {
			selection(){
				let queue = store.state.queues
				var queues = []
				queue.forEach(item =>{
					queues.push({'name' : item.title, 'text': item.title, 'id': item.id})
				})
				return queues
			},
			emptyTicket(){
				return store.state.emptyTicket
			},
			newTicket(){
				return store.state.selectedTicket.id
			},
			dialog(){
				return store.state.dialog
			},

		to:{
				get(){
					return store.state.selectedTicket.to
				},
				set(value){
				store.commit('updateTicketData', ['to', value])}
			},
		state:{
			get(){
				return store.state.selectedTicket.status
			},
			set(value){
				store.commit('updateTicketData', ['status', value])
			}
		},
		subject:{
				get(){
					return store.state.selectedTicket.subject
				},
				set(value){ store.commit('updateTicketData', ['subject', value])}
			},

		content:{
				get(){
					return store.state.selectedTicket.content
				},
				set(value){store.commit('updateTicketData', ['content', value])}
			},
		messages(){
			return store.state.selectedTicket.messages
		},
			picket(){return store.state.selectedTicket}
		},
		data: () => ({
			files: null,
			stateSelection: ['open', 'inquiry', 'closed'],
			items:[
				{
					actions: 'mdi-ticket',
					content:  'List Item',
					title: 'Atrats'
				}
			],
			message: '',
			show: 0,
		}),
	
methods:{
		roles() {
			return store.state.userRoles 
		},
		contains(list,role){
			return list.includes(role)
		},
		async clear(){
				this.to = ''
				this.subject = ''
				this.content = ''
				store.commit('clearFiles')
				requestAnimationFrame(() => {
				this.$refs.form.reset();
			});
		},
		onSubmit(){
			this.$refs.form.validate().then(e =>{
				if( e ){
					this.addTicket()
				}
			})
		},
		download(file, messageId){
			store.dispatch('downloadFile', [file, messageId])

		},
		onFileChange(event){
			this.files = event.target.files[0]
		},
		switchDialog(){
			store.commit('switch')
		},
		addTicket(){
			store.dispatch('postSelected')
			store.commit('switch')
		},
		updateTicket(){
			store.dispatch('putSelected')
			store.commit('switch')
		}
	},
	components:{
		ValidationObserver,
		ValidationSelect,
		ValidationTextfield,
		ValidationTextarea,
		Upload
	}
}
</script>


<style scoped>

.v-textarea textarea[readonly="readonly"] {
    background-color: #f0f0f0;
    color: gray;
}
.v-text-field--solo input[readonly="readonly"] {
    background-color: yellowgreen
}

.swole{
	max-width:80vw !important;
}

</style>
