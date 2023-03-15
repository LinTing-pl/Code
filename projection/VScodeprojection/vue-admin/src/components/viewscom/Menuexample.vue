<script setup lang="ts">
import { defineAsyncComponent } from "vue";
import Loading4 from "../loading/Loading4.vue";
const MusicPlayer = defineAsyncComponent(() => import("../MusicPlayer.vue"));
const CarouselMap = defineAsyncComponent(() => import("../CarouselMap.vue"));
const Navigationbar1 = defineAsyncComponent(
	() => import("../Navigationbar1.vue")
);
const Navigationbar2 = defineAsyncComponent(
	() => import("../Navigationbar2.vue")
);
const Navigationbar3 = defineAsyncComponent(
	() => import("../Navigationbar3.vue")
);
const Navigationbar4 = defineAsyncComponent(
	() => import("../Navigationbar4.vue")
);
</script>

<template>
	<div class="example-container">
		<div class="top">
			<div class="top-sub">
				<Suspense>
					<template #default>
						<MusicPlayer></MusicPlayer>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
			<div class="top-sub">
				<Suspense>
					<template #default>
						<CarouselMap></CarouselMap>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
		</div>
		<div class="bottom">
			<div class="bottom-sub">
				<Suspense>
					<template #default>
						<Navigationbar1></Navigationbar1>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
			<div class="bottom-sub">
				<Suspense>
					<template #default>
						<Navigationbar2></Navigationbar2>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
			<div class="bottom-sub">
				<Suspense>
					<template #default>
						<Navigationbar3></Navigationbar3>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
			<div class="bottom-sub">
				<Suspense>
					<template #default>
						<Navigationbar4></Navigationbar4>
					</template>
					<template #fallback><Loading4></Loading4></template>
				</Suspense>
			</div>
		</div>
	</div>
</template>

<style scoped lang="scss">
.example-container {
	height: 100%;
	width: 100%;
	position: relative;
	background: linear-gradient(#ff9a9e, #fecfef);
	overflow: hidden;
	display: flex;
	flex-direction: column;
	.top {
		flex: 1;
		display: flex;
		.top-sub {
			border: 1px dashed #f7f8fa;
			flex: 1;
			display: flex;
			justify-content: center;
			align-items: center;
			overflow: hidden;
			&:nth-child(2) {
				align-items: start;
			}
		}
	}
	.bottom {
		flex: 1;
		display: grid;
		grid-template-rows: repeat(2, 50%);
		grid-template-columns: repeat(2, 50%);
		.bottom-sub {
			border: 1px dashed #f7f8fa;
			display: flex;
			justify-content: center;
			align-items: center;
			overflow: hidden;
		}
	}
}
</style>
