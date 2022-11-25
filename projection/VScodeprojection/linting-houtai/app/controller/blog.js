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
  async addOneBlog() {
    const { ctx } = this;
    const data = await ctx.service.blog.addOneBlog(ctx.request.body);

    ctx.body = data;
  }
  async updateBlog() {
    const { ctx } = this;
    const data = await ctx.service.blog.updateBlog(ctx.request.body);

    ctx.body = data;
  }
  async deleteOneBlog() {
    const { ctx } = this;
    const data = await ctx.service.blog.deleteOneBlog(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = BlogController;
