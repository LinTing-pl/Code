<template>
  <div class="admin-container">
    <Nav :searchSelect="searchSelect"></Nav>
    <div class="admin-main">
      <AdminMenu @searchSelect="pushSearchSelect"></AdminMenu>
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
import Nav from "./Nav.vue";
import AdminMenu from "./AdminMenu.vue";
export default {
  components: {
    Nav,
    AdminMenu,
  },
  data() {
    return {
      searchSelect: "",
    };
  },
  methods: {
    pushSearchSelect(data) {
      this.searchSelect = data;
    },
  },
};
</script>
<style lang='scss' scoped>
.main-container {
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.admin-main {
  display: flex;
}
</style>