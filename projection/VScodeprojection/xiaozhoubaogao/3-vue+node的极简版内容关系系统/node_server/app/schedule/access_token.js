const Subscription = require('egg').Subscription;

class UpdateCache extends Subscription {
    static get schedule() {
        return {
            interval: '1h',
            type: 'all',
        };
    }

    async subscribe() {
        const config = this.ctx.app.config.wechat;
        const access_token_url = config.mp_access_token
            .replace('APPID', config.mp_appid)
            .replace('SECRET', config.mp_secret);
        const access_token_res = await this.ctx.curl(access_token_url, {
            dataType: 'json',
        });
        this.ctx.app['access_token'] = access_token_res.data.access_token;

        const access_token = access_token_res.data.access_token;
        const jsapi_ticket_url = config.mp_jsapi_ticket
            .replace('ACCESS_TOKEN', access_token);
        //获取jsapi_ticket，用于调用jsapi接口。
        const jsapi_ticket_res = await this.ctx.curl(jsapi_ticket_url, {
            dataType: 'json',
        });
        this.ctx.app['jsapi_ticket'] = jsapi_ticket_res.data.ticket;
    }
}

module.exports = UpdateCache;