import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        user: {
            username:
                window.localStorage.getItem("user" || "[]") == null
                    ? ""
                    : JSON.parse(window.localStorage.getItem("user" || "[]")).username,
        },
        superusername: "",
    },
    mutations: {
        login(state, user) {
            state.user = user;
            window.localStorage.setItem("user", JSON.stringify(user));
        },
        setSuperusername(state, user) {
            state.superusername = user;
        },
    },
    actions: {},
    modules: {},
});
