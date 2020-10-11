<template>
  <v-row  justify="center">
    <v-dialog   v-model="dialog" persistent max-width="600px">
            <v-card >
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container class="swole">
            <v-row>
              <v-col cols="12"  md="4">
							<v-select :readonly="!emptyTicket"
					v-model="to"
					:items="selection"
					label="Contact"
					dense
					solo
					/>

		<ValidationProvider v-slot="{ errors, valid }" name="subject" rules="required|max:50">
        <v-text-field  :readonly="!emptyTicket"
			solo
          v-model="subject"
          :counter="50"
          :error-messages="errors"
				:success="valid"
          label="Betreff"
          required
        ></v-text-field>
			</ValidationProvider>

              </v-col>
              <v-col cols="12">
			
			<ValidationProvider v-slot="{ errors }" name="Message" rules="required">
					<v-textarea
      label="Message"
		v-model="content"
		:auto-grow="true"
		:solo="true"
		:error-messages="errors"
		required
    ></v-textarea>

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


		</ValidationProvider>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" text @click="switchDialog">Close</v-btn>
          <v-btn v-if='!newTicket' color="grey darken-1" text @click="addTicket">Send</v-btn>
          <v-btn v-if='newTicket' color="grey darken-1" text @click="updateTicket">Update</v-btn>
        </v-card-actions>
      </v-card>
		
    </v-dialog>
  </v-row>
</template>

<script>


	import { required, max } from 'vee-validate/dist/rules'
	import { extend,  ValidationProvider  } from 'vee-validate'
	import store from '@/store'	
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
				this.$validator.clean() 
				store.commit('updateTicketData', ['to', value])}
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
			items:[
				{
					actions: 'mdi-ticket',
					content:  'List Item',
					title: 'Atrats'
				}
			],
			message: '',
			show: 0,
			selection : [{name:'Foo', text:'Foo'}, {name:'Bar', text:'Bar'}],
		}),
	
	methods:{
		download(file, messageId){
			console.log(file)
			console.log(messageId)
			store.dispatch('downloadFile', [file, messageId])

		},
		onFileChange(event){
			this.files = event.target.files[0]
			console.log(this.files)
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
		ValidationProvider,
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
