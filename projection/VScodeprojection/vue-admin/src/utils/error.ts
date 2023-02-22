import { createApp } from "vue";
import router from "../router";
import Error from "../components/Error.vue";

export function showError(errorType: string, global: boolean) {
  const div = document.createElement("div");
  div.setAttribute("id", "error");
  document.body.appendChild(div);
  const app = createApp(Error, {
    errorType,
    global,
    onClick() {
      app.unmount();
      div.remove();
    },
  });
  router.push("/error").then(() => {
    app.mount(div);
  });
}
