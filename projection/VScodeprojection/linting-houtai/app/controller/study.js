"use strict";
const { Controller } = require("egg");

class StudyController extends Controller {
  async get() {
    const { ctx } = this;
    let data = [
      {
        id: 1,
        cls: "精选手册",
        img: "http://localhost:7001/public/img/img1.jpeg",
        title: "22",
        date: "1",
        info: "444444444",
      },
      {
        id: 1,
        cls: "精选手册",
        img: "http://localhost:7001/public/img/img2.jpeg",
        title: "33",
        date: "2",
        info: "555555555",
      },
      {
        id: 1,
        cls: "精选手册",
        img: "http://localhost:7001/public/img/img3.jpeg",
        title: "22",
        date: "1",
        info: "3333333333",
      },
      {
        id: 1,
        cls: "精选手册",
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "33",
        date: "2",
        info: "222222222222",
      },
      {
        id: 1,
        cls: "精选手册",
        img: "http://localhost:7001/public/img/img4.jpeg",
        title: "33",
        date: "2",
        info: "1111111111",
      },
    ];
    ctx.body = data;
  }
  async getOneBook() {
    const { ctx } = this;
    let data = {
      id: 1,
      title: "前端开发学习手册",
      bookInfo: "很多同学在学习前端只是的时候都会有些许迷茫...",
      img: "http://localhost:7001/public/img/img4.jpeg",
      chapters: [
        {
          chapter: "第01章 开发学习手册",
          sections: [
            {
              section: "第01节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第02节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第03节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
          ],
        },
        {
          chapter: "第02章 开发学习手册",
          sections: [
            {
              section: "第01节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第02节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第03节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
          ],
        },
        {
          chapter: "第01章 开发学习手册",
          sections: [
            {
              section: "第01节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第01节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
            {
              section: "第01节：前端开发概述",
              content:
                "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            },
          ],
        },
      ],
    };
    ctx.body = data;
  }
}
module.exports = StudyController;
