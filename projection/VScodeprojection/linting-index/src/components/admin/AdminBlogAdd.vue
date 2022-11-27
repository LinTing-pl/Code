<template>
  <div class="adminblogadd-container">
    <div class="left">
      <div class="display">
        <div class="display-content" v-html="blogContent"></div>
        <div class="display-btns">
          <el-dialog
            title="提交博客"
            :visible.sync="dialogVisible"
            width="300px"
            :before-close="handleClose"
            center
          >
            <span
              ><strong>请为《{{ data.title }}》添加一段介绍:</strong></span
            >
            <div
              class="blogInfo"
              style="border: 1px solid; border-radius: 4px"
              contenteditable="true"
              ref="bloginfo"
            >
              这是一篇值得阅读的博客
            </div>
            <span slot="footer" class="dialog-footer">
              <el-button @click="dialogVisible = false">取 消</el-button>
              <el-button type="primary" @click="submitBlog">确 定</el-button>
            </span>
          </el-dialog>

          <button class="submitBlog" @click="dialogVisible = true">提交</button>
          <button class="saveBlog" @click="saveBlog">保存</button>
          <button class="delDraft" @click="delDraft">删除草稿</button>
        </div>
      </div>
      <quillEditor class="quillEditor" v-model="blogContent"></quillEditor>
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
        <label class="img" for="blogImg">
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
          class="blogImg"
          name=""
          id="blogImg"
          @change="addImg"
        />
      </div>
    </div>
  </div>
</template>
<script>
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

import { quillEditor } from "vue-quill-editor";

export default {
  components: {
    quillEditor,
  },
  data() {
    return {
      data: {
        title: "博客",
        img: "",
        content: "",
      },
      blogContent: "",
      dialogVisible: false,
      back: true,
    };
  },
  mounted() {
    if (localStorage.getItem("adminblogdraft")) {
      this.data = JSON.parse(localStorage.getItem("adminblogdraft"));
    }
    if (this.data.img) {
      this.$refs.img.style.visibility = "visible";
    }
    this.blogContent = this.data.content || "";
    window.addEventListener("beforeunload", this.beforeUnload);
  },
  destroyed() {
    window.removeEventListener("beforeunload", this.beforeUnload);
  },
  methods: {
    beforeUnload(e) {
      if (
        this.back &&
        JSON.stringify(this.data) !== localStorage.getItem("adminblogdraft")
      ) {
        e = e || window.event;
        if (e) {
          e.returnValue = "关闭提示";
        }
        return "关闭提示";
      }
    },
    delDraft() {
      if (localStorage.getItem("adminblogdraft")) {
        this.$confirm(`是否删除草稿, 是否继续?`, "提示", {
          confirmButtonText: "确定",
          cancelButtonText: "取消",
          type: "warning",
        })
          .then(() => {
            this.$axios.default
              .post("/dev-api/draftoredit/blog/update", {
                cls: "draft",
                img: "",
              })
              .then((res) => {
                this.$message({
                  type: "success",
                  message: "删除成功!",
                  showClose: true,
                });
                localStorage.removeItem("adminblogdraft");
                this.back = false;
                this.$router.push("/adminblog");
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
    async submitBlog() {
      this.data.content = this.blogContent;
      localStorage.setItem("adminblogdraft", JSON.stringify(this.data));
      this.dialogVisible = false;
      let nowTime = new Date();
      this.data.cls = "博客";
      this.data.img =
        this.data.img ||
        "http://localhost:7001/public/img/defaultImg/default.jpeg";
      this.data.orderby = 0;
      this.data.date =
        nowTime.toLocaleDateString() + " " + nowTime.toLocaleTimeString();
      this.data.info = this.$refs.bloginfo.innerText;
      await this.$axios.default
        .post("/dev-api/blog/add", { blog: this.data })
        .then((res) => {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          this.$axios.default
            .post("/dev-api/draftoredit/blog/update", {
              cls: "draft",
              img: "",
            })
            .then((res) => {
              localStorage.removeItem("adminblogdraft");
              this.back = false;
              this.$router.push("/adminblog");
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
      localStorage.setItem("adminblogdraft", JSON.stringify(this.data));
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
            .post("/dev-api/draftoredit/blog/update", {
              user: localStorage.getItem("user"),
              time: time,
              img: e.target.result,
              cls: "draft",
            })
            .then((res) => {
              _this.data.img = res.data;
              _this.$refs.img.style.visibility = "visible";
              localStorage.setItem(
                "adminblogdraft",
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
    saveBlog() {
      this.data.content = this.blogContent;
      localStorage.setItem("adminblogdraft", JSON.stringify(this.data));
      this.$message({
        type: "success",
        message: "保存成功!",
        showClose: true,
      });
    },
  },
};
</script>
<style lang='scss' scoped>
.adminblogadd-container {
  display: flex;
  flex-direction: row;
  width: calc(100vw - 284px);
  min-width: 730px;
  min-height: 606px;
  margin: 4px 1px;
}
.adminblogadd-container .left {
  width: 77%;
  display: flex;
  flex-direction: column;
}
.adminblogadd-container .right {
  width: 23%;
  height: 606px;
  padding: 5px;
}
.left .display {
  height: 270px;
  border: 1px solid #ccc;
  padding: 0 5px;
  border-bottom: none;
}
.left .display .display-content {
  height: 240px;
  text-align: left;
  word-break: break-all;
  overflow: auto;
}
.left .display .display-btns {
  height: 30px;
  text-align: right;
  padding: 0 20px;
}
.left .display .display-btns .saveBlog {
  height: 28px;
  margin-right: 10px;
  background-color: #409eff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .saveBlog:hover {
  background-color: #66b1ff;
}
.left .display .display-btns .submitBlog {
  height: 28px;
  margin-right: 10px;
  background-color: #67c23a;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  user-select: none;
}
.left .display .display-btns .submitBlog:hover {
  background-color: #85ce61;
}
.left .display .display-btns .delDraft {
  height: 28px;
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
.left .quillEditor {
  height: 270px;
  word-break: break-all;
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
.right .middle .blogImg {
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
</style>