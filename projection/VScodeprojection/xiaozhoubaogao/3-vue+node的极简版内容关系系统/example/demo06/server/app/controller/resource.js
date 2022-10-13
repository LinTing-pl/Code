'use strict';

const Controller = require('egg').Controller;

class ResourceController extends Controller {
  async index() {
    this.ctx.body = await this.app.model.Resource.findAll();
  }

  async create() {
    let title = this.ctx.request.body.content.title;
    let code = this.ctx.request.body.content.code;
    let imgurl = this.ctx.request.body.content.imgurl;
    let downloadurl = this.ctx.request.body.content.downloadurl;
    await this.app.model.Resource.create({
      title,
      code,
      imgurl,
      downloadurl
    })
    this.ctx.body = true;
  }

  async destroy() {
    let id = this.ctx.params.id;
    await this.app.model.Resource.destroy({
      where: {
        id
      }
    })
    this.ctx.body = true;
  }

  async listPage() {
    let list = await this.app.model.Resource.findAll();
    await this.ctx.render("index", {
      list
    })
  }

}

module.exports = ResourceController;