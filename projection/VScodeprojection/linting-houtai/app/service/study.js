"use strict";
const Service = require("egg").Service;
class StudyService extends Service {
  async get() {
    const data = await this.app.mysql.select("books", {
      orders: [["orderby", "desc"]],
    });
    let res = data.map((v) => {
      return {
        id: v.id,
        cls: v.cls,
        title: v.title,
        img: v.img,
        orderby: v.orderby,
        date: v.date,
        info: v.info,
      };
    });
    // const count = await this.app.mysql.query("select count(1) from books");

    return res;
  }
  async getOneBook(id) {
    const data = await this.app.mysql.get("books", { id: id });
    let res = Object.assign(data);
    res.chapters = JSON.parse(res.chapters);
    return res;
  }
  async setBookPriority(requestBody) {
    const data = await this.app.mysql.update(
      "books",
      { orderby: requestBody.orderby },
      {
        where: { id: requestBody.id },
      }
    );
    return data;
  }
  async deleteOneBook(id) {
    const data = await this.app.mysql.delete("books", { id: id });
    return data;
  }
}
module.exports = StudyService;
