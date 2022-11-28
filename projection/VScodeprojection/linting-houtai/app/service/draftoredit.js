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
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        return;
      }
    }
  }
  async videoUpdateVideo(requestBody) {
    if (requestBody.cls === "draft") {
      var videoData = requestBody.video;
      if (videoData) {
        //过滤data:URL
        var base64Data = videoData.replace(/^data:video\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        // var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/video/${requestBody.user}-${requestBody.time}.mp4`,
          base64Data,
          "base64",
          function (err) {}
        );
        return `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        return;
      }
    } else if (requestBody.cls === "edit") {
      var videoData = requestBody.img;
      if (videoData) {
        //过滤data:URL
        var base64Data = videoData.replace(/^data:video\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.writeFile(
          `./app/public/video/${requestBody.user}-${requestBody.time}.mp4`,
          dataBuffer,
          function (err) {}
        );
        return `http://localhost:7001/public/video/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        return;
      }
    }
  }
  async loadUpdate(requestBody) {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
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
          function (err) {}
        );
        return `http://localhost:7001/public/img/${requestBody.user}-${requestBody.time}.jpeg`;
      } else {
        return;
      }
    }
  }
}
module.exports = DraftOrEditService;
