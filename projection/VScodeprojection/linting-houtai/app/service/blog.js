"use strict";
const Service = require("egg").Service;
class BlogService extends Service {
  async get() {
    const data = await this.app.mysql.select("blogs", {
      orders: [["orderby", "desc"]],
    });
    const res = data.map((v) => {
      return {
        id: v.id,
        cls: v.cls,
        title: v.title,
        img: v.img,
        date: v.date,
        info: v.info,
        orderby: v.orderby,
      };
    });
    return res;
  }
  async getOneBlog(id) {
    const data = await this.app.mysql.get("blogs", { id: id });

    return data;
  }
  async addOneBlog(requestBody) {
    const blog = requestBody.blog;
    const data = await this.app.mysql.insert("blogs", {
      cls: blog.cls,
      title: blog.title,
      img: blog.img,
      date: blog.date,
      info: blog.info,
      orderby: blog.orderby,
      content: blog.content,
    });
    return "200";
  }
  async updateBlog(requestBody) {
    if (requestBody.orderby) {
      const data = await this.app.mysql.update(
        "blogs",
        { orderby: requestBody.orderby },
        {
          where: { id: requestBody.id },
        }
      );
      return data;
    } else {
      const blog = requestBody.blog;
      const data = await this.app.mysql.update(
        "blogs",
        {
          title: blog.title,
          img: blog.img,
          date: blog.date,
          info: blog.info,
          chapters: blog.chapters,
        },
        {
          where: { id: blog.id },
        }
      );
      return data;
    }
  }
  async deleteOneBlog(id) {
    const data = await this.app.mysql.delete("blogs", { id: id });
    return data;
  }
}
module.exports = BlogService;
