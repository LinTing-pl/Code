"use strict";
const Service = require("egg").Service;

class LoadService extends Service {
  async get() {
    const data = this.app.mysql.select("loads", {
      orders: [["orderby", "desc"]],
    });
    return data;
  }
  async addOneLoad(requestBody) {
    const load = requestBody.load;
    const data = await this.app.mysql.insert("loads", {
      cls: load.cls,
      title: load.title,
      img: load.img,
      orderby: load.orderby,
      url: load.url,
      code: load.code,
    });
    return "200";
  }
  async updateLoad(requestBody) {
    if (requestBody.orderby) {
      const data = await this.app.mysql.update(
        "loads",
        { orderby: requestBody.orderby },
        {
          where: { id: requestBody.id },
        }
      );
      return data;
    } else if (requestBody.remark) {
      const remark = requestBody.remark;
      const data = await this.app.mysql.update(
        "loads",
        {
          remark: remark,
        },
        {
          where: { id: requestBody.id },
        }
      );
    } else {
      const load = requestBody.load;
      const data = await this.app.mysql.update(
        "loads",
        {
          title: load.title,
          img: load.img,
          url: load.url,
          code: load.code,
        },
        {
          where: { id: requestBody.id },
        }
      );
      return data;
    }
  }
  async delete(id) {
    const data = this.app.mysql.delete("loads", {
      id: id,
    });
    return data;
  }
}
module.exports = LoadService;
