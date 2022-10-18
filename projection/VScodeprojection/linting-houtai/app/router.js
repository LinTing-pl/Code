"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.get("/index/get", controller.index.get);
  router.get("/side/get", controller.sideContent.get);
  router.get("/study/get", controller.study.get);
  router.get(`/study/get/:id`, controller.study.getOneBook);
  router.get("/blog/get", controller.blog.get);
  router.get("/video/get", controller.video.get);
  router.get("/load/get", controller.load.get);
};
