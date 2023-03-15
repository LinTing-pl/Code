<script setup lang="ts">
import { onMounted, ref } from "vue";
let items: any = ref([]);
let item = (e: any) => {
	(items.value as any).push(e);
};

onMounted(() => {
	function setActive(e: any) {
		items.value.forEach((item: any) => {
			item.classList.remove("active");
		});
		e.target.classList.add("active");
	}
	items.value.forEach((item: any) => {
		item.addEventListener("click", setActive);
	});
});
</script>

<template>
	<div class="tabbar">
		<ul>
			<li :ref="item" class="item active">
				<a href="">
					<span class="iconfont icon-home2"></span>
					<span class="text">首页</span>
				</a>
			</li>
			<li :ref="item" class="item">
				<a href="">
					<span class="iconfont icon-heart-fill"></span>
					<span class="text">动态</span>
				</a>
			</li>
			<li :ref="item" class="item">
				<a href="">
					<span class="iconfont icon-jia"></span>
					<span class="text">发布</span>
				</a>
			</li>
			<li :ref="item" class="item">
				<a href="">
					<span class="iconfont icon-xiaoxi-fill"></span>
					<span class="text">消息</span>
				</a>
			</li>
			<li :ref="item" class="item">
				<a href="">
					<span class="iconfont icon-user"></span>
					<span class="text">我的</span>
				</a>
			</li>
			<div class="active-bg"></div>
		</ul>
	</div>
</template>

<style scoped>
@import url("../assets/iconfont/iconfont.css");
* {
	margin: 0;
	padding: 0;
}
.tabbar {
	width: 350px;
	height: 70px;
	position: relative;
	border-radius: 35px;
	filter: drop-shadow(0 0 4px #fff);
	box-shadow: 0 0 4px #fff;
}
.tabbar ul {
	display: flex;
}
.tabbar ul li {
	list-style: none;
	width: 70px;
	height: 70px;
	position: relative;
	z-index: 1;
	cursor: pointer;
}
.tabbar ul li a {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	color: #fff;
	text-align: center;
	pointer-events: none;
}
.tabbar ul li a .iconfont {
	position: absolute;
	font-size: 30px;
	transform: all 0.5s;
	top: 13px;
	transition: all 0.5s;
}
.tabbar ul li .text {
	position: absolute;
	font-size: 12px;
	bottom: 13px;
	transition: all 0.5s;
	transform: scale(0);
}
.tabbar ul li.active a .iconfont {
	font-size: 27px;
	transform: translateY(-10px);
}
.tabbar ul li.active a .text {
	transform: scale(1);
}
.active-bg {
	position: absolute;
	left: 0;
	top: 0;
	width: 70px;
	height: 70px;
	border-radius: 50%;
	--c: gold;
	--cc: gold;
	background-color: var(--c);
	box-shadow: 0 10px 15px var(--cc);
	transition: all 0.5s;
}
.tabbar ul li:nth-child(1).active ~ .active-bg {
	--c: #ffa502;
	--cc: #ffa50299;
	left: 0;
}
.tabbar ul li:nth-child(2).active ~ .active-bg {
	--c: #ff6348;
	--cc: #ff634899;
	left: calc(1 * 70px);
}
.tabbar ul li:nth-child(3).active ~ .active-bg {
	--c: #2ed573;
	--cc: #2ed57399;
	left: calc(2 * 70px);
}
.tabbar ul li:nth-child(4).active ~ .active-bg {
	--c: #1e90ff;
	--cc: #1e90ff99;
	left: calc(3 * 70px);
}
.tabbar ul li:nth-child(5).active ~ .active-bg {
	--c: #ff6b81;
	--cc: #ff6b8199;
	left: calc(4 * 70px);
}
</style>
