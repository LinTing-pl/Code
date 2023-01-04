import http from "../utils/http";

export default {
  install(app) {
    app.config.globalProperties.http = http;
  },
};
