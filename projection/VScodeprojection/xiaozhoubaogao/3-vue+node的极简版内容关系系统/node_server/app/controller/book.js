'use strict';

const Controller = require('egg').Controller;
const checkAgent = require("../utils/checkagent");
class BookController extends Controller {
    //添加书籍
    async create() {
        try {
            const body = this.ctx.request.body;
            body.orderby = Number(body.orderby)
            await this.ctx.service.book.createBook(body)
            this.ctx.body = {
                code: 20000,
                message: true,
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false,
            }
        }
    }

    //查看书籍列表
    async index() {
        try {
            const query = this.ctx.request.query;
            const bookList = await this.ctx.service.book.getBookList(query); 
            this.ctx.body = {
                code: 20000,
                message: true,
                data: bookList,
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false,
            }
        }
    }

    //修改书籍
    async update() {
        try {
            const body = this.ctx.request.body;
            const id = this.ctx.params.id;
            await this.ctx.service.book.updateBook(id, body)
            this.ctx.body = {
                code: 20000,
                data: true
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false
            }
        }
    }
    //删除
    async destroy() {
        try {
            const id = this.ctx.params.id;
            await this.ctx.service.book.deleteBook(id);
            this.ctx.body = {
                code: 20000,
                message: true
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false
            }
        }
    }

    //书籍列表页面
    async getBookList() {
        const ua = checkAgent(this.ctx.request.header["user-agent"]);
        let data = await this.ctx.service.website.getBookList(); //获取书列表
        if (ua) {
            await this.ctx.render("pc/book.html", data);
        } else {
            await this.ctx.render("phone/book.html", data)
        }
    }
    //
    async toFirstSection(){
        const id = this.ctx.params.id;
        let section_id = await this.ctx.service.book.getFirstSectionIdByBookId(id);
        await this.ctx.redirect(`/section/${section_id}`)
    }
}

module.exports = BookController;