<script setup lang="ts">
import { UploadFilled, Delete } from "@element-plus/icons-vue";
import { ElMessage, ElNotification } from "element-plus";
import { onMounted, ref } from "vue";

const ipt = ref();
const select = ref();
const data: any = ref([]);
let nums = ref(0);
let successNums = ref(0);
let size = ref(0);
let limit = 4;
const pool: any = [];
let max = ref(3);
let isShow = ref(false);
let curIpt: any = max.value;

const accept = [
	".jpg",
	".jpeg",
	".bmp",
	".webp",
	".gif",
	".png",
	".mp3",
	".mp4",
];
onMounted(() => {
	select.value.ondragenter = function (e: any) {
		e.preventDefault();
	};
	select.value.ondragover = function (e: any) {
		e.preventDefault();
	};
	select.value.ondrop = function (e: any) {
		e.preventDefault();
		for (const item of e.dataTransfer.items) {
			const entry = item.webkitGetAsEntry();
			dfs(entry);
		}
	};
});
const clickIpt = (cls: string) => {
	if (cls === "only") {
	} else if (cls === "mutiple") {
		ipt.value.setAttribute("webkitdirectory", "");
	}
	ipt.value.click();
};
const iptChange = (e: any) => {
	let files = e.target.files;
	if (files.length === 0) return;
	else if (files.length === 1) {
		let file = files[0];
		pushData(file);
	} else {
		Array.from(files).map((v: any) => {
			pushData(v);
		});
	}
	e.target.value = "";
};
const btnBlur = (cls: string) => {
	if (cls === "only") {
	} else if (cls === "mutiple") {
		ipt.value.removeAttribute("webkitdirectory");
	}
};
const pushData = (file: any) => {
	if (!validate(file)) {
		let now = "." + file.name.split(".").pop();
		ElMessage({
			showClose: true,
			message:
				"您选择的类型为" +
				now +
				"。Warning, 仅支持文件的类型：" +
				accept.join("、"),
			type: "warning",
		});
		return;
	}
	let reader = new FileReader();
	reader.onload = function (e) {
		let result = e.target?.result;
		data.value.push({
			name: file.name,
			type: "." + file.name.split(".").pop(),
			size: file.size,
			status: "pending",
			progress: 0,
			result,
			success: false,
			t1: null,
			t2: null,
		});
		nums.value = data.value.length;
		size.value += file.size;
	};
	reader.readAsDataURL(file);
};
const dfs = (entry: any) => {
	if (entry.isDirectory) {
		const reader = entry.createReader();
		reader.readEntries((en: any) => {
			for (let i of en) {
				dfs(i);
			}
		});
	} else {
		entry.file((file: any) => {
			pushData(file);
		});
	}
};
const validate = (file: any) => {
	if (accept.indexOf("." + file.name.split(".").pop()) !== -1) return true;
};
const del = (item: any) => {
	clearTimeout(item.t1);
	clearInterval(item.t2);
	if (item.status === "pending") {
		ElMessage({
			showClose: true,
			message: "Oops, 删除成功.",
			type: "error",
		});
	} else if (item.status === "upload") {
		if (item.abort1) {
			item.abort1();
		} else {
			item.abort2();
		}
		ElMessage({
			showClose: true,
			message: "Oops, 停止上传, 并删除成功.",
			type: "error",
		});
	} else if (item.status === "success") {
		successNums.value--;
		ElMessage({
			showClose: true,
			message: "Oops, 撤销上传, 成功删除服务器文件.",
			type: "error",
		});
	}
	data.value.splice(
		data.value.findIndex((v: any) => v == item),
		1
	);
	nums.value--;
	size.value -= item.size;
};
const startUpload = async () => {
	let loop = data.value.filter(
		(v: any) => !v.success && !(v.status === "upload")
	);
	if (!loop.length) {
		if (pool.length) {
			ElMessage({
				showClose: true,
				message: "Success, 所有文件已在下载队列中！",
				type: "success",
			});
			return;
		}
		ElMessage({
			showClose: true,
			message: "Warning, 还没有选择文件。",
			type: "warning",
		});
		return;
	}
	loop.map((v: any) => {
		v.status = "upload";
		if (v.size > 1024 * 1024 * limit) {
			setTimeout(() => {
				v.status = "error文件太大";
			}, 250);
		}
		v.abort2 = () => {
			let index = loop.findIndex((vv: any) => vv == v);
			loop.splice(index, 1);
		};
	});
	const execute = async () => {
		for (let v of loop) {
			if (v.size > 1024 * 1024 * limit) {
				continue;
			}
			let second = 5 + Math.ceil(Math.random() * 9);
			const xhr = new XMLHttpRequest();
			const pro = new Promise((resolve) => {
				xhr.onload = function (e) {
					clearInterval(v.t2);
					v.status = "success";
					v.success = true;
					successNums.value++;
				};
				xhr.open("POST", "/upload/upload");
				v.abort1 = () => {
					// xhr.abort1()
					resolve("请求被删除");
				};
				v.t2 = setInterval(() => {
					v.progress = parseInt(v.progress + 100 / second);
				}, 1000);
				v.t1 = setTimeout(() => {
					xhr.send();
					resolve("上传成功");
				}, second * 1000);
			});
			pro.then((resp) => {
				let index = pool.findIndex((v: any) => v == pro);
				pool.splice(index, 1);
				console.log(resp);
			});
			pool.push(pro);
			while (pool.length >= max.value) {
				await Promise.race(pool);
			}
		}
	};
	execute();
};
const inputHandler = (e: any) => {
	isShow.value = true;
};
const comfirmHandler = () => {
	if (Number.isNaN(Number(curIpt)) || !curIpt) {
		curIpt = max.value;
	} else {
		curIpt = parseInt(curIpt);
		if (curIpt < 1) {
			curIpt = 1;
		} else if (curIpt > 10) {
			curIpt = 10;
		}
		if (curIpt !== max.value) {
			max.value = curIpt;
			ElNotification({
				title: "Success",
				message: `小爱同学会在‘完成一个正在上传任务后’为您同步设置‘同时上传任务数量为${max.value}’`,
				type: "success",
			});
		}
	}
	isShow.value = false;
};
</script>

<template>
	<div class="example-container">
		<div ref="select" class="upload-area" @click="clickIpt('none')">
			<span class="info-top">
				<UploadFilled class="icon1" /><span
					>将目录或多个文件拖拽到此进行扫描</span
				>
			</span>
			<span>支持文件的类型：{{ accept.join("、") }}</span>
			<span>每个文件允许的最大尺寸：{{ limit }}M</span>
			<input
				ref="ipt"
				type="file"
				title=""
				@change="iptChange"
				multiple
				accept=".jpg,.jpeg,.bmp,.webp,.gif,.png,.mp3,.mp4" />
		</div>
		<div class="upload-opts">
			<button @click="clickIpt('only')" @blur="btnBlur('only')">
				选择文件
			</button>
			<button @click="clickIpt('mutiple')" @blur="btnBlur('mutiple')">
				选择文件夹
			</button>
		</div>
		<div class="upload-content">
			<div class="content-header">
				<span>文件名</span><span>类型</span><span>大小</span
				><span>状态</span><span>操作</span>
			</div>
			<div
				class="content-main"
				v-for="(item, index) in data"
				:key="index">
				<span>{{ item.name }}</span>
				<span>{{ item.type }}</span>
				<span>{{
					item.size / 1024 / 1024 > 1
						? (item.size / 1024 / 1024).toFixed(2) + "MB"
						: item.size / 1024 > 1
						? (item.size / 1024).toFixed(2) + "KB"
						: item.size + "bype"
				}}</span>
				<span>
					<span
						v-show="item.status !== 'upload'"
						:class="{
							'content-status': true,
							pending: item.status === 'pending',
							success: item.status === 'success',
							error: item.status.slice(0, 5) === 'error',
						}"
						>{{
							item.status === "pending"
								? "待上传"
								: item.status === "success"
								? "已上传"
								: item.status.slice(5)
						}}</span
					>
					<span v-show="item.status === 'upload'"
						><progress max="100" :value="item.progress"></progress
						><span class="progress">{{ item.progress }}%</span
						><span class="progress-etr">{{
							item.progress === 0 ? "待上传" : "上传中"
						}}</span></span
					>
				</span>
				<span>
					<Delete class="icon2" @click="del(item)" />
				</span>
			</div>
		</div>
		<div class="upload-info">
			<span>文件数量：{{ nums }}</span
			><span>成功上传：{{ successNums }}</span
			><span
				>总大小：{{
					size / 1024 / 1024 > 1
						? (size / 1024 / 1024).toFixed(2) + "MB"
						: size / 1024 > 1
						? (size / 1024).toFixed(2) + "KB"
						: size + "bype"
				}}</span
			>
			<button
				:class="{ isenable: data.length ? true : false }"
				@click="startUpload">
				开始上传
			</button>
			<span
				>同时上传数量：<input
					type="text"
					v-model="curIpt"
					@input="inputHandler"
			/></span>
			<button v-show="isShow" class="confirm" @click="comfirmHandler">
				确定
			</button>
		</div>
	</div>
</template>

<style scoped lang="scss">
.icon1 {
	width: 3em;
	height: 3em;
	color: #545c6490;
}
.icon2 {
	width: 1.2em;
	height: 1.2em;
	cursor: pointer;
	&:hover {
		filter: drop-shadow(0 0 4px red);
		color: red;
	}
}
.example-container {
	height: 100%;
	width: 100%;
	background: #fff;
	position: relative;
	overflow: hidden;
	display: flex;
	flex-direction: column;
	.upload-area {
		width: auto;
		height: 200px;
		border: 1px dashed #000;
		border-radius: 20px;
		position: relative;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		cursor: pointer;
		user-select: none;
		input {
			display: none;
		}
		input::-webkit-file-upload-button {
			cursor: pointer;
		}
		& > span {
			height: 48px;
			color: #666;
		}
		& > span:nth-child(2),
		& > span:nth-child(3) {
			margin-top: 20px;
			line-height: 48px;
		}
		.info-top {
			display: flex;
			align-items: center;
			span {
				margin-left: 15px;
			}
		}
		&:hover {
			border-color: rgb(72, 222, 236);
		}
	}
	.upload-opts {
		padding: 6px 10px;
		button {
			background: #409eff;
			margin: 0 5px;
			user-select: none;
		}
		button:hover {
			background: #79bbff;
		}
	}
	.upload-content {
		width: auto;
		height: 160px;
		border: 1px solid #ddd;
		flex: 1;
		overflow: auto;
		.content-header {
			position: sticky;
			position: -webkit-sticky;
			top: 0px;
			background: #eee;
			height: 40px;
			border-bottom: 1px solid #ddd;
			display: flex;
			align-items: center;
			span {
				border-left: 1px solid #ddd;
				display: inline-block;
				height: 20px;
				line-height: 20px;
				flex: 1;
				padding: 0 20px;
			}
			span:nth-child(1) {
				border-left: none;
			}
		}
		.content-main {
			height: 40px;
			border-bottom: 1px solid #ddd;
			display: flex;
			align-items: center;
			&:nth-last-child(1) {
				border-bottom: none;
			}
			& > span {
				flex: 1;
				padding: 0 20px;
				.content-status {
					padding: 2px 5px;
					user-select: none;
				}
				.pending {
					border: 1px solid #409eff;
					background: #ecf5ff;
					color: #409eff;
				}
				.success {
					border: 1px solid #95d475;
					background: #f0f9eb;
					color: #95d475;
				}
				.error {
					border: 1px solid #fcd3d3;
					background: #fef0f0;
					color: #fcd3d3;
				}
			}
			span:nth-child(1) {
				overflow: hidden;
				text-overflow: ellipsis;
			}
			progress {
				width: 80px;
				margin-right: 5px;
			}
			.progress {
				display: inline-block;
				width: 40px;
				font-size: 15px;
				text-align: right;
			}
			.progress-etr {
				font-size: 10px;
				margin-left: 4px;
				color: #ddd;
			}
		}
	}
	.upload-info {
		user-select: none;
		span {
			border: 1px solid #ddd;
			margin-right: 10px;
			padding: 2px 5px;
			&:nth-child(2) {
				background: #b3e19d80;
				color: #529b2e;
			}
			&:nth-last-of-type(1) {
				color: #aaa;
				input {
					width: 23px;
					text-align: right;
				}
			}
		}
		button {
			border: 1px solid #ddd;
			margin: 2px 10px 0 0;
			&:hover {
				background: #eee;
			}
			&.isenable,
			&.confirm {
				background: #409eff;
				&:hover {
					background: #79bbff;
				}
			}
			&.confirm {
				width: 40px;
				padding: 2px;
				border: 1px solid #000;
			}
		}
	}
}
</style>
