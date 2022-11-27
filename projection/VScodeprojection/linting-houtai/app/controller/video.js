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
  async addOneVideo() {
    const { ctx } = this;
    const data = await ctx.service.video.addOneVideo(ctx.request.body);

    ctx.body = data;
  }
  async updateVideo() {
    const { ctx } = this;
    const data = await ctx.service.video.updateVideo(ctx.request.body);

    ctx.body = data;
  }
  async deleteOneVideo() {
    const { ctx } = this;
    const data = await ctx.service.video.deleteOneVideo(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = VideoController;
