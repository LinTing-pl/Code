<template>
  <!-- 主体展示部分 -->
  <div class="container">
    <div class="main-content">
      <router-view />
    </div>
    <SideContent></SideContent>
  </div>
</template>
<script>
import SideContent from "./SideContent.vue";
export default {
  components: {
    SideContent,
  },
};
</script>
<style lang='scss' scoped>
.container {
  width: 960px;
  height: calc(100vh - 93.6px);
  margin-top: 10px;
  display: flex;
}
.main-content {
  width: 70%;
  height: 100%;
}
.side-content {
  background: #999;
  width: 30%;
  height: 100%;
  margin-left: 2%;
}
</style>