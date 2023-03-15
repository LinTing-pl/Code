<script setup lang="ts">
// import "../assets/iconfont/iconfont.js";
</script>

<template>
	<div class="search-container">
		<div class="search-box">
			<input type="text" class="search-txt" placeholder="想搜啥？" />
			<a class="search-btn"><span class="iconfont icon-search"></span></a>
		</div>
	</div>
</template>

<style scoped>
@import url("../assets/iconfont/iconfont.css");
.search-container {
	margin: 0;
	padding: 0;
}
.search-box {
	background-color: #545c64;
	height: 30px;
	padding: 2px;
	border-radius: 40px;
	display: flex;
	justify-content: space-between;
	border: 1px solid #2f3640;
}
.search-txt {
	border: none;
	background: none;
	outline: none;
	padding: 0;
	color: #fff;
	font-size: 16px;
	line-height: 40px;
	width: 0;
	transition: all 0.4s;
	text-indent: 6px;
}
.search-txt::placeholder {
	color: #fff;
}
.search-btn {
	color: #e84118;
	width: 30px;
	height: 30px;
	border-radius: 50%;
	background-color: #545c64;
	display: flex;
	justify-content: center;
	align-items: center;
	cursor: pointer;
	transition: all 0.4s;
}
.search-txt:focus,
.search-box:hover .search-txt {
	width: 200px;
	padding: 0 6px;
}
.search-box:hover .search-btn {
	background-color: #fff;
}
</style>
