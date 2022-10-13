<template>
    <div class="login">
        <!-- <form @submit.prevent="login">
            <input type="text" v-model="user.username" />
            <input type="text" v-model="user.password" />
            <button>登录</button>
        </form>-->
        <div class="form">
            <h1>用户登录</h1>
            <el-form label-width="80px">
                <el-form-item label="用户名称">
                    <el-input v-model="user.username"></el-input>
                </el-form-item>
                <el-form-item label="用户密码">
                    <el-input v-model="user.password"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="login">登录</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
import request from "../utils/request";
export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
            },
        };
    },
    methods: {
        login() {
            request.post("/login", this.user).then((res) => {
                if (res.data.code === 20000) {
                    localStorage.setItem("token", res.data.token);
                    this.$router.push("/");
                } else {
                    console.log("登录失败");
                }
            });
        },
    },
};
</script>

<style scoped>
.login {
    display: flex;
    justify-content: center;
    align-items: center;
    height:500px;
}
.login h1{
  text-align: center;
}

</style>