"use strict";

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = (app) => {
  const { router, controller } = app;
  router.post("/login/login", controller.login.login);
  router.post("/login/register", controller.login.register);
  router.post("/login/register/validate", controller.login.validate);
  router.post("/index/get", controller.index.get);
  router.get("/study/get", controller.study.get);
  router.get(`/study/get/:id`, controller.study.getOneBook);
  router.post(`/study/add`, controller.study.addOneBook);
  router.post(`/study/update`, controller.study.updateBook);
  router.delete(`/study/delete/:id`, controller.study.deleteOneBook);
  router.get("/blog/get", controller.blog.get);
  router.get("/blog/get/:id", controller.blog.getOneBlog);
  router.post(`/blog/add`, controller.blog.addOneBlog);
  router.post(`/blog/update`, controller.blog.updateBlog);
  router.delete(`/blog/delete/:id`, controller.blog.deleteOneBlog);
  router.get("/video/get", controller.video.get);
  router.get(`/video/get/:id`, controller.video.getOneVideo);
  router.post(`/video/add`, controller.video.addOneVideo);
  router.post(`/video/update`, controller.video.updateVideo);
  router.delete(`/video/delete/:id`, controller.video.deleteOneVideo);
  router.get("/load/get", controller.load.get);
  router.post("/draftoredit/study/update", controller.draftoredit.studyUpdate);
  router.post("/draftoredit/blog/update", controller.draftoredit.blogUpdate);
  router.post(
    "/draftoredit/video/updateimg",
    controller.draftoredit.videoUpdateImg
  );
  router.post(
    "/draftoredit/video/updatevideo",
    controller.draftoredit.videoUpdateVideo
  );
};
