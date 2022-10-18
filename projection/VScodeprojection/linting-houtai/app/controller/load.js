"use strict";
const { Controller } = require("egg");
class LoadController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      {
        img: "http://localhost:7001/public/img/img2.jpeg",
        title: "资源1",
        psd: "71h29a",
      },
      {
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "资源2",
        psd: "1tsg62",
      },
    ];
    ctx.body = data;
  }
}
module.exports = LoadController;
