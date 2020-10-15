import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
   {
      path: '/',
      name: 'Limbo',
      component: () => import( '../views/Queue.vue')
	},

	{
      path: '/queue',
      name: 'Queue',
      component: () => import( '../views/Queue.vue')
	},
	{
      path: '/roles',
      name: 'Roles',
      component: () => import( '../views/Roles.vue')
	},
	{
      path: '/mail',
      name: 'Queue',
      component: () => import( '../views/Mail.vue')
	},
	{
      path: '/config',
      name: 'Configuration',
      component: () => import( '../views/Config.vue')
	}



]



const router = new VueRouter({
  routes
})

export default router
