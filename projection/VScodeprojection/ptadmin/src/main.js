import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Element from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

var axios = require("axios");
axios.default.baseURL = "http://localhost:8888";
Vue.prototype.$axios = axios;
Vue.use(Element);
Vue.config.productionTip = false;

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (store.state.user.username) {
      next();
    } else {
      next({
        path: "/",
        query: { redirect: to.fullPath },
      });
    }
  } else {
    next();
  }
});
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
