"use strict";
const { Controller } = require("egg");

class IndexController extends Controller {
  async get() {
    const { ctx } = this;
    let flag = ctx.request.body.flag;
    if (flag === "all") {
      const data1 = await ctx.service.study.get();
      const data2 = await ctx.service.blog.get();
      const data3 = await ctx.service.video.get();
      const data4 = await ctx.service.load.get();
      let data = [];
      data = [data1, data2, data3, data4];
      ctx.body = data;
    } else if (flag === "study") {
      const data1 = await ctx.service.study.get();
      ctx.body = data1;
    } else if (flag === "blog") {
      const data2 = await ctx.service.blog.get();
      ctx.body = data2;
    } else if (flag === "video") {
      const data3 = await ctx.service.video.get();
      ctx.body = data3;
    } else if (flag === "load") {
      const data4 = await ctx.service.load.get();
      ctx.body = data4;
    }
  }
}
module.exports = IndexController;
