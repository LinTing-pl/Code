<script setup lang="ts"></script>

<template>
	<div class="loading">
		<div class="dot-box">
			<div class="dot" style="--i: 0"></div>
			<div class="dot" style="--i: 1"></div>
			<div class="dot" style="--i: 2"></div>
			<div class="dot" style="--i: 3"></div>
			<div class="dot" style="--i: 4"></div>
			<div class="dot" style="--i: 5"></div>
			<div class="dot" style="--i: 6"></div>
			<div class="dot" style="--i: 7"></div>
			<div class="dot" style="--i: 8"></div>
			<div class="dot" style="--i: 9"></div>
		</div>
		<p>敬请期待后续开发...</p>
		<div class="dot-box">
			<div class="dot" style="--i: 0"></div>
			<div class="dot" style="--i: 1"></div>
			<div class="dot" style="--i: 2"></div>
			<div class="dot" style="--i: 3"></div>
			<div class="dot" style="--i: 4"></div>
			<div class="dot" style="--i: 5"></div>
			<div class="dot" style="--i: 6"></div>
			<div class="dot" style="--i: 7"></div>
			<div class="dot" style="--i: 8"></div>
			<div class="dot" style="--i: 9"></div>
		</div>
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
	animation: colorChange 5s linear infinite;
	--c: gold;
}
.dot-box {
	display: flex;
}
.dot-box .dot {
	width: 20px;
	height: 20px;
	border-radius: 50%;
	background-color: var(--c);
	margin: 20px 10px;
	box-shadow: 0 0 10px var(--c), 0 0 20px var(--c), 0 0 40px var(--c),
		0 0 60px var(--c), 0 0 80px var(--c), 0 0 100px var(--c);
	transform: scale(0.1);
	animation: dotAnimate 2s linear infinite;
	animation-delay: calc(0.1s * var(--i));
}
.loading p {
	color: var(--c);
	font-size: 20px;
	font-weight: 500;
	letter-spacing: 5px;
}
.dot-box:nth-child(3) .dot {
	animation-delay: calc(-0.1s * var(--i));
}
@keyframes dotAnimate {
	0% {
		transform: scale(0.1);
	}
	10% {
		transform: scale(1);
	}
	50%,
	100% {
		transform: scale(0.1);
	}
}
@keyframes colorChange {
	0% {
		filter: hue-rotate(0deg);
	}
	100% {
		filter: hue-rotate(360deg);
	}
}
</style>
