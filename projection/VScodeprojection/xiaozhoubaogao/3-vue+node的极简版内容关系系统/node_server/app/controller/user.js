'use strict';

const Controller = require('egg').Controller;
class UserController extends Controller {
    async create() {
        try {
            const body = this.ctx.request.body;
            await this.ctx.service.user.createUser(body);
            this.ctx.body = {
                code: 20000,
                message: true
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                data: "失败"
            }
        }
    }

    async index() {
        try {
            const userList = await this.ctx.service.user.getUserList()
            this.ctx.body = {
                code: 20000,
                message: true,
                data: userList
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false,
            }
        }
    }

    async destroy() {
        try {
            const id = await this.ctx.params.id
            await this.ctx.service.user.deleteUser(id)
            this.ctx.body = {
                code: 20000,
                message: true,
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false,
            }
        }
    }
    async update() {
        try {
            const body = await this.ctx.request.body
            const id = await this.ctx.params.id;
            const user = await this.ctx.service.user.resetPassword(id,body.password)
            this.ctx.body = {
                code: 20000,
                message: true,
            }
        } catch (error) {
            this.ctx.body = {
                code: 30000,
                message: false,
            }
        }
    }
}

module.exports = UserController;