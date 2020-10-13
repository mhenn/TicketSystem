<template>
	<Inferno>
      <v-row>
         <v-col cols="9"  md="4" align-self="center">
				The user settings are administrated via keycloak:
			</v-col>
			<v-col cols="12" md="4">
				<v-btn @click="open" dense solo>Open</v-btn>
			</v-col>
		</v-row>
	</Inferno>
</template>

<script>

import Inferno from '@/components/Inferno'

export default {
	name: 'Settings',
	components: {
		Inferno
	},
	methods: {
		open(){
			window.open("http://localhost:8000/auth/realms/Odonata/account")
		}	
	}	
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
