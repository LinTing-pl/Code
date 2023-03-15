<script setup lang="ts"></script>

<template>
	<ul class="icon-nav">
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-home2"></i>
				<span>首页</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-product-hunt"></i>
				<span>产品管理</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-user-circle"></i>
				<span>会员管理</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-shopping-bag"></i>
				<span>订单管理</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-credit_card"></i>
				<span>财务中心</span>
			</a>
		</li>
		<li class="split">
			<a href="javascript:void(0)">
				<i class="iconfont icon-bell"></i>
				<span>消息</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-gear"></i>
				<span>系统配置</span>
			</a>
		</li>
		<li>
			<a href="javascript:void(0)">
				<i class="iconfont icon-user-fill"></i>
				<span>用户中心</span>
			</a>
		</li>
	</ul>
</template>

<style scoped>
@import url(../assets/iconfont/iconfont.css);
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}
.icon-nav {
	list-style: none;
	background-color: #231f2e;
	padding: 0 12px 12px 12px;
	display: flex;
	justify-content: center;
	border-radius: 10px;
	box-shadow: 0 0px 30px -4px rgba(6, 5, 59);
}
.icon-nav li {
	margin-top: 12px;
}
.icon-nav li.split {
	margin-left: 20px;
	padding-left: 20px;
	border-left: 1px solid rgba(255, 255, 255, 0.15);
}
.icon-nav a {
	color: #fff;
	text-decoration: none;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 48px;
	height: 48px;
	border-radius: 8px;
	position: relative;
	cursor: pointer;
}
.icon-nav a i {
	font-size: 20px;
}
.icon-nav a span {
	position: absolute;
	background-color: #fa5c51;
	white-space: nowrap;
	font-size: 15px;
	padding: 8px 16px;
	border-radius: 6px;
	opacity: 0;
	transform-origin: center left;
	transition: 0.15s ease;
}
.icon-nav li:nth-child(even) a span {
	top: calc(100% + 14px);
}
.icon-nav li:nth-child(odd) a span {
	bottom: calc(100% + 14px);
}
.icon-nav li:nth-child(odd) a span::before {
	content: "";
	width: 12px;
	height: 12px;
	background-color: #fa5c51;
	border-radius: 3px;
	position: absolute;
	left: 50%;
	bottom: 0;
	transform: translate(-50%, 50%) rotate(45deg);
}
.icon-nav li:nth-child(even) a span::before {
	content: "";
	width: 12px;
	height: 12px;
	background-color: #fa5c51;
	border-radius: 3px;
	position: absolute;
	left: 50%;
	top: 0;
	transform: translate(-50%, -50%) rotate(45deg);
}
.icon-nav a:hover,
.icon-nav a:focus,
.icon-nav a:active {
	background-color: #fa5c51;
	outline: none;
}
.icon-nav a:hover span,
.icon-nav a:focus span,
.icon-nav a:active span {
	opacity: 1;
}
</style>
