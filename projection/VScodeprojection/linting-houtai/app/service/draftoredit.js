"use strict";
const Service = require("egg").Service;
const fs = require("fs");
class DraftOrEditService extends Service {
  async studyUpdate(requestBody) {
    if (requestBody.cls === "draft") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          },
          {
            where: { id: 1 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: "",
          },
          {
            where: { id: 1 },
          }
        );
        return;
      }
    } else if (requestBody.cls === "edit") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        let res = await this.app.mysql.get("draftoredit", { id: 2 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
        }
        img[
          requestBody.user + requestBody.idx
        ] = `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: JSON.stringify(img),
          },
          {
            where: { id: 2 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        let res = await this.app.mysql.get("draftoredit", { id: 2 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
          if (img[requestBody.user + requestBody.idx] !== undefined) {
            delete img[requestBody.user + requestBody.idx];
            const data = await this.app.mysql.update(
              "draftoredit",
              {
                img: JSON.stringify(img),
              },
              {
                where: { id: 2 },
              }
            );
          }
        }
        return;
      }
    }
  }
  async blogUpdate(requestBody) {
    if (requestBody.cls === "draft") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          },
          {
            where: { id: 3 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: "",
          },
          {
            where: { id: 3 },
          }
        );
        return;
      }
    } else if (requestBody.cls === "edit") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        let res = await this.app.mysql.get("draftoredit", { id: 4 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
        }
        img[
          requestBody.user + requestBody.idx
        ] = `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: JSON.stringify(img),
          },
          {
            where: { id: 4 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        let res = await this.app.mysql.get("draftoredit", { id: 4 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
          if (img[requestBody.user + requestBody.idx] !== undefined) {
            delete img[requestBody.user + requestBody.idx];
            const data = await this.app.mysql.update(
              "draftoredit",
              {
                img: JSON.stringify(img),
              },
              {
                where: { id: 4 },
              }
            );
          }
        }
        return;
      }
    }
  }
  async videoUpdateImg(requestBody) {
    if (requestBody.cls === "draft") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          },
          {
            where: { id: 5 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: "",
          },
          {
            where: { id: 5 },
          }
        );
        return;
      }
    } else if (requestBody.cls === "edit") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/img/${requestBody.user}-${requestBody.time}.jpeg`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        let res = await this.app.mysql.get("draftoredit", { id: 6 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
        }
        img[
          requestBody.user + requestBody.idx
        ] = `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            img: JSON.stringify(img),
          },
          {
            where: { id: 6 },
          }
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        let res = await this.app.mysql.get("draftoredit", { id: 6 });
        let img = {};
        if (res.img) {
          img = JSON.parse(res.img);
          if (img[requestBody.user + requestBody.idx] !== undefined) {
            delete img[requestBody.user + requestBody.idx];
            const data = await this.app.mysql.update(
              "draftoredit",
              {
                img: JSON.stringify(img),
              },
              {
                where: { id: 6 },
              }
            );
          }
        }
        return;
      }
    }
  }
  async videoUpdateVideo(requestBody) {
    if (requestBody.cls === "draft") {
      var imgData = requestBody.video;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:mp4\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/video/${requestBody.user}-${requestBody.time}.mp4`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            video: `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`,
          },
          {
            where: { id: 5 },
          }
        );
        return `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            video: "",
          },
          {
            where: { id: 5 },
          }
        );
        return;
      }
    } else if (requestBody.cls === "edit") {
      var imgData = requestBody.img;
      if (imgData) {
        //过滤data:URL
        var base64Data = imgData.replace(/^data:video\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/video/${requestBody.user}-${requestBody.time}.mp4`,
          dataBuffer,
          function (err) {
            console.log(err);
          }
        );
        let res = await this.app.mysql.get("draftoredit", { id: 6 });
        let video = {};
        if (res.video) {
          video = JSON.parse(res.video);
        }
        video[
          requestBody.user + requestBody.idx
        ] = `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`;
        const data = await this.app.mysql.update(
          "draftoredit",
          {
            video: JSON.stringify(video),
          },
          {
            where: { id: 6 },
          }
        );
        return `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        let res = await this.app.mysql.get("draftoredit", { id: 6 });
        let video = {};
        if (res.video) {
          video = JSON.parse(res.video);
          if (video[requestBody.user + requestBody.idx] !== undefined) {
            delete video[requestBody.user + requestBody.idx];
            const data = await this.app.mysql.update(
              "draftoredit",
              {
                video: JSON.stringify(video),
              },
              {
                where: { id: 6 },
              }
            );
          }
        }
        return;
      }
    }
  }
}
module.exports = DraftOrEditService;
