<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading1 from "../components/loading/Loading1.vue";
const DVexample = defineAsyncComponent(
	() => import("../components/viewscom/DVexample.vue")
);
</script>

<template>
	<div ref="main" class="content-container">
		<Suspense>
			<template #default>
				<DVexample></DVexample>
			</template>
			<template #fallback>
				<Loading1></Loading1>
			</template>
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
