<template>
  <div id="main">
    <side-menu></side-menu>
    <router-view />
  </div>
</template>
<script>
import SideMenu from "./SideMenu.vue";
export default {
  components: {
    SideMenu,
  },
};
</script>
<style lang='scss' scoped>
#main {
  display: flex;
  height: 621.6px;
}
</style>