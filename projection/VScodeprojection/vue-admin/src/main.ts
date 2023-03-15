import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import axios from "axios";
import "./utils/mock.js";
import { useLoginStore } from "./store/loginStore";

const app: any = createApp(App);
app.config.globalProperties.$axios = axios;
app.use(router);
app.use(store);
app.use(ElementPlus);
const useLogin = useLoginStore();

router.beforeEach((to, from, next) => {
	if (to.meta.required && !useLogin.flag) {
		next("/login");
	} else {
		if (from.path === "/error") {
			let div = document.querySelector("#error");
			if (div) {
				div.remove();
			}
		}
		next();
	}
});

app.mount("#app");
