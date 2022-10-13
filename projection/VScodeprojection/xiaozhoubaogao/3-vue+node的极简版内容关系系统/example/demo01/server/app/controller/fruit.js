'use strict';

const Controller = require('egg').Controller;

class FruitController extends Controller {
  async index() {
    this.ctx.body = await this.app.model.Fruit.findAll();
  }
  async create(){
    let fruit = this.ctx.request.body.fruit;
    await this.app.model.Fruit.create({name:fruit});
    this.ctx.body = true;
  }
  async destroy(){
    let id = this.ctx.params.id;
    await this.app.model.Fruit.destroy({where:{id:id}});
    this.ctx.body = true;
  }

  async renderPage(){
    let data = await this.app.model.Fruit.findAll();
    await this.ctx.render("fruit",{data})
  }
}

module.exports = FruitController;
