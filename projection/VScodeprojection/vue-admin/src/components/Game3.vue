<script setup lang="ts">
import { onBeforeUnmount, onMounted, onUnmounted, ref } from "vue";

const emit = defineEmits(["reset"]);
const controllerClick = new AbortController();
const controllerContextMenu = new AbortController();
let timeId: any = null;
let timeCounter = ref(0);
const rows: number = 20;
const cols: number = 20;
const size: number = 30;
const res = ref([]);
const it = (e: any) => {
	(res.value as any).push(e);
};
let minesCount = ref(0);
const mines: any = [];
for (let i = 0; i < rows; i++) {
	for (let j = 0; j < cols; j++) {
		mines[i + "-" + j] = Math.random() > 0.9;
		minesCount.value += mines[i + "-" + j];
	}
}
const box = ref();
const message = ref();
let data: any = [];
let index = 0;
for (let i = 0; i < rows; i++) {
	for (let j = 0; j < cols; j++) {
		const isMines = mines[i + "-" + j];
		const number = Object.values({
			0: mines[`${i - 1}-${j - 1}`],
			1: mines[`${i - 1}-${j}`],
			2: mines[`${i - 1}-${j + 1}`],
			3: mines[`${i}-${j - 1}`],
			4: mines[`${i}-${j + 1}`],
			5: mines[`${i + 1}-${j - 1}`],
			6: mines[`${i + 1}-${j}`],
			7: mines[`${i + 1}-${j + 1}`],
		}).filter((v) => v).length;
		data.push([`${i}-${j}`, isMines, number]);
		index++;
	}
}
onMounted(() => {
	res.value.forEach((v: any) => {
		v.addEventListener(
			"click",
			(e: any) => {
				v.classList.remove("hide");
				if (
					minesCount.value ===
					box.value.querySelectorAll(".hide").length
				) {
					clearInterval(timeId);
					let r = confirm(
						`恭喜您成功了,用时${timeCounter.value}秒,是否重新开始游戏？`
					);
					if (r) {
						emit("reset", true);
					} else {
						controllerClick.abort();
						controllerContextMenu.abort();
					}
				} else if (v.querySelector(".circle")) {
					setTimeout(() => {
						clearInterval(timeId);
						let r = confirm(
							`游戏失败，猜中地雷了。用时${timeCounter.value}秒,是否重新开始游戏？`
						);
						if (r) {
							emit("reset", true);
						} else {
							controllerClick.abort();
							controllerContextMenu.abort();
						}
					}, 100);
				} else if (v.innerText.trim() === "") {
					const indexs = v
						.getAttribute("data-v")
						.split("-")
						.map((v: any) => Number(v));
					const loop = (indexs: any) => {
						[
							[indexs[0] - 1, indexs[1] - 1],
							[indexs[0] - 1, indexs[1]],
							[indexs[0] - 1, indexs[1] + 1],
							[indexs[0], indexs[1] - 1],
							[indexs[0], indexs[1] + 1],
							[indexs[0] + 1, indexs[1] - 1],
							[indexs[0] + 1, indexs[1]],
							[indexs[0] + 1, indexs[1] + 1],
						].forEach((subIndexs) => {
							const el = document.querySelector(
								`[data-v='${subIndexs.join("-")}']`
							);
							if (el) {
								const text = (el as any)
									.querySelector(".number")
									.innerText.trim();
								if (
									el.className.indexOf("hide") >= 0 &&
									text === ""
								) {
									el.classList.remove("hide");
									loop(subIndexs);
								} else {
									el.classList.remove("hide");
								}
							}
						});
					};
					loop(indexs);
				}
			},
			{ signal: controllerClick.signal }
		);
		v.addEventListener(
			"contextmenu",
			(e: any) => {
				v.classList.toggle("info");
				message.value.innerHTML = `地雷${
					minesCount.value -
					box.value.querySelectorAll(".info").length
				}`;
				e.preventDefault();
			},
			{ signal: controllerContextMenu.signal }
		);
	});
	timeId = setInterval(() => {
		timeCounter.value++;
	}, 1000);
});
onBeforeUnmount(() => {
	controllerClick.abort();
	controllerContextMenu.abort();
});
</script>

<template>
	<div ref="box" class="box">
		<div ref="message" class="message"
			>地雷: {{ minesCount }} 时间：{{ timeCounter }}s</div
		>
		<div
			:ref="it"
			:data-v="item[0]"
			class="item hide"
			v-for="item in data"
			:key="item">
			<div class="circle" v-if="item[1]"></div>
			<div class="number" v-else>{{ item[2] ? item[2] : "" }}</div>
		</div>
	</div>
</template>

<style scoped>
.box {
	display: flex;
	flex-wrap: wrap;
	width: 500px;
	height: 500px;
	background: #fff;
	position: relative;
}
.item {
	border: 1px solid #ddd;
	box-sizing: border-box;
	display: flex;
	justify-content: center;
	align-items: center;
	cursor: pointer;
	width: 25px;
	height: 25px;
}
.item:hover {
	border: 1px solid #000;
}
.circle {
	border: 10px solid #a33939;
	border-radius: 50%;
}
.hide {
	background-color: #b3b1b1;
}
.hide > * {
	display: none;
}
.info::after {
	content: "雷";
	color: #a86868;
}
.message {
	font-size: 14px;
	position: absolute;
	left: 50%;
	top: -52px;
	transform: translate(-50%, 0);
	font-weight: bold;
	font-size: 20px;
}
</style>
