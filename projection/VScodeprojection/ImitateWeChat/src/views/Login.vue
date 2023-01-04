<template>
  <div class="container">
    <transition @after-leave="afterLeave" leave-active-class="login-active">
      <div v-if="showLogin" class="login">
        <div class="login-top">登录</div>
        <div class="login-center clearfix">
          <div class="login-center-img"><img src="/images/name.png" /></div>
          <div class="login-center-input">
            <input
              type="text"
              v-model="wxid"
              placeholder="请输入您的用户名"
              onfocus="this.placeholder=''"
              onblur="this.placeholder='请输入您的用户名'"
            />
            <div class="login-center-input-text">用户名</div>
          </div>
        </div>
        <div class="login-center clearfix">
          <div class="login-center-img">
            <img src="images/password.png" />
          </div>
          <div class="login-center-input">
            <input
              type="password"
              v-model="password"
              placeholder="请输入您的密码"
              onfocus="this.placeholder=''"
              onblur="this.placeholder='请输入您的密码'"
            />
            <div class="login-center-input-text">密码</div>
          </div>
        </div>

        <div class="login-button" @click="handleLogin">登录</div>
      </div>
    </transition>
    <transition :duration="10000" enter-active-class="sk-rotating-plane-active">
      <div v-if="showRotate" class="sk-rotating-plane"></div>
    </transition>
  </div>
</template>
<script>
import "../assets/css/login.less";
export default {
  data() {
    return {
      showLogin: true,
      showRotate: false,
      wxid: "",
      password: "",
    };
  },
  methods: {
    handleLogin() {
      this.showLogin = false;
      try {
        this.http
          .post("/login", {
            wxid: this.wxid,
            password: this.password,
          })
          .then((resp) => {
            if (resp.data.success) {
              localStorage.setItem("user", JSON.stringify(resp.data.user));
              this.state.user = resp.data.user;
              this.$router.push("/chat");
            } else {
              alert("登陆失败");
              this.showLogin = true;
              this.showRotate = false;
            }
          });
      } catch (e) {
        alert("服务器出问题了");
      }
    },
    afterLeave() {
      this.showRotate = true;
    },
  },
};
</script>
<style lang='scss' scoped>
</style>