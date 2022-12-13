<template>
  <div class="searchcontent-container">
    <div class="title">
      <div class="adminSearchBack" @click="back">返回</div>
      查询结果
      <div class="refresh-box" @click="refresh" title="刷新资源">
        <svg
          t="1668673374534"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="2512"
          width="40"
          height="40"
        >
          <path
            d="M721.066667 725.333333c-59.733333 55.466667-132.266667 85.333333-209.066667 85.333334-157.866667 0-290.133333-123.733333-298.666667-281.6l12.8 12.8c8.533333 8.533333 17.066667 12.8 29.866667 12.8s21.333333-4.266667 29.866667-12.8c17.066667-17.066667 17.066667-42.666667 0-59.733334l-85.333334-85.333333c-17.066667-17.066667-42.666667-17.066667-59.733333 0l-85.333333 85.333333c-17.066667 17.066667-17.066667 42.666667 0 59.733334s42.666667 17.066667 59.733333 0l12.8-12.8c8.533333 204.8 179.2 366.933333 384 366.933333 98.133333 0 192-38.4 268.8-110.933333 17.066667-17.066667 17.066667-42.666667 0-59.733334-12.8-17.066667-42.666667-17.066667-59.733333 0zM968.533333 482.133333c-17.066667-17.066667-42.666667-17.066667-59.733333 0l-12.8 12.8C887.466667 290.133333 716.8 128 512 128c-98.133333 0-192 38.4-268.8 110.933333-17.066667 17.066667-17.066667 42.666667 0 59.733334 17.066667 17.066667 42.666667 17.066667 59.733333 0 59.733333-55.466667 132.266667-85.333333 209.066667-85.333334 157.866667 0 290.133333 123.733333 298.666667 281.6l-12.8-12.8c-17.066667-17.066667-42.666667-17.066667-59.733334 0s-17.066667 42.666667 0 59.733334l85.333334 85.333333c8.533333 8.533333 21.333333 12.8 29.866666 12.8s21.333333-4.266667 29.866667-12.8l85.333333-85.333333c17.066667-17.066667 17.066667-42.666667 0-59.733334z"
            fill="#ddd"
            p-id="2513"
          ></path>
        </svg>
      </div>
    </div>
    <el-dialog
      title="编辑资源"
      :visible.sync="editDialogVisible"
      width="300px"
      :before-close="handleClose"
      center
    >
      <div style="font-weight: bold">
        图片:
        <div class="middle">
          <label class="img" for="loadEditImg">
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
            <img v-if="editData.img" :src="editData.img" alt="封面" />
          </label>
          <input
            type="file"
            name=""
            id="loadEditImg"
            @change="addImg($event, 'edit')"
            style="display: none"
          />
        </div>
      </div>
      <div style="font-weight: bold">
        标题:
        <div
          class="loadaddtitle"
          style="
            border: 1px solid;
            border-radius: 4px;
            margin-bottom: 5px;
            font-weight: normal;
          "
          contenteditable="true"
          ref="loadedittitle"
          v-text="editData.title"
        ></div>
      </div>
      <div style="font-weight: bold">
        链接:
        <div
          class="loadaddurl"
          style="
            border: 1px solid;
            border-radius: 4px;
            margin-bottom: 5px;
            font-weight: normal;
          "
          contenteditable="true"
          ref="loadediturl"
          v-text="editData.url"
        ></div>
      </div>
      <div style="font-weight: bold">
        提取码:
        <div
          class="loadaddcode"
          style="
            border: 1px solid;
            border-radius: 4px;
            margin-bottom: 5px;
            font-weight: normal;
          "
          contenteditable="true"
          ref="loadeditcode"
          v-text="editData.code"
        ></div>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="editDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="updateLoad">确 定</el-button>
      </span>
    </el-dialog>
    <div class="searchcard" v-for="(item, index) in cardList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info" v-if="item.cls !== '下载'">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-info">{{ item.info }}</span>
      </div>
      <div class="info" v-else>
        <span class="info-title">{{ item.title }}</span>
        <span class="info-url">链接: {{ item.url }}</span>
        <span class="info-code">提取码: {{ item.code }}</span>
      </div>
      <div class="opts">
        <div class="cls" v-text="item.cls"></div>
        <div class="diary-btns">
          <button
            class="edit-btn"
            v-if="item.cls !== '下载'"
            @click="edit(item.id, item.cls)"
          >
            编辑
          </button>
          <button
            class="edit-btn"
            v-else
            @click="
              editLoad(item.id, item.title, item.url, item.code, item.img)
            "
          >
            编辑
          </button>
          <button class="del-btn" @click="del(item.id, item.cls)">删除</button>
        </div>
      </div>
    </div>
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="5"
      layout="total, prev, pager, next"
      :total="length"
    >
    </el-pagination>
  </div>
</template>
<script>
export default {
  props: ["nativeSearch"],
  data() {
    return {
      allList: [],
      cardList: [],
      currentPage: 1,
      length: 0,
      optscount: 0,
      editDialogVisible: false,
      editData: {
        img: "",
        title: "资源",
        url: "",
        code: "",
      },
    };
  },
  created() {
    this.allList = JSON.parse(sessionStorage.getItem("adminsearchcontent"));
    this.handleCurrentChange();
  },
  watch: {
    nativeSearch: {
      handler() {
        this.allList = JSON.parse(sessionStorage.getItem("adminsearchcontent"));
        this.length = this.allList.length;
        this.handleCurrentChange();
      },
    },
  },
  methods: {
    handleCurrentChange() {
      sessionStorage.setItem(
        "currAdminSearchPage",
        this.currentPage.toString()
      );
      this.cardList = this.allList.slice(
        5 * (this.currentPage - 1),
        this.currentPage * 5
      );
    },
    back() {
      this.$router.push(sessionStorage.getItem("adminIndex"));
    },
    refresh() {
      this.$emit("successOpts", this.optscount++);
    },
    del(id, cls) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          let CLS = "";
          switch (cls) {
            case "手册":
              CLS = "study";
              break;
            case "博客":
              CLS = "blog";
              break;
            case "视频":
              CLS = "video";
              break;
            case "下载":
              CLS = "load";
              break;
            default:
              break;
          }
          this.$axios.default
            .delete(`/dev-api/${CLS}/delete/${id}`)
            .then((res) => {
              this.$message({
                type: "success",
                message: "删除成功!",
                showClose: true,
              });
              this.$emit("successOpts", this.optscount++);
              this.allList = JSON.parse(
                sessionStorage.getItem("adminsearchcontent")
              );
              this.length = this.allList.length;
              this.handleCurrentChange();
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
    edit(id, cls) {
      sessionStorage.setItem("target", id.toString());
      let CLS = null;
      switch (cls) {
        case "手册":
          CLS = "study";
          break;
        case "博客":
          CLS = "blog";
          break;
        case "视频":
          CLS = "video";
          break;
        case "下载":
          CLS = "load";
          break;
        default:
          break;
      }
      if (!localStorage.getItem(`admin${CLS}edit${id}`)) {
        let loading = this.$loading({
          lock: true,
          text: "资源获取中。。。",
          background: "rgba(0, 0, 0, 0.5)",
        });
        this.$axios.default(`/dev-api/${CLS}/get/${id}`).then((res) => {
          loading.close();
          localStorage.setItem(
            `admin${CLS}edit${id}`,
            JSON.stringify(res.data)
          );
          this.$router.push({ name: `admin${CLS}edit`, params: { id: id } });
        });
      } else {
        this.$router.push({ name: `admin${CLS}edit`, params: { id: id } });
      }
    },
    editLoad(id, title, url, code, img) {
      sessionStorage.setItem("target", id.toString());
      this.editData.title = title;
      this.editData.url = url;
      this.editData.code = code;
      this.editData.img = img;
      this.editDialogVisible = true;
    },
    async updateLoad() {
      // 转换后的base64就在e.target.result里面,直接放到img标签的src属性即可
      let time = new Date().getTime();
      if (this.isBase64(this.editData.img)) {
        await this.$axios.default
          .post("/dev-api/draftoredit/load/update", {
            user: localStorage.getItem("user"),
            time: time,
            img: this.editData.img,
            cls: "edit",
          })
          .then((res) => {
            this.editData.img = res.data;
          });
      }
      this.editData.title = this.$refs.loadedittitle.innerText;
      this.editData.url = this.$refs.loadediturl.innerText;
      this.editData.code = this.$refs.loadeditcode.innerText;
      this.editDialogVisible = false;
      await this.$axios.default
        .post("/dev-api/load/update", {
          load: this.editData,
          id: JSON.parse(sessionStorage.getItem("target")),
        })
        .then((res) => {
          this.$message({
            type: "success",
            message: "提交成功!",
          });
          this.$emit("successOpts", this.optscount++);
          this.editData = {
            img: "",
            title: "资源",
            url: "",
            code: "",
          };
        });
    },
    isBase64(str) {
      if (str.slice(0, 11) === "data:image/") {
        return true;
      } else {
        return false;
      }
    },
    handleClose(done) {
      this.$confirm("确认关闭？")
        .then((_) => {
          done();
        })
        .catch((_) => {});
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
          _this.editData.img = e.target.result;
        };
      } catch (e) {
        this.$message({
          type: "warning",
          message: "需要jpeg格式的图片!",
          showClose: true,
        });
      }
    },
  },
};
</script>
<style lang='scss' scoped>
.searchcontent-container {
  width: calc(100vw - 240px - 60px);
  min-width: 705px;
  min-height: 600px;
  height: 600px;
  border: 4px solid #545c64;
  margin: 20px 30px 30px 30px;
  border-radius: 20px;
  box-shadow: 0 0 20px 5px #545c6450;
  overflow: hidden;
  position: relative;
}
.title {
  width: 100%;
  height: 59px;
  line-height: 59px;
  background-color: #fff;
  font-size: 20px;
  font-weight: bold;
  position: relative;
}
.title .adminSearchBack {
  height: 25px;
  line-height: 25px;
  position: absolute;
  top: 17px;
  left: 10px;
  font-weight: normal;
  background: #545c6433;
  font-size: 16px;
  padding: 0 5px;
  cursor: pointer;
  border-radius: 6px;
}
.title .adminSearchBack:hover {
  background: #545c6455;
  color: #fff;
}
.refresh-box {
  width: 40px;
  height: 40px;
  position: absolute;
  right: 15px;
  top: 8px;
  border-radius: 8px;
  cursor: pointer;
}
.refresh-box:hover {
  background-color: #eee;
}
.refresh-box:hover svg path {
  fill: #fff;
}
.searchcard {
  height: 100px;
  border-top: 1px solid #545c64;
  display: flex;
}
.searchcard .img {
  border: 1px solid #545c64;
  margin: 4px 10px 4px 10px;
  display: flex;
  align-items: center;
  height: 90px;
  width: 120px;
  min-width: 120px;
}
.searchcard .img img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.searchcard .info {
  min-width: 357.6px;
  max-width: 644px;
  width: 644px;
  border-left: 1px dashed #545c64;
  border-right: 1px dashed #545c64;
  display: flex;
  flex-direction: column;
  padding: 0 5px;
}
.searchcard .info .info-title {
  margin-bottom: 5px;
  font-weight: bold;
  font-size: 18px;
  overflow: hidden;
}
.searchcard .info .info-info {
  text-align: left;
  line-height: 1.5;
  overflow: hidden;
}
.searchcard .info .info-url {
  font-size: 17px;
  margin-bottom: 5px;
  text-align: left;
  line-height: 1.5;
  overflow: hidden;
}
.searchcard .info .info-code {
  text-align: left;
  line-height: 1.5;
  overflow: hidden;
}
.searchcard .opts {
  min-width: 220px;
  display: flex;
}
.searchcard .opts .diary-btns {
  display: flex;
  flex-direction: column;
}
.searchcard .opts .diary-btns button {
  width: 99px;
  height: 48px;
  margin: 1px 1px;
  outline: none;
  border-radius: 4px;
  cursor: pointer;
}
.searchcard .opts .diary-btns .edit-btn {
  border: 1px solid #409eff;
  background: #409eff;
  color: #fff;
}
.searchcard .opts .diary-btns .edit-btn:hover {
  background: #66b1ff;
}
.searchcard .opts .diary-btns .del-btn {
  border: 1px solid #f56c6c;
  background: #f56c6c;
  color: #fff;
}
.searchcard .opts .diary-btns .del-btn:hover {
  background: #f78989;
}
::v-deep.searchcard .el-input-number {
  width: 120px;
}
.searchcontent-container .searchcard:nth-last-child(2) {
  border-bottom: 1px solid #545c64;
}
::v-deep.el-pagination {
  position: absolute;
  width: 100%;
  bottom: 0;
  background-color: #fff;
}
.cls {
  width: 118px;
  border-right: 1px dashed #545c64;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 18px;
}
.middle .img {
  display: block;
  border: none;
  margin: 3px 0;
  cursor: pointer;
  position: relative;
  width: 100px;
  height: 100px;
}
.middle .img:hover {
  background: #eee;
  box-shadow: 0 0 5px rgb(46, 46, 46);
}
.middle .loadImg {
  display: none;
}
.middle .img img {
  width: 100%;
  height: 100%;
  display: block;
  border: 1px solid #ddd;
  cursor: pointer;
  position: absolute;
  left: 0;
  top: 0;
  object-fit: cover;
}
</style>