<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from "vue";
import Intro from "../../utils/intro";
import mp3Url from "../../assets/mp3/juwairen.mp3?url";
const audioEle = ref();
const cvs = ref();
let isInit = false;
let isEnable: boolean = false;
let ctx: any;
let dataArray: any;
let analyser: any;
let alpha = 99;
let up = false;
let t: any;
const colorArray = ["#33ccff", "#ff99cc"];
let color = colorArray[0];
const homeSteps = {
	shifts: {
		step: "1",
		intro: "上传音频。",
		position: "top",
	},
	attendGroup: {
		step: "2",
		intro: "点击播放。",
		position: "top",
	},
	writeOff: {
		step: "3",
		intro: "实现音频可视化。",
		position: "bottom",
	},
};
onMounted(() => {
	if (localStorage.getItem("isShowHelp") === "1") {
		Intro.start();
		// 退出引导回调函数
		Intro.onexit(function () {
			localStorage.setItem("isShowHelp", "2");
		});
	}
});
onBeforeUnmount(() => {
	isEnable = false;
});

const changeHandler = (e: any) => {
	const file = e.target.files[0];
	if (file) {
		const reader = new FileReader();
		reader.readAsDataURL(file);
		reader.onload = function (e) {
			audioEle.value.src = e.target?.result;
		};
	}
};

const init = () => {
	if (isInit) {
		isEnable = true;
		clearTimeout(t);
		draw();
		return;
	}
	ctx = cvs.value.getContext("2d");
	const audCtx = new AudioContext();
	const source = audCtx.createMediaElementSource(audioEle.value);
	analyser = audCtx.createAnalyser();
	analyser.fftSize = 512;
	dataArray = new Uint8Array(analyser.frequencyBinCount);
	source.connect(analyser);
	analyser.connect(audCtx.destination);
	isInit = true;
	isEnable = true;
	draw();
};
const draw = () => {
	if (!isInit) return;
	if (!isEnable) return;
	requestAnimationFrame(draw);
	const { width, height } = cvs.value;
	ctx.clearRect(0, 0, width, height);
	analyser.getByteFrequencyData(dataArray);
	const len = dataArray.length / 2.5;
	const barWidth = width / len / 2;
	ctx.fillStyle = color + Math.ceil(alpha);
	if (up) {
		alpha = alpha + 0.5;
		if (alpha === 99) up = false;
	} else {
		alpha = alpha - 0.5;
		if (alpha === 50) {
			up = true;
			color === colorArray[0]
				? (color = colorArray[1])
				: (color = colorArray[0]);
		}
	}
	for (let i = 0; i < len; i++) {
		const data = dataArray[i];
		const barHeight = (data / 255) * height;
		const x1 = i * barWidth + width / 2;
		const x2 = width / 2 - (i + 1) * barWidth;
		const y = height - barHeight;
		ctx.fillRect(x1, y, barWidth - 3, barHeight);
		ctx.fillRect(x2, y, barWidth - 3, barHeight);
	}
};
const pause = () => {
	t = setTimeout(() => {
		isEnable = false;
	}, 2000);
};
const pushModel = () => {
	audioEle.value.setAttribute("src", mp3Url);
};
</script>

<template>
	<div class="example-container">
		<canvas
			ref="cvs"
			:data-step="homeSteps.writeOff.step"
			:data-intro="homeSteps.writeOff.intro"
			:data-position="homeSteps.writeOff.position"
			:data-disable-interaction="true"></canvas>
		<div class="opts">
			<span class="model" @click="pushModel">样品</span>
			<label for="ipt">
				<span
					class="up"
					:data-step="homeSteps.shifts.step"
					:data-intro="homeSteps.shifts.intro"
					:data-position="homeSteps.shifts.position"
					:data-disable-interaction="true"
					>上传</span
				>
			</label>
			<audio
				ref="audioEle"
				src=""
				controls
				@play="init"
				@pause="pause"
				:data-step="homeSteps.attendGroup.step"
				:data-intro="homeSteps.attendGroup.intro"
				:data-position="homeSteps.attendGroup.position"
				:data-disable-interaction="true"></audio>
			<input
				id="ipt"
				type="file"
				style="display: none"
				@change="changeHandler"
				accept="audio/*,video/*" />
		</div>
	</div>
</template>

<style scoped lang="scss">
.example-container {
	height: 100%;
	width: 100%;
	background: #fff;
	position: relative;
	display: flex;
	flex-direction: column;
	canvas {
		margin: 20px;
		height: 200px;
		background: #000;
		flex: 1;
	}
	.opts {
		flex-shrink: 0;
		align-self: center;
		position: relative;
		span {
			position: absolute;
			border: 1px solid transparent;
			top: 5px;
			padding: 8px 12px;
			font-size: 17px;
			background: #f1f3f4;
			border-radius: 8px;
			cursor: pointer;
		}
		span:hover {
			border-color: #646cff;
		}
		.up {
			left: -80px;
		}
		.model {
			left: -150px;
		}
		audio {
			border: 1px solid transparent;
			border-radius: 26px;
		}
		audio:hover {
			border-color: #646cff;
		}
	}
}
</style>
