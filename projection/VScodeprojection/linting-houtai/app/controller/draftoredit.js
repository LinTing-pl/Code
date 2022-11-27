"use strict";
const { Controller } = require("egg");

class DraftOrEditController extends Controller {
  async studyUpdate() {
    const { ctx } = this;
    const data = await ctx.service.draftoredit.studyUpdate(ctx.request.body);

    ctx.body = data;
  }
  async blogUpdate() {
    const { ctx } = this;
    const data = await ctx.service.draftoredit.blogUpdate(ctx.request.body);

    ctx.body = data;
  }
  async videoUpdateImg() {
    const { ctx } = this;
    const data = await ctx.service.draftoredit.videoUpdateImg(ctx.request.body);

    ctx.body = data;
  }
  async videoUpdateVideo() {
    const { ctx } = this;
    const data = await ctx.service.draftoredit.videoUpdateVideo(
      ctx.request.body
    );

    ctx.body = data;
  }
}
module.exports = DraftOrEditController;
