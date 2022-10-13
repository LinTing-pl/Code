const Controller = require('egg').Controller;

class ChapterController extends Controller {
    // 通过书的id找章的列表
    async index() {
        let book_id = this.ctx.params.bookid;
        this.ctx.body = await this.app.model.chapter.findAll({
            where:{book_id}
        })
    }

    async create() {

    }

    async destroy(){

    }
}

module.exports = ChapterController;