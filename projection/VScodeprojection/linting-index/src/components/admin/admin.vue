<template>
  <div class="admin-container">
    <Nav :searchSelect="searchSelect" @nativeSearch="pushNativeSearch"></Nav>
    <div class="admin-main">
      <AdminMenu @searchSelect="pushSearchSelect"></AdminMenu>
      <router-view :nativeSearch="nativeSearch"></router-view>
    </div>
  </div>
</template>
<script>
import Nav from "./AdminNav.vue";
import AdminMenu from "./AdminMenu.vue";
export default {
  components: {
    Nav,
    AdminMenu,
  },
  data() {
    return {
      searchSelect: "",
      nativeSearch: false,
    };
  },
  methods: {
    pushSearchSelect(data) {
      this.searchSelect = data;
    },
    pushNativeSearch(data) {
      this.nativeSearch = data;
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