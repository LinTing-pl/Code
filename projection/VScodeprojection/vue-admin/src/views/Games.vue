<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading1 from "../components/loading/Loading1.vue";

const Gamesexample = defineAsyncComponent(
	() => import("../components/viewscom/Gamesexample.vue")
);
</script>

<template>
	<div class="content-container">
		<Suspense>
			<template #default><Gamesexample></Gamesexample></template>
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
	background: #fff;
	overflow: hidden;
	display: flex;
	justify-content: center;
	align-items: center;
}
</style>
