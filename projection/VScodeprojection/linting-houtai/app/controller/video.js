"use strict";
const { Controller } = require("egg");

class VideoController extends Controller {
  async get() {
    const { ctx } = this;
    const data = await ctx.service.video.get();

    ctx.body = data;
  }
  async getOneVideo() {
    const { ctx } = this;
    const data = await ctx.service.video.getOneVideo(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = VideoController;
