<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading1 from "../components/loading/Loading1.vue";
const Locationexample = defineAsyncComponent(
	() => import("../components/viewscom/Locationexample.vue")
);
</script>

<template>
	<div class="content-container">
		<Suspense>
			<template #default><Locationexample></Locationexample></template>
			<template #fallback><Loading1></Loading1></template>
		</Suspense>
	</div>
</template>

<style scoped lang="scss">
.content-container {
	height: 80vh;
	margin: 24px 40px;
	min-height: 600px;
	min-width: 900px;
	background: #fff;
	display: flex;
	justify-content: center;
	align-items: center;
}
</style>
