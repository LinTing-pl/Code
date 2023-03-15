<script setup lang="ts">
import mapHtml from "../../assets/html/map.html?url";
</script>

<template>
	<div class="example-container">
		<div class="info">
			<span
				>由于不可抗力因素，地图可能存在无法使用情况，敬请期待后续开发。</span
			>
		</div>
		<iframe :src="mapHtml" frameborder="0"></iframe>
	</div>
</template>

<style scoped lang="scss">
.example-container {
	height: 100%;
	width: 100%;
	background: #fff;
	iframe {
		height: 100%;
		width: 100%;
		border: 1px solid #ddd;
		box-shadow: 0 0 2px #ddd;
	}
	.info {
		background: rgb(221, 228, 12);
		width: 100vmax;
		height: 22.5px;
		position: absolute;
		left: 0px;
		top: 47px;
		z-index: 99;
		overflow: hidden;
		font-size: 15px;
	}
	span {
		position: absolute;
		right: -490px;
		animation: move 15s linear infinite;
	}
	@keyframes move {
		0% {
			transform: translateX(0);
		}
		100% {
			transform: translateX(-1800px);
		}
	}
}
</style>
