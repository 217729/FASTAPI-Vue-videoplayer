import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Player from '../views/Player.vue'
import Admin from '../views/Admin.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name:'Login',
      component:Login,
    },
    {
      path: '/Player',
      name: 'Player',
      component: Player
    },
    {
      path: '/Register',
      name: 'Register',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/Register.vue')
    },
    {
      path:'/Admin',
      name:'Admin',
      component:Admin
    }
  ]
})

export default router
