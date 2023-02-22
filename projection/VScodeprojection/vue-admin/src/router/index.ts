import { createRouter, createWebHistory } from "vue-router";
const router = createRouter({
  // 指定路由模式
  history: createWebHistory(),
  // 路由地址
  routes: [
    {
      path: "/",
      name: "Layout",
      component: () => import("../layout/Layout.vue"),
      redirect: "/document",
      children: [
        {
          path: "/document",
          name: "Document",
          component: () => import("../views/Document.vue"),
        },
        {
          path: "/menu",
          name: "Menu",
          component: () => import("../views/Menu.vue"),
        },
        {
          path: "/location",
          name: "Location",
          component: () => import("../views/Location.vue"),
        },
        {
          path: "/setting",
          name: "Setting",
          component: () => import("../views/Setting.vue"),
        },
        {
          path: "/audio",
          name: "Audio",
          component: () => import("../views/Audio.vue"),
        },
        {
          path: "/warning",
          name: "Warning",
          component: () => import("../views/Warning.vue"),
        },
        {
          path: "/author",
          name: "Author",
          component: () => import("../views/Author.vue"),
        },
      ],
    },
    {
      path: "/error",
      name: "Error",
      component: () => import("../App.vue"),
    },
  ],
});
router.beforeEach((to, from, next) => {
  if (from.path === "/error") {
    let div = document.querySelector("#error");
    if (div) {
      div.remove();
    }
  }
  next();
});
export default router;
