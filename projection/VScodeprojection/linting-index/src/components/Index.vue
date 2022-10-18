<template>
  <div class="container">
    <!-- 遍历三个卡片 -->
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="title">
        <span>{{ item[0].cls }}</span
        ><router-link class="more" :to="item[0].index"
          ><span @click="pushIndex(item[0].index)"
            >查看更多 ></span
          ></router-link
        >
      </div>
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
    pushIndex(index) {
      this.$emit("pushIndex", index);
    },
  },
};
</script>
<style lang='scss' scoped>
.container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  margin: 0;
}
.card {
  width: 100%;
  height: 260px;
  position: relative;
  margin-bottom: 25px;
}
.title {
  width: calc(100% - 40px);
  height: 25px;
  text-align: left;
  font-size: 18px;
  background-color: #fff;
  color: #000;
  font-weight: bold;
  margin-bottom: 10px;
  display: flex;
  justify-content: space-between;
  padding: 5px 20px;
}
.more {
  color: #878787;
  text-decoration: none;
}
.content {
  width: calc(100% - 20px);
  height: 110px;
  background-color: #fff;
  margin-bottom: 10px;
  position: relative;
  display: flex;
  padding-left: 20px;
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