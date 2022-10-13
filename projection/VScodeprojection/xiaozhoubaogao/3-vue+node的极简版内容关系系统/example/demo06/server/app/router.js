'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.delete('/resource/:id', controller.resource.destroy);
  router.get('/resource', controller.resource.index);
  router.post('/resource', controller.resource.create);
  router.get('/list', controller.resource.listPage);
  router.post('/upload', controller.upload.upload);
};
