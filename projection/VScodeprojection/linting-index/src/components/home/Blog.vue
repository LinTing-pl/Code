<template>
  <div class="container">
    <div
      class="card"
      v-for="(item, index) in srcList"
      :key="index"
      @click="read(item.id)"
    >
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-date">{{ item.date }}</span>
        <span class="info-info">{{ item.info }}</span>
      </div>
    </div>
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="5"
      layout="total, prev, pager, next"
      :total="blogLength"
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
      blogLength: JSON.parse(sessionStorage.getItem("blog")).length,
    };
  },
  mounted() {
    this.currentPage = JSON.parse(sessionStorage.getItem("currBlogPage")) || 1;
    this.handleCurrentChange();
  },
  methods: {
    read(id) {
      this.$router.push({
        name: "blogcontent",
        params: { id: id },
      });
    },
    handleCurrentChange() {
      sessionStorage.setItem("currBlogPage", this.currentPage.toString());
      try {
        this.srcList = JSON.parse(sessionStorage.getItem("blog")).slice(
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
.container {
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: column;
  margin: 0;
}
.card {
  width: 100%;
  height: 110px;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #fff;
  margin-bottom: 10px;
  cursor: pointer;
}
.img {
  display: flex;
  align-items: center;
  height: 90px;
  width: 120px;
}
.img img {
  height: 100%;
  width: 100%;
}
.info {
  height: 100%;
  width: calc(100% - 180px);
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
}
.info .info-date {
  font-size: 14px;
  color: #ccc;
  margin: 10px 0;
}
.info .info-info {
  font-size: 20px;
  color: #aaa;
}
.block {
  width: 100%;
  background-color: #fff;
  margin-bottom: 10px;
}
</style>