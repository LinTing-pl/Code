"use strict";
const { Controller } = require("egg");
class UserController extends Controller {
  async get() {
    const { ctx } = this;

    let data = await ctx.service.user.get();
    ctx.body = data;
  }
}
module.exports = UserController;
