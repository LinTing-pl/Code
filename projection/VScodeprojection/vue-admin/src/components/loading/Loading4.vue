<script setup lang="ts"></script>

<template>
	<div class="loading">
		<span>加载中...</span>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
}

.loading {
	width: 100px;
	height: 100px;
	box-sizing: border-box;
	border-radius: 50%;
	border-top: 10px solid #63a69f;
	filter: drop-shadow(0 0 5px #63a69f6c);
	position: relative;
	animation: a1 2s linear infinite;
}

.loading::before,
.loading::after {
	content: "";
	width: 100px;
	height: 100px;
	position: absolute;
	left: 0;
	top: -10px;
	box-sizing: border-box;
	border-radius: 50%;
}

.loading::before {
	border-top: 10px solid #f2e1ac;
	transform: rotate(120deg);
	filter: drop-shadow(0 0 5px #f2e1ac6c);
}

.loading::after {
	border-top: 10px solid #f2836b;
	transform: rotate(240deg);
	filter: drop-shadow(0 0 5px #f2836b6c);
}

.loading span {
	position: absolute;
	width: 100px;
	height: 100px;
	line-height: 100px;
	text-align: center;
	color: #fff;
	animation: a2 2s linear infinite;
	filter: blur(0px);
}

@keyframes a1 {
	to {
		transform: rotate(360deg);
	}
}

@keyframes a2 {
	to {
		transform: rotate(-360deg);
	}
}
</style>
