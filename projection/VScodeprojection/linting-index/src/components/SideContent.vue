<template>
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
          <button class="btn">阅读</button>
        </div>
      </div>
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
    this.getData();
  },
  methods: {
    getData() {
      this.$axios.default.get("/dev-api/side/get").then((res) => {
        this.sideList = res.data;
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
  },
};
</script>
<style lang='scss' scoped>
.side-content {
  width: 30%;
  height: 100%;
  margin-left: 2%;
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
}
.info {
  width: 100%;
  height: 30px;
  border-top: 1px solid #ddd;
  position: relative;
}
.info .img {
  position: absolute;
  opacity: 0;
  visibility: hidden;
  left: 5px;
}
.info .info-title {
  position: relative;
  font-size: 18px;
  font-weight: bold;
  text-align: left;
  left: 5px;
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
  visibility: initial;
  position: relative;
  height: 70px;
  width: 90px;
  top: 5px;
}
.info.active .info-side {
  position: relative;
}
.info.active .info-side .info-title {
  font-size: 18px;
  font-weight: bold;
  left: 10px;
  top: 5px;
}
.info.active .info-side .btn {
  opacity: 1;
  visibility: initial;
  width: 50px;
  height: 25px;
  position: absolute;
  left: 10px;
  bottom: 5px;
  background-color: #e4f0fc;
  color: #46a5fd;
  outline: none;
  border: none;
}
</style>