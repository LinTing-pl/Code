"use strict";
const { Controller } = require("egg");

class VideoController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      {
        cls: "精选视频",
        img: "http://localhost:7001/public/img/img1.jpeg",
        title: "Git",
        date: "1",
        info: "444444444",
      },
      {
        cls: "精选视频",
        img: "http://localhost:7001/public/img/img2.jpeg",
        title: "Git",
        date: "2",
        info: "555555555",
      },
      {
        cls: "精选视频",
        img: "http://localhost:7001/public/img/img3.jpeg",
        title: "Git",
        date: "1",
        info: "3333333333",
      },
      {
        cls: "精选视频",
        img: "http://localhost:7001/public/img/img3.jpeg",
        title: "Git",
        date: "2",
        info: "222222222222",
      },
      {
        cls: "精选视频",
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "Git",
        date: "2",
        info: "1111111111",
      },
    ];
    ctx.body = data;
  }
}
module.exports = VideoController;
