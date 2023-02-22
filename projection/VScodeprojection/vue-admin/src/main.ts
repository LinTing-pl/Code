import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import axios from "axios";
import "./utils/mock.js";

const app: any = createApp(App);
app.config.globalProperties.$axios = axios;
app.use(router);
app.use(store);
app.use(ElementPlus);
app.mount("#app");
