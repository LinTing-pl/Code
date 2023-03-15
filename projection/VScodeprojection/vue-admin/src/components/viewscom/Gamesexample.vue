<script setup lang="ts">
import { onMounted, ref } from "vue";
import Game1 from "../Game1.vue";
import Game2 from "../Game2.vue";
import Game3 from "../Game3.vue";
const ipt1 = ref();
const ipt2 = ref();
const ipt3 = ref();
const game = ref(sessionStorage.getItem("game") || "game1");
const click = (g: string) => {
	game.value = g;
	sessionStorage.setItem("game", g);
};
const reset = () => {
	let temp = game.value;
	game.value = "";
	setTimeout(() => {
		game.value = temp;
	}, 250);
};
onMounted(() => {
	switch (game.value) {
		case "game1":
			ipt1.value.setAttribute("checked", "");
			break;
		case "game2":
			ipt2.value.setAttribute("checked", "");
			break;
		case "game3":
			ipt3.value.setAttribute("checked", "");
			break;
	}
});
</script>

<template>
	<div class="example-container">
		<div class="opts">
			<input
				ref="ipt1"
				type="radio"
				style="display: none"
				id="g1"
				name="game" />
			<input
				ref="ipt2"
				type="radio"
				style="display: none"
				id="g2"
				name="game" />
			<input
				ref="ipt3"
				type="radio"
				style="display: none"
				id="g3"
				name="game" />
			<label class="game-opt g1" @click="click('game1')" for="g1"
				>拼图</label
			>
			<label class="game-opt g2" @click="click('game2')" for="g2"
				>贪吃蛇</label
			>
			<label class="game-opt g3" @click="click('game3')" for="g3"
				>扫雷</label
			>
			<button @click="reset">重新开始</button>
		</div>

		<div class="game-content">
			<Game1 v-if="game === 'game1'" @reset="reset"></Game1>
			<Game2 v-else-if="game === 'game2'" @reset="reset"></Game2>
			<Game3 v-else-if="game === 'game3'" @reset="reset"></Game3>
		</div>
	</div>
</template>

<style scoped lang="scss">
.example-container {
	height: 100%;
	width: 100%;
	position: relative;
	background-image: linear-gradient(200deg, #5ee7df, #b490ca);
	overflow: hidden;
	display: flex;
	justify-content: center;
	align-items: center;
	user-select: none;
	.opts {
		padding: 10px;
		position: absolute;
		left: 0;
		top: 0;
		.game-opt {
			position: relative;
			display: inline-block;
			width: 66px;
			height: 44px;
			margin-right: 10px;
			text-align: center;
			line-height: 44px;
			font-size: 16px;
			color: #fff;
			background-image: linear-gradient(
				90deg,
				#03a9f4,
				#f441a5,
				#ffeb3b,
				#09a8f4
			);
			border-radius: 50px;
			background-size: 400%;
			z-index: 1;
			cursor: pointer;
		}

		.game-opt::before {
			content: "";
			position: absolute;
			top: -5px;
			left: -5px;
			bottom: -5px;
			right: -5px;
			background-image: linear-gradient(
				90deg,
				#03a9f4,
				#f441a5,
				#ffeb3b,
				#09a8f4
			);
			border-radius: 50px;
			background-size: 400%;
			z-index: -1;
			filter: blur(20px);
		}

		#g1:checked ~ .g1,
		#g2:checked ~ .g2,
		#g3:checked ~ .g3,
		.game-opt:hover {
			color: #ddd;
			animation: streamer 8s infinite;
		}

		#g1:checked ~ .g1::before,
		#g2:checked ~ .g2::before,
		#g3:checked ~ .g3::before,
		.game-opt:hover::before {
			animation: streamer 8s infinite;
		}

		@keyframes streamer {
			100% {
				background-position: -400% 0;
			}
		}
	}
	.game-content {
		border: 10px solid #78cdd9;
		padding: 15px;
		border-radius: 24px;
		background: #fff;
		box-shadow: 0px 0px 5px #92b1d2, inset 0 0 15px #92b1d2;
	}
}
</style>
