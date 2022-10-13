'use strict';

const Service = require('egg').Service;

class ChapterService extends Service {
    //添加章
    async createChapter(body) {
        try {
            const chapter = {
                title: body.title,
                book_id: body.book_id,
                orderby: body.orderby,
            }
            await this.app.model.Chapter.create(chapter);
            return true
        } catch (error) {
            console.log(error);
            return false
        }
    }

    //删除章
    async deleteChapter(id) {
        try {
            await this.app.model.Chapter.destroy({
                where: {
                    id
                }
            })
            return true
        } catch (error) {
            return false
        }
    }

    //通过书的ID获取此书籍的章节
    async getChapterList(book_id) {
        try {
            const chapterList = await this.app.model.Chapter.findAll({
                'order': [
                    ['orderby', 'asc'],
                ],
                include: [{
                    model: this.app.model.Book,
                    as: 'book'
                }],
                where: {
                    book_id: book_id
                }
            });
            return chapterList
        } catch (error) {
            console.log(error);
            return false
        }
    }

    

    //修改章
    async updateChapter(id, {title,orderby,book_id}) {
        try {
            await this.app.model.Chapter.update({
                title,
                book_id,
                orderby
            }, {
                where: {
                    id
                }
            })
            return true
        } catch (error) {
            console.log(error)
            return false
        }
    }

}

module.exports = ChapterService;