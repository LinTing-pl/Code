<script setup lang="ts"></script>

<template>
	<div class="loading">
		<div class="loading-content">
			<span style="--i: 1"></span>
			<span style="--i: 2"></span>
			<span style="--i: 3"></span>
			<span style="--i: 4"></span>
			<span style="--i: 5"></span>
			<span style="--i: 6"></span>
			<span style="--i: 7"></span>
		</div>
		<svg>
			<filter id="gooey">
				<feGaussianBlur
					in="SourceGraphic"
					stdDeviation="10"></feGaussianBlur>
				<feColorMatrix
					values="
          1 0 0 0 0
          0 1 0 0 0
          0 0 1 0 0
          0 0 0 20 -10
          "></feColorMatrix>
			</filter>
		</svg>
		<div class="loading-info">作者坐着火箭赶过来了，请稍后！</div>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
}
.loading {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
.loading-content {
	position: relative;
	width: 200px;
	height: 200px;
	filter: url(#gooey);
}

svg {
	width: 0;
	height: 0;
}

.loading-content span {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	display: block;
	animation: animate 4s ease-in-out infinite;
	animation-delay: calc(0.2s * var(--i));
}

.loading-content span::before {
	content: "";
	top: 0;
	position: absolute;
	left: calc(50% - 20px);
	width: 40px;
	height: 40px;
	border-radius: 50px;
	background-image: linear-gradient(#d1f5ff, #1683ff);
	box-shadow: 0 0 30px #1683ff;
}
.loading .loading-info {
	font-weight: bold;
	color: #ddd;
	font-size: 18px;
}
@keyframes animate {
	0% {
		transform: rotate(0deg);
	}
	50%,
	100% {
		transform: rotate(360deg);
	}
}
</style>
