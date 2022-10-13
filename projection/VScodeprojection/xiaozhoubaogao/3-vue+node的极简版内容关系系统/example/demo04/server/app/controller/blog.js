'use strict';

const Controller = require('egg').Controller;

class BlogController extends Controller {
    async index() {
        this.ctx.body = await this.app.model.Blog.findAll();
    }

    async show(){
        let id = this.ctx.params.id;
        let detail = await this.app.model.Blog.findOne({
            where:{
                id
            }
        })
        if(detail){
            this.ctx.body = detail;
        }else{
            this.ctx.body = false;
        }
    }

    async create() {
        let title = this.ctx.request.body.content.title;
        let md_text = this.ctx.request.body.content.md_text;
        let html_text = this.ctx.request.body.content.html_text;
        await this.app.model.Blog.create({
            title,
            md_text,
            html_text
        })
        this.ctx.body = true;
    }

    async update(){
        let id = this.ctx.params.id;
        let title = this.ctx.request.body.content.title;
        let md_text = this.ctx.request.body.content.md_text;
        let html_text = this.ctx.request.body.content.html_text;
        await this.app.model.Blog.update({
            title,
            md_text,
            html_text
        },{
            where:{
                id
            }
        })
        this.ctx.body = true;
    }

    async destroy() {
        let id = this.ctx.params.id;
        await this.app.model.Blog.destroy({
            where:{id}
        })
        this.ctx.body = true;
    }

    async listPage() {
        let list = await this.app.model.Blog.findAll();
        await this.ctx.render("index",{list})
    }
    async detailPage() {
        let id = this.ctx.params.id;
        let detail = await this.app.model.Blog.findOne({
            where:{
                id
            }
        })
        if(detail){
            await this.ctx.render("detail",{detail})
        }else{
            this.ctx.body = "获取页面失败";
        }
    }
}

module.exports = BlogController;