'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.home.index);
  router.get('/video', controller.video.index);
  router.post('/video', controller.video.create);
  router.delete('/video/:id', controller.video.destroy);
  router.get('/list', controller.video.listPage);
  router.get('/detail/:id', controller.video.detailPage);
};
