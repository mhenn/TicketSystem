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
	url: 'http://0.0.0.0:8080/auth', realm: 'Odonata', clientId: 'config-service', onLoad:'login-required'
}

Vue.config.productionTip = false

const admin = new KcAdminClient()
admin.baseUrl = 'http://localhost:8080/auth'
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
	store.commit('misc/updateRoles', await admin.roles.find())
}



blyn(admin)
let keycloak = Keycloak(initOptions);

keycloak.init({ onLoad: initOptions.onLoad }).success((auth) =>{
	store.commit('misc/setCloak', keycloak)
	store.commit('misc/selfUpdateUserRoles')
	console.log(store)	
	let roles = store.state.misc.userRoles
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

}).catch((e) => {
	console.log(e)
	console.log("Authentication Failed");
});
