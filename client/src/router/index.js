import Vue from 'vue';
import VueRouter from 'vue-router';
// import { Store } from 'vuex';
import store from '@/store/index.js'; 
import Home from '../views/Home.vue';
import Missing from '../views/Missing.vue';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/sign_up',
    name: 'signup',
    component: () => import('../views/SignUp.vue')
  },
  {
    path: '/set_up',
    name: 'setup',
    component: () => import('../views/Setup.vue'),
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag == false) {
        next('/login')
      }else {
        next()
      }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.common.loginFlag == false) {
        next('/login')
      }else {
        next()
      }
    }
  },
  {
    path: '/text_analysis',
    name: 'TextAnalysis',
    component: () => import('../views/TextAnalysis.vue'),
    // beforeRouteUpdate: (to, from, next) => {
    beforeEnter: (to, from, next) => {
      if (store.state.common.loginFlag == false) {
        next('/login')
      }else {
        next()
        //to({ path: '/text_analysis' })
        //next({ name: 'TextAnalysis' })
      }
    }
  },
  {
    path: '*',
    component: Missing
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
