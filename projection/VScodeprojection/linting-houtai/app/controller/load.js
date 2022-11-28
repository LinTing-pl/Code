"use strict";
const { Controller } = require("egg");
class LoadController extends Controller {
  async get() {
    const { ctx } = this;

    let data = await ctx.service.load.get();
    ctx.body = data;
  }
  async addOneLoad() {
    const { ctx } = this;
    const data = await ctx.service.load.addOneLoad(ctx.request.body);

    ctx.body = data;
  }
  async updateLoad() {
    const { ctx } = this;
    const data = await ctx.service.load.updateLoad(ctx.request.body);

    ctx.body = data;
  }
  async delete() {
    const { ctx } = this;

    let data = await ctx.service.load.delete(ctx.params.id);
    ctx.body = data;
  }
}
module.exports = LoadController;
