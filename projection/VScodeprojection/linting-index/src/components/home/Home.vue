<template>
  <div class="home">
    <!-- 导航 -->
    <keep-alive>
      <Nav></Nav>
    </keep-alive>
    <!-- 主体 -->
    <Main></Main>
  </div>
</template>
<script>
import Nav from "../public/Nav.vue";
import Main from "./Main.vue";
export default {
  components: {
    Nav,
    Main,
  },
};
</script>
<style lang='scss' scoped>
.home {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>