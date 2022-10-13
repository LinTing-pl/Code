const Controller = require('egg').Controller;

class VideoController extends Controller {
  async index() {
    this.ctx.body = await this.app.model.Video.findAll();
  }

  async create(){
    let title = this.ctx.request.body.title;
    let iframe = this.ctx.request.body.iframe;
    await this.app.model.Video.create({
        title,
        iframe
    })
    this.ctx.body = true;
  }

  async destroy(){
    let id = this.ctx.params.id;
    await this.app.model.Video.destroy({
        where:{
            id
        }
    })
    this.ctx.body = true;
  }
  async listPage(){
    let list = await this.app.model.Video.findAll();
    await this.ctx.render("index",{list})
  }

  async detailPage(){
    let id = this.ctx.params.id;
    let detail = await this.app.model.Video.findOne({
        where:{
            id
        }
    })
    let list = await this.app.model.Video.findAll();
    if(detail){
        await this.ctx.render("detail",{detail,list})
    }else{
        this.ctx.body = "获取页面失败";
    }
  }
}

module.exports = VideoController;
