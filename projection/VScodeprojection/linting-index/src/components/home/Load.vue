<template>
  <div class="load-container">
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-url">链接: {{ item.url }}</span>
        <span class="info-psd">提取码: {{ item.code }}</span>
      </div>
      <a :href="item.url" target="_blank">立即下载</a>
    </div>
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="5"
      layout="total, prev, pager, next"
      :total="loadLength"
    >
    </el-pagination>
  </div>
</template>
<script>
export default {
  data() {
    return {
      srcList: [],
      currentPage: 1,
      loadLength: JSON.parse(sessionStorage.getItem("load")).length,
    };
  },
  created() {
    this.currentPage = JSON.parse(sessionStorage.getItem("currLoadPage")) || 1;
    this.handleCurrentChange();
  },
  methods: {
    handleCurrentChange() {
      sessionStorage.setItem("currLoadPage", this.currentPage.toString());
      try {
        this.srcList = JSON.parse(sessionStorage.getItem("load")).slice(
          (this.currentPage - 1) * 5,
          this.currentPage * 5
        );
      } catch (e) {
        this.$router.push("/");
      }
    },
  },
};
</script>
<style lang='scss' scoped>
.load-container {
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
  padding-left: 10px;
}
.img img {
  height: 100%;
  width: 100%;
  object-fit: cover;
}
.info {
  height: 100%;
  width: 472.8px;
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