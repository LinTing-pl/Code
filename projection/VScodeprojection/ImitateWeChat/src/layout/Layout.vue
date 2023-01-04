<template>
  <div id="app">
    <!-- 侧边栏 -->
    <div class="sidebar">
      <section>
        <header>
          <img :src="'/images/face/' + state.user?.icon" class="avatar" />
        </header>
        <nav>
          <!-- <a href="/chat" class="icon iconfont icon-msg active"></a>
          <a href="/friends" class="icon iconfont icon-friend"></a>
          <a href="#" class="icon iconfont icon-collection"></a> -->
          <router-link to="/chat" class="icon iconfont icon-msg"></router-link>
          <router-link
            to="/friends"
            class="icon iconfont icon-friend"
          ></router-link>
          <router-link
            to="/coloction"
            class="icon iconfont icon-collection"
          ></router-link>
        </nav>
        <footer>
          <i class="icon iconfont icon-more"></i>
        </footer>
      </section>
    </div>
    <div class="main">
      <!-- 聊天窗口 -->
      <div class="container">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  created() {
    this.state.recents = JSON.parse(
      localStorage.getItem("recents" + this.state.user?.id) || "[]"
    );
    this.loadFriends();
  },
  methods: {
    async loadFriends() {
      this.http
        .get("/friends", {
          headers: {
            token: this.state.user?.token,
          },
        })
        .then((resp) => {
          this.state.friends = resp.data;
        });
    },
  },
};
</script>
<style lang='scss' scoped>
</style>