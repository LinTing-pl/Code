"use strict";

const { app, assert } = require("egg-mock/bootstrap");

describe('test/app/controller/client.test.js', () => {
    it('测试service.client', async() => {
        const ctx = app.mockContext();
        const user = await ctx.service.section.updateSection({
          "sectionName":"sectionName",
          "admin":"admin",
          "sectionNumb":"3"
        },1);
        console.log(user);
  });
});
