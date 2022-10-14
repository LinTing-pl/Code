"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.get("/index/get", controller.index.get);
  router.get("/side/get", controller.sideContent.get);
};
