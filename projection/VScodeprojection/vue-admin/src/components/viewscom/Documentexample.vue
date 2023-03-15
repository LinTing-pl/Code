<script setup lang="ts">
import { ref } from "vue";
import "../../assets/iconfont/iconfont.js";
import { useDocStore } from "../../store/docStore";
const edit = ref();
const info = ref();
const title = ref();
const content = ref();
const useDoc = useDocStore();
let id: any;
const list = ref(useDoc.docList);
let data = ref({ id: null, title: "", content: "" });
let temp: any;
let flag: boolean = false;
function dragover(event: any) {
	event.preventDefault();
	event.dataTransfer.dropEffect = "move";
}
function dragstart(e: any, item: any) {
	edit.value.classList.add("is-active");
	info.value.style.display = "inline";
	temp = item;
	Array.from(e.target.parentNode.children).map((v: any) => {
		v.classList.remove("active");
	});
	e.target.classList.add("active");
}
function dragend() {
	edit.value.classList.remove("is-active");
	edit.value.classList.remove("is-active1");
	info.value.innerText = "拖放此处";
	info.value.style.display = "none";
}
function dragenter() {
	edit.value.classList.add("is-active1");
	info.value.innerText = "松开鼠标";
}
function dragleave(e: any) {
	edit.value.classList.remove("is-active1");
	info.value.innerText = "拖放此处";
}
function mouseup(e: any) {
	data.value = temp;
	id = temp.id;
	e.target.setAttribute("contenteditable", true);
}
function confirm() {
	if (!!title.value.innerText || !!content.value.innerText) {
		data.value.title = title.value.innerText;
		data.value.content = content.value.innerText;
		useDoc.update(data);
	}
}
function del() {
	if (!!id) {
		useDoc.delete(id);
		id = null;
		data.value = { id: null, title: "", content: "" };
		edit.value.removeAttribute("contenteditable");
	}
}
function add() {
	if (list.value[0].content.length || list.value[0].title.length) {
		useDoc.add({ title: "", content: "" });
		id = list.value[0].id;
		(data.value as any) = list.value[0];
		edit.value.setAttribute("contenteditable", "true");
	}
}
</script>

<template>
	<div class="example-container" @dragover="dragover">
		<div class="edit" ref="edit">
			<div class="top">
				<svg class="icon icon1" aria-hidden="true" @click="del">
					<use xlink:href="#icon-jianqu"></use>
				</svg>
				<svg class="icon icon2" aria-hidden="true" @click="confirm">
					<use xlink:href="#icon-confirm-circle"></use>
				</svg>
			</div>
			<div
				class="down"
				@dragenter="dragenter"
				@dragleave="dragleave"
				@drop="mouseup">
				<h2 ref="title">{{ data.title }}</h2>
				<div ref="content">
					{{ data.content }}
				</div>
				<span ref="info" class="info" v-show="!id">拖放此处</span>
			</div>
		</div>
		<div class="list">
			<div class="top">
				<svg class="icon icon3" aria-hidden="true" @click="add">
					<use xlink:href="#icon-add"></use>
				</svg>
			</div>
			<div class="down">
				<div
					class="item"
					v-for="(item, index) in list"
					draggable="true"
					@dragstart="dragstart($event, item)"
					@dragend="dragend">
					<h3>{{ item.title.replaceAll(" ", "") }}</h3>
					<div>
						{{ item.content }}
					</div>
				</div>
			</div>
		</div>
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
	.edit {
		height: 80%;
		width: 40%;
		min-width: 300px;
		border: 25px solid #edeff2;
		box-shadow: inset 0 0 10px #edeff2;
		border-radius: 20px;
		margin-right: 20px;
		position: relative;
		display: flex;
		flex-direction: column;
		.top {
			.icon {
				position: absolute;
				cursor: pointer;
				&:hover {
					width: 1.6em;
					height: 1.6em;
					filter: drop-shadow(0 0 6px #1296db);
				}
			}
			.icon1 {
				width: 1.34em;
				height: 1.34em;
				right: 40px;
				top: -23px;
			}
			.icon2 {
				top: -24px;
				right: 0;
			}
		}
		.down {
			display: flex;
			flex-direction: column;
			overflow-x: hidden;
			overflow-y: auto;
			flex: 1;
			display: flex;
			flex-direction: column;
			.info {
				position: absolute;
				left: 50%;
				top: 50%;
				transform: translate(-50%, -50%);
				border: 1px dashed #000;
				font-size: 20px;
				pointer-events: none;
			}
			h2 {
				word-break: break-all;
				line-height: 20px;
				margin: 0;
				padding: 10px;
				border: 1px solid transparent;
				border-radius: 10px;
				flex-shrink: 0;
				pointer-events: none;
			}
			div {
				margin: 0;
				padding: 10px;
				word-break: break-all;
				border: 1px solid transparent;
				flex: 1;
				border-radius: 10px;
				pointer-events: none;
			}
			&::-webkit-scrollbar {
				width: 3px;
			}
			&:hover::-webkit-scrollbar-thumb {
				background-color: rgba(0, 0, 0, 0.2);
				border-radius: 20px;
				-webkit-box-shadow: inset1px1px0rgba(0, 0, 0, 0.1);
			}
			&::-webkit-scrollbar-track {
				background: #fff;
			}
		}
	}
	.list {
		height: 80%;
		width: 30%;
		background: #edeff2;
		border-top: 25px solid #edeff2;
		border-bottom: 25px solid #edeff2;
		border-radius: 25px;
		display: flex;
		flex-direction: column;
		position: relative;
		box-shadow: 0 0 5px #edeff2;
		.top {
			.icon3 {
				position: absolute;
				right: 20px;
				top: -20px;
				width: 1.8em;
				height: 1.8em;
				cursor: pointer;
				&:hover {
					width: 2em;
					height: 2em;
					filter: drop-shadow(0 0 6px #1296db);
				}
			}
		}
		.down {
			display: flex;
			flex-direction: column;
			align-items: center;
			overflow-y: auto;
			overflow-x: hidden;
			&::-webkit-scrollbar {
				width: 3px;
			}
			&:hover::-webkit-scrollbar-thumb {
				background-color: rgba(0, 0, 0, 0.2);
				border-radius: 20px;
				-webkit-box-shadow: inset 1px 1px 0 rgba(0, 0, 0, 0.1);
			}
			&::-webkit-scrollbar-track {
				background: #edeff2;
			}
			.item {
				width: 90%;
				background: #fff;
				margin: 10px;
				border-radius: 10px;
				padding: 0 5px;
				&:hover {
					border: 1px solid #000;
					box-shadow: 0 0 6px rgb(228, 235, 136);
					cursor: pointer;
				}
				h3 {
					min-height: 28px;
					margin: 0;
					overflow: hidden;
					text-overflow: ellipsis;
				}
				div {
					min-height: 24px;
					word-break: break-all;
					display: -webkit-box;
					overflow: hidden;
					-webkit-line-clamp: 3;
					-webkit-box-orient: vertical;
					text-overflow: ellipsis;
				}
			}
		}
	}
}
.is-active {
	border-color: rgb(66, 66, 221) !important;
}
.is-active1 {
	box-shadow: 0 0 20px rgb(66, 66, 221), 0 0 40px rgb(66, 66, 221),
		inset 0 0 10px rgb(66, 66, 221) !important;
}
.active {
	border: 1px solid #000;
	box-shadow: 0 0 6px rgb(228, 235, 136);
	cursor: pointer;
}
</style>
