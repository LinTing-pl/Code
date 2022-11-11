<template>
  <el-menu
    :default-active="adminIndex"
    class="el-menu-vertical-demo"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b"
    router
  >
    <el-submenu index="1">
      <template slot="title">
        <i class="el-icon-setting"></i>
        <span>内容管理</span>
      </template>
      <el-menu-item
        :index="item[0]"
        @click="setIndex(item[0])"
        v-for="(item, index) in contentMenuList"
        :key="index"
        >{{ item[1] }}</el-menu-item
      >
    </el-submenu>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-menu"></i>
        <span>用户管理</span>
      </template>
      <el-menu-item index="/adminusers" @click="setIndex('/adminusers')"
        >用户列表</el-menu-item
      >
    </el-submenu>
  </el-menu>
</template>
<script>
export default {
  data() {
    return {
      adminIndex: "/adminstudy",
      contentMenuList: [
        ["/adminstudy", "Study"],
        ["/adminblog", "Blog"],
        ["/adminvideo", "Video"],
        ["/adminload", "Load"],
      ],
    };
  },
  mounted() {
    this.adminIndex = sessionStorage.getItem("adminIndex") || "/adminstudy";
  },
  methods: {
    to() {
      this.$router.push("/adminstudy");
    },
    setIndex(index) {
      sessionStorage.setItem("adminIndex", index);
    },
  },
};
</script>
<style lang='scss' scoped>
.el-menu {
  width: 240px;
  height: calc(100vh - 40px);
}
.el-menu-item {
  text-indent: 20px;
}
</style>