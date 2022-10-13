# 晓舟报告_内容管理系统

### 一、宗旨

**晓舟报告，让学习更高效！**

本项目的目标是让前端开发学员熟悉一个完整的web项目开发流程，以及熟悉必要的知识点。

我们的宗旨是让热爱web开发的同学获得更高的学习效率。

### 二、启动项目

1. 启动项目之前，先按下面第四节的内容，在mysql数据库中创建xiaozhoucms数据库。
2. 在server目录中使用`npm install`下载依赖，然后执行`npm run dev`即可启动项目（启动前请先创建数据库，下面内容有介绍）
3. 在client目录中使用`npm install`下载依赖，然后执行`npm run serve`即可启动项目
4. 访问http://127.0.0.1:8080/#/login可以进入后台登录页面
5. 访问http://127.0.0.1:7001/可以打开前端展示页。

### 三、目录结构

* docs：项目开发的相关文档
* server：项目服务器端（基于node，egg，mysql）
* client：项目前端（基于vue）
* example：以项目为基础拆分的小案例，每一个demo都是一个项目，
* example/demo_module_backup：是一个基础项目备份，大家可以直接拷贝过去，然后在此基础上去开发，这样可以省去vue和egg项目初始化的过程。


### 四、数据库初始化

``` sql
-- 使用下面语句创建数据库
create database xiaozhoucms default character set utf8mb4 collate utf8mb4_unicode_ci;
-- 启动egg项目后，所有数据表会自动创建，然后使用下面语句创建管理员用户。
insert into users (
    username,
    password,
    created_at,
    updated_at
) values (
    "admin",
    "e10adc3949ba59abbe56e057f20f883e",
    "2020-10-01",
    "2020-10-01"
);
-- 管理员用户名为admin，密码使用md5加密，所以初始值设置为‘123456’的加密字符串。
```

### 五、扫二维码关注【程序员晓舟】公众号

![晓舟报告公众号二维码](mpQrcode.jpg)
### 六、联系作者
![晓舟微信](myQrcode.jpg)

