<script setup lang="ts"></script>

<template>
	<div class="navbar">
		<input type="checkbox" />
		<span></span>
		<span></span>
		<ul>
			<li><a>点赞</a></li>
			<li><a>关注</a></li>
			<li><a>收藏</a></li>
			<li><a>分享</a></li>
			<li><a>评论</a></li>
		</ul>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
}
.navbar,
.navbar ul {
	display: flex;
	justify-content: center;
	align-items: center;
}

.navbar ul li a {
	text-decoration: none;
	font-size: 20px;
	font-weight: 700;
	color: #333;
}

.navbar {
	position: relative;
	padding: 20px;
	background-color: #fff;
	border-radius: 50px;
}

.navbar input {
	width: 40px;
	height: 40px;
	cursor: pointer;
	opacity: 0;
}

.navbar span {
	width: 30px;
	height: 4px;
	border-radius: 15px;
	background-color: #999;
	position: absolute;
	left: 25px;
	top: calc(50% - 10px);
	pointer-events: none;
	transition: transform 0.3s, ease-in-out 0.3s, top 0.3s ease-in-out;
}

.navbar span:nth-child(3) {
	top: calc(50% + 6px);
}

.navbar ul {
	width: 0;
	overflow: hidden;
	transition: all 0.5s;
	white-space: nowrap;
}

.navbar ul li {
	margin: 0 15px;
	list-style: none;
}
.navbar ul li:hover {
	color: #fff;
}
.navbar input:checked ~ ul {
	width: 350px;
}

.navbar input:checked ~ span:nth-child(3) {
	top: calc(50% - 2px);
	transform: rotate(45deg);
	background-color: #fb7299;
	transition: top 0.3s ease-in-out, transform 0.3s, ease-in-out 0.3s;
}

.navbar input:checked ~ span:nth-child(2) {
	top: calc(50% - 2px);
	transform: rotate(-45deg);
	background-color: #fb7299;
	transition: top 0.3s ease-in-out, transform 0.3s, ease-in-out 0.3s;
}
a {
	cursor: pointer;
}
a:hover {
	color: #ddd !important;
}
</style>
