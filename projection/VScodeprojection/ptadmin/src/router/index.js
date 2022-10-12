import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../components/Login.vue";
import Home from "../components/Home.vue";
import Users from "../components/Users.vue";
import Powers from "../components/Powers.vue";
import Job from "../components/JobControl.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Login",
        component: Login,
    },
    {
        path: "/home",
        name: "Home",
        component: Home,
        redirect: "/users",
        meta: {
            requireAuth: true,
        },
        children: [
            {
                path: "/users",
                name: "Users",
                component: Users,
                meta: {
                    requireAuth: true,
                },
            },
            {
                path: "/powers",
                name: "Powers",
                component: Powers,
                meta: {
                    requireAuth: true,
                },
            },
            {
                path: "/job",
                name: "Job",
                component: Job,
                meta: {
                    requireAuth: true,
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
