<template>
  <div class="adminstudyadd-container">
    <div class="left">
      <div class="display"></div>
      <quillEditor class="quillEditor"></quillEditor>
    </div>
    <div class="right">
      <div class="top">
        <div class="name" ref="name">{{ bookname }}</div>
        <button class="modify" @click="modifyName">修改</button>
        <button class="confirm" @click="confirmName">确认</button>
      </div>
      <div class="middle">
        <label class="img" for="bookImg">
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
          <img ref="img" :src="bookImg" alt="" />
        </label>
        <input
          type="file"
          class="bookImg"
          name=""
          id="bookImg"
          @change="addImg"
        />
      </div>
      <div class="bottom" ref="bottom">
        <div class="chapter" v-for="(item, index) in chaptersList" :key="index">
          <div
            :class="{ title: true, active: addActiveIndex === index }"
            @dblclick="modifyDom"
            @blur="finishModify($event, index)"
            @click="isClick && toggleActive($event)"
          >
            {{ item.chapter }}
          </div>
          <div :class="{ sections: true, active: addActiveIndex === index }">
            <button class="delChapter" @click="delChapter(item.chapter, index)">
              删除章节
            </button>
            <div
              class="section"
              v-for="(item1, index1) in item.sections"
              :key="index1"
              @dblclick="modifyDom"
              @click="setIndex(index, index1)"
              @blur="finishModify($event, index, index1)"
            >
              {{ item1.section
              }}<button
                class="delSection"
                @click="delSection(item1.section, index, index1)"
              >
                删除
              </button>
            </div>
            <button class="addSection" @click="addSection(index)">
              添加小节
            </button>
          </div>
        </div>
        <button class="addChapter" @click="addChapter">添加章节</button>
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
      bookname: "书名",
      bookImg: "",
      chaptersList: [],
      chapterId: null,
      isClick: true,
      addActiveIndex: 0,
      addActiveIndex1: 0,
    };
  },
  mounted() {
    this.bookImg = localStorage.getItem(`${this.bookname}1025`) || "";
    if (this.bookImg) {
      this.$refs.img.style.visibility = "visible";
    }
    this.addActiveIndex =
      JSON.parse(sessionStorage.getItem("adminstudyAddIndex")) || 0;
    this.addActiveIndex1 =
      JSON.parse(sessionStorage.getItem("adminstudyAddIndex1")) || 0;
    this.chaptersList =
      JSON.parse(sessionStorage.getItem("adminstudydraft")) || [];
  },
  methods: {
    modifyName() {
      let name = this.$refs.name;
      name.setAttribute("contenteditable", true);
      name.focus();
    },
    confirmName() {
      let name = this.$refs.name;
      name.removeAttribute("contenteditable");
      this.bookname = name.innerText;
    },
    addImg(e) {
      let file = e.target.files[0];
      let reader;
      if (file) {
        // 创建流对象
        reader = new FileReader();
        reader.readAsDataURL(file);
      }
      // 捕获 转换完毕
      let _this = this;
      reader.onload = function (e) {
        // 转换后的base64就在e.target.result里面,直接放到img标签的src属性即可
        _this.bookImg = e.target.result;
        _this.$refs.img.style.visibility = "visible";
        localStorage.setItem(`${_this.bookname}1025`, _this.bookImg);
      };
    },
    addChapter() {
      this.chaptersList.push({ chapter: "第 章 章节名", sections: [] });
      sessionStorage.setItem(
        "adminstudydraft",
        JSON.stringify(this.chaptersList)
      );
    },
    delChapter(chapter, index) {
      this.$confirm(`是否删除《${chapter}》章节, 是否继续?`, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.chaptersList.splice(index, 1);
          this.$refs.bottom
            .querySelectorAll(".sections")
            .forEach((v) => v.classList.remove("active"));
          sessionStorage.setItem(
            "adminstudydraft",
            JSON.stringify(this.chaptersList)
          );
          this.$message({
            type: "success",
            message: "删除成功!",
            showClose: true,
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
            showClose: true,
          });
        });
    },
    modifyDom(e) {
      clearTimeout(this.chapterId);
      this.isClick = false;
      e.target.setAttribute("contenteditable", true);
      e.target.style.cursor = "initial";
      e.target.focus();
    },
    finishModify(e, index, index1) {
      this.isClick = true;
      if (index1 === undefined) {
        this.chaptersList[index].chapter = e.target.innerText;
      } else {
        this.chaptersList[index].sections[index1].section = e.target.innerText;
      }
      e.target.removeAttribute("contenteditable");
      e.target.style.cursor = "pointer";
      sessionStorage.setItem(
        "adminstudydraft",
        JSON.stringify(this.chaptersList)
      );
    },
    toggleActive(e) {
      clearTimeout(this.chapterId);
      this.chapterId = setTimeout(() => {
        e.target.classList.toggle("active");
        e.target.nextSibling.classList.toggle("active");
      }, 250);
    },
    addSection(index) {
      console.log(index);
      this.chaptersList[index].sections.push({ section: "第 节 小节名" });
      sessionStorage.setItem(
        "adminstudydraft",
        JSON.stringify(this.chaptersList)
      );
    },
    delSection(section, index, index1) {
      this.$confirm(`是否删除《${section}》小节, 是否继续?`, "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.chaptersList[index].sections.splice(index1, 1);
          sessionStorage.setItem(
            "adminstudydraft",
            JSON.stringify(this.chaptersList)
          );
          this.$message({
            type: "success",
            message: "删除成功!",
            showClose: true,
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
            showClose: true,
          });
        });
    },
    setIndex(index, index1) {
      sessionStorage.setItem("adminstudyAddIndex", index);
      sessionStorage.setItem("adminstudyAddIndex1", index1);
    },
  },
};
</script>
<style lang='scss' scoped>
.adminstudyadd-container {
  display: flex;
  flex-direction: row;
  width: calc(100vw - 270px);
  min-width: 730px;
  min-height: 606px;
  margin: 4px 1px;
}
.adminstudyadd-container .left {
  flex: 1;
  display: flex;
  flex-direction: column;
}
.adminstudyadd-container .right {
  flex: 0.3;
  height: 606px;
  padding: 5px;
}
.left .display {
  height: 270px;
  border: 1px solid #ccc;
  border-bottom: none;
}
.left .quillEditor {
  height: 270px;
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
  cursor: pointer;
}
.right .top .modify {
  background: #e6a23c;
  color: #fff;
  position: relative;
  left: -5px;
}

