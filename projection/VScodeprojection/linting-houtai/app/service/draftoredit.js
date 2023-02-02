"use strict";
const Service = require("egg").Service;
const fs = require("fs");

function update(requestBody) {
  function fileWrite(cls, idx, user, time, dataBuffer) {
    fs.writeFile(
      `./app/public/img/${cls + idx}/${user}-${time}.jpeg`,
      dataBuffer,
      function (err) {
        return console.log(err);
      }
    );
  }
  function unlink(oldimg) {
    if (oldimg && oldimg.indexOf("default.jpeg") === -1) {
      fs.unlink(
        oldimg.replace("http://localhost:7001", "./app"),
        function (err) {
          return console.log(err);
        }
      );
    }
  }
  if (requestBody.opts === "draft") {
    var imgData = requestBody.img;
    if (imgData) {
      //过滤data:URL
      var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
      // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
      var dataBuffer = Buffer.from(base64Data, "base64");
      fs.exists(
        `./app/public/img/${requestBody.cls + requestBody.idx}/`,
        function (exists) {
          if (exists) {
            unlink(requestBody.oldimg);
            fileWrite(
              requestBody.cls,
              requestBody.idx,
              requestBody.user,
              requestBody.time,
              dataBuffer
            );
          } else {
            fs.mkdir(
              `./app/public/img/${requestBody.cls + requestBody.idx}/`,
              function (err) {
                if (err) {
                  return console.error(err);
                }
                console.log("目录创建成功");
                fileWrite(
                  requestBody.cls,
                  requestBody.idx,
                  requestBody.user,
                  requestBody.time,
                  dataBuffer
                );
              }
            );
          }
        }
      );

      return `http://localhost:7001/public/img/${
        requestBody.cls + requestBody.idx
      }/${requestBody.user}-${requestBody.time}.jpeg`;
    } else {
      unlink(requestBody.oldimg);
      return;
    }
  } else if (requestBody.opts === "edit") {
    var imgData = requestBody.img;
    if (imgData) {
      //过滤data:URL
      var base64Data = imgData.replace(/^data:image\/\w+;base64,/, "");
      // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
      var dataBuffer = Buffer.from(base64Data, "base64");
      fs.exists(
        `./app/public/img/${requestBody.cls + requestBody.idx}/`,
        function (exists) {
          if (exists) {
            unlink(requestBody.oldimg);
            fileWrite(
              requestBody.cls,
              requestBody.idx,
              requestBody.user,
              requestBody.time,
              dataBuffer
            );
          } else {
            fs.mkdir(
              `./app/public/img/${requestBody.cls + requestBody.idx}/`,
              function (err) {
                if (err) {
                  return console.error(err);
                }
                console.log("目录创建成功");
                fileWrite(
                  requestBody.cls,
                  requestBody.idx,
                  requestBody.user,
                  requestBody.time,
                  dataBuffer
                );
              }
            );
          }
        }
      );

      return `http://localhost:7001/public/img/${
        requestBody.cls + requestBody.idx
      }/${requestBody.user}-${requestBody.time}.jpeg`;
    } else {
      unlink(requestBody.oldimg);
      return;
    }
  }
}
class DraftOrEditService extends Service {
  async studyUpdate(requestBody) {
    return update(requestBody);
  }
  async blogUpdate(requestBody) {
    return update(requestBody);
  }
  async videoUpdateImg(requestBody) {
    return update(requestBody);
  }
  async videoUpdateVideo(requestBody) {
    function fileWrite(cls, idx, user, time, dataBuffer) {
      fs.writeFile(
        `./app/public/video/${cls + idx}/${user}-${time}.mp4`,
        dataBuffer,
        function (err) {
          return console.log(err);
        }
      );
    }
    function unlink(oldvideo) {
      if (oldvideo && oldvideo.indexOf("default.jpeg") === -1) {
        fs.unlink(
          oldvideo.replace("http://localhost:7001", "./app"),
          function (err) {
            return console.log(err);
          }
        );
      }
    }
    if (requestBody.opts === "draft") {
      var videoData = requestBody.video;
      if (videoData) {
        //过滤data:URL
        var base64Data = videoData.replace(/^data:video\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.exists(
          `./app/public/video/${requestBody.cls + requestBody.idx}/`,
          function (exists) {
            if (exists) {
              unlink(requestBody.oldvideo);
              fileWrite(
                requestBody.cls,
                requestBody.idx,
                requestBody.user,
                requestBody.time,
                dataBuffer
              );
            } else {
              fs.mkdir(
                `./app/public/video/${requestBody.cls + requestBody.idx}/`,
                function (err) {
                  if (err) {
                    return console.error(err);
                  }
                  console.log("目录创建成功");
                  fileWrite(
                    requestBody.cls,
                    requestBody.idx,
                    requestBody.user,
                    requestBody.time,
                    dataBuffer
                  );
                }
              );
            }
          }
        );

        return `http://localhost:7001/public/video/${
          requestBody.cls + requestBody.idx
        }/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        unlink(requestBody.oldvideo);
        return;
      }
    } else if (requestBody.opts === "edit") {
      var videoData = requestBody.video;
      if (videoData) {
        //过滤data:URL
        var base64Data = videoData.replace(/^data:video\/\w+;base64,/, "");
        // 返回一个被 string 的值初始化的新的 Buffer 实例,原始二进制数据存储在 Buffer 类的实例中，        一个 Buffer 类似于一个整数数组，但它对应于 V8 堆内存之外的一块原始内存。
        var dataBuffer = Buffer.from(base64Data, "base64");
        fs.exists(
          `./app/public/video/${requestBody.cls + requestBody.idx}/`,
          function (exists) {
            if (exists) {
              unlink(requestBody.oldvideo);
              fileWrite(
                requestBody.cls,
                requestBody.idx,
                requestBody.user,
                requestBody.time,
                dataBuffer
              );
            } else {
              fs.mkdir(
                `./app/public/video/${requestBody.cls + requestBody.idx}/`,
                function (err) {
                  if (err) {
                    return console.error(err);
                  }
                  console.log("目录创建成功");
                  fileWrite(
                    requestBody.cls,
                    requestBody.idx,
                    requestBody.user,
                    requestBody.time,
                    dataBuffer
                  );
                }
              );
            }
          }
        );

        return `http://localhost:7001/public/video/${
          requestBody.cls + requestBody.idx
        }/${requestBody.user}-${requestBody.time}.mp4`;
      } else {
        unlink(requestBody.oldvideo);
        return;
      }
    }
  }
  async loadUpdate(requestBody) {
    return update(requestBody);
  }
}
module.exports = DraftOrEditService;
