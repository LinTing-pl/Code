"use strict";

const Service = require("egg").Service;
class VideoService extends Service {
  async get() {
    const data = await this.app.mysql.select("videos");
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
  async getOneVideo(id) {
    const data = this.app.mysql.get("videos", { id: id });

    return data;
  }
}
module.exports = VideoService;
