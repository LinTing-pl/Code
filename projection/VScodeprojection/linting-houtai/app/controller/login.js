"user strict";

const { Controller } = require("egg");

class LoginController extends Controller {
  async login() {
    const { ctx } = this;
    const requestBody = ctx.request.body;
    const data = await ctx.service.login.login(requestBody);
    ctx.body = data;
  }
  async register() {
    const { ctx } = this;
    const requestBody = ctx.request.body;
    const data = await ctx.service.login.register(requestBody);
    ctx.body = data;
  }
  async validate() {
    const { ctx } = this;
    const requestBody = ctx.request.body;
    const data = await ctx.service.login.validate(requestBody);
    ctx.body = data;
  }
}
module.exports = LoginController;
