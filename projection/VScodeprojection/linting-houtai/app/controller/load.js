"use strict";
const { Controller } = require("egg");
class LoadController extends Controller {
  async get() {
    const { ctx } = this;

    let data = await ctx.service.load.get();
    ctx.body = data;
  }
}
module.exports = LoadController;
