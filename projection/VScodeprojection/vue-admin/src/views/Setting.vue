<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading1 from "../components/loading/Loading1.vue";
const Settingexample = defineAsyncComponent(
	() => import("../components/viewscom/Settingexample.vue")
);
</script>

<template>
	<div class="content-container">
		<Suspense>
			<template #default><Settingexample></Settingexample></template>
			<template #fallback><Loading1></Loading1></template>
		</Suspense>
	</div>
</template>

<style scoped lang="scss">
.content-container {
	height: 80vh;
	min-height: 600px;
	min-width: 900px;
	margin: 20px 40px;
	display: flex;
	justify-content: center;
	align-items: center;
}
</style>
