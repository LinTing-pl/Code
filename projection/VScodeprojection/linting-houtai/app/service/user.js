"use strict";
const Service = require("egg").Service;
class UserService extends Service {
  async get() {
    const data = await this.app.mysql.select("users", {
      orders: [["admin", "desc"]],
    });
    return data;
  }
}
module.exports = UserService;
