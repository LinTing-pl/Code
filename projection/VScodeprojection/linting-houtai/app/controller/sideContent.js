"use strict";
const { Controller } = require("egg");

class SideContentController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      {
        img: "http://localhost:7001/public/img/img1.jpeg",
        title: "编程学习的五大误区，你占了几点？",
      },
      {
        img: "http://localhost:7001/public/img/img2.jpeg",
        title: "编程学习的五大误区，你占了几点？",
      },
      {
        img: "http://localhost:7001/public/img/img3.jpeg",
        title: "编程学习的五大误区，你占了几点？",
      },
      {
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "编程学习的五大误区，你占了几点？",
      },
    ];
    ctx.body = data;
  }
}
module.exports = SideContentController;
