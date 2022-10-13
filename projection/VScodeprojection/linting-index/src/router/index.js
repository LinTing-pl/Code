import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home";
import Index from "../components/Index";
import Study from "../components/Study";
import Blog from "../components/Blog";
import Video from "../components/Video";
import Load from "../components/Load";

Vue.use(VueRouter);

const routes = [
  { path: "/", redirect: "/home" },
  {
    path: "/home",
    name: "home",
    component: Home,
    redirect: "/index",
    children: [
      {
        path: "/index",
        name: "index",
        component: Index,
      },
      {
        path: "/study",
        name: "study",
        component: Study,
      },
      {
        path: "/blog",
        name: "blog",
        component: Blog,
      },
      {
        path: "/video",
        name: "video",
        component: Video,
      },
      {
        path: "/load",
        name: "load",
        component: Load,
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
