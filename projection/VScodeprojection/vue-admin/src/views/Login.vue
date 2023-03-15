<script setup lang="ts">
import { getCurrentInstance, ref } from "vue";
import { useLoginStore } from "../store/loginStore";
import { ElMessage } from "element-plus";
const con = ref();
const useLogin = useLoginStore();
const proxy: any = getCurrentInstance();
const _this: any = proxy.appContext.config.globalProperties;
let account: string = "admin";
let psw: string = "123456";
function success() {
	if (useLogin.login(account, psw)) {
		con.value.classList.add("success");
		setTimeout(() => {
			_this.$router.push("/");
		}, 1000);
	} else {
		ElMessage.error("Oops, 账号或密码错误。");
	}
}
</script>

<template>
	<div class="layout">
		<div class="con" ref="con">
			<h1>Welcome</h1>
			<div class="form">
				<input type="text" placeholder="您的账号" v-model="account" />
				<input type="password" placeholder="您的密码" v-model="psw" />
				<button class="btn-login" @click="success">登录</button>
			</div>
		</div>
		<ul class="bg-squares">
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
			<li></li>
		</ul>
	</div>
</template>

<style scoped lang="scss">
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}
.layout {
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
	background-image: linear-gradient(-45deg, #ffe29f, #ffa99f, #ff719a);
	overflow: hidden;
	position: relative;
}
.con {
	text-align: center;
	color: #fff;
}
.con h1 {
	font-size: 40px;
	font-weight: 100;
	letter-spacing: 2px;
	margin-bottom: 15px;
	transition: all 1s ease-in-out;
}
.form {
	display: flex;
	flex-direction: column;
	align-items: center;
	position: relative;
	z-index: 2;
	opacity: 1;
	transition: opacity 0.5s;
}
.form input {
	outline: none;
	border: 1px solid rgba(255, 255, 255, 0.4);
	background-color: rgba(255, 255, 255, 0.2);
	width: 250px;
	padding: 10px 15px;
	border-radius: 3px;
	margin: 0 auto 10px auto;
	text-align: center;
	color: #fff;
	font-size: 15px;
	transition: all 0.25s;
}
.form input::placeholder {
	color: #fff;
	font-size: 14px;
	font-weight: 300;
}
.form input:hover {
	background-color: rgba(255, 255, 255, 0.4);
}
.form input:focus {
	background-color: #fff;
	width: 300px;
	color: #ff719a;
}
.btn-login {
	outline: none;
	background-color: #fff;
	color: #ff719a;
	border: none;
	width: 250px;
	padding: 10px 15px;
	border-radius: 3px;
	font-size: 15px;
	cursor: pointer;
	transition: all 0.25s;
}
.btn-login:hover {
	background-color: #f5f7f9;
}
.bg-squares {
	list-style: none;
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: 1;
}
.bg-squares li {
	width: 40px;
	height: 40px;
	background-color: rgba(255, 255, 255, 0.15);
	position: absolute;
	bottom: -160px;
	animation: square 20s linear infinite;
}
.bg-squares li:nth-child(1) {
	left: 10%;
	animation-delay: -10s;
}
.bg-squares li:nth-child(2) {
	left: 20%;
	width: 80px;
	height: 80px;
	animation-delay: -8s;
	animation-duration: 17s;
}
.bg-squares li:nth-child(3) {
	left: 25%;
	animation-delay: -6s;
}
.bg-squares li:nth-child(4) {
	left: 40%;
	width: 60px;
	height: 60px;
	background-color: rgba(255, 255, 255, 0.25);
	animation-duration: 22s;
	animation-delay: -10s;
}
.bg-squares li:nth-child(5) {
	left: 70%;
	animation-delay: -10s;
}
.bg-squares li:nth-child(6) {
	left: 80%;
	width: 120px;
	height: 120px;
	background-color: rgba(255, 255, 255, 0.2);
	animation-delay: -7s;
}
.bg-squares li:nth-child(7) {
	left: 32%;
	width: 160px;
	height: 160px;
	animation-delay: -3s;
}
.bg-squares li:nth-child(8) {
	left: 55%;
	width: 20px;
	height: 20px;
	animation-delay: 5s;
	animation-duration: 40 s;
}
.bg-squares li:nth-child(9) {
	left: 25%;
	width: 10px;
	height: 10px;
	background-color: rgba(255, 255, 255, 0.3);
	animation-delay: -8s;
	animation-duration: 40 s;
}
.bg-squares li:nth-child(10) {
	left: 90%;
	width: 160px;
	height: 160px;
	animation-delay: 1s;
}
.con.success h1 {
	transform: translateY(75px);
}
.con.success .form {
	opacity: 0;
}
@keyframes square {
	0% {
		transform: translateY(0);
	}
	100% {
		transform: translateY(-120vh) rotate(600deg);
	}
}
</style>
