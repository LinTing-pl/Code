<script setup lang="ts"></script>

<template>
	<div class="loading">
		<div style="--x: 0"></div>
		<div style="--x: 1"></div>
		<div style="--x: 2"></div>
		<div style="--x: 3"></div>
		<div style="--x: 4"></div>
		<div style="--x: 5"></div>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

.loading {
	display: flex;
}

.loading div {
	position: relative;
	width: 40px;
	height: 120px;
	background-image: linear-gradient(180deg, rgba(0, 0, 0, 0.05), #eef1f5);
	margin: 8px;
	border-radius: 20px;
	border: 2px solid #eef1f5;
	box-shadow: 15px 15px 20px rgba(0, 0, 0, 0.1), -15px -15px 20px #fff,
		inset -5px -5px 5px rgba(255, 255, 255, 0.5);
	overflow: hidden;
}

.loading div::before {
	content: "·";
	position: absolute;
	top: 0;
	left: 0;
	width: 36px;
	height: 36px;
	line-height: 36px;
	text-align: center;
	border-radius: 50%;
	box-shadow: inset -5px -5px 5px rgba(0, 0, 0, 0.1),
		0 420px 0 400px lightskyblue;
	animation: animate 2s ease-in-out infinite;
	animation-delay: calc(var(--x) * 0.2s);
	transform: translateY(160px);
}
.loading div:nth-child(1):before {
	content: "加";
}
.loading div:nth-child(2):before {
	content: "载";
}
.loading div:nth-child(3):before {
	content: "中";
}
@keyframes animate {
	0% {
		transform: translateY(80px);
		filter: hue-rotate(0deg);
	}
	50% {
		transform: translateY(0px);
		filter: hue-rotate(180deg);
	}
	100% {
		transform: translateY(80px);
		filter: hue-rotate(360deg);
	}
}
</style>
