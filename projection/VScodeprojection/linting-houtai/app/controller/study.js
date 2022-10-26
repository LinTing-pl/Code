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
}
module.exports = StudyController;
