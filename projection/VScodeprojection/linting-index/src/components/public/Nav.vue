<template>
  <!-- 导航栏 -->
  <el-menu
    mode="horizontal"
    class="el-menu-demo"
    router
    :default-active="index"
    background-color="#ffffff"
    text-color="#313131"
  >
    <!-- logo -->
    <span class="logo" title="麟听" @click="logoClick">Linting</span>
    <!-- 导航 -->
    <el-menu-item
      :index="item.name"
      v-for="(item, index) in navList"
      :key="index"
      :id="item.name"
      @click="setIndex(item.name)"
      >{{ item.navItem }}</el-menu-item
    >
    <!-- 搜索框 -->
    <el-input
      class="search-input"
      placeholder="搜索书名"
      v-model="searchParams"
      @keyup.native.enter="toSearch"
    >
      <i
        slot="suffix"
        class="el-input__icon el-icon-search"
        @click="toSearch"
      ></i>
    </el-input>
    <!-- 登录按钮 -->
    <div class="btn-container">
      <div
        class="login-btn logined"
        @mouseenter="loginedEnter"
        @mouseleave="loginedLeave"
        v-if="isLogin"
      >
        已登录
      </div>
      <div class="login-btn" v-else @click="toLogin">登录</div>
      <div
        class="btn-hover"
        @mouseenter="btnHoverEnter"
        @mouseleave="btnHoverLeave"
      >
        <li @click="toAdmin" v-if="admin">管理</li>
        <li @click="quit">退出登录</li>
      </div>
    </div>
  </el-menu>
</template>
<script>
export default {
  data() {
    return {
      isLogin: false,
      index: "/index",
      navList: [
        {
          name: "/index",
          navItem: "首页",
        },
        {
          name: "/study",
          navItem: "学习手册",
        },
        {
          name: "/blog",
          navItem: "技术博客",
        },
        {
          name: "/video",
          navItem: "教学视频",
        },
        {
          name: "/load",
          navItem: "资源下载",
        },
      ],
      searchParams: "",
      admin: false,
      btnHover: null,
    };
  },
  mounted() {
    let flag = sessionStorage.getItem("index");
    if (flag) {
      this.index = flag;
    }
    this.searchParams = sessionStorage.getItem("search");
    this.isLogin = !!localStorage.getItem("user");
    this.admin = this.isLogin && localStorage.getItem("admin") === "1025";
  },
  methods: {
    logoClick() {
      this.setIndex("/index");
      this.$router
        .push("/")
        .then((res) => {
          this.$router.go(0);
        })
        .catch((err) => {});
    },
    setIndex(index) {
      sessionStorage.setItem("index", index);
    },
    toSearch() {
      if (!!this.searchParams) {
        sessionStorage.setItem("search", this.searchParams);
        if (this.$router.history.current.name !== "search") {
          this.$router.push("/search");
        } else {
          this.$router.go(0);
        }
      }
    },
    toLogin() {
      this.$router.push("/login");
    },
    toAdmin() {
      this.$router.push({ name: "adminstudy" });
    },
    quit() {
      localStorage.removeItem("user");
      localStorage.removeItem("admin");
      this.$router.go(0);
    },
    loginedEnter(e) {
      clearTimeout(this.btnHover);
      e.target.parentNode.children[1].style.display = "block";
    },
    loginedLeave(e) {
      this.btnHover = setTimeout(() => {
        e.target.parentNode.children[1].style.display = "none";
      }, 800);
    },
    btnHoverEnter() {
      clearTimeout(this.btnHover);
    },
    btnHoverLeave(e) {
      this.btnHover = setTimeout(() => {
        e.target.style.display = "none";
      }, 800);
    },
  },
};
</script>
<style lang='scss' scoped>
ul {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 62px;
  user-select: none;
}
.logo {
  font-size: 33px;
  font-weight: bold;
  color: #108cff;
  margin-right: 15px;
  cursor: pointer;
  text-shadow: 0 0 10px #108cff;
}
.search-input {
  width: 200px;
  margin-left: 70px;
  margin-right: 12px;
  position: relative;
}
.btn-container {
  position: relative;
  margin: 0;
  padding: 0;
  height: auto;
}
.login-btn {
  background: #0084ff;
  color: #fff;
  letter-spacing: 3px;
  width: 100px;
  height: 100%;
  line-height: 62px;
  border-radius: 0 0 30px 30px;
  font-size: 16px;
  cursor: pointer;
}
.logined {
  background: green;
}

.login-btn:hover {
  background-color: #108cff;
}
.logined:hover {
  background: red;
}
.el-input__icon.el-icon-search {
  cursor: pointer;
}
.el-input__icon.el-icon-search:hover {
  color: #108cff;
}
.btn-hover {
  display: none;
  width: 100px;
  height: auto;
  background: #bebebedd;
  position: absolute;
  top: 72px;
  color: #444343;
  border-radius: 10px;
  z-index: 100;
}
.btn-hover::before {
  content: "";
  width: 0;
  height: 0;
  border: 10px solid transparent;
  border-bottom: 10px solid #bebebedd;
  position: absolute;
  left: 40px;
  top: -20px;
}
.btn-hover li {
  margin: 6px 0;
  width: 100%;
  text-align: center;
  cursor: pointer;
}
.btn-hover li:hover {
  background: #bebebe;
}
.btn-hover:hover {
  display: block;
}
</style>