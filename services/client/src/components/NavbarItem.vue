<template>
<v-list-item link :to='linkto'>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ title }}</v-list-item-title> 
			</v-list-item-content>
        </v-list-item>

</template>


<script>

	export default {
		name: "NavbarItem",
		props: {
			title: String,
			linkto: String
		}
	}



</script>
