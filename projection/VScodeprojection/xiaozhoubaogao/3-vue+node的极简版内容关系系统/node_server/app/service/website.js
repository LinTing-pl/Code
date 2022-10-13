'use strict';

const Service = require('egg').Service;
const queryString = require('querystring');
const crypto = require('crypto');

class WebsitService extends Service {

    async getHomePageData() { //首页
        let bookList = await this.ctx.service.book.getBookList({page:1,total:3}) //推荐书
        let blogList = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:1}) //推荐书
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let videoList = await this.ctx.service.video.getVideoList({page:1,total:3}) //推荐一个视频
        let title = "首页-晓舟报告"
        return {
            bookList,
            blogList,
            videoList,
            recommendBook,
            recommendBlog,
            title
        }
    };

    async getBookList() { //电子书列表
        let bookList = await this.ctx.service.book.getBookList({page:1,total:100}); //所有书籍
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:3}) //推荐书
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let recommendVideo = await this.ctx.service.video.getVideoList({page:1,total:3}) //推荐一个视频
        let title = "学习手册-晓舟报告"
        return {
            bookList,
            recommendBook,
            recommendBlog,
            recommendVideo,
            title,
        }
    }

    async getSectionDetail(id) { //电子书详情 -- 待完善，获取目录
        let section = await this.ctx.service.section.getSectionDetail(id) //通过笑节id获取内容
        let menu = await this.ctx.service.section.getMenuBySectionId(id) //通过书的id获取这本书的章节目录
        let bookList = await this.ctx.service.book.getBookList({page:1,total:100}); //获取所有书籍
        return {
            section,
            bookList,
            menu,
            title: section.title + "-晓舟报告"
        }
    }

    async getBlogList(query) { //博客列表
        let blog = await this.ctx.service.blog.getBlogList({page:1,total:100}) //通过query方法获取博客的所有数据
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:3}) //推荐书
        let title = "博客-晓舟报告" //标题
        return {
            blog,
            recommendBook,
            recommendBlog,
            title,
        }
    }

    async getBlogDetail(id) { //博客详情
        let blog = await this.ctx.service.blog.getBlogDetail(id) //查看一篇博客
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:3}) //推荐书
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let title = blog.title + "-晓舟报告" //标题
        return {
            blog: blog,
            recommendBook,
            recommendBlog,
            title
        }
    }


    async getResourceList() { //下载列表
        let resourceList = await this.ctx.service.resource.getResourceList({page:1,total:100}) //获取所有资源
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:1}) //推荐书
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let title = "资源下载-晓舟报告" //标题
        return {
            resourceList,
            recommendBook,
            recommendBlog,
            title,
        }
    }


    async getVideoList() { //视频列表
        let videoList = await this.ctx.service.video.getVideoList({page:1,total:100}) //查看所有视频类别以及视频类别所属的视频
        let recommendBook = await this.ctx.service.book.getBookList({page:1,total:3}) //推荐书
        let recommendBlog = await this.ctx.service.blog.getBlogList({page:1,total:3}) //推荐博客
        let recommendVideo = await this.ctx.service.video.getVideoList({page:1,total:3}) //推荐一个视频
        let title = '视频-晓舟报告' //标题名称
        return {
            videoList,
            recommendBook,
            recommendBlog,
            recommendVideo,
            title,
        }
    }

    async getVideoDetail(id) { //获取视频类别详情
        let video = await this.ctx.service.video.getVideoDetail(id); //通过视频类别id获取视频类别
        let videoList = await this.ctx.service.video.getVideoList({page:1,total:100}); //通过视频类别的id获取这个视频类别的所有视频
        let title = video.title + "-晓舟报告"
        return {
            video,
            videoList,
            title
        }
    }
}

module.exports = WebsitService;