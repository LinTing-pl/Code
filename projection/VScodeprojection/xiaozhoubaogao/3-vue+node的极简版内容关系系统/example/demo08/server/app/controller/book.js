const Controller = require('egg').Controller;

class BookController extends Controller {
    async index() {
        this.ctx.body = await this.app.model.Book.findAll();
    }

    async create() {
        let title = this.ctx.request.body.content.title;
        let imgurl = this.ctx.request.body.content.imgurl;
        await this.app.model.Book.create({
            title,
            imgurl
        })
    }

    async destroy(){
        let id = this.ctx.params.id;
        await this.app.model.Book.destroy({
            where:{id}
        })
        this.ctx.body = true;
    }

    async listPage(){
        let list = await this.app.model.Book.findAll();
        await this.ctx.render("list",{list});
    }
}

module.exports = BookController;