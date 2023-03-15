<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading2 from "../components/loading/Loading2.vue";
const Authorexample = defineAsyncComponent(
	() => import("../components/viewscom/Authorexample.vue")
);
</script>

<template>
	<div class="content-container">
		<Suspense>
			<template #default><Authorexample></Authorexample></template>
			<template #fallback><Loading2></Loading2></template>
		</Suspense>
	</div>
</template>

<style scoped>
.content-container {
	height: 80vh;
	min-height: 600px;
	min-width: 900px;
	margin: 20px 40px;
	background: #fff;
	display: flex;
	justify-content: center;
	align-items: center;
}
</style>
