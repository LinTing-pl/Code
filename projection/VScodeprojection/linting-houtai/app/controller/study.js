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
  async setBookPriority() {
    const { ctx } = this;
    const requestBody = ctx.request.body;
    const data = await ctx.service.study.setBookPriority(requestBody);

    ctx.body = data;
  }
  async deleteOneBook() {
    const { ctx } = this;
    const data = await ctx.service.study.deleteOneBook(ctx.params.id);

    ctx.body = data;
  }
}
module.exports = StudyController;
