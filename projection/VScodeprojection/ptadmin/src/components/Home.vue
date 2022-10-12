<template>
  <div id="home">
    <Nav></Nav>
    <Main></Main>
  </div>
</template>
<script>
import Main from "./Main.vue";
import Nav from "./Nav.vue";
export default {
  components: {
    Main,
    Nav,
  },
};
</script>
<style lang='scss' scoped>
#home {
  height: 100%;
}
</style>