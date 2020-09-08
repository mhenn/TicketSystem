<template>
  <v-row  justify="center">
    <v-dialog  v-model="dialog" persistent max-width="600px">
            <v-card >
        <v-card-title>
          <span class="headline">User Profile</span>
        </v-card-title>
        <v-card-text>
          <v-container class="swole">
            <v-row>
              <v-col cols="12"  md="4">
							<v-select 
					:items="items"
					label="Contact"
					dense
					solo
					/>
			<ValidationProvider v-slot="{ errors }" name="Subject" rules="required|max:50">
        <v-text-field
			solo
          v-model="subject"
          :counter="50"
          :error-messages="errors"
          label="Betreff"
          required
        ></v-text-field>
			</ValidationProvider>

              </v-col>
              <v-col cols="12">
			
			<ValidationProvider v-slot="{ errors }" name="Message" rules="required">
					<v-textarea
      label="Message"
		v-model="message"
		:auto-grow="true"
		:solo="true"
		:error-messages="errors"
		required
    ></v-textarea>
		</ValidationProvider>	
			<FileDrop/>
              </v-col>
            </v-row>
          </v-container>
          <small>*indicates required field</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="grey darken-1" text @click="switchDialog">Close</v-btn>
          <v-btn color="grey darken-1" text @click="switchDialog">Send</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>


	import { required, max } from 'vee-validate/dist/rules'
	import { extend,  ValidationProvider  } from 'vee-validate'
	import FileDrop from '@/components/FileDrop'	
	import store from '@/store'	


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
			dialog(){
				return store.state.dialog
			}
		},
		data: () => ({
			subject: '',
			show: 0,
			items : [{name:'Foo', text:'Foo'}, {name:'Bar', text:'Bar'}],
		}),
	
	methods:{
		close(){
			this.$emit('showTicket', 0)
		},
		switchDialog(){
			store.commit('switch')
		}
	},
	components:{
		ValidationProvider,
		FileDrop
	}
}
</script>


<style scoped>

.swole{
	max-width:80vw !important;
}

</style>
