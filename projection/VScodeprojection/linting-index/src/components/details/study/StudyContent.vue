<template>
  <div class="studycontent-container">
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
      <StudySrc :bookcontent="bookcontent"></StudySrc>
    </div>
    <div class="right">
      <div
        class="others"
        @click="read(item.id)"
        v-for="(item, index) in othersList"
        :key="index"
      >
        {{ item.title }}
      </div>
    </div>
  </div>
</template>
<script>
import Chapter from "./StudyChapter.vue";
import StudySrc from "./StudySrc.vue";
export default {
  components: {
    Chapter,
    StudySrc,
  },
  data() {
    return {
      studyContentList: [],
      othersList: [],
      bookcontent: "",
    };
  },
  mounted() {
    let storage = sessionStorage.getItem(
      `studycontent${this.$route.params.id}`
    );
    if (storage) {
      let data = JSON.parse(storage);
      this.studyContentList = data;
      this.othersList = JSON.parse(sessionStorage.getItem("study")).slice(0, 4);
    } else {
      this.getData();
    }
  },
  methods: {
    getData() {
      let index = this.$route.params.id;
      this.$axios.default.get(`/dev-api/study/get/${index}`).then((res) => {
        sessionStorage.setItem(
          `studycontent${index}`,
          JSON.stringify(res.data)
        );
        this.studyContentList = res.data;
      });
      this.othersList = JSON.parse(sessionStorage.getItem("study")).slice(0, 4);
    },

    putBookcontent(data) {
      this.bookcontent = data;
    },
    read(id) {
      this.$router
        .push("/studycontent/" + id)
        .then((res) => {
          this.$router.go(0);
        })
        .catch((err) => {});
    },
  },
};
</script>
<style lang='scss' scoped>
.studycontent-container {
  background-color: #f6f6f6;
  width: 960px;
  display: flex;
  flex-direction: row;
  align-items: start;
  margin-top: 10px;
}
.left {
  width: 22%;
  position: relative;
}
.middle {
  width: 65%;
  height: 590px;
  background-color: #fff;
  margin: 0 10px 10px;
}
.right {
  width: 13%;
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
.right .others {
  width: 100%;
  height: 30px;
  padding: 10px 5px;
  margin-bottom: 10px;
  line-height: 30px;
  border-radius: 10px;
  background-color: #fff;
  cursor: pointer;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.right .others:hover {
  background-color: #e6e6e6;
}
</style>