<template>
  <div class="container">
    <div class="card" v-for="(item, index) in curList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-info">{{ item.info }}</span>
        <button class="info-btn" @click="read(item.cls, item.id)">阅读</button>
      </div>
    </div>
    <div class="block">
      <el-pagination
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="5"
        layout="total, prev, pager, next"
        :total="searchLength"
      >
      </el-pagination>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      srcList: [],
      curList: [],
      currentPage: 1,
      searchLength: 0,
      cls: {
        手册: "studycontent",
        博客: "blogcontent",
        视频: "videocontent",
      },
    };
  },
  mounted() {
    this.srcList = this.search();
    this.searchLength = this.srcList.length;
    this.handleCurrentChange();
  },
  methods: {
    read(cls, id) {
      this.$router.push({
        name: this.cls[cls],
        params: { id: id },
      });
    },
    handleCurrentChange() {
      this.curList = this.srcList.slice(
        (this.currentPage - 1) * 5,
        this.currentPage * 5
      );
    },
    search() {
      let searchParams = sessionStorage.getItem("search");
      const data1 = JSON.parse(sessionStorage.getItem("study"));
      const data2 = JSON.parse(sessionStorage.getItem("blog"));
      const data3 = JSON.parse(sessionStorage.getItem("video"));
      let res = [];
      data1.forEach((v) => {
        if (v.title.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      data2.forEach((v) => {
        if (v.title.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      data3.forEach((v) => {
        if (v.title.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      return res;
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
  margin-bottom: 20px;
}
.img {
  display: flex;
  align-items: center;
  height: 100%;
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