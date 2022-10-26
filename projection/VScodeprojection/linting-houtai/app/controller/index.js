"use strict";
const { Controller } = require("egg");

class IndexController extends Controller {
  async get() {
    const { ctx } = this;
    const data1 = await ctx.service.study.get();
    const data2 = await ctx.service.blog.get();
    const data3 = await ctx.service.video.get();
    let data = [];
    data = [data1, data2, data3];

    ctx.body = data;
  }
}
module.exports = IndexController;
