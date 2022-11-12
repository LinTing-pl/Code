<template>
  <div class="side">
    <div class="side-content">
      <!-- side的大图片 -->
      <div class="img">
        <img :src="bigImg" alt="" />
      </div>
      <span class="title">精选</span>
      <!-- 精选展示内容 -->
      <div class="content">
        <!-- enter可展示内容 -->
        <div
          :class="{ info: true, active: index === 0 }"
          v-for="(item, index) in sideList"
          :key="index"
          @mouseenter="addActive"
        >
          <div class="img"><img :src="item.img" alt="" /></div>
          <div class="info-side">
            <div class="info-title">{{ item.title }}</div>
            <button class="btn" @click="read(item.id)">阅读</button>
          </div>
        </div>
      </div>
    </div>
    <div class="side-footer">
      Linting | 移动端 <br />
      团队介绍 <br />
      Linting官方网站
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      sideList: [],
      bigImg: "",
    };
  },
  mounted() {
    if (sessionStorage.getItem("sidecontent")) {
      let data = JSON.parse(sessionStorage.getItem("sidecontent"));
      this.sideList = data.slice(0, 4);
      this.bigImg = this.sideList[0]["img"];
    } else {
      this.getData();
    }
  },
  methods: {
    getData() {
      this.$axios.default.get("/dev-api/blog/get").then((res) => {
        sessionStorage.setItem("sidecontent", JSON.stringify(res.data));
        this.sideList = res.data.slice(0, 4);
        this.bigImg = this.sideList[0]["img"];
      });
    },
    addActive(e) {
      const divs = document.querySelectorAll(".side-content .info");
      divs.forEach((div) => {
        div.classList.remove("active");
      });
      e.target.classList.add("active");
    },
    read(id) {
      this.$router
        .push({
          name: "blogcontent",
          params: {
            id: id,
          },
        })
        .catch((err) => {});
    },
  },
};
</script>
<style lang='scss' scoped>
.side {
  min-width: 288px;
  height: 100%;
  margin-left: 2%;
}
.side-content {
  width: 100%;
  background-color: #fff;
  padding-bottom: 10px;
}
.img {
  height: 200px;
  width: 100%;
}
.img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.title {
  display: block;
  text-align: left;
  font-size: 20px;
  font-weight: bold;
  margin: 5px 0;
  text-indent: 5px;
}
.info {
  width: 100%;
  height: 30px;
  border-top: 1px solid #ddd;
  position: relative;
  padding: 5px 0;
}
.info .img {
  position: absolute;
  opacity: 0;
  visibility: hidden;
  left: 5px;
}
.info .info-title {
  width: 100%;
  height: 30px;
  position: relative;
  font-size: 18px;
  font-weight: bold;
  text-align: justify;
  left: 5px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.info .btn {
  opacity: 0;
  visibility: hidden;
  cursor: pointer;
}
.info.active {
  height: 80px;
  display: flex;
}

.info.active .img {
  opacity: 1;
  visibility: visible;
  position: relative;
  height: 70px;
  width: 100px;
  top: 5px;
}
.info.active .img img {
  width: 100px;
  height: 70px;
  object-fit: cover;
}
.info.active .info-side {
  position: relative;
}
.info.active .info-side .info-title {
  font-size: 15px;
  font-weight: bold;
  left: 10px;
  top: 5px;
  height: 43px;
  width: 120px;
  text-align: left;
  white-space: normal;
}
.info.active .info-side .btn {
  opacity: 1;
  visibility: initial;
  width: 50px;
  height: 30px;
  line-height: 30px;
  position: absolute;
  left: 10px;
  bottom: 5px;
  background-color: #e4f0fc;
  color: #46a5fd;
  outline: none;
  border: none;
}
.info.active .info-side .btn:hover {
  box-shadow: 0 0 5px rgb(156, 209, 233);
}
.side-footer {
  font-size: 18px;
  color: #c6c6c6;
  text-align: left;
  line-height: 1.5;
}
</style>