<template>


	<v-app :dark="this.$vuetify.theme.dark = false">
		<v-navigation-drawer dark
			v-model="drawer"
			app
			clipped
		>
      <v-list dense>
			<NavbarItem v-if="!contains(roles,'Support')" linkto="/" title="Dashboard">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
			<NavbarItem v-if="contains(roles,'Support')" linkto="/" title="Support Dashboard">
            <v-icon>mdi-view-dashboard</v-icon>
			</NavbarItem>
			<v-list-item @click='settings()'> 
				<v-list-item-action>
					<v-icon>mdi-tools</v-icon>
				</v-list-item-action>
				<v-list-item-content>
					<v-list-item-title>Settings</v-list-item-title> 
				</v-list-item-content>
			</v-list-item>
			<NavbarItem linkto="/legal" title="Impressum">
            <v-icon>mdi-briefcase</v-icon>
			</NavbarItem>
			<NavbarItem linkto="/privacy" title="Datenschutz">
            <v-icon>mdi-security</v-icon>
			</NavbarItem>


      </v-list>
		</v-navigation-drawer>

		<v-app-bar dark
			app
			clipped-left
		>
			<v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
			<v-toolbar-title>Odonata</v-toolbar-title>
			<v-spacer></v-spacer>
			<v-btn @click="logout" icon>
				<v-icon>mdi-logout-variant</v-icon>
			</v-btn>
		</v-app-bar>
		<v-container class="content" fluid>

		<v-alert
			v-if='show'
			prominent
			dismissible
			type='error'
			@click='clear()'
			>
			Your client is experiencing issues due to the failure of the following function(s): {{ failed }}
		</v-alert>




			<v-row  dense>
				<v-col
					v-for="card in cards"
					:key="card.title"
					:cols="card.flex"
				>
					<v-card   class="flex">
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
	import store from '@/store'
	export default {
		name: "Inferno",
		components: {
			NavbarItem
	//		Footer
		},
		computed:{
			roles() {
				return store.state.config.userRoles
			},
			failed(){
				return store.state.misc.failed
			},
			show(){
				return this.failed.length != 0 
			}
		},
		data: () =>({
			cards:[{title:'test'}],
			drawer: null
		}),
		created() {
			this.$vuetify.theme.dark=false
		},
		methods:{
			settings(){
				store.state.config.cloak.accountManagement()
			},
			contains(list,role){
				return list.includes(role)
			},
			logout(){
				store.dispatch('config/logout')
			},
			clear(){
				store.commit('misc/clearFail')
			}
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
