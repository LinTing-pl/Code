'use strict';

const Service = require('egg').Service;

class DownloadService extends Service {
    //添加下载资源
    async createResource(body) {
        try {

            let resource = {
                title: body.title,
                code: body.code,
                url: body.url,
            }
            await this.app.model.Resource.create(resource)
            return true
        } catch (error) {
            return false
        }
    }

    //删除资源
    async deleteResource(id) {
        try {
            await this.app.model.Resource.destroy({
                where: {
                    id
                }
            })
            return true
        } catch (error) {
            return false
        }
    }

    //修改资源
    async updateResource(id, {
        title,
        code,
        url
    }) {
        try {
            await this.app.model.Resource.update({
                title,
                code,
                url
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
   
    //通过query查询条件查询资源列表
    async getResourceList(query) {
        try {
            const number = parseInt(query.page)
            const start = number * 10 - 10
            const degree = parseInt(query.total)
            const resourceList = await this.app.model.Resource.findAll({
                limit: [start, degree]
            })
            return resourceList
        } catch (error) {
            return null
        }
    }
}
module.exports = DownloadService;