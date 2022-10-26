<template>
  <div class="con3">
    <div class="left">
      <VideoSrc :videoSrcList="videoSrcList"></VideoSrc>
      <Bottom></Bottom>
    </div>
    <div class="right">
      <div class="side">
        <div class="nav">选集</div>
        <div class="sections">
          <div
            :class="{ section: true, active3: index === activeIndex }"
            v-for="(item, index) in srcList.sections"
            :key="index"
            @click="
              toVideoSrc(item);
              addActive($event, index);
            "
          >
            {{ item.section }}
          </div>
        </div>
      </div>
      <div class="others">
        <div class="big-img"><img :src="bigImg" alt="" /></div>
        <div class="nav">推荐视频</div>
        <div class="card" v-for="(item, index) in othersSrcList" :key="index">
          <div class="img">
            <img :src="item.img" alt="" />
          </div>
          <div class="info">
            <span class="info-title">{{ item.title }}</span>
          </div>
        </div>
      </div>
      <div class="side-footer">
        Linting | 移动端 <br />
        团队介绍 <br />
        Linting官方网站
      </div>
    </div>
  </div>
</template>
<script>
import VideoSrc from "../components/VideoSrc.vue";
import Bottom from "../components/Bottom.vue";
export default {
  components: {
    VideoSrc,
    Bottom,
  },
  data() {
    return {
      srcList: [],
      videoSrcList: [],
      othersSrcList: [],
      bigImg: "",
      activeIndex: null,
    };
  },
  mounted() {
    this.getData();
    this.activeIndex =
      JSON.parse(sessionStorage.getItem("videoSectionIndex")) || 0;
  },
  updated() {
    if (!!document.querySelector(".active3")) {
      document.querySelector(".active3").click();
    }
  },
  methods: {
    getData() {
      let id = this.$route.params.id;
      this.$axios.default.get(`/dev-api/video/get/${id}`).then((res) => {
        this.srcList = res.data;
        this.srcList.sections = JSON.parse(res.data.sections);
      });

      this.othersSrcList = JSON.parse(sessionStorage.getItem("video")).slice(
        0,
        3
      );
      this.bigImg = this.othersSrcList[0].img;
    },
    addActive(e, index) {
      let sections = e.target.parentNode.querySelectorAll(".section");
      sections.forEach((v) => {
        v.classList.remove("active3");
      });
      e.target.classList.add("active3");
      sessionStorage.setItem("videoSectionIndex", index);
    },
    toVideoSrc(item) {
      this.videoSrcList = item;
    },
  },
};
</script>
<style lang='scss' scoped>
.con3 {
  width: 960px;
  display: flex;
  margin-top: 10px;
}
.left {
  width: 70%;
}
.right {
  width: 28%;
  margin-left: 2%;
}
.right .nav {
  text-align: left;
  padding: 5px 10px;
  font-weight: bold;
  font-size: 18px;
}
.right .side {
  background-color: #fff;
}
.right .sections {
  height: 300px;
  overflow: auto;
}
.right .sections::-webkit-scrollbar {
  width: 6px;
}
.right .sections::-webkit-scrollbar-thumb {
  background-color: #0687ff;
  border-radius: 10px;
}
.sections .section {
  padding: 5px 10px;
  text-align: left;
  cursor: pointer;
  position: relative;
}
.sections .section:hover {
  background-color: #ddd;
}
.sections .section.active3 {
  color: #0184ff;
  padding-left: 30px;
}
.sections .section.active3::before {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-left: 12px solid #0184ff;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  left: 0;
  top: 50%;
  transform: translateY(-50%) translateX(12px);
}
.right .others {
  background-color: #fff;
  margin: 10px 0;
}
.right .others .big-img {
  width: 100%;
  height: 160px;
}
img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.card {
  position: relative;
  width: 100%;
  height: 60px;
  margin-bottom: 10px;
  display: flex;
}
.card .img {
  height: 100%;
  width: 100px;
  left: 10px;
}
.info .info-title {
  padding-left: 5px;
  height: 30px;
  font-weight: bold;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.side-footer {
  font-size: 18px;
  color: #c6c6c6;
  text-align: left;
  line-height: 1.5;
}
</style>