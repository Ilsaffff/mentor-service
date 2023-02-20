import Vue from 'vue'
import VueRouter from 'vue-router'
import Registration from "@/components/pages/Registration.vue";

Vue.use(VueRouter)

// const routes = [
//   {
//     path: '/',
//     name: 'Registration',
//     component: Registration
//   },
//   {
//     path: '/about',
//     name: 'about',
//     // route level code-splitting
//     // this generates a separate chunk (about.[hash].js) for this route
//     // which is lazy-loaded when the route is visited.
//     component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
//   }
// ]
//
// const router = new VueRouter({
//   mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })
//
// export default router

export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'registration',
      component: Registration
    },
  ]
})