.right .top .modify:hover {
  background: #ebb563;
}
.right .top .confirm {
  background: #409eff;
  color: #fff;
  position: relative;
  left: 5px;
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
.right .middle .bookImg {
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
.right .bottom .addChapter {
  background-color: #409eff;
  border: none;
  border-radius: 4px;
  letter-spacing: 4px;
  padding: 2px 0;
  cursor: pointer;
  box-shadow: 0 0 5px #66b1ff;
  color: #fff;
}
.right .bottom .addChapter:hover {
  background: #66b1ff;
}
.right .bottom .chapter .title {
  background-color: #ebb56377;
  margin: 0 2px 2px 2px;
  border-radius: 4px;
  cursor: pointer;
}
.right .bottom .chapter .title.active,
.right .bottom .chapter .title:hover {
  background-color: #ebb563dd;
  box-shadow: 0 0 5px #ebb56388;
}
.right .bottom .chapter .sections {
  display: none;
}
.right .bottom .chapter .sections.active {
  display: block;
}
.right .bottom .chapter .sections .delChapter {
  width: 90%;
  background-color: #f56c6c;
  color: #fff;
  margin-bottom: 2px;
  border: none;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
}
.right .bottom .chapter .sections .delChapter:hover {
  background-color: #f78989;
}
.right .bottom .chapter .sections .addSection {
  width: 90%;
  background-color: #409eff;
  color: #fff;
  margin-bottom: 2px;
  border: none;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
}
.right .bottom .chapter .sections .addSection:hover {
  background-color: #66b1ff;
}
.right .bottom .chapter .sections .section {
  margin: 0 5%;
  background-color: #b3d8ff;
  margin-bottom: 2px;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}
</style>