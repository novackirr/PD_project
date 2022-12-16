import { createRouter, createWebHistory } from 'vue-router'
import Main from '@/views/Main.vue'
import Info from '@/views/Info.vue'
import Account from '@/views/Account.vue'
import LogIn from '@/views/LogIn.vue'
import Register from '@/views/Register.vue'
import VerifyEmail from '@/views/VerifyEmail.vue'
import Generate from '@/views/Generate.vue'
import StudentsDo from '@/views/StudentsDo.vue'
import store from "@/store"

const routes = [
  {
    path: '/',
    name: 'home',
    component: Main
  },
  {
    path: '/info',
    name: 'info',
    component: Info
  },
  {
    path: '/account',
    name: 'account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: LogIn
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/generate',
    name: 'generate',
    component: Generate,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/studentsdo',
    name: 'studentsdo',
    component: StudentsDo,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/verifyemail/',
    name: 'verifyemail',
    component: VerifyEmail
  },
  {
    path: '/verifyemail/:uid/',
    name: 'verifyemail',
    component: VerifyEmail
  },
  {
    path: '/verifyemail/:uid/:token',
    name: 'verifyemail',
    component: VerifyEmail
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/login')
  } else {
    next()
  }
})

export default router
