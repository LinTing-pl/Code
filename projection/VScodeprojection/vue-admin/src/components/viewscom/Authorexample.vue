<script setup lang="ts">
import { getCurrentInstance, ref } from "vue";
import img from "../../assets/img/linting.jpeg";
const proxy: any = getCurrentInstance();
const _this: any = proxy.appContext.config.globalProperties;
let success = ref(false);
_this.$axios.get("/author/get").then((resp: any) => {
	success.value = resp.data.success;
	console.log(resp.data);
});
</script>

<template>
	<div class="example-container">
		<img src="../../assets/img/linting.jpeg" />
	</div>
</template>

<style scoped lang="scss">
.example-container {
	height: 100%;
	width: 100%;
	background: #fff;
	display: flex;
	justify-content: center;
	align-items: center;
	img {
		width: 100%;
		height: 100%;
		object-fit: contain;
	}
}
</style>
