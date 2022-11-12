<template>
  <div class="container">
    <!-- 遍历三个卡片 -->
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="title">
        <span>精选{{ item[0].cls }}</span
        ><span class="more" @click="pushIndex(index)">查看更多 ></span>
      </div>
      <!-- 每个卡片两个内容 -->
      <div class="content" v-for="(item2, i) in item" :key="i">
        <div class="img">
          <img :src="item2.img" alt="" />
        </div>
        <div class="info">
          <span class="info-title">{{ item2.title }}</span>
          <span class="info-info">{{ item2.info }}</span>
          <button class="info-btn" @click="toSrc(index, item2.id)">
            {{ item2.cls === "视频" ? "观看" : "阅读" }}
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
      indexes: ["study", "blog", "video"],
      srcList: [],
    };
  },
  created() {
    if (!this.srcList.length) {
      if (sessionStorage.getItem("study") === null) {
        this.getData();
      } else {
        this.srcList = [
          JSON.parse(sessionStorage.getItem("study")).slice(0, 2),
          JSON.parse(sessionStorage.getItem("blog")).slice(0, 2),
          JSON.parse(sessionStorage.getItem("video")).slice(0, 2),
        ];
      }
    }
  },
  methods: {
    async getData() {
      await this.$axios.default
        .post("/dev-api/index/get", { flag: "all" })
        .then((res) => {
          this.srcList = [
            res.data[0].slice(0, 2),
            res.data[1].slice(0, 2),
            res.data[2].slice(0, 2),
          ];
          sessionStorage.setItem("study", JSON.stringify(res.data[0]));
          sessionStorage.setItem("blog", JSON.stringify(res.data[1]));
          sessionStorage.setItem("video", JSON.stringify(res.data[2]));
          sessionStorage.setItem("load", JSON.stringify(res.data[3]));
        });
    },
    pushIndex(index) {
      this.$router.push({
        name: this.indexes[index],
      });
    },
    toSrc(index, id) {
      this.$router.push({
        name: this.indexes[index] + "content",
        params: {
          id: id,
        },
      });
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
  color: #ccc;
  text-decoration: none;
  cursor: pointer;
  font-size: 16px;
}
.more:hover {
  color: #878787;
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
  width: 472.8px;
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
.info .info-info {
  font-size: 14px;
  color: #ccc;
  margin: 10px 0;
  max-width: 480px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
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
.info .info-btn:hover {
  box-shadow: 0 0 5px rgb(156, 209, 233);
}
</style>