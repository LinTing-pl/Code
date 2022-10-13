'use strict';

const Controller = require('egg').Controller;
const checkAgent = require("../utils/checkagent")
class HomeController extends Controller {
  async index() {
    const ua = checkAgent(this.ctx.request.header["user-agent"]);
    if (ua) {
      await this.ctx.render("pc/index")
    } else {
      await this.ctx.render("pe/index")
    }
  }
  async fruit(){
    await this.ctx.render("pc/fruit")
  }
}

module.exports = HomeController;