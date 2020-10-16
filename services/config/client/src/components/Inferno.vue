<template>
	<v-app :dark='this.$vuetify.theme.dark = false'>
		<v-navigation-drawer 
			dark
			v-model="drawer"
			app
			clipped
		>
      <v-list dense >
			<NavbarItem linkto="/queue" title="Queues">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
			<NavbarItem linkto="/roles" title="Roles">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
			<NavbarItem linkto="/mail" title="Mail">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
			<NavbarItem linkto="/config" title="Main Config">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
      </v-list>
		</v-navigation-drawer>
		<v-app-bar
			dark
			app
			clipped-left
		>
		<v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
			<v-toolbar-title>Odonata</v-toolbar-title>
		</v-app-bar>
		<v-container class="content" fluid>
			<v-row dense>
				<v-col
					v-for="card in cards"
					:key="card.title"
					:cols="card.flex"
				>
					<v-card class="flex">
					<slot></slot>

					</v-card>
				</v-col>
			</v-row>
		</v-container>
	</v-app>
</template>


<script>
	//import Footer from '@/components/Footer'
	import NavbarItem from '@/components/NavbarItem'

	export default {
		name: "Inferno",
		components: {
			NavbarItem
	//		Footer
		},
		data: () =>({
			cards:[{title:'test'}],
			drawer: null
		}),
		created() {
		this.$vuetify.theme.dark=false
		}
	}


</script>

<style>

.content{
	margin-top:60px;
}

.flex{
	display:flex;
	justify-content:center;
}
</style>
