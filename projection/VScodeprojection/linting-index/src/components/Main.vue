<template>
  <!-- 主体展示部分 -->
  <div class="container">
    <div class="main-content">
      <router-view />
      <Bottom></Bottom>
    </div>
    <SideContent></SideContent>
  </div>
</template>
<script>
import Bottom from "./Bottom";
import SideContent from "./SideContent.vue";
export default {
  components: {
    Bottom,
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
}
</style>