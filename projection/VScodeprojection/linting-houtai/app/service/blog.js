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
      };
    });
    return res;
  }
  async getOneBlog(id) {
    const data = await this.app.mysql.get("blogs", { id: id });

    return data;
  }
}
module.exports = BlogService;
