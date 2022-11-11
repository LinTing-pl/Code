"use strict";
const Service = require("egg").Service;

class LoadService extends Service {
  async get() {
    const data = this.app.mysql.select("loads");
    return data;
  }
}
module.exports = LoadService;
