<template>
  <div class="search-container">
    <div class="card" v-for="(item, index) in curList" :key="index">
      <div class="img">
        <img :src="item.img" alt="" />
      </div>
      <div class="info" v-if="item.cls !== '下载'">
        <span class="info-title">{{ item.title }}</span>
        <span class="info-info">{{ item.info }}</span>
        <button class="info-btn" @click="read(item.cls, item.id)">阅读</button>
      </div>
      <div class="info" v-else>
        <span class="info-title">{{ item.title }}</span>
        <span class="info-url">链接: {{ item.url }}</span>
        <span class="info-psd">提取码: {{ item.code }}</span>
      </div>
      <a :href="item.url" v-if="item.cls === '下载'" target="_blank"
        >立即下载</a
      >
    </div>
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page.sync="currentPage"
      :page-size="5"
      layout="total, prev, pager, next"
      :total="searchLength"
    >
    </el-pagination>
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
  created() {
    this.srcList = this.search();
    this.searchLength = this.srcList.length;
    this.handleCurrentChange();
  },
  methods: {
    read(cls, id) {
      if (sessionStorage.getItem(`${this.cls[cls]}${id}`)) {
        this.$router.push({
          name: this.cls[cls],
          params: { id: id },
        });
      } else {
        let loading = this.$loading({
          lock: true,
          text: "资源获取中。。。",
          background: "rgba(0, 0, 0, 0.5)",
        });
        this.$axios.default
          .get(`/dev-api/${this.cls[cls].slice(0, -7)}/get/${id}`)
          .then((res) => {
            sessionStorage.setItem(
              `${this.cls[cls]}${id}`,
              JSON.stringify(res.data)
            );
            this.$router
              .push({
                name: this.cls[cls],
                params: { id: id },
              })
              .then((res) => {
                loading.close();
              });
          });
      }
    },
    handleCurrentChange() {
      this.curList = this.srcList.slice(
        (this.currentPage - 1) * 5,
        this.currentPage * 5
      );
    },
    search() {
      let searchParams = sessionStorage.getItem("search").toLowerCase();
      const data1 = JSON.parse(sessionStorage.getItem("study"));
      const data2 = JSON.parse(sessionStorage.getItem("blog"));
      const data3 = JSON.parse(sessionStorage.getItem("video"));
      const data4 = JSON.parse(sessionStorage.getItem("load"));
      let res = [];
      data1.forEach((v) => {
        let src = v.title.toLowerCase();
        if (src.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      data2.forEach((v) => {
        let src = v.title.toLowerCase();
        if (src.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      data3.forEach((v) => {
        let src = v.title.toLowerCase();
        if (src.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      data4.forEach((v) => {
        let src = v.title.toLowerCase();
        if (src.indexOf(searchParams) !== -1) {
          res.push(v);
        }
      });
      return res;
    },
  },
};
</script>
<style lang='scss' scoped>
.search-container {
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