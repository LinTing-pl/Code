<template>
  <div class="container">
    <Nav></Nav>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>
<script>
import Nav from "./Nav.vue";
import Footer from "./Footer.vue";
export default {
  components: {
    Nav,
    Footer,
  },
};
</script>
<style lang='scss' scoped>
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>