import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import * as Keycloak from 'keycloak-js'
import store from './store'

let initOptions = {
  url: 'http://127.0.0.1:8000/auth', realm: 'Odonata', clientId: 'ticket-client', onLoad:'login-required'
}

Vue.config.productionTip = false

let keycloak = Keycloak(initOptions);

keycloak.init({ onLoad: initOptions.onLoad }).success((auth) =>{
    
    if(!auth) {
      window.location.reload();
    }

	new Vue({
      router,
      vuetify,
      store,
      render: h => h(App)
    }).$mount('#app')

	localStorage.setItem("vue-token", keycloak.token);
	localStorage.setItem("vue-refresh-token", keycloak.refreshToken);
})
