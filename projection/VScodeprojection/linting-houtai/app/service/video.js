"use strict";

const Service = require("egg").Service;
class VideoService extends Service {
  async get() {
    const data = await this.app.mysql.select("videos", {
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
  async getOneVideo(id) {
    const data = this.app.mysql.get("videos", { id: id });

    return data;
  }
  async addOneVideo(requestBody) {
    const video = requestBody.video;
    const data = await this.app.mysql.insert("videos", {
      cls: video.cls,
      title: video.title,
      img: video.img,
      date: video.date,
      info: video.info,
      orderby: video.orderby,
      sections: video.sections,
    });
    return "200";
  }
  async updateVideo(requestBody) {
    if (requestBody.orderby) {
      const data = await this.app.mysql.update(
        "videos",
        { orderby: requestBody.orderby },
        {
          where: { id: requestBody.id },
        }
      );
      return data;
    } else if (requestBody.remark) {
      const remark = requestBody.remark;
      const data = await this.app.mysql.update(
        "videos",
        {
          remark: remark,
        },
        {
          where: { id: requestBody.id },
        }
      );
    } else {
      const video = requestBody.video;
      const data = await this.app.mysql.update(
        "videos",
        {
          title: video.title,
          img: video.img,
          date: video.date,
          info: video.info,
          sections: video.sections,
        },
        {
          where: { id: video.id },
        }
      );
      return data;
    }
  }
  async deleteOneVideo(id) {
    const data = await this.app.mysql.delete("videos", { id: id });
    return data;
  }
}
module.exports = VideoService;
