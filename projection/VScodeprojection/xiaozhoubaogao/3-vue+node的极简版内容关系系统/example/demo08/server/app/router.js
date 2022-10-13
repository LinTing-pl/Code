'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.home.index);

  // nunjucks
  router.get('/list', controller.book.listPage);
  router.get('/detail', controller.section.detailPage);

  //book
  router.get('/book', controller.book.index);
  router.post('/book', controller.book.create);
  router.delete('/book/:id', controller.book.destroy);
  //chapter
  router.get('/chapter/:bookid', controller.chapter.index);
  router.post('/chapter', controller.chapter.create);
  router.delete('/chapter/:id', controller.chapter.destroy);
  //section
  router.get('/section/:chapterid', controller.section.index);
  router.post('/section', controller.section.create);
  router.delete('/section/:id', controller.section.destroy);
  router.put('/section/:id', controller.section.update);
  router.get('/section/:id/edit', controller.section.edit);
};
