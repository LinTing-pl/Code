import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  linkActiveClass: "active",
  history: createWebHistory(),
  routes: [
    {
      name: "Login",
      path: "/login",
      component: () => import("../views/Login.vue"),
    },
    {
      name: "Layout",
      path: "/",
      component: () => import("../layout/Layout.vue"),
      redirect: "/chat",
      children: [
        {
          name: "Chat",
          path: "/chat",
          component: () => import("../views/Chat.vue"),
        },
        {
          name: "Friends",
          path: "/friends",
          component: () => import("../views/Friends.vue"),
        },
      ],
    },
  ],
});

router.beforeEach((to, from, next) => {
  if (to.path.toLowerCase() === "/login") {
    next();
  } else {
    const user = JSON.parse(localStorage.getItem("user"));
    if (user?.token) {
      next();
    } else {
      alert("请先登录");
      next("/login");
    }
  }
});

export default router;
