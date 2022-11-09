<template>
  <!-- 主体展示部分 -->
  <div class="main-container">
    <div class="main-content">
      <router-view />
      <Bottom></Bottom>
    </div>
    <keep-alive>
      <SideContent></SideContent>
    </keep-alive>
  </div>
</template>
<script>
import Bottom from "../public/Bottom.vue";
import SideContent from "../public/SideContent.vue";
export default {
  components: {
    Bottom,
    SideContent,
  },
};
</script>
<style lang='scss' scoped>
.main-container {
  width: 960px;
  // height: calc(100vh - 93.6px);
  margin-top: 10px;
  display: flex;
}
.main-content {
  width: 70%;
}
</style>