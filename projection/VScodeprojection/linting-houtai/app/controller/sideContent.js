"use strict";
const { Controller } = require("egg");

class SideContentController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      { img: "http://localhost:7001/public/img/img1.jpeg", title: "adadada" },
      { img: "http://localhost:7001/public/img/img2.jpeg", title: "adadada" },
      { img: "http://localhost:7001/public/img/img3.jpeg", title: "adadada" },
      { img: "http://localhost:7001/public/img/img4.jpeg", title: "adadada" },
    ];
    ctx.body = data;
  }
}
module.exports = SideContentController;
