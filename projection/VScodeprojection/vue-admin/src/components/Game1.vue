<script setup lang="ts">
import { onMounted, ref } from "vue";
const emit = defineEmits(["reset"]);
const gamemap = ref();
const rows: number = 3;
const cols: number = 3;
const size: number = 120;
const itemEls = ref([]);
const posClsName: any = [];
const item = (e: any) => {
	(itemEls.value as any).push(e);
};
onMounted(() => {
	let index = 0;
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
			(itemEls.value[index] as any).setAttribute("data-v", `${i}-${j}`);
			(
				itemEls.value[index] as any
			).style.cssText = `width:${size}px;height:${size}px;`;
			posClsName.push(`s${i}-${j}`);
			index++;
		}
	}
	gamemap.value.style.width = `${size * cols}px`;
	const list = [...gamemap.value.childNodes];
	list.sort(() => {
		return Math.random() - 0.5;
	});
	list.forEach((el) => {
		el.classList.add(posClsName.shift());
		el.onclick = () => {
			const indexs = el
				.getAttribute("data-v")
				.split("-")
				.map((v: any) => Number(v));
			[
				`${indexs[0] - 1}-${indexs[1]}`,
				`${indexs[0] + 1}-${indexs[1]}`,
				`${indexs[0]}-${indexs[1] - 1}`,
				`${indexs[0]}-${indexs[1] + 1}`,
			].forEach((v) => {
				const makeEl = gamemap.value.querySelector(`[data-v='${v}']`);
				if (makeEl && makeEl.classList.contains("hide")) {
					const sCls = makeEl.classList[1];
					makeEl.className = `map-item ${el.classList[1]}`;
					el.className = `map-item ${sCls} hide`;
				}
			});
			let isOk = list.every((el) => {
				return "s" + el.getAttribute("data-v") === el.classList[1];
			});
			if (isOk) {
				setTimeout(() => {
					let r = confirm("拼接成功,是否重新开始游戏？");
					if (r) {
						emit("reset", true);
					} else {
						list.forEach((el) => {
							el.onclick = null;
						});
					}
				}, 250);
			}
		};
	});
	gamemap.value
		.querySelector(`.s${rows - 1}-${cols - 1}`)
		.classList.add("hide");
});
</script>

<template>
	<div ref="gamemap" class="gamemap">
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
		<div :ref="item" class="map-item"></div>
	</div>
</template>

<style scoped lang="scss">
.gamemap {
	display: flex;
	flex-wrap: wrap;
	.map-item {
		background-image: url(../assets/img/cat.jpeg?url);
		box-sizing: border-box;
		background-size: 360px 360px;
	}
	.hide {
		opacity: 0;
		pointer-events: none;
	}
	.s0-0 {
		background-position: 0 0;
	}
	.s0-1 {
		background-position: -120px 0;
	}
	.s0-2 {
		background-position: -240px 0;
	}
	.s1-0 {
		background-position: 0 -120px;
	}
	.s1-1 {
		background-position: -120px -120px;
	}
	.s1-2 {
		background-position: -240px -120px;
	}
	.s2-0 {
		background-position: 0 -240px;
	}
	.s2-1 {
		background-position: -120px -240px;
	}
	.s2-2 {
		background-position: -240px -240px;
	}
}
</style>
