'use strict';

const Service = require('egg').Service;

class BookService extends Service {
    //添加书籍
    async createBook(body) {
        try {
            const book = {
                title: body.title,
                img: body.img,
                orderby: body.orderby,
            }
            await this.app.model.Book.create(book);
            return true;
        } catch (error) {
            return false;
        }
    }

    //查询所有书籍列表
    async getBookList(query) {
        try {
            const number = parseInt(query.page)
            const start = number * 10 - 10
            const degree = parseInt(query.total)
            const bookList = await this.app.model.Book.findAll({
                limit: [start, degree],
                'order': [
                    ['orderby', 'asc']
                ],
            })
            return bookList
        } catch (error) {
            return null
        }
    }

    //修改书籍
    async updateBook(id, {title,img,orderby}) {
        try {
            await this.app.model.Book.update({
                title,
                img,
                orderby
            }, {
                where: {
                    id
                }
            })
            return true
        } catch (error) {
            return false;;

        }
    }

    //删除书籍
    async deleteBook(id) {
        try {
            await this.app.model.Book.destroy({
                where: {
                    id
                }
            })
            return true
        } catch (error) {
            return false
        }
    }

    async getFirstSectionIdByBookId(id){
        const chapters = await this.app.model.Chapter.findAll({
            'order': [
                ['orderby', 'asc']
            ],
            where:{
                book_id:id
            }
        })
        let firstChapterId = chapters[0].dataValues.id;
        const sections = await this.app.model.Section.findAll({
            'order': [
                ['orderby', 'asc']
            ],
            where:{
                chapter_id:firstChapterId
            }
        })
        console.log("~~~~~~~~~~~")
        console.log(chapters)
        return sections[0].dataValues.id;
    }
}


module.exports = BookService;