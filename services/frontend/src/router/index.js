import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
	{
		path: '/',
		name: 'EnterHell',
		component: () => import( '../views/GateOfHell.vue')
	},
	{
		path: '/Home',
		name: 'Limbo',
		component: () => import( '../views/Limbo.vue')
	},
	{
		path: '/about',
		name: 'About',
		component: () => import( '../views/About.vue')
	}
]

const router = createRouter({
history: createWebHashHistory(),
routes
})

export default router
