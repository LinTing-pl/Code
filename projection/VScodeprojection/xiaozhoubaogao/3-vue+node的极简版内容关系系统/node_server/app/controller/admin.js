'use strict';

const Controller = require('egg').Controller;

class XiaozhouController extends Controller {
    async index() {
        await this.ctx.render("admin/index.html")
    }

    async login() {
        try {
            const body = this.ctx.request.body
            const token = await this.ctx.service.user.login(body.username,body.password)
            if (token) {
                this.ctx.body = {
                    code: 20000,
                    message: true,
                    token: token
                }
            } else {
                this.ctx.body = {
                    code: 40000,
                    message: false,
                }
            }
        } catch (error) {
            this.ctx.body = {
                code: 40000,
                message: false
            };
        }
    }
}

module.exports = XiaozhouController;