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
        <div class="img" @click="addImg">
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
        </div>
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
    };
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
    addImg() {},
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
  border: 1px solid #ccc;
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
  border: 1px solid #ddd;
  margin-top: 3px;
  cursor: pointer;
}
.right .middle .img:hover {
  background: #eee;
}
</style>