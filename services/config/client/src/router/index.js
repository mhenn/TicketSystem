import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
   {
      path: '/',
      name: 'Limbo',
      component: () => import( '../views/Limbo.vue')
	}
]



const router = new VueRouter({
  routes
})

export default router
