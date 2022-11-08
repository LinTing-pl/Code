import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Element from "element-ui";
import "element-ui/lib/theme-chalk/index.css";

var axios = require("axios");
Vue.prototype.$axios = axios;
Vue.config.productionTip = false;
router.beforeEach((to, from, next) => {
  if (to.meta.required) {
    if (localStorage.getItem("admin") === "1025") {
      next();
    } else {
      next("/login");
    }
  } else if (to.meta.logined) {
    if (localStorage.getItem("user") === null) {
      next();
    }
  } else {
    next();
  }
});
Vue.use(Element);
new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
