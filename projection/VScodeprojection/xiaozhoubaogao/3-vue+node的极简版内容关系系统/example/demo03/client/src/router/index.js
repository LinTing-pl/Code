import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "../views/Home"


Vue.use(VueRouter)

const routes = [
  {
    path:"/",
    name:"Home",
    component: Home
  },
]

const router = new VueRouter({
  // mode: 'history',   //模式  history hash ，
  base: process.env.BASE_URL, //定义一个基础URL，用的是vue-cli默认的配置项。
  routes  //配置项
})

export default router
