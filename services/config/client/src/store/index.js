import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import queues from './modules/queues'
import mapping from './modules/mapping'
import mail from './modules/mail'
import misc from './modules/misc'

Vue.use(Vuex)

export default new Vuex.Store({
	modules:{
		queues,
		mapping,
		mail,
		misc
	},
})
