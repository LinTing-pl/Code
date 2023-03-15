<script setup lang="ts">
import { random } from "lodash";
import { onBeforeUnmount, onMounted, ref } from "vue";
const emit = defineEmits(["reset"]);
const rows: number = 20;
const cols: number = 20;
const size: number = 20;
const score = ref(0);
let intervalId: any;
const mf = ref();
const res: any = ref([]);
const it = (e: any) => {
	(res.value as any).push(e);
};
const player = [[1, 1]];
let key = "";
const updatePlayer = () => {
	mf.value
		.querySelectorAll(".player")
		.forEach((v: any) => v.classList.remove("player"));
	player.forEach((v) => {
		mf.value
			.querySelector(`[data-v='${v.join("-")}']`)
			.classList.add("player");
		if (
			res.value.filter((v: any) => v.className.indexOf("eat") !== -1)
				.length === 0
		) {
			let i = Math.floor(Math.random() * 400);
			res.value[i].classList.add("eat");
		}
	});
};
const keydown = (e: any) => {
	key = e.key;
};
onMounted(() => {
	let index = 0;
	for (let i = 0; i < rows; i++) {
		for (let j = 0; j < cols; j++) {
			res.value[index].setAttribute("data-v", `${i}-${j}`);
			if (Math.random() > 0.9) {
				res.value[index].classList.add("eat");
			}
			index++;
		}
	}
	document.addEventListener("keydown", keydown);
	intervalId = setInterval(() => {
		if (key) {
			const needPos = JSON.parse(
				JSON.stringify(player.slice(0, player.length - 1))
			);
			switch (key) {
				case "w":
					player[0][0] -= 1;
					break;
				case "a":
					player[0][1] -= 1;
					break;
				case "s":
					player[0][0] += 1;
					break;
				case "d":
					player[0][1] += 1;
					break;
			}
			const el = mf.value.querySelector(
				`[data-v='${player[0].join("-")}']`
			);
			if (!el) {
				clearInterval(intervalId);
				let r = confirm(
					`撞墙了,游戏结束。得分：${score.value}分,是否重新开始游戏？`
				);
				document.removeEventListener("keydown", keydown);
				if (r) {
					emit("reset", true);
				}
			} else {
				for (let i = 1; i <= player.length - 1; i++) {
					player[i] = needPos[i - 1];
				}
				if (el.className.indexOf("eat") >= 0) {
					el.classList.remove("eat");
					player.push([...player[0]]);
					score.value++;
				}
				updatePlayer();
			}
		}
	}, 100);
	updatePlayer();
});
onBeforeUnmount(() => {
	document.removeEventListener("keydown", keydown);
	clearInterval(intervalId);
});
</script>

<template>
	<div ref="mf" class="mf">
		<div :ref="it" class="item" v-for="item in 400" :key="item"></div>
		<span class="score">分数：{{ score }}</span>
	</div>
</template>

<style scoped>
.mf {
	border: 1px solid #ddd;
	display: flex;
	flex-wrap: wrap;
	width: 400px;
	position: relative;
}
.item {
	box-sizing: border-box;
	border: 1px solid #ddd;
	width: 20px;
	height: 20px;
}
.eat {
	background-color: rosybrown;
}
.player {
	background-color: #444;
}
.score {
	position: absolute;
	left: 50%;
	top: -80px;
	font-weight: bold;
	font-size: 30px;
	transform: translate(-50%, 0);
}
</style>
