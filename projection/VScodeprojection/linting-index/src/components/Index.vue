<template>
  <div class="container">
    <!-- 遍历三个卡片 -->
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="title">{{ item[0].cls }}</div>
      <!-- 每个卡片两个内容 -->
      <div class="content" v-for="(item2, i) in item" :key="i">
        <div class="img">
          <img :src="item2.img" alt="" />
        </div>
        <div class="info">
          <span class="info-title">{{ item2.title }}</span>
          <span class="info-date">{{ item2.date }}</span>
          <span class="info-info" v-if="item2.info">{{ item2.info }}</span>
          <button v-else class="info-btn">
            {{ item2.cls === "精选手册" ? "阅读" : "观看" }}
          </button>
        </div>
      </div>
    </div>
    <div class="bottom">更多精彩内容敬请期待~</div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      srcList: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      this.$axios.default.get("/dev-api/index/get").then((res) => {
        this.srcList = res.data;
      });
    },
  },
};
</script>
<style lang='scss' scoped>
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 0;
}
.card {
  width: 100%;
  height: 260px;
  position: relative;
  margin-bottom: 15px;
}
.title {
  width: 100%;
  height: 25px;
  text-align: left;
  text-indent: 20px;
  font-size: 18px;
  background-color: #fff;
  color: #000;
  font-weight: bold;
  margin-bottom: 10px;
}
.content {
  width: 100%;
  height: 110px;
  background-color: #fff;
  margin-bottom: 10px;
  position: relative;
  display: flex;
}
.bottom {
  width: 100%;
  height: 25px;
  font-size: 18px;
  background-color: #fff;
  color: #ddd;
}
.img {
  margin: auto 0;
  height: 90px;
  width: 120px;
  position: relative;
}
.img img {
  height: 100%;
  width: 100%;
}
.info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
  margin-left: 20px;
}
.info .info-title {
  font-weight: bold;
  font-size: 20px;
}
.info .info-date {
  font-size: 14px;
  color: #ccc;
  margin: 10px 0;
}
.info .info-info {
  font-size: 14px;
  color: #aaa;
}
.info .info-btn {
  width: 80px;
  height: 30px;
  background-color: #e4f0fc;
  color: #46a5fd;
  outline: none;
  border: none;
  cursor: pointer;
  user-select: none;
}
</style>