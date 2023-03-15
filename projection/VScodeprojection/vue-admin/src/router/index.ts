import { createRouter, createWebHashHistory } from "vue-router";
const router = createRouter({
	// 指定路由模式
	history: createWebHashHistory(),
	// 路由地址
	routes: [
		{
			path: "/login",
			name: "Login",
			component: () => import("../views/Login.vue"),
		},
		{
			path: "/",
			name: "Layout",
			component: () => import("../layout/Layout.vue"),
			meta: {
				required: true,
			},
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
					path: "/permissions",
					name: "Permissions",
					component: () => import("../views/Permissions.vue"),
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
					path: "/upload",
					name: "Upload",
					component: () => import("../views/Upload.vue"),
				},
				{
					path: "/dv",
					name: "DV",
					component: () => import("../views/DV.vue"),
				},
				{
					path: "/games",
					name: "Games",
					component: () => import("../views/Games.vue"),
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
export default router;
