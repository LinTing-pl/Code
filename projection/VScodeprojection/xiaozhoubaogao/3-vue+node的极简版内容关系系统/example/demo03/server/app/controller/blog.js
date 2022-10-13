'use strict';

const Controller = require('egg').Controller;

let content = {
    md_text:"",
    html_text:""
}

class BlogController extends Controller {
  async index() {
    await this.ctx.render("index",{content})
  }

  async show(){
    this.ctx.body = content;
  }

  async create(){
    let md_text = this.ctx.request.body.content.md_text;
    let html_text = this.ctx.request.body.content.html_text;
    content = {
        md_text,
        html_text
    }
    this.ctx.body = "添加成功";
  }
}

module.exports = BlogController;
