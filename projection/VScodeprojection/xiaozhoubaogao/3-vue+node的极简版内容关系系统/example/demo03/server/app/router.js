'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.blog.index);
  router.post('/create', controller.blog.create);
  router.get('/show', controller.blog.show);
};
