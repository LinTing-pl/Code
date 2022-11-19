<template>
  <div class="study-container">
    <div class="card" v-for="(item, index) in srcList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-info">{{ item.info }}</span>
        <button class="info-btn" @click="read(item.id)">阅读</button>
      </div>
    </div>
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="5"
      layout="total, prev, pager, next"
      :total="studyLength"
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
      studyLength: JSON.parse(sessionStorage.getItem("study")).length,
    };
  },
  mounted() {
    this.currentPage = JSON.parse(sessionStorage.getItem("currStudyPage")) || 1;
    this.handleCurrentChange();
  },
  methods: {
    read(id) {
      this.$router.push({
        name: "studycontent",
        params: { id: id },
      });
    },
    handleCurrentChange() {
      sessionStorage.setItem("currStudyPage", this.currentPage.toString());
      try {
        this.srcList = JSON.parse(sessionStorage.getItem("study")).slice(
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
.study-container {
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
  margin-bottom: 20px;
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
  border-bottom: 1px solid #ddd;
}
.info .info-title {
  font-weight: bold;
  font-size: 20px;
}
.info .info-info {
  width: 100%;
  margin: 5px 0;
  font-size: 16px;
  text-align: left;
  color: #aaa;
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
</style>