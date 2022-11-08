<template>
  <div class="container">
    <div :class="{ 'register-box': true, 'slide-up': !flag }">
      <h2 class="register-title" @click="toggleFlag">
        <span>没有账号，去</span>注册
      </h2>
      <div class="err">{{ register_err }}</div>
      <div class="input-box">
        <input
          type="text"
          v-model="register_account"
          @input="debounce"
          placeholder="用户名"
        />
        <input type="password" v-model="register_password" placeholder="密码" />
        <input
          type="password"
          v-model="register_password_again"
          placeholder="确认密码"
        />
      </div>
      <button @click="register">注册</button>
    </div>
    <div :class="{ 'login-box': true, 'slide-up': flag }">
      <div class="center">
        <h2 class="login-title" @click="toggleFlag">
          <span>已有账号，去</span>登录
        </h2>
        <div class="err">{{ login_err }}</div>
        <div class="input-box">
          <input type="text" v-model="login_account" placeholder="用户名" />
          <input type="password" v-model="login_password" placeholder="密码" />
        </div>
        <button @click="login" ref="login">登录</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      flag: false,
      login_account: "",
      login_password: "",
      register_account: "",
      register_password: "",
      register_password_again: "",
      login_err: "",
      register_err: "",
      register_t: null,
    };
  },
  mounted() {
    this.clickBtn();
  },
  methods: {
    toggleFlag() {
      this.flag = !this.flag;
    },
    debounce() {
      if (this.register_t !== null) {
        clearTimeout(this.register_t);
      }
      this.register_t = setTimeout(() => {
        this.$axios.default
          .post("/dev-api/login/register/validate", {
            account: this.register_account,
          })
          .then((res) => {
            this.register_err = res.data.status;
          });
      }, 500);
    },
    login() {
      this.$axios.default
        .post("/dev-api/login/login", {
          account: this.login_account,
          password: this.login_password,
        })
        .then((res) => {
          if (res.data.status == 200) {
            this.login_err = "";
            localStorage.setItem("user", this.login_account);
            if (res.data.admin) {
              localStorage.setItem("admin", res.data.admin);
            }
            this.$router.go(-1);
          } else {
            this.login_err = res.data.status;
          }
        });
    },
    register() {
      if (!this.register_account) {
        this.register_err = "请填写用户名！";
      } else if (!this.register_password) {
        this.register_err = "请填写密码！";
      } else if (!this.register_password_again) {
        this.register_err = "请再次填写密码！";
      } else if (this.register_password !== this.register_password_again) {
        this.register_err = "两次密码不一致！";
      } else {
        this.$axios.default
          .post("/dev-api/login/register", {
            account: this.register_account,
            password: this.register_password,
          })
          .then((res) => {
            if (res.data.status == 200) {
              this.register_err = "";
              this.flag = !this.flag;
            } else {
              this.register_err = res.data.status;
            }
          });
      }
    },
    clickBtn() {
      document.addEventListener("keyup", (e) => {
        if (e.keyCode === 13) {
          this.$refs.login.click();
        }
      });
    },
  },
};
</script>
<style lang='scss' scoped>
* {
  margin: 0;
  padding: 0;
}
.container {
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  width: 350px;
  height: 550px;
  border-radius: 15px;
  overflow: hidden;
  position: absolute;
}
.container::after {
  content: "";
  position: absolute;
  inset: 0;
  background: url("../../public/login.jpg") no-repeat;
  background-size: cover;
  background-position: center;
  opacity: 0.8;
}
.register-box {
  width: 70%;
  position: absolute;
  z-index: 1;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.3s ease;
}
.register-title,
.login-title {
  color: #fff;
  font-size: 27px;
  text-align: center;
}
.register-title span,
.login-title span {
  color: rgba(0, 0, 0, 0.4);
  display: none;
}
.register-box .input-box,
.login-box .input-box {
  background-color: #fff;
  border-radius: 15px;
  overflow: hidden;
  margin-top: 50px;
  opacity: 1;
  visibility: visible;
  transition: all 0.6s ease;
}
.register-box input,
.login-box input {
  width: 100%;
  height: 30px;
  border: none;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  font-size: 12px;
  padding: 8px 0;
  text-indent: 15px;
  outline: none;
}
.register-box input:last-child,
.login-box input:last-child {
  border-bottom: none;
}
.register-box input::placeholder,
.login-box input::placeholder {
  color: rgba(0, 0, 0, 0.4);
}
.register-box button,
.login-box button {
  width: 100%;
  padding: 15px 45px;
  margin: 15px 0;
  background: rgba(0, 0, 0, 0.4);
  border: none;
  border-radius: 15px;
  color: rgba(255, 255, 255, 0.8);
  font-size: 13px;
  font-weight: bold;
  cursor: pointer;
  opacity: 1;
  visibility: visible;
  transition: all 0.3s ease;
}
.register-box button:hover,
.login-box button:hover {
  background-color: rgba(0, 0, 0, 0.8);
}
.login-box {
  position: absolute;
  inset: 0;
  top: 20%;
  z-index: 2;
  background-color: #fff;
  transition: all 0.3s ease;
}
.login-box::before {
  content: "";
  background-color: #fff;
  width: 200%;
  height: 250px;
  border-radius: 50%;
  position: absolute;
  top: -20px;
  left: 50%;
  transform: translateX(-50%);
}
.login-box .center {
  width: 70%;
  position: absolute;
  z-index: 3;
  left: 50%;
  top: 40%;
  transform: translate(-50%, -50%);
}
.login-title {
  color: #000;
}
.login-box .input-box {
  border: 1px solid rgba(0, 0, 0, 0.1);
}
.login-box button {
  background-color: #75a297;
}
.login-box.slide-up {
  top: 90%;
}
.login-box.slide-up .center {
  top: 10%;
  transform: translate(-50%, 0);
}
.register-box.slide-up .register-title,
.login-box.slide-up .login-title {
  font-size: 16px;
  cursor: pointer;
}
.login-box.slide-up .login-title span,
.register-box.slide-up .register-title span {
  margin-right: 5px;
  display: inline-block;
}
.register-box.slide-up .input-box,
.register-box.slide-up button,
.login-box.slide-up .input-box,
.login-box.slide-up button {
  opacity: 0;
  visibility: hidden;
}
.register-box.slide-up {
  top: 6%;
  transform: translate(-50%, 0);
}
.err {
  color: red;
  font-size: 15px;
  position: absolute;
  left: 22px;
  top: 62px;
}
</style>