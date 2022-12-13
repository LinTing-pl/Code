<template>
  <div class="studycontent-container">
    <div class="btns">
      学习手册
      <div class="add-box" @click="toAdd">
        <svg
          t="1668674263391"
          class="icon"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="2389"
          width="40"
          height="40"
        >
          <path
            d="M512 74.666667C270.933333 74.666667 74.666667 270.933333 74.666667 512S270.933333 949.333333 512 949.333333 949.333333 753.066667 949.333333 512 753.066667 74.666667 512 74.666667z m0 810.666666c-204.8 0-373.333333-168.533333-373.333333-373.333333S307.2 138.666667 512 138.666667 885.333333 307.2 885.333333 512 716.8 885.333333 512 885.333333z"
            p-id="2390"
            fill="#1296db"
          ></path>
          <path
            d="M682.666667 480h-138.666667V341.333333c0-17.066667-14.933333-32-32-32s-32 14.933333-32 32v138.666667H341.333333c-17.066667 0-32 14.933333-32 32s14.933333 32 32 32h138.666667V682.666667c0 17.066667 14.933333 32 32 32s32-14.933333 32-32v-138.666667H682.666667c17.066667 0 32-14.933333 32-32s-14.933333-32-32-32z"
            p-id="2391"
            fill="#1296db"
          ></path>
        </svg>
      </div>
      <div class="refresh-box" @click="getData(false)" title="刷新资源">
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
    <div class="studycard" v-for="(item, index) in cardList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-info">{{ item.info }}</span>
      </div>
      <div class="opts">
        <div class="count">
          <div class="top-box">优先级</div>
          <div class="middle-box">
            <button @click="valueDel(item.id)">-</button>
            <input type="number" name="" id="" v-model="priorities[item.id]" />
            <button @click="valueAdd(item.id)">+</button>
          </div>
          <div class="bottom-box">
            <button @click="resetCurr(item.id)">重置</button>
            <button @click="confirm(item.id)">确定</button>
          </div>
        </div>
        <div class="diary-btns">
          <button class="edit-btn" @click="edit(item.id)">编辑</button>
          <button class="del-btn" @click="del(item.id)">删除</button>
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
  data() {
    return {
      allList: [],
      cardList: [],
      currentPage: 1,
      length: 0,
      priorities: {},
      prioritiesCopy: {},
    };
  },
  created() {
    let data = JSON.parse(sessionStorage.getItem("adminStudy"));

    this.currentPage =
      JSON.parse(sessionStorage.getItem("currAdminStudyPage")) || 1;
    if (data) {
      this.allList = data;
      this.length = this.allList.length;
      this.handleCurrentChange();
      data.forEach((v) => {
        this.priorities[v.id] = v.orderby;
      });
      this.prioritiesCopy = { ...this.priorities };
    } else {
      this.getData();
    }
  },
  methods: {
    async getData(flag) {
      let loading = this.$loading({
        lock: true,
        text: "资源获取中。。。",
        background: "rgba(0, 0, 0, 0.5)",
      });
      await this.$axios.default.get("/dev-api/study/get").then((res) => {
        loading.close();
        this.allList = res.data;
        this.length = this.allList.length;
        flag ? null : (this.currentPage = 1);
        this.cardList = this.allList.slice(
          (this.currentPage - 1) * 5,
          this.currentPage * 5
        );
        res.data.forEach((v) => {
          this.priorities[v.id] = v.orderby;
        });
        this.prioritiesCopy = { ...this.priorities };
        sessionStorage.setItem("adminStudy", JSON.stringify(res.data));
      });
    },
    handleCurrentChange() {
      sessionStorage.setItem("currAdminStudyPage", this.currentPage.toString());
      this.cardList = this.allList.slice(
        5 * (this.currentPage - 1),
        this.currentPage * 5
      );
    },
    toAdd() {
      this.$router.push({ name: "adminstudyadd" });
    },
    edit(id) {
      sessionStorage.setItem("target", id.toString());
      if (!localStorage.getItem(`adminstudyedit${id}`)) {
        let loading = this.$loading({
          lock: true,
          text: "资源获取中。。。",
          background: "rgba(0, 0, 0, 0.5)",
        });
        this.$axios.default(`/dev-api/study/get/${id}`).then((res) => {
          localStorage.setItem(`adminstudyedit${id}`, JSON.stringify(res.data));
          this.$router
            .push({ name: "adminstudyedit", params: { id: id } })
            .then((res) => {
              loading.close();
            });
        });
      } else {
        this.$router.push({ name: "adminstudyedit", params: { id: id } });
      }
    },
    del(id) {
      this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$axios.default
            .delete(`/dev-api/study/delete/${id}`)
            .then((res) => {
              this.$message({
                type: "success",
                message: "删除成功!",
                showClose: true,
              });
              this.getData(true);
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
    valueDel(id) {
      if (this.priorities[id] > 0) {
        this.priorities[id] = this.priorities[id] - 1;
        this.$forceUpdate();
      }
    },
    valueAdd(id) {
      if (this.priorities[id] < 100) {
        this.priorities[id] = this.priorities[id] + 1;
        this.$forceUpdate();
      }
    },
    resetCurr(id) {
      this.priorities[id] = this.prioritiesCopy[id];
      this.$forceUpdate();
    },
    confirm(id) {
      this.$axios.default
        .post("/dev-api/study/update", {
          id: id,
          orderby: this.priorities[id],
        })
        .then((res) => {
          if (res.status === 200) {
            this.getData(true);
            this.$message({
              showClose: true,
              message: "优先级设置成功",
              type: "success",
            });
          }
        });
    },
  },
};
</script>
<style lang='scss' scoped>
.studycontent-container {
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
.btns {
  width: 100%;
  height: 59px;
  line-height: 59px;
  background-color: #fff;
  font-size: 20px;
  font-weight: bold;
  position: relative;
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
.add-box {
  width: 40px;
  height: 40px;
  position: absolute;
  right: 65px;
  top: 8px;
  border-radius: 8px;
  cursor: pointer;
}
.add-box:hover {
  background-color: #eee;
}
.studycard {
  height: 100px;
  border-top: 1px solid #545c64;
  display: flex;
}
.studycard .img {
  border: 1px solid #545c64;
  margin: 4px 10px 4px 10px;
  display: flex;
  align-items: center;
  height: 90px;
  width: 120px;
  min-width: 120px;
}
.studycard .img img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.studycard .info {
  min-width: 335px;
  max-width: 644px;
  width: 644px;
  border-left: 1px dashed #545c64;
  border-right: 1px dashed #545c64;
  display: flex;
  flex-direction: column;
  padding: 0 5px;
}
.studycard .info .info-title {
  margin-bottom: 5px;
  font-weight: bold;
  font-size: 18px;
  overflow: hidden;
}
.studycard .info .info-info {
  text-align: left;
  line-height: 1.5;
  overflow: hidden;
}
.studycard .opts {
  min-width: 220px;
  display: flex;
}
.studycard .opts .diary-btns {
  display: flex;
  flex-direction: column;
}
.studycard .opts .diary-btns button {
  width: 99px;
  height: 48px;
  margin: 1px 1px;
  outline: none;
  border-radius: 4px;
  cursor: pointer;
}
.studycard .opts .diary-btns .edit-btn {
  border: 1px solid #409eff;
  background: #409eff;
  color: #fff;
}
.studycard .opts .diary-btns .edit-btn:hover {
  background: #66b1ff;
}
.studycard .opts .diary-btns .del-btn {
  border: 1px solid #f56c6c;
  background: #f56c6c;
  color: #fff;
}
.studycard .opts .diary-btns .del-btn:hover {
  background: #f78989;
}
::v-deep.studycard .el-input-number {
  width: 120px;
}
.studycontent-container .studycard:nth-last-child(2) {
  border-bottom: 1px solid #545c64;
}
::v-deep.el-pagination {
  position: absolute;
  width: 100%;
  bottom: 0;
  background-color: #fff;
}
.count {
  width: 118px;
  border-right: 1px dashed #545c64;
}
.count .top-box {
  font-weight: bold;
  height: 28px;
  line-height: 28px;
}
.count .middle-box {
  height: 31px;
  margin: 1px;
  display: flex;
  border: 1px solid #dcdfe6;
}
.count .middle-box:hover {
  border: 1px solid #409eff;
}
.count .middle-box button:hover {
  color: #409eff;
}
.count .middle-box button {
  width: 35px;
  font-size: 20px;
  font-weight: bold;
  background: #f5f7fa;
  border: none;
  cursor: pointer;
}
.count .middle-box input {
  text-align: center;
  width: 38px;
  outline: none;
  border: 1px solid #dcdfe6;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
}
.count .middle-box input::-webkit-outer-spin-button,
.count .middle-box input::-webkit-inner-spin-button {
  -webkit-appearance: none;
}
.count .bottom-box {
  display: flex;
  justify-content: space-around;
  height: 35px;
}
.count .bottom-box button {
  width: 58px;
  background: #f5f7fa;
  border: 1px solid #dcdfe6;
  cursor: pointer;
}
.count .bottom-box button:hover {
  background: #dcdfe6;
  color: #409eff;
}
</style>