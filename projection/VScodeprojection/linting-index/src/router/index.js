import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  { path: "/", redirect: "/home" },
  {
    path: "/login",
    name: "login",
    component: () => import("../components/Login.vue"),
  },
  {
    path: "/home",
    name: "home",
    component: () => import("../components/Home"),
    redirect: "/index",
    children: [
      {
        path: "/index",
        name: "index",
        component: () => import("../components/Index"),
      },
      {
        path: "/study",
        name: "study",
        component: () => import("../components/Study"),
      },
      {
        path: "/blog",
        name: "blog",
        component: () => import("../components/Blog"),
      },
      {
        path: "/video",
        name: "video",
        component: () => import("../components/Video"),
      },
      {
        path: "/load",
        name: "load",
        component: () => import("../components/Load"),
      },
      {
        path: "/search",
        name: "search",
        component: () => import("../components/Search.vue"),
      },
    ],
  },
  {
    path: "/details",
    name: "details",
    component: () => import("../components/Details.vue"),
    children: [
      {
        path: "/studycontent/:id",
        name: "studycontent",
        component: () => import("../components/StudyContent.vue"),
      },
      {
        path: "/blogcontent/:id",
        name: "blogcontent",
        component: () => import("../components/BlogContent.vue"),
      },
      {
        path: "/videocontent/:id",
        name: "videocontent",
        component: () => import("../components/VideoContent.vue"),
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
