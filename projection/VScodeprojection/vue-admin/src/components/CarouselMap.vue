<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from "vue";
import img1 from "../assets/img/img1.jfif?url";
import img2 from "../assets/img/img2.jfif?url";
import img3 from "../assets/img/img3.jfif?url";
import img4 from "../assets/img/img4.jfif?url";
import img5 from "../assets/img/img5.jfif?url";
let big_box = ref();
let imgs = ref([]);
const img = (el: any) => {
	(imgs.value as Array<any>).push(el);
};
let timer: any = null;
let imgUrls = [img1, img2, img3, img4, img5];
let index = 0;
function reset() {
	for (let i = 0; i < imgs.value.length; i++) {
		(imgs.value[i] as HTMLDivElement).className = "img";
	}
}
function selected() {
	reset();
	(imgs.value[index] as HTMLDivElement).className = "img active";
}
function play() {
	timer = setInterval(function () {
		selected();
		index++;
		big_box.value.style.backgroundImage = "url(" + imgUrls[index - 1] + ")";
		if (index == 5) {
			index = 0;
		}
	}, 1500);
}
onMounted(() => {
	for (let i = 0; i < imgs.value.length; i++) {
		(imgs.value[i] as HTMLDivElement).onmousemove = function () {
			big_box.value.style.backgroundImage = "url(" + imgUrls[i] + ")";
			reset();
			clearInterval(timer);
			index = i + 1;
			if (index == 5) {
				index = 0;
			}
			play();
		};
	}
	play();
});
onBeforeUnmount(() => {
	clearInterval(timer);
});
</script>

<template>
	<div class="container">
		<div ref="big_box" class="big-box"></div>
		<div class="small-box">
			<div :ref="img" class="img"><img :src="img1" alt="" /></div>
			<div :ref="img" class="img"><img :src="img2" alt="" /></div>
			<div :ref="img" class="img"><img :src="img3" alt="" /></div>
			<div :ref="img" class="img"><img :src="img4" alt="" /></div>
			<div :ref="img" class="img"><img :src="img5" alt="" /></div>
		</div>
	</div>
</template>

<style scoped>
* {
	margin: 0;
	padding: 0;
}
.container {
	width: 100%;
	height: 85%;
	display: flex;
	justify-content: space-evenly;
	overflow: hidden;
	-webkit-box-reflect: below 13px
		linear-gradient(transparent 70%, rgba(0, 0, 0, 0.2));
}
.big-box {
	width: 75%;
	height: 100%;
	background-size: cover;
	transition: all 0.4s;
}
.small-box {
	width: 20%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}
.small-box .img {
	position: relative;
	width: 100%;
	height: 19%;
	right: 0;
	transition: all 0.5s;
}
.small-box .img img {
	width: 100%;
	height: 100%;
	object-fit: cover;
	right: 0;
	transition: all 0.5s;
	position: absolute;
}
.small-box .img.active {
	opacity: 0;
	right: 250px;
}
.small-box .img:hover img {
	opacity: 0;
	right: 250px;
}
</style>
