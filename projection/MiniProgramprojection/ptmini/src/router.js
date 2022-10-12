import {RouterMount, createRouter} from "uni-simple-router";

const router = createRouter({
    platform: process.env.VUE_APP_PLATFORM,
    routes: [
        ...ROUTES,
        {
            path: "/pages/index",
        },
        {
            path: "/pages/fatie",
        },
        {
            path: "/pages/me",
        },
        {
            path: "/pages/addform",
        },
    ],
});
//全局路由前置守卫
router.beforeEach((to, from, next) => {
    next();
});
// 全局路由后置守卫
router.afterEach((to, from) => {
    console.log("跳转结束");
});

export {router, RouterMount};
