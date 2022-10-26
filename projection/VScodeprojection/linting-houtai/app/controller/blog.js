"use strict";
const { Controller } = require("egg");

class BlogController extends Controller {
  async get() {
    const { ctx } = this;
    const data = await ctx.service.blog.get();

    ctx.body = data;
  }
  async getOneBlog() {
    const { ctx } = this;
    const data = await ctx.service.blog.getOneBlog(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = BlogController;
