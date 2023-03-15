<script setup lang="ts">
const props = defineProps(["handler"]);
</script>

<template>
	<input
		ref="menuBtn"
		type="checkbox"
		id="menu-ipt"
		@click="props.handler"
		style="display: none"
		checked />
	<label for="menu-ipt"><span></span><span></span><span></span></label>
</template>

<style scoped>
label {
	position: absolute;
	right: -35px;
	top: 10px;
	width: 30px;
	height: 30px;
	border: 1px solid #545c64;
	cursor: pointer;
	z-index: 20;
}
label:hover {
	box-shadow: 0 0 6px #545c64;
}
span {
	content: "";
	width: 20px;
	height: 2px;
	background: #545c64;
	position: absolute;
	left: 5px;
	transform: rotate(0);
	transition: all 0.5s;
}
span:nth-child(1) {
	top: 7px;
}
span:nth-child(2) {
	top: 14px;
}
span:nth-child(3) {
	top: 21px;
}
input:checked ~ label span {
	transform: rotate(90deg);
}
input:checked ~ label span:nth-child(1) {
	top: 14px;
	left: -2px;
}
input:checked ~ label span:nth-child(3) {
	top: 14px;
	left: 12px;
}
</style>
