<script setup lang="ts">
import { onMounted, ref } from "vue";
import mp3_1 from "../assets/mp3/红模仿.mp3?url";
import mp3_2 from "../assets/mp3/感官先生.mp3?url";
import mp3_3 from "../assets/mp3/夜曲.mp3?url";
import mp3_4 from "../assets/mp3/我的名字.mp3?url";
import mp3_5 from "../assets/mp3/本草纲目.mp3?url";

let play_pause = ref();
let player_track = ref();
let album_cover = ref();
let bg = ref();
let album_name = ref();
let track_name = ref();
let current_time = ref();
let total_time = ref();
let progress_box = ref();
let hover_time = ref();
let hover_bar = ref();
let progress_bar = ref();
let play_prev = ref();
let play_next = ref();
let audio: any = new Audio();

let albums = ["红模仿", "感官先生", "夜曲", "我的名字", "本草纲目"];
let ablums_url = [mp3_1, mp3_2, mp3_3, mp3_4, mp3_5];
let track_names = [
	"周杰伦 - 红模仿",
	"刘凤瑶 - 感官先生",
	"周杰伦 - 夜曲",
	"焦麦奇 - 我的名字",
	"周杰伦 - 本草纲目",
];
let progress_t: any,
	progress_loc: any,
	c_m: any,
	ct_minutes: any,
	ct_seconds: any,
	cur_minutes: any,
	cur_seconds: any,
	dur_minutes: any,
	dur_seconds: any,
	play_progress: any;
let cur_index = -1;

function intiPlayer() {
	selectTrack(0);
	(play_pause.value as any).addEventListener("click", playPause);
	(progress_box.value as any).addEventListener(
		"mousemove",
		function (e: any) {
			showHover(e);
		}
	);
	(progress_box.value as any).addEventListener("mouseout", hideHover);
	(progress_box.value as any).addEventListener("click", playFromClickedPos);
	audio.addEventListener("timeupdate", updateCurTime);
	(play_prev.value as any).addEventListener("click", function () {
		selectTrack(-1);
	});
	(play_next.value as any).addEventListener("click", function () {
		selectTrack(1);
	});
}
function playPause() {
	setTimeout(() => {
		if ((audio as any).paused) {
			player_track.value.classList.add("active");
			play_pause.value.querySelector(".iconfont").classList =
				"iconfont icon-pause";
			album_cover.value.classList.add("active");
			(audio as any).play();
		} else {
			player_track.value.classList.remove("active");
			play_pause.value.querySelector(".iconfont").classList =
				"iconfont icon-playfill";
			album_cover.value.classList.remove("active");
			audio.pause();
		}
	}, 300);
}
function showHover(e: any) {
	progress_t = e.clientX - progress_box.value.getBoundingClientRect().left;
	progress_loc =
		audio.duration *
		(progress_t / progress_box.value.getBoundingClientRect().width);
	hover_bar.value.style.width = progress_t + "px";
	c_m = progress_loc / 60;
	ct_minutes = Math.floor(c_m);
	ct_seconds = Math.floor(progress_loc - ct_minutes * 60);
	if (ct_minutes < 10) {
		ct_minutes = "0" + ct_minutes;
	}
	if (ct_seconds < 10) {
		ct_seconds = "0" + ct_seconds;
	}
	if (isNaN(ct_minutes) || isNaN(ct_seconds)) {
		hover_time.value.innerText = "--:--";
	} else {
		hover_time.value.innerText = ct_minutes + ":" + ct_seconds;
	}
	hover_time.value.style.left = progress_t + "px";
	hover_time.value.style.marginLeft = "-20px";
	hover_time.value.style.display = "block";
}
function hideHover() {
	hover_bar.value.style.width = "0px";
	hover_time.value.innerText = "00:00";
	hover_time.value.style.left = "0px";
	hover_time.value.style.marginLeft = "0px";
	hover_time.value.style.display = "none";
}
function playFromClickedPos() {
	audio.currentTime = progress_loc;
	progress_bar.value.style.width = progress_t + "px";
	hideHover();
}
function updateCurTime() {
	cur_minutes = Math.floor(audio.currentTime / 60);
	cur_seconds = Math.floor(audio.currentTime - cur_minutes * 60);
	dur_minutes = Math.floor(audio.duration / 60);
	dur_seconds = Math.floor(audio.duration - dur_minutes * 60);
	play_progress = (audio.currentTime / audio.duration) * 100;

	if (cur_minutes < 10) {
		ct_minutes = "0" + ct_minutes;
	}
	if (cur_seconds < 10) {
		ct_seconds = "0" + ct_seconds;
	}
	if (dur_minutes < 10) {
		ct_minutes = "0" + ct_minutes;
	}
	if (dur_seconds < 10) {
		ct_seconds = "0" + ct_seconds;
	}
	if (isNaN(cur_minutes) || isNaN(cur_seconds)) {
		current_time.value.innerText = "00:00";
	} else {
		current_time.value.innerText = cur_minutes + ":" + cur_seconds;
	}
	if (isNaN(dur_minutes) || isNaN(dur_seconds)) {
		total_time.value.innerText = "00:00";
	} else {
		total_time.value.innerText = dur_minutes + ":" + dur_seconds;
	}

	(progress_bar.value as any).style.width = play_progress + "%";
	if (play_progress == 100) {
		play_pause.value.querySelector(".iconfont").classList =
			"iconfont icon-playfill";
		progress_bar.value.style.width = "0px";
		current_time.value.innerText = "00:00";
		player_track.value.classList.remove("active");
		album_cover.value.classList.remove("active");
	}
}
function selectTrack(flag: number) {
	if (flag == 0 || flag == 1) {
		++cur_index;
		if (cur_index >= albums.length) {
			cur_index = 0;
		}
	} else {
		--cur_index;
		if (cur_index < 0) {
			cur_index = albums.length - 1;
		}
	}

	if (cur_index > -1 && cur_index < albums.length) {
		if (flag == 0) {
			(play_pause.value as any).querySelector(".iconfont").classList =
				"iconfont icon-playfill";
		} else {
			(play_pause.value as any).querySelector(".iconfont").classList =
				"iconfont icon-pause";
		}
		(progress_bar.value as any).style.width = "0px";
		(current_time.value as any).innerText = "00:00";
		(total_time.value as any).innerText = "00:00";
		let cur_ablum = albums[cur_index];
		let cur_track_name = track_names[cur_index];
		audio.src = ablums_url[cur_index];
		if (flag != 0) {
			audio.play();
			(player_track.value as any).classList.add("active");
			(album_cover.value as any).classList.add("active");
		}
		(album_name.value as any).innerText = cur_ablum;
		(track_name.value as any).innerText = cur_track_name;
		(album_cover.value as any)
			.querySelector(".active")
			.classList.remove("active");
		(album_cover.value as any)
			.getElementsByTagName("img")
			[cur_index].classList.add("active");
		(bg.value as any).style.backgroundImage =
			"url(" +
			(album_cover.value as any)
				.getElementsByTagName("img")
				[cur_index].getAttribute("src") +
			")";
	} else {
		if (flag == 0 || flag == 1) {
			--cur_index;
		} else {
			++cur_index;
		}
	}
}
onMounted(() => {
	intiPlayer();
});
</script>

<template>
	<div class="container">
		<div ref="bg" class="bg"></div>
		<div class="player">
			<div ref="player_track" class="player-track">
				<div ref="album_name" class="album-name">红模仿</div>
				<div ref="track_name" class="track-name">周杰伦 - 红模仿</div>
				<div class="track-time">
					<div ref="current_time" class="current-time">00:00</div>
					<div ref="total_time" class="total-time">03:50</div>
				</div>
				<div ref="progress_box" class="progress-box">
					<div ref="hover_time" class="hover-time">00:36</div>
					<div ref="hover_bar" class="hover-bar"></div>
					<div ref="progress_bar" class="progress-bar"></div>
				</div>
			</div>
			<div class="player-content">
				<div ref="album_cover" class="album-cover">
					<img
						src="../assets/img/红模仿.jfif"
						alt=""
						class="active" />
					<img src="../assets/img/感官先生.jfif" alt="" />
					<img src="../assets/img/夜曲.jfif" alt="" />
					<img src="../assets/img/我的名字.jfif" alt="" />
					<img src="../assets/img/本草纲目.jfif" alt="" />
				</div>
				<div class="play-controls">
					<div class="control">
						<div ref="play_prev" class="button play-prev">
							<span class="iconfont icon-step-backward"></span>
						</div>
					</div>
					<div class="control">
						<div ref="play_pause" class="button play-pause">
							<span class="iconfont icon-playfill"></span>
						</div>
					</div>
					<div class="control">
						<div ref="play_next" class="button play-next">
							<span class="iconfont icon-step-forward"></span>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<style scoped>
@import url("../assets/iconfont/iconfont.css");
* {
	margin: 0;
	padding: 0;
}
.container {
	width: 430px;
	height: 100px;
	position: relative;
	user-select: none;
}
.bg {
	position: absolute;
	inset: -40px;
	background: url(../assets/img/红模仿.jfif) no-repeat;
	background-size: cover;
	background-position: center;
	filter: blur(40px);
	z-index: 1;
}
.player {
	position: relative;
	z-index: 3;
	width: 100%;
	height: 100%;
}
.player-track {
	position: absolute;
	top: 0;
	right: 15px;
	bottom: 0;
	left: 15px;
	padding: 13px 22px 10px 184px;
	background-color: rgba(255, 255, 255, 0.8);
	border-radius: 15px 15px 0 0;
	transition: top 0.3s ease;
}
.player-track.active {
	top: -95px;
}
.ablum-name {
	color: #333;
	font-size: 17px;
	font-weight: bold;
}
.track-name {
	color: #888;
	font-size: 13px;
	margin: 3px 0 12px 0;
}
.track-time {
	height: 12px;
	line-height: 12px;
	margin-bottom: 4px;
	overflow: hidden;
}
.current-time,
.total-time {
	color: #ff668f;
	font-size: 11px;
	transition: all 0.3s ease;
}
.current-time {
	float: left;
}
.total-time {
	float: right;
}
.progress-box {
	position: relative;
	height: 4px;
	background-color: #ead2d7;
	border-radius: 4px;
	cursor: pointer;
}
.hover-time {
	position: absolute;
	top: -30px;
	background-color: rgba(0, 0, 0, 0.8);
	color: #fff;
	font-size: 12px;
	padding: 5px 6px;
	border-radius: 4px;
	display: none;
}
.hover-bar {
	position: absolute;
	inset: 0;
	background-color: rgba(0, 0, 0, 0.1);
	border-radius: 4px;
	z-index: 2;
}
.progress-bar {
	position: absolute;
	inset: 0;
	background-color: #fd6d94;
	border-radius: 4px;
	z-index: 1;
	width: 0;
	transition: width 0.2s ease;
}
.player-content {
	position: relative;
	height: 100%;
	background-color: #fff;
	border-radius: 15px;
	z-index: 2;
	box-shadow: 0 30px 80px #656565;
}
.album-cover {
	width: 115px;
	height: 115px;
	border-radius: 50%;
	position: absolute;
	top: -40px;
	left: 40px;
	box-shadow: 0 0 0 10px #fff;
	overflow: hidden;
	transition: 0.3s ease;
}
.album-cover::before {
	content: "";
	width: 20px;
	height: 20px;
	background-color: #d6dee7;
	position: absolute;
	inset: 0;
	top: 50%;
	border-radius: 50%;
	margin: -10px auto auto auto;
	box-shadow: inset 0 0 0 2px #fff;
	z-index: 1;
}
.album-cover.active {
	top: -60px;
	box-shadow: 0 0 0 4px #fff7f7, 0 30px 50px -15px #afb7c1;
}
.album-cover img {
	display: block;
	width: 100%;
	height: 0;
	object-fit: cover;
	opacity: 0;
}
.album-cover img.active {
	height: 100%;
	opacity: 1;
}
.album-cover.active img.active {
	animation: rotateAlbumCover 3s linear infinite;
}
.play-controls {
	width: 255px;
	height: 100%;
	float: right;
	overflow: hidden;
	display: flex;
	align-items: center;
}
.control {
	flex: 1;
}
.control .button {
	width: 75px;
	height: 75px;
	display: flex;
	justify-content: center;
	align-items: center;
	background-color: #fff;
	border-radius: 6px;
	cursor: pointer;
	transition: 0.2s ease;
}
.control .button span {
	color: #d6dee6;
	font-size: 30px;
	transition: 0.2s ease;
}
.control .button:hover {
	background-color: #d6d6de;
}
.control .button:hover span {
	color: #fff;
}
@keyframes rotateAlbumCover {
	0% {
		transform: rotate(0deg);
	}
	100% {
		transform: rotate(360deg);
	}
}
</style>
