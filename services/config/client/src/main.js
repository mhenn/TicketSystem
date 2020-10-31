import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import * as Keycloak from 'keycloak-js'
import store from './store'
import Unauthorized from './Unauthorized.vue'

import KcAdminClient from 'keycloak-admin'

const config_role = 'config_admin'

let initOptions = {
	url: 'http://127.0.0.1:8000/auth', realm: 'Odonata', clientId: 'config-service', onLoad:'login-required'
}

Vue.config.productionTip = false

const admin = new KcAdminClient()
admin.baseUrl = 'http://localhost:8000/auth'
admin.realmName = 'Odonata'
async function blyn(admin){

		

	await admin.auth(
		{
			username: 'oadmin',
			password: 'oadmin',
			grantType: 'password',
			clientId: 'config-service'	
		} 
	)
	store.commit('updateRoles', await admin.roles.find())
	console.log(admin)
}




blyn(admin)
let keycloak = Keycloak(initOptions);

keycloak.init({ onLoad: initOptions.onLoad }).success((auth) =>{
	store.commit('setCloak', keycloak)
	store.commit('selfUpdateUserRoles')
	
	let roles = store.state.userRoles
	console.log(roles)

	if(!auth) {
		window.location.reload();
	}

	if( roles.includes(config_role)){
		new Vue({
			router,
			vuetify,
			store,
			render: h => h(App)
		}).$mount('#app')

	}else{
		new Vue({
			vuetify,
			store,
			render: h => h(Unauthorized)
		}).$mount('#app')
	}
	localStorage.setItem("vue-refresh-token", keycloak.refreshToken);


	setInterval(() => {
		keycloak.updateToken(70).then((refreshed) => {
			if (refreshed) {
				console.log('Token refreshed' + refreshed);
			}
	
		}).catch(() => {
			console.log('Failed to refresh token');
		});
	}, 6000)

}).catch(() => {
	console.log("Authenticated Failed");
});
