/* eslint valid-jsdoc: "off" */

"use strict";

/**
 * @param {Egg.EggAppInfo} appInfo app info
 */
module.exports = (appInfo) => {
  /**
   * built-in config
   * @type {Egg.EggAppConfig}
   **/
  const config = (exports = {});

  // use for cookie sign key, should change to your own and keep security
  config.keys = appInfo.name + "_1665586879431_163";

  // add your middleware config here
  config.middleware = [];

  // add your user config here
  const userConfig = {
    // myAppName: 'egg',
  };
  config.view = {
    defaultViewEngine: "nunjucks",
  };
  config.bodyParser = {
    formLimit: "50mb",
    jsonLimit: "50mb",
    textLimit: "50mb",
  };
  config.security = {
    csrf: {
      enable: false,
    },
    domainWhiteList: ["http://localhost:8081"],
  };
  config.cors = {
    //解决跨域访问
    allowMethods: "GET,HEAD,PUT,POST,DELETE,PATCH,OPTIONS",
    credentials: true,
    origin: () => "http://localhost:8081", //这边不能为*号，需要指定明确的、与请求网页一致的域名
  };
  config.mysql = {
    client: {
      host: "localhost",
      port: "3306",
      user: "root",
      password: "Linting1025",
      database: "linting-code",
      multipleStatements: true,
    },
    app: true,
    agent: false,
  };
  config.multipart = {
    // mode: "file",
    fileSize: "100mb",
    mode: "stream",
    // fileExtensions: [".mp3"], // 扩展几种上传的文件格式
  };

  return {
    ...config,
    ...userConfig,
  };
};
