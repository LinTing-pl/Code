"use strict";
const { Controller } = require("egg");

class StudyController extends Controller {
  async get() {
    const { ctx } = this;
    const data = await ctx.service.study.get();

    ctx.body = data;
  }
  async getOneBook() {
    const { ctx } = this;
    const data = await ctx.service.study.getOneBook(ctx.params.id);

    ctx.body = data;
  }
  async addOneBook() {
    const { ctx } = this;
    const data = await ctx.service.study.addOneBook(ctx.request.body);

    ctx.body = data;
  }
  async updateBook() {
    const { ctx } = this;
    const data = await ctx.service.study.updateBook(ctx.request.body);

    ctx.body = data;
  }
  async deleteOneBook() {
    const { ctx } = this;
    const data = await ctx.service.study.deleteOneBook(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = StudyController;
