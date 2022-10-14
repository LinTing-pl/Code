"use strict";
const { Controller } = require("egg");

class IndexController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      [
        {
          cls: "精选手册",
          img: "http://localhost:7001/public/img/img1.jpeg",
          title: "22",
          date: "1",
          info: "",
        },
        {
          cls: "精选手册",
          img: "http://localhost:7001/public/img/img1.jpeg",
          title: "33",
          date: "2",
          info: "",
        },
      ],
      [
        {
          cls: "精选博客",
          img: "http://localhost:7001/public/img/img2.jpeg",
          title: "11",
          date: "1",
          info: "博客",
        },
        {
          cls: "精选博客",
          img: "http://localhost:7001/public/img/img2.jpeg",
          title: "22",
          date: "2",
          info: "博客",
        },
      ],

      [
        {
          cls: "精选视频",
          img: "http://localhost:7001/public/img/img3.jpeg",
          title: "22",
          date: "1",
          info: "",
        },
        {
          cls: "精选视频",
          img: "http://localhost:7001/public/img/img3.jpeg",
          title: "22",
          date: "2",
          info: "",
        },
      ],
    ];
    ctx.body = data;
  }
}
module.exports = IndexController;
