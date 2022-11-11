<template>
  <div class="nav-tit">
    <div class="nav-back" @click="toHome">返回首页</div>
    后台管理系统
  </div>
</template>
<script>
export default {
  methods: {
    toHome() {
      this.$router.push("/");
    },
  },
};
</script>
<style lang='scss' scoped>
.nav-tit {
  background: rgb(141, 139, 139);
  height: 40px;
  line-height: 40px;
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 10px;
  position: relative;
}
.nav-back {
  position: absolute;
  left: 10px;
  top: 5px;
  font-weight: normal;
  font-size: 15px;
  letter-spacing: normal;
  height: 30px;
  width: 70px;
  line-height: 30px;
  background: #545c64;
  color: #fff;
  border-radius: 10px;
  cursor: pointer;
}
.nav-back:hover {
  background: #ddd;
  color: #545c64;
}
</style>