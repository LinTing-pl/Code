<template>
  <el-menu class="el-menu-vertical-demo" :default-active="'/users'" router>
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>用户管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item
          v-for="(item, i) in navList.userList"
          :key="i"
          :index="item.name"
        >
          {{ item.navItem }}
        </el-menu-item>
      </el-menu-item-group>
    </el-submenu>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-menu"></i>
        <span>权限管理</span>
      </template>
      <el-menu-item-group>
        <el-menu-item
          v-for="(item, i) in navList.powerList"
          :key="i"
          :index="item.name"
        >
          {{ item.navItem }}
        </el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>
<script>
export default {
  data() {
    return {
      navList: {
        userList: [{ name: "/users", navItem: "用户列表" }],
        powerList: [
          { name: "/powers", navItem: "权限列表" },
          { name: "/job", navItem: "内容列表" },
        ],
      },
    };
  },
};
</script>
<style lang="scss">
.el-submenu__title {
  padding-left: 0 !important;
}
</style>
<style lang="scss" scoped>
.el-menu-vertical-demo {
  width: 20%;
  min-width: 222px;
  background: #545d64;
}
.el-menu-vertical-demo span {
  font-size: 30px;
  font-weight: 700;
  width: 200px;
  color: white;
}
li.el-menu-item {
  font-size: 25px;
  margin: 0;
  padding: 0 0 0 0 !important;
  color: white;
}
li.el-menu-item:focus {
  color: black;
}
.el-menu-item-group {
  background: #545d64;
}
a {
  text-decoration: none;
}
</style>
