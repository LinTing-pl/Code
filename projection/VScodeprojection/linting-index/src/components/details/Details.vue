<template>
  <div class="container">
    <Nav></Nav>
    <router-view></router-view>
    <Footer></Footer>
  </div>
</template>
<script>
import Nav from "../public/Nav.vue";
import Footer from "../public/Footer.vue";
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
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
}
</style>