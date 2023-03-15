<script lang="ts" setup>
import Intro from "../utils/intro";
import { ElNotification } from "element-plus";
import {
	Document,
	Menu as IconMenu,
	Location,
	Setting,
	Film,
	UploadFilled,
	TrendCharts,
	SwitchFilled,
	Warning,
	User,
	FolderChecked,
} from "@element-plus/icons-vue";
import MenuBtn from "../components/MenuBtn.vue";
import { onMounted, ref } from "vue";
import PageHeader from "../components/PageHeader.vue";
import { useIndexStore } from "../store/indexStore";
import { useColorStore } from "../store/colorStore";
import { ElRow, ElMenu, ElMenuItem, ElIcon } from "element-plus";
import { RouterView } from "vue-router";
const list = [
	{ name: "文档", cls: "doc", router: "/document" },
	{ name: "菜单", cls: "menu", router: "/menu" },
	{ name: "设置", cls: "setting", router: "/setting" },
	{ name: "权限", cls: "permissions", router: "/permissions" },
	{ name: "地图", cls: "location", router: "/location" },
	{ name: "音频可视化", cls: "audio", router: "/audio" },
	{ name: "文件上传", cls: "upload", router: "/upload" },
	{ name: "数据可视化", cls: "dv", router: "/dv" },
	{ name: "Games", cls: "games", router: "/games" },
	{ name: "Warning", cls: "warning", router: "/warning" },
	{ name: "作者", cls: "author", router: "/author" },
];
const span = ref(null);
const menuTitle = ref(null);
const layout = ref(null);
let header = ref(list[0].name);
let isShow = ref(false);
const useIndex = useIndexStore();
const useColor = useColorStore();
const homeSteps = {
	shifts: {
		step: "1",
		intro: "可编辑记录文档。",
		position: "right",
	},
	attendGroup: {
		step: "2",
		intro: "可设置主题风格。",
		position: "right",
	},
	writeOff: {
		step: "3",
		intro: "上传音频后，可实现音频可视化。",
		position: "right",
	},
};
onMounted(() => {
	useColor.layoutE = layout.value;
	useColor.changeColor("layout", "");
	let menuDom: any = document.querySelector(".el-menu");
	useColor.menuE = menuDom;
	useColor.changeColor("menu", "");
	if (!localStorage.getItem("isShowHelp")) {
		Intro.start();
		// 退出引导回调函数
		Intro.onexit(function () {
			localStorage.setItem("isShowHelp", "1");
		});
	}
	ElNotification({
		title: "Warning",
		message:
			"初次加载，切换页面会出现卡顿情况，如出现长时间页面无反应请刷新页面重试。",
		type: "warning",
	});
});

const handleSelect = (key: string, keyPath: string[], item: any) => {
	if (useIndex.menuIndex !== key) {
		let name = "文档";
		switch (key) {
			case "/document":
				name = "文档";
				break;
			case "/menu":
				name = "菜单";
				break;
			case "/permissions":
				name = "权限";
				break;
			case "/setting":
				name = "设置";
				break;
			case "/location":
				name = "地图";
				break;
			case "/audio":
				name = "音频可视化";
				break;
			case "/upload":
				name = "文件上传";
				break;
			case "/dv":
				name = "数据可视化";
				break;
			case "/games":
				name = "Games";
				break;
			case "/warning":
				name = "Warning";
				break;
			case "/author":
				name = "作者";
				break;
		}
		!!key ? (header.value = name) : null;
		useIndex.menuIndex = key;
	}
};
const menuBtnHandle = ($event: any) => {
	let spanValue: any = span.value;
	let menuTitleValue: any = menuTitle.value;
	if ($event.target.checked) {
		spanValue.map((v: any) => {
			v.style.width = "80px";
			setTimeout(() => {
				v.style.visibility = "visible";
			}, 200);
		});
		menuTitleValue.style.fontSize = "20px";
		isShow.value = false;
	} else {
		spanValue.map((v: any) => {
			v.style.width = "0px";
			v.style.visibility = "hidden";
			menuTitleValue.style.fontSize = "16px";
		});
		isShow.value = true;
	}
};
</script>

<template>
	<div class="container" ref="layout">
		<el-row class="tac">
			<MenuBtn :handler="menuBtnHandle"></MenuBtn>
			<el-menu
				router
				active-text-color="#ffd04b"
				background-color="#545c64"
				class="el-menu-vertical-demo"
				:default-active="useIndex.menuIndex"
				text-color="#ffffff"
				@select="handleSelect">
				<span class="nav" ref="menuTitle">Admin</span>
				<el-menu-item
					:index="item.router"
					v-for="(item, index) in list"
					:key="index">
					<el-icon
						><icon-menu
							v-if="item.cls === 'menu'"
							:data-step="homeSteps.shifts.step"
							:data-intro="homeSteps.shifts.intro"
							:data-position="homeSteps.shifts.position"
							:data-disable-interaction="true" />
						<setting
							v-else-if="item.cls === 'setting'"
							:data-step="homeSteps.attendGroup.step"
							:data-intro="homeSteps.attendGroup.intro"
							:data-position="homeSteps.attendGroup.position"
							:data-disable-interaction="true" />
						<location v-else-if="item.cls === 'location'" />
						<Film
							v-else-if="item.cls === 'audio'"
							:data-step="homeSteps.writeOff.step"
							:data-intro="homeSteps.writeOff.intro"
							:data-position="homeSteps.writeOff.position"
							:data-disable-interaction="true" />
						<UploadFilled v-else-if="item.cls === 'upload'" />
						<FolderChecked v-else-if="item.cls === 'permissions'" />
						<TrendCharts v-else-if="item.cls === 'dv'" />
						<SwitchFilled v-else-if="item.cls === 'games'" />
						<warning v-else-if="item.cls === 'warning'" />
						<user v-else-if="item.cls === 'author'" />
						<document v-else-if="item.cls === 'doc'" />
					</el-icon>
					<span ref="span">{{ item.name }}</span>
				</el-menu-item>
			</el-menu>
		</el-row>
		<div class="main-content">
			<PageHeader :header="header" :is-show="isShow"></PageHeader>
			<router-view title="btn"></router-view>
		</div>
	</div>
</template>

<style scoped lang="scss">
.container {
	width: 100vw;
	height: 100vh;
	min-width: 1050px;
	min-height: 700px;
	display: flex;
	background: #f7f8fa;
	position: relative;
	.el-row {
		width: fit-content;
		text-align: center;
		position: relative;
		flex-shrink: 0;
		z-index: 999;
		user-select: none;
		.nav {
			display: inline-block;
			height: 60px;
			line-height: 60px;
			font-weight: 1000;
			font-size: 20px;
			color: #ffffff;
			padding-top: 10px;
			transition: all 1s;
			user-select: none;
		}

		.nav:hover {
			filter: drop-shadow(0 0 10px #ffffff);
		}

		.el-menu {
			.el-menu-item {
				span {
					width: 80px;
					transition: width 0.5s;
				}
			}

			.el-menu-item:hover,
			.el-menu-item.is-active {
				background: linear-gradient(
					90deg,
					transparent 10%,
					rgba(88, 91, 95, 0.78) 10%,
					var(--el-menu-hover-bg-color) 90%,
					transparent 90%
				);
			}
		}
	}

	.main-content {
		flex: 1;
		min-height: 450px;
		background: #f7f8fa;
	}
}
</style>
