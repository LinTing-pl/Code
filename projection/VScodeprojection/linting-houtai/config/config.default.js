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
  config.security = {
    crsf: {
      enable: false,
      ignoreJSON: true,
    },
    domainWhiteList: [],
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
  return {
    ...config,
    ...userConfig,
  };
};
