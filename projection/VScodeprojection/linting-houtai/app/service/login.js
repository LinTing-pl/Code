"user strict";

const Service = require("egg").Service;

class LoginService extends Service {
  async login(requestBody) {
    const data = await this.app.mysql.get("users", {
      username: requestBody.account,
    });
    if (data === null) {
      return {
        status: "用户名不存在",
      };
    } else if (data.password == requestBody.password) {
      if (data.admin) {
        return {
          status: 200,
          admin: "1025",
        };
      } else {
        return {
          status: 200,
        };
      }
    } else {
      return {
        status: "密码错误",
      };
    }
  }
  async register(requestBody) {
    const data = await this.app.mysql.get("users", {
      username: requestBody.account,
    });
    if (data === null) {
      await this.app.mysql.insert("users", {
        username: requestBody.account,
        password: requestBody.password,
      });
      return {
        status: 200,
      };
    } else {
      return {
        status: "用户名已存在",
      };
    }
  }
  async validate(requestBody) {
    const data = await this.app.mysql.get("users", {
      username: requestBody.account,
    });
    if (data === null) {
      return {
        status: "",
      };
    } else {
      return {
        status: "用户名已存在",
      };
    }
  }
}
module.exports = LoginService;
