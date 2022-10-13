'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.home.index);
  router.post("/fruit",controller.fruit.create)
  router.delete("/fruit/:id",controller.fruit.destroy)
  router.get("/fruit",controller.fruit.index)
  router.get("/fruitpage",controller.fruit.renderPage);
};
