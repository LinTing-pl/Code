<template>
  <div class="usercontent-container">
    <div class="btns">
      用户列表
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
    <div class="usercard" v-for="(item, index) in cardList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-username">账号: {{ item.username }}</span>
        <span class="info-password">密码: {{ item.password }}</span>
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
    };
  },
  created() {
    let data = JSON.parse(sessionStorage.getItem("adminUser"));
    this.currentPage =
      JSON.parse(sessionStorage.getItem("currAdminUserPage")) || 1;
    if (data) {
      this.allList = data;
      this.length = this.allList.length;
      this.handleCurrentChange();
    } else {
      this.getData();
    }
  },
  methods: {
    async getData(flag) {
      await this.$axios.default.get("/dev-api/user/get").then((res) => {
        this.allList = res.data;
        this.length = this.allList.length;
        flag ? null : (this.currentPage = 1);
        this.cardList = this.allList.slice(
          (this.currentPage - 1) * 5,
          this.currentPage * 5
        );
        sessionStorage.setItem("adminUser", JSON.stringify(res.data));
      });
    },
    handleCurrentChange() {
      sessionStorage.setItem("currAdminUserPage", this.currentPage.toString());
      this.cardList = this.allList.slice(
        5 * (this.currentPage - 1),
        this.currentPage * 5
      );
    },
  },
};
</script>
<style lang="scss" scoped>
.usercontent-container {
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
.usercard {
  height: 100px;
  border-top: 1px solid #545c64;
  display: flex;
}
.usercard .img {
  border: 1px solid #545c64;
  margin: 4px 10px 4px 10px;
  display: flex;
  align-items: center;
  height: 90px;
  width: 120px;
  min-width: 120px;
}
.usercard .img img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.usercard .info {
  min-width: 335px;
  max-width: 644px;
  width: 644px;
  border-left: 1px dashed #545c64;
  border-right: 1px dashed #545c64;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 5px;
}
.usercard .info .info-username {
  margin-bottom: 5px;
  font-weight: bold;
  font-size: 18px;
  overflow: hidden;
  text-align: left;
}
.usercard .info .info-password {
  text-align: left;
  line-height: 1.5;
  overflow: hidden;
}
.usercard .opts {
  min-width: 220px;
  display: flex;
}
.usercontent-container .usercard:nth-last-child(2) {
  border-bottom: 1px solid #545c64;
}
::v-deep.el-pagination {
  position: absolute;
  width: 100%;
  bottom: 0;
  background-color: #fff;
}
</style>
