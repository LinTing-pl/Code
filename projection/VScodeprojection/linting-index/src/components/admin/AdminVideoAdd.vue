<template>
  <div class="adminvideoadd-container">
    <div class="left">
      <div class="display">
        <div class="display-content">
          <video :src="sectionContent" controls></video>
        </div>
        <div class="display-btns">
          <el-dialog
            title="提交视频"
            :visible.sync="dialogVisible"
            width="300px"
            :before-close="handleClose"
            center
          >
            <span
              ><strong>请为《{{ data.title }}》添加一段介绍:</strong></span
            >
            <div
              class="videoInfo"
              style="border: 1px solid; border-radius: 4px"
              contenteditable="true"
              ref="videoinfo"
            >
              这是一个值得观看的视频
            </div>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="submitVideo">确 定</el-button>
            </span>
          </el-dialog>
          <button class="delDraft" @click="delDraft">删除草稿</button>
          <button class="submitVideo" @click="dialogVisible = true">
            提交
          </button>
          <button class="saveVideo" @click="saveVideo">保存</button>
          <label for="videofile"><span class="pushVideo">上传视频</span></label>
          <button class="delVideo" @click="delVideo">删除视频</button>
          <input
            type="file"
            @change="pushVideo"
            name=""
            id="videofile"
            class="videofile"
          />
        </div>
      </div>
    </div>
    <div class="right">
      <div class="top">
        <div class="name" ref="name">{{ data.title }}</div>
        <button class="modify" @click="modifyName">修改</button>
        <button class="confirm" ref="confirmBtn" @click="confirmName" disabled>
          确认
        </button>
      </div>
      <div class="middle">
        <label class="img" for="videoImg">
          <svg
            t="1668884460269"
            class="icon"
            viewBox="0 0 1040 1024"
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            p-id="2259"
            width="100"
            height="100"
          >
            <path
              d="M986.4068 263.666098l-75.878155 0 0 75.877131c0 20.937868-16.997116 37.936007-37.934984 37.936007-20.945031 0-37.942147-16.999163-37.942147-37.936007l0-75.877131L758.774383 263.666098c-20.942985 0-37.936007-16.999163-37.936007-37.942147 0-20.942985 16.993023-37.934984 37.936007-37.934984l75.877131 0 0-75.878155c0-20.942985 16.997116-37.940101 37.942147-37.940101 20.937868 0 37.934984 16.997116 37.934984 37.940101l0 75.878155 75.878155 0c20.942985 0 37.940101 16.991999 37.940101 37.934984C1024.346901 246.667959 1007.349785 263.666098 986.4068 263.666098L986.4068 263.666098zM758.774383 396.447241c0 31.41243-25.491581 56.909128-56.909128 56.909128-31.413454 0-56.904011-25.497721-56.904011-56.909128s25.490557-56.904011 56.904011-56.904011C733.281779 339.54323 758.774383 365.035834 758.774383 396.447241L758.774383 396.447241zM607.019097 263.666098 75.877131 263.666098l0 528.748453c0.076748-0.265036 83.047438-372.255259 225.244021-372.255259 93.66731 0 188.932 287.689235 248.310366 374.648772 0 0 46.549176-188.480722 126.866433-189.69641 79.44233-1.177825 120.417557 187.301873 120.417557 187.301873l37.936007 0L834.651514 567.175647c0-20.942985 16.997116-37.942147 37.942147-37.942147 20.937868 0 37.934984 16.999163 37.934984 37.942147l0 303.509549c0 41.919738-33.989115 75.877131-75.877131 75.877131L75.877131 946.562327c-41.919738 0-75.877131-33.957393-75.877131-75.877131L0 263.666098c0-41.924855 33.957393-75.877131 75.877131-75.877131l531.141966 0c20.942985 0 37.942147 16.991999 37.942147 37.934984C644.961244 246.667959 627.962082 263.666098 607.019097 263.666098L607.019097 263.666098zM607.019097 263.666098"
              p-id="2260"
              fill="#aaa"
            ></path>
          </svg>
          <img ref="img" :src="data.img" alt="封面" />
        </label>
        <input
          type="file"
          class="videoImg"
          name=""
          id="videoImg"
          @change="addImg"
        />
      </div>
      <div class="bottom" ref="bottom">
        <div
          :class="{ chapter: true, active: activeIndex === index }"
          v-for="(item, index) in data.sections"
          :key="index"
          ref="chapter"
          @dblclick="modifyDom"
          @blur="finishModify($event, index)"
          @click="setIndex($event, index)"
        >
          {{ item.section }}
        </div>
        <button class="addChapter" @click="addChapter">添加集数</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      data: {
        title: "视频",
        img: "",
        sections: [],
      },
      chapterId: null,
      activeIndex: null,
      sectionContent: "",
      dialogVisible: false,
      save: false,
      back: true,
    };
  },
  mounted() {
    if (localStorage.getItem("adminvideodraft")) {
      this.data = JSON.parse(localStorage.getItem("adminvideodraft"));
    }
    if (this.data.img) {
      this.$refs.img.style.visibility = "visible";
    }
    this.activeIndex = JSON.parse(sessionStorage.getItem("adminvideoAddIndex"));
    if (this.activeIndex) {
      this.sectionContent = this.data.sections[this.activeIndex]?.mp4 || null;
    }
    window.addEventListener("beforeunload", this.beforeUnload);
  },
  destroyed() {
    window.removeEventListener("beforeunload", this.beforeUnload);
  },
  methods: {
    beforeUnload(e) {
      if (
        this.back &&
        JSON.stringify(this.data) !== localStorage.getItem("adminvideodraft")
      ) {
        e = e || window.event;
        if (e) {
          e.returnValue = "关闭提示";
        }
        return "关闭提示";
      }
    },
    delDraft() {
      if (localStorage.getItem("adminvideodraft")) {
        this.$confirm(`是否删除草稿, 是否继续?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            this.$axios.default
              .post("/dev-api/draftoredit/video/updateimg", {
                cls: "draft",
                img: "",
              })
              .then((res) => {
                this.$message({
                  type: "success",
                  message: "删除成功!",
                  showClose: true,
                });
                localStorage.removeItem("adminvideodraft");
                this.back = false;
                this.$router.push("/adminvideo");
              });
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消删除",
              showClose: true,
            });
          });
      } else {
        this.$message({
          type: "warning",
          message: "还没有草稿!",
          showClose: true,
        });
      }
    },
    async submitVideo() {
      localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
      this.dialogVisible = false;
      let nowTime = new Date();
      this.data.cls = "视频";
      this.data.img =
        this.data.img ||
        "http://localhost:7001/public/img/defaultImg/default.jpeg";
      this.data.orderby = 0;
      this.data.date =
        nowTime.toLocaleDateString() + " " + nowTime.toLocaleTimeString();
      this.data.info = this.$refs.videoinfo.innerText;
      this.data.sections = JSON.stringify(this.data.sections);
      this.$axios.default
        .post("/dev-api/video/add", { video: this.data })
        .then((res) => {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          this.$axios.default
            .post("/dev-api/draftoredit/video/updateimg", {
              cls: "draft",
              img: "",
            })
            .then((res) => {
              localStorage.removeItem("adminvideodraft");
              this.back = false;
              this.$router.push("/adminvideo");
            });
        });
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
    },
    modifyName() {
      let name = this.$refs.name;
      name.setAttribute("contenteditable", true);
      name.focus();
      this.$refs.confirmBtn.removeAttribute("disabled");
      this.$refs.confirmBtn.style.cursor = "pointer";
    },
    confirmName() {
      let name = this.$refs.name;
      name.removeAttribute("contenteditable");
      this.data.title = name.innerText;
      this.$refs.confirmBtn.setAttribute("disabled", true);
      this.$refs.confirmBtn.style.cursor = "not-allowed";
      localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
    },
    addImg(e) {
      try {
        let file = e.target.files[0];
        let reader;
        if (file) {
          // 创建流对象
          reader = new FileReader();
          reader.readAsDataURL(file);
        }
        // 捕获 转换完毕
        let _this = this;
        reader.onload = async function (e) {
          // 转换后的base64就在e.target.result里面,直接放到img标签的src属性即可
          let time = new Date().getTime();
          await _this.$axios.default
            .post("/dev-api/draftoredit/video/updateimg", {
              user: localStorage.getItem("user"),
              time: time,
              img: e.target.result,
              cls: "draft",
            })
            .then((res) => {
              _this.data.img = res.data;
              _this.$refs.img.style.visibility = "visible";
              localStorage.setItem(
                "adminvideodraft",
                JSON.stringify(_this.data)
              );
            });
        };
      } catch (e) {
        this.$message({
          type: "warning",
          message: "需要jpeg格式的图片!",
          showClose: true,
        });
      }
    },
    addChapter() {
      this.data.sections.push({ section: "第 集 视频名" });
      localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
    },
    modifyDom(e) {
      clearTimeout(this.chapterId);
      e.target.setAttribute("contenteditable", true);
      e.target.style.cursor = "initial";
      e.target.focus();
    },
    finishModify(e, index) {
      this.data.sections[index].section = e.target.innerText;
      e.target.removeAttribute("contenteditable");
      e.target.style.cursor = "pointer";
      localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
    },
    setIndex(e, index) {
      clearTimeout(this.chapterId);
      this.chapterId = setTimeout(() => {
        if (this.save) {
          let i = JSON.parse(sessionStorage.getItem("adminvideoAddIndex"));
          this.data.sections[i].mp4 = this.sectionContent;
        } else {
          this.save = true;
        }

        this.$refs.chapter.forEach((v) => {
          v.classList.remove("active");
        });
        e.target.classList.add("active");
        this.sectionContent = this.data.sections[index].mp4 || null;
        sessionStorage.setItem("adminvideoAddIndex", index);
      }, 250);
    },
    pushVideo(e) {
      let i = JSON.parse(sessionStorage.getItem("adminvideoAddIndex"));
      if (i !== null) {
        let file = e.target.files[0];
        let reader;
        if (file) {
          reader = new FileReader();
          reader.readAsDataURL(file);
        }
        let _this = this;
        reader.onload = async function (e) {
          let time = new Date().getTime();
          await _this.$axios.default
            .post("/dev-api/draftoredit/video/updatevideo", {
              user: localStorage.getItem("user"),
              time: time,
              video: e.target.result,
              cls: "draft",
            })
            .then((res) => {
              console.log(res.data, 11111111);
              // _this.data.sections = res.data;
              // localStorage.setItem(
              //   "adminvideodraft",
              //   JSON.stringify(_this.data)
              // );
            });
        };
      } else {
        this.$message({
          type: "info",
          message: "还没有选中小节!",
          showClose: true,
        });
      }
    },
    delVideo() {
      let i = JSON.parse(sessionStorage.getItem("adminvideoAddIndex"));
      if (i !== null) {
        this.$confirm(
          `是否删除《${this.data.sections[i].section}》视频, 是否继续?`,
          "提示",
          {
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            type: "warning",
          }
        )
          .then(() => {
            this.data.sections.splice(i, 1);
            this.sectionContent = null;
            this.save = false;
            localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
            sessionStorage.removeItem("adminvideoAddIndex");
            this.activeIndex = null;
            this.$message({
              type: "success",
              message: "删除成功!",
              showClose: true,
            });
            this.$refs.chapter.forEach((v) => {
              v.classList.remove("active");
            });
          })
          .catch(() => {
            this.$message({
              type: "info",
              message: "已取消删除",
              showClose: true,
            });
          });
      } else {
        this.$message({
          type: "info",
          message: "还没有选中小节!",
          showClose: true,
        });
      }
    },
    saveVideo() {
      if (!this.$refs.chapter) {
        this.$message({
          type: "warning",
          message: "请添加章节!",
          showClose: true,
        });
      } else {
        let i = JSON.parse(sessionStorage.getItem("adminvideoAddIndex"));
        if (i !== null) {
          this.data.sections[i].mp4 = this.sectionContent;
          localStorage.setItem("adminvideodraft", JSON.stringify(this.data));
          this.$message({
            type: "success",
            message: "保存成功!",
            showClose: true,
          });
        } else {
          this.$message({
            type: "info",
            message: "还没有选中小节!",
            showClose: true,
          });
        }
      }
    },
  },
};
</script>
<style lang='scss' scoped>
.adminvideoadd-container {
  display: flex;
  flex-direction: row;
  width: calc(100vw - 284px);
  min-width: 730px;
  min-height: 606px;
  margin: 4px 1px;
}
.adminvideoadd-container .left {
  width: 77%;
  display: flex;
  flex-direction: column;
}
.adminvideoadd-container .right {
  width: 23%;
  height: 606px;
  padding: 5px;
}
.left .display {
  height: auto;
  border: 1px solid #ccc;
  padding: 5px 5px;
}
.left .display .display-content {
  text-align: left;
  overflow: auto;
  padding-bottom: 5px;
}
.left .display .display-content video {
  width: 100%;
  height: auto;
  cursor: pointer;
}
.left .display .display-btns {
  height: 30px;
  text-align: right;
  padding-top: 5px;
  border-top: 1px solid #ccc;
}
.left .display .display-btns .videofile {
  display: none;
}
.left .display .display-btns .delVideo {
  height: 28px;
  background-color: #f56c6c;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .delVideo:hover {
  background-color: #f78989;
}
.left .display .display-btns .saveVideo {
  height: 28px;
  margin-right: 10px;
  background-color: #409eff;
  color: #fff;
  border: none;
  outline: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .saveVideo:hover {
  background-color: #66b1ff;
}
.left .display .display-btns .submitVideo,
.left .display .display-btns .pushVideo {
  height: 28px;
  margin-right: 10px;
  background-color: #67c23a;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .pushVideo {
  display: inline-block;
  position: relative;
  line-height: 28px;
  top: -1.5px;
  font-size: 13px;
  width: 65px;
  text-align: center;
}
.left .display .display-btns .submitVideo:hover,
.left .display .display-btns .pushVideo:hover {
  background-color: #85ce61;
}
.left .display .display-btns .delDraft {
  height: 28px;
  margin-right: 10px;
  background-color: #f56c6c;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .delDraft:hover {
  background-color: #f78989;
}
.right .top {
  position: relative;
}
.right .top .name {
  font-size: 20px;
  font-weight: bold;
  background-color: #fff;
  border-radius: 6px;
  box-shadow: 0 0 5px rgb(46, 46, 46);
  margin-bottom: 4px;
}
.right .top button {
  width: 70px;
  height: 30px;
  border: none;
  border-radius: 4px;
}
.right .top .modify {
  background: #e6a23c;
  color: #fff;
  position: relative;
  left: -5px;
  cursor: pointer;
}

.right .top .modify:hover {
  background: #ebb563;
}
.right .top .confirm {
  background: #409eff;
  color: #fff;
  position: relative;
  left: 5px;
  cursor: not-allowed;
}
.right .top .confirm:hover {
  background: #66b1ff;
}
.right .middle .img {
  display: block;
  border: 1px solid #ddd;
  margin: 3px 0;
  cursor: pointer;
  position: relative;
}
.right .middle .img:hover {
  background: #eee;
  box-shadow: 0 0 5px rgb(46, 46, 46);
}
.right .middle .videoImg {
  display: none;
}
.right .middle .img img {
  width: 100%;
  height: 100%;
  display: block;
  border: 1px solid #ddd;
  cursor: pointer;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
  visibility: hidden;
}
.right .bottom {
  height: 456px;
  display: flex;
  flex-direction: column;
  overflow: auto;
}
.right .bottom::-webkit-scrollbar {
  width: 6px;
}
.right .bottom::-webkit-scrollbar-thumb {
  background-color: #0687ff;
  border-radius: 10px;
}
.right .bottom .chapter {
  margin-bottom: 4px;
}
.right .bottom .addChapter {
  background-color: #409eff;
  border: none;
  border-radius: 4px;
  letter-spacing: 4px;
  padding: 2px 0;
  cursor: pointer;
  box-shadow: 0 0 4px #66b1ff;
  color: #fff;
  user-select: none;
}
.right .bottom .addChapter:hover {
  background: #66b1ff;
}
.right .bottom .chapter {
  background-color: #ebb56377;
  margin: 0 2px 2px 2px;
  padding: 2px;
  border-radius: 4px;
  cursor: pointer;
  height: auto;
}
.right .bottom .chapter.active,
.right .bottom .chapter:hover {
  background-color: #ebb563;
  box-shadow: 0 0 5px #ebb56388;
}
.right .bottom .chapter:hover {
  text-shadow: 0 0 4px #fff;
}
</style>