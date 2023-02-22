<template>
  <div class="videocontent-container">
    <div class="left">
      <div class="videosrc">
        <div class="video-title">{{ videoContent.section }}</div>
        <div class="video-date">{{ videoContent.date }}</div>
        <div class="video-content">
          <video ref="videoEle" :src="videoContent.mp4" controls @click="checkLogin" @play="init" crossorigin="anonymous"></video>
        </div>
      </div>
      <button class="opt-showVideo" @click="open">{{ isShow?'关闭音频可视化':'打开音频可视化' }}</button>
      <canvas ref="cvs" v-show="isShow"></canvas>
      <remark cls="video" :id="data.id"></remark>
    </div>
    <div class="right">
      <div class="side">
        <div class="nav">选集</div>
        <div class="sections">
          <div
            :class="{ section: true, active3: index === activeIndex }"
            v-for="(item, index) in data.sections"
            :key="index"
            @click="
              setIndex(index);
              addActive($event);
            "
          >
            {{ item.section }}
          </div>
        </div>
      </div>
      <div class="others">
        <div class="nav">推荐视频</div>
        <div
          class="card"
          @click="read(item.id)"
          v-for="(item, index) in othersSrcList"
          :key="index"
        >
          <div class="img">
            <img :src="item.img" alt="" />
          </div>
          <div class="info">
            <span class="info-title">{{ item.title }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import Remark from "../../public/Remark";
export default {
  components: {
    Remark,
  },
  data() {
    return {
      data: [],
      videoContentist: [],
      othersSrcList: [],
      bigImg: "",
      activeIndex: 0,
      readId: null,
      isShow:false,
      isInit:false,
      dataArray:null,
      analyser:null,
      ctx:null,
      flag:false,
    };
  },
  created() {
    this.data = JSON.parse(
      sessionStorage.getItem(`videocontent${this.$route.params.id}`)
    );
    this.data.sections = JSON.parse(this.data.sections);
    this.othersSrcList = JSON.parse(sessionStorage.getItem("video")).slice(
      0,
      3
    );
    this.activeIndex =
      JSON.parse(
        sessionStorage.getItem(`videoSectionIndex${this.$route.params.id}`)
      ) || 0;
    this.videoContent = this.data.sections[this.activeIndex];
  },
  // watch: {
  //   $route: {
  //     handler() {
  //       this.id = this.$route.params.id;
  //       if (this.id) {
  //         this.data = JSON.parse(
  //           sessionStorage.getItem(`videocontent${this.$route.params.id}`)
  //         );
  //         this.data.sections = JSON.parse(this.data.sections);
  //         this.activeIndex =
  //           JSON.parse(
  //             sessionStorage.getItem(
  //               `videoSectionIndex${this.$route.params.id}`
  //             )
  //           ) || 0;
  //         this.videoContent = this.data.sections[this.activeIndex];
  //         this.$forceUpdate();
  //       }
  //     },
  //     immediate: true, //在watch中首次绑定的时候，是否执行handler
  //   },
  // },
  methods: {
    read(id) {
      clearTimeout(this.readId);
      this.readId = setTimeout(() => {
        if (sessionStorage.getItem(`videocontent${id}`)) {
          this.$router.push("/videocontent/" + id).catch((e) => {});
          this.$router.go(0);
        } else {
          this.$axios.default.get(`/dev-api/video/get/${id}`).then((res) => {
            sessionStorage.setItem(
              `videocontent${id}`,
              JSON.stringify(res.data)
            );
            this.$router.push("/videocontent/" + id).catch((e) => {});
            this.$router.go(0);
          });
        }
      }, 250);
    },
    addActive(e) {
      let sections = e.target.parentNode.querySelectorAll(".section");
      sections.forEach((v) => {
        v.classList.remove("active3");
      });
      e.target.classList.add("active3");
    },
    setIndex(index) {
      this.videoContent = this.data.sections[index];
      this.$forceUpdate();
      sessionStorage.setItem(
        `videoSectionIndex${this.$route.params.id}`,
        index
      );
    },
    checkLogin(e) {
      if (!localStorage.getItem("user")) {
        e.preventDefault();
        if (confirm("观看视频，需要先登录")) {
          this.$router.push("/login");
        }
      }
    },
    init(){
        if(this.isInit){
          return
        }
        this.ctx=this.$refs.cvs.getContext('2d')
        const audCtx=new AudioContext()
        const source=audCtx.createMediaElementSource(this.$refs.videoEle)
        this.analyser=audCtx.createAnalyser()
        this.analyser.fftSize=512
        this.dataArray=new Uint8Array(this.analyser.frequencyBinCount)
        source.connect(this.analyser)
        this.analyser.connect(audCtx.destination)
        this.isInit=true
        if(this.isShow){
          this.draw()
        }
    },
    draw(){
      if(this.isShow){
        if(!this.isInit)return
        this.flag=true
        requestAnimationFrame(this.draw)
        const {width,height}=this.$refs.cvs
        this.ctx.clearRect(0,0,width,height)
        this.analyser.getByteFrequencyData(this.dataArray)
        const len=this.dataArray.length/2.5
        const barWidth=width/len/2
        this.ctx.fillStyle='#78C5F7'
        for(let i=0;i<len;i++){
          const data=this.dataArray[i]
          const barHeight=data/255*height
          const x1=i*barWidth +width/2
          const x2=width/2 - (i+1)*barWidth
          const y=height-barHeight
          this.ctx.fillRect(x1,y,barWidth-1,barHeight)
          this.ctx.fillRect(x2,y,barWidth-1,barHeight)
        }
      }
    },
    open(){
      this.isShow=!this.isShow
      if(!this.flag){
        this.draw()
      }
      if(!this.isShow){
        this.flag=false
      }
    }

  },
};
</script>
<style lang='scss' scoped>
.videocontent-container {
  width: 960px;
  min-height: 590px;
  display: flex;
  margin-top: 10px;
  margin-bottom: 10px;
}
.left {
  width: 70%;
  position: relative;
  .opt-showVideo{
    position: absolute;
    right: 20px;
    top: 20px;
    border: none;
    padding: 5px;
    cursor: pointer;
    background: rgb(119, 159, 228);
    border-radius: 6px;
  }
  .opt-showVideo:hover{
    box-shadow: 0 0 4px rgb(119, 159, 228);
    color: #fff;
  }
  canvas{
    background: #000;
    width: 100%;
    height: 100px;
  }
}
.right {
  width: 30%;
  margin-left: 15px;
}
.left .videosrc {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: start;
  padding: 10px;
  margin-bottom: 15px;
}
.left .videosrc .video-title {
  font-weight: bold;
  font-size: 20px;
  letter-spacing: 3px;
}
.left .videosrc .video-date {
  color: #aaa;
  margin: 12px 0 12px;
}
.left .videosrc .video-content {
  width: 100%;
  height: auto;
  padding-bottom: 20px;
}
.left .videosrc .video-content video {
  width: 100%;
  height: auto;
  cursor: pointer;
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
  user-select: none;
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
  padding-left: 5px;
}
img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.others .card {
  position: relative;
  width: 100%;
  height: 60px;
  padding: 5px 0;
  margin-bottom: 5px;
  display: flex;
  cursor: pointer;
}
.others .card:hover {
  box-shadow: 0 0 5px #000;
}
.others .card .img {
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