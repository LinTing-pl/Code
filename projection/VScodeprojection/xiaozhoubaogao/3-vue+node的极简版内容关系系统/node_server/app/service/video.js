"use strict";

const Service = require("egg").Service;

class VideoService extends Service {
  //添加视频
  async createVideo(body) {
    try {
      const chapter = {
        title: body.title,
        img: body.img,
        iframe_url: body.iframe_url
      }
      await this.app.model.Video.create(chapter);
      return true
    } catch (error) {
      return false
    }
  }

  //删除视频
  async deleteVideo(id) {
    try {
      await this.app.model.Video.destroy({
        where: {
          id
        }
      })
      return true
    } catch (error) {
      return false
    }
  }
  //修改视频
  async updateVideo(id, {
    title,
    img,
    iframe_url
  }) {
    try {
      await this.app.model.Video.update({
        title,
        img,
        iframe_url
      }, {
        where: {
          id
        }
      })
      return true
    } catch (error) {
      return false
    }
  }
  //根据视频类别查找视频
  async getVideoList(query) {
    try {
      const number = parseInt(query.page)
      const start = number * 10 - 10
      const degree = parseInt(query.total)
      const blogList = await this.app.model.Video.findAll({
        limit: [start, degree]
      })
      return blogList
    } catch (error) {
      return null
    }
  }

  //通过视频本身id查找视频
  async getVideoDetail(id) {
    try {
      let video = await this.app.model.Video.findOne({
        where: {
          id: id
        }
      });
      return video
    } catch (error) {
      return false;
    }
  }

}

module.exports = VideoService;