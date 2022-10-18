<template>
  <div class="home">
    <!-- 导航 -->
    <Nav></Nav>
    <!-- 主体 -->
    <Main></Main>
  </div>
</template>
<script>
import Nav from "./Nav";
import Main from "./Main";
export default {
  components: {
    Nav,
    Main,
  },
  data() {
    return {
      index: "",
    };
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