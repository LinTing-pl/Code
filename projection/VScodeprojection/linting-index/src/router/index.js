import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../components/Home";
import Index from "../components/Index";
import Study from "../components/Study";
import Blog from "../components/Blog";
import Video from "../components/Video";
import Load from "../components/Load";
import Details from "../components/Details.vue";
import StudyContent from "../components/StudyContent.vue";
import BlogContent from "../components/BlogContent.vue";
import VideoContent from "../components/VideoContent.vue";
import Search from "../components/Search.vue";

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
      {
        path: "/search",
        name: "search",
        component: Search,
      },
    ],
  },
  {
    path: "/details",
    name: "details",
    component: Details,
    children: [
      {
        path: "/studycontent/:id",
        name: "studycontent",
        component: StudyContent,
      },
      {
        path: "/blogcontent/:id",
        name: "blogcontent",
        component: BlogContent,
      },
      {
        path: "/videocontent/:id",
        name: "videocontent",
        component: VideoContent,
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
