"use strict";
const { Controller } = require("egg");

class BlogController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      {
        cls: "精选博客",
        img: "http://localhost:7001/public/img/img1.jpeg",
        title: "22",
        date: "1",
        info: "444444444",
      },
      {
        cls: "精选博客",
        img: "http://localhost:7001/public/img/img1.jpeg",
        title: "33",
        date: "2",
        info: "555555555",
      },
      {
        cls: "精选博客",
        img: "http://localhost:7001/public/img/img3.jpeg",
        title: "22",
        date: "1",
        info: "3333333333",
      },
      {
        cls: "精选博客",
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "33",
        date: "2",
        info: "222222222222",
      },
      {
        cls: "精选博客",
        img: "http://localhost:7001/public/img/img2.jpeg",
        title: "33",
        date: "2",
        info: "1111111111",
      },
    ];
    ctx.body = data;
  }
}
module.exports = BlogController;
