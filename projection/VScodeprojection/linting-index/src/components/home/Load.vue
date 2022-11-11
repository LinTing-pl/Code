<template>
  <div class="container">
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-url">链接: {{ item.url }}</span>
        <span class="info-psd">提取码: {{ item.code }}</span>
      </div>
      <a href="#">立即下载</a>
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
      this.$axios.default.get("/dev-api/load/get").then((res) => {
        this.srcList = res.data;
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
  background-color: #fff;
  margin-bottom: 10px;
}
.card {
  width: 100%;
  height: 100px;
  position: relative;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #ddd;
  padding: 10px 0;
}
.img {
  display: flex;
  align-items: center;
  height: 100%;
  width: 120px;
}
.img img {
  height: 90%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.info {
  height: 100%;
  width: calc(100% - 250px);
  display: flex;
  position: relative;
  margin-left: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: start;
}
.info .info-title {
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 10px;
}
.info .info-url {
  font-size: 18px;
}
.info .info-psd {
  font-size: 18px;
  color: #aaa;
}
.card a {
  text-decoration: none;
  color: #319bff;
  position: absolute;
  right: 40px;
}
.card a:hover {
  color: green;
}
</style>