<script setup lang="ts">
import "../assets/iconfont/iconfont.js";
import { getCurrentInstance, onMounted, ref } from "vue";
import { useColorStore } from "../store/colorStore";
import { useLoginStore } from "../store/loginStore";
import Search from "./Search.vue";
const _this = getCurrentInstance()?.appContext.config.globalProperties;
const props = defineProps(["header", "isShow"]);
const useColor = useColorStore();
const useLogin = useLoginStore();
const pageH = ref(null);
onMounted(() => {
	useColor.pageHeaderE = pageH.value;
	useColor.changeColor("pageHeader", "");
});
const exit = () => {
	useLogin.exit();
	_this?.$router.go(0);
};
</script>

<template>
	<div class="pageH" ref="pageH">
		<span v-show="props.isShow" style="color: #545c64">{{
			props.header
		}}</span>
		<div class="right-top">
			<Search class="svg"></Search>
			<svg class="icon" aria-hidden="true">
				<use xlink:href="#icon-alert"></use>
			</svg>
			<img src="../assets/img/default.jpeg" alt="" /><span tabindex="0"
				>麟听
				<svg class="icon" aria-hidden="true">
					<use xlink:href="#icon-sanjiao"></use>
				</svg>
			</span>
			<div class="opts">
				<div class="opt" @click="exit">退出登录</div>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.pageH {
	height: 45px;
	line-height: 45px;
	padding-left: 45px;
	padding-top: 2px;
	background: #ffffff;
	user-select: none;
	position: relative;
	z-index: 10;
	.right-top {
		position: absolute;
		right: 0;
		top: 50%;
		transform: translateY(-50%);
		.svg {
			display: inline-block;
			position: relative;
			top: -6px;
			margin-right: 10px;
		}
		svg {
			margin-right: 10px;
			cursor: pointer;
		}
		svg:hover {
			filter: drop-shadow(0 0 20px blue) invert(100%);
		}
		svg:nth-child(2) {
			margin-right: 15px;
		}
		svg:nth-last-child(1) {
			width: 0.7em;
			height: 0.7em;
		}
		img {
			width: 40px;
			height: 40px;
			border-radius: 50%;
			position: relative;
			top: 10px;
			border: 1px solid #000;
			padding: 2px;
			cursor: pointer;
			margin-right: 5px;
		}
		img:hover {
			filter: drop-shadow(0 0 20px blue);
		}
		span {
			position: relative;
			top: -7px;
			color: rgb(232, 113, 230);
			margin-right: 16px;
			cursor: pointer;
		}
		span:hover {
			text-decoration: underline;
			svg {
				filter: drop-shadow(0 0 20px blue) invert(100%);
			}
		}
		span:focus + .opts,
		.opts:hover {
			display: block;
		}
		.opts {
			display: none;
			position: absolute;
			top: 50px;
			right: 25px;
			background: #545c6450;
			padding: 5px;
			border-radius: 12px 0 12px 12px;
			z-index: 10;
			.opt {
				background: #545c6470;
				border-radius: 10px;
				color: #fff;
				padding: 0 10px;
				border: 1px solid transparent;
				cursor: pointer;
			}
			.opt:hover {
				border: 1px solid #000;
			}
		}
		.opt::after {
			content: "";
			border: 6px solid #545c6450;
			border-top: 6px solid transparent;
			border-right: 6px solid transparent;
			border-left: 6px solid transparent;
			position: absolute;
			right: 0px;
			top: -12px;
		}
	}
}
</style>
