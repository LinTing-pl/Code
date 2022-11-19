<template>
  <div class="searchcontent-container">
    <div class="title">
      <div class="adminSearchBack" @click="back">返回</div>
      查询结果
    </div>
    <div class="searchcard" v-for="(item, index) in cardList" :key="index">
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
          <button class="edit-btn" @click="read(item.id)">编辑</button>
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
  props: ["nativeSearch"],
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
  watch: {
    nativeSearch: {
      handler() {
        this.allList = this.nativeSearch;
        this.length = this.allList.length;
        this.handleCurrentChange();
      },
    },
  },
  methods: {
    handleCurrentChange() {
      sessionStorage.setItem("currAdminStudyPage", this.currentPage.toString());
      this.cardList = this.allList.slice(
        5 * (this.currentPage - 1),
        this.currentPage * 5
      );
    },
    back() {
      this.$router.push(sessionStorage.getItem("adminIndex"));
    },
    // del(id) {
    //   this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
    //     confirmButtonText: "确定",
    //     cancelButtonText: "取消",
    //     type: "warning",
    //   })
    //     .then(() => {
    //       this.$axios.default
    //         .delete(`/dev-api/study/delete/${id}`)
    //         .then((res) => {
    //           this.$message({
    //             type: "success",
    //             message: "删除成功!",
    //             showClose: true,
    //           });
    //           this.getData(true);
    //         });
    //     })
    //     .catch(() => {
    //       this.$message({
    //         type: "info",
    //         message: "已取消删除",
    //         showClose: true,
    //       });
    //     });
    // },
    // valueDel(id) {
    //   if (this.priorities[id] > 0) {
    //     this.priorities[id] = this.priorities[id] - 1;
    //     this.$forceUpdate();
    //   }
    // },
    // valueAdd(id) {
    //   if (this.priorities[id] < 100) {
    //     this.priorities[id] = this.priorities[id] + 1;
    //     this.$forceUpdate();
    //   }
    // },
    // resetCurr(id) {
    //   this.priorities[id] = this.prioritiesCopy[id];
    //   this.$forceUpdate();
    // },
    // confirm(id) {
    //   this.$axios.default
    //     .post("/dev-api/study/update", {
    //       id: id,
    //       orderby: this.priorities[id],
    //     })
    //     .then((res) => {
    //       if (res.status === 200) {
    //         this.getData(true);
    //         this.$message({
    //           showClose: true,
    //           message: "优先级设置成功",
    //           type: "success",
    //         });
    //       }
    //     });
    // },
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