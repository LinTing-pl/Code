import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  { path: "/", redirect: "/home" },
  {
    path: "/login",
    name: "login",
    component: () => import("../components/login/Login.vue"),
    meta: {
      logined: true,
    },
  },
  {
    path: "/home",
    name: "home",
    component: () => import("../components/home/Home.vue"),
    redirect: "/index",
    children: [
      {
        path: "/index",
        name: "index",
        component: () => import("../components/home/Index.vue"),
      },
      {
        path: "/study",
        name: "study",
        component: () => import("../components/home/Study.vue"),
      },
      {
        path: "/blog",
        name: "blog",
        component: () => import("../components/home/Blog.vue"),
      },
      {
        path: "/video",
        name: "video",
        component: () => import("../components/home/Video.vue"),
      },
      {
        path: "/load",
        name: "load",
        component: () => import("../components/home/Load.vue"),
      },
      {
        path: "/search",
        name: "search",
        component: () => import("../components/home/Search.vue"),
      },
    ],
  },
  {
    path: "/details",
    name: "details",
    component: () => import("../components/details/Details.vue"),
    children: [
      {
        path: "/studycontent/:id",
        name: "studycontent",
        component: () => import("../components/details/study/StudyContent.vue"),
      },
      {
        path: "/blogcontent/:id",
        name: "blogcontent",
        component: () => import("../components/details/blog/BlogContent.vue"),
      },
      {
        path: "/videocontent/:id",
        name: "videocontent",
        component: () => import("../components/details/video/VideoContent.vue"),
      },
    ],
  },
  {
    path: "/admin",
    name: "admin",
    component: () => import("../components/admin/Admin.vue"),
    meta: {
      required: true,
    },
    children: [
      {
        path: "/adminsearch",
        name: "adminsearch",
        component: () => import("../components/admin/AdminSearch.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminstudyadd",
        name: "adminstudyadd",
        component: () => import("../components/admin/AdminStudyAdd.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminstudyedit/:id",
        name: "adminstudyedit",
        component: () => import("../components/admin/AdminStudyEdit.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminstudy",
        name: "adminstudy",
        component: () => import("../components/admin/AdminStudy.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminblog",
        name: "adminblog",
        component: () => import("../components/admin/AdminBlog.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminblogadd",
        name: "adminblogadd",
        component: () => import("../components/admin/AdminBlogAdd.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminblogedit/:id",
        name: "adminblogedit",
        component: () => import("../components/admin/AdminBlogEdit.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminvideo",
        name: "adminvideo",
        component: () => import("../components/admin/AdminVideo.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminvideoadd",
        name: "adminvideoadd",
        component: () => import("../components/admin/AdminVideoAdd.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminvideoedit/:id",
        name: "adminvideoedit",
        component: () => import("../components/admin/AdminVideoEdit.vue"),
        meta: {
          required: true,
        },
      },
      {
        path: "/adminload",
        meta: {
          required: true,
        },
      },
      {
        path: "/adminusers",
        meta: {
          required: true,
        },
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
