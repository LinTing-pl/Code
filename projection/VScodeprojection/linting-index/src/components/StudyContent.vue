<template>
  <div class="container">
    <div class="left">
      <div class="book">
        <div class="img"><img :src="studyContentList.img" alt="" /></div>
        <div class="info">
          <p class="info-title">{{ studyContentList.title }}</p>
          <p>{{ studyContentList.bookInfo }}</p>
        </div>
      </div>
      <Chapter
        :list="studyContentList.chapters"
        @putBookcontent="putBookcontent"
      ></Chapter>
    </div>
    <div class="middle">
      <router-view :bookcontent="bookcontent"></router-view>
    </div>
    <div class="right">
      <div class="others"></div>
    </div>
  </div>
</template>
<script>
import Chapter from "./StudyChapter";
export default {
  components: {
    Chapter,
  },
  data() {
    return {
      studyContentList: [],
      bookcontent: "",
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      let index = this.$route.params.id;
      this.$axios.default.get(`/dev-api/study/get/${index}`).then((res) => {
        this.studyContentList = res.data;
      });
    },
    putBookcontent(value) {
      this.bookcontent = value;
    },
  },
};
</script>
<style lang='scss' scoped>
.container {
  background-color: #f6f6f6;
  width: 960px;
  display: flex;
  flex-direction: row;
  align-items: start;
  margin-top: 10px;
}
.left {
  width: 22%;
}
.middle {
  width: 65%;
  min-height: calc(100vh - 160px);
  background-color: #fff;
  margin: 0 10px;
}
.right {
  width: 13%;
  border: 1px solid red;
}
.book {
  width: 100%;
  height: 120px;
  display: flex;
  align-items: center;
  background-color: #fff;
  margin-bottom: 10px;
}
.book .img {
  width: 40%;
  height: 80%;
  margin: 0 8px;
}
.book .img img {
  width: 100%;
  height: 100%;
}
.book .info {
  width: 60%;
  height: 100%;
  position: relative;
  text-align: left;
}
.book .info p {
  margin: 0;
  padding: 0;
  font-size: 10px;
  position: relative;
  top: 15px;
}
.book .info .info-title {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 5px;
}
.book .info p:nth-child(2) {
  color: #a4a4a4;
  width: 116px;
  height: 70px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
}
</style>