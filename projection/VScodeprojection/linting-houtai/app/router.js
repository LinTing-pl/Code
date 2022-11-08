"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.post("/login/login", controller.login.login);
  router.post("/login/register", controller.login.register);
  router.post("/login/register/validate", controller.login.validate);
  router.get("/index/get", controller.index.get);
  router.get("/study/get", controller.study.get);
  router.get(`/study/get/:id`, controller.study.getOneBook);
  router.get("/blog/get", controller.blog.get);
  router.get("/blog/get/:id", controller.blog.getOneBlog);
  router.get("/video/get", controller.video.get);
  router.get(`/video/get/:id`, controller.video.getOneVideo);
  router.get("/load/get", controller.load.get);
};
