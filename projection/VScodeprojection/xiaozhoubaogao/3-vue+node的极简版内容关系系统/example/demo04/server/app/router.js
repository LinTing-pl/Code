'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  // nunjucks路由
  router.get('/list', controller.blog.listPage);
  router.get('/detail/:id', controller.blog.detailPage);

  //vue的路由
  router.get('/blog', controller.blog.index);
  router.post('/blog', controller.blog.create);
  router.delete('/blog/:id', controller.blog.destroy);
  router.put('/blog/:id', controller.blog.update);
  router.get('/blog/:id', controller.blog.show);
};
