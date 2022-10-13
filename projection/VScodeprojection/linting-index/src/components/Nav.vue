<template>
  <!-- 导航栏 -->
  <el-menu
    mode="horizontal"
    class="el-menu-demo"
    router
    :default-active="'/index'"
    background-color="#ffffff"
    text-color="#313131"
  >
    <!-- logo -->
    <span class="logo">Linting</span>
    <!-- 导航 -->
    <el-menu-item
      :index="item.name"
      v-for="(item, index) in navList"
      :key="index"
      >{{ item.navItem }}</el-menu-item
    >
    <!-- 搜索框 -->
    <el-input class="search-input" placeholder="搜索">
      <i slot="suffix" class="el-input__icon el-icon-search"></i>
    </el-input>
    <!-- 登录按钮 -->
    <div class="login-btn">登录</div>
  </el-menu>
</template>
<script>
// 差一个搜索功能

export default {
  data() {
    return {
      navList: [
        {
          name: "/index",
          navItem: "首页",
        },
        {
          name: "/study",
          navItem: "学习手册",
        },
        {
          name: "/blog",
          navItem: "技术博客",
        },
        {
          name: "/video",
          navItem: "教学视频",
        },
        {
          name: "/load",
          navItem: "资源下载",
        },
      ],
    };
  },
};
</script>
<style lang='scss' scoped>
ul {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 62px;
}
.logo {
  font-size: 33px;
  font-weight: bold;
  color: #108cff;
  margin-right: 15px;
  cursor: pointer;
  text-shadow: 0 0 10px #108cff;
}
.search-input {
  width: 200px;
  margin-left: 70px;
  margin-right: 12px;
}
.login-btn {
  background: #0084ff;
  color: #fff;
  letter-spacing: 3px;
  width: 100px;
  height: 100%;
  line-height: 62px;
  border-radius: 0 0 30px 30px;
  font-size: 16px;
  cursor: pointer;
}
.login-btn:hover {
  background-color: #108cff;
}
</style>