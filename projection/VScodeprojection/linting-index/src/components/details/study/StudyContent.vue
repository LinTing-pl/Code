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
      <div class="middle-up">
        <StudySrc :bookcontent="bookcontent"></StudySrc>
      </div>
      <div class="middle-down">
        <Remark cls="study" :id="studyContentList.id"></Remark>
      </div>
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
import Remark from "@/components/public/Remark";
import Chapter from "./StudyChapter.vue";
import StudySrc from "./StudySrc.vue";
export default {
  components: {
    Chapter,
    StudySrc,
    Remark,
  },
  data() {
    return {
      studyContentList: [],
      othersList: [],
      bookcontent: "",
      remarkData: [],
    };
  },
  created() {
    let data = JSON.parse(
      sessionStorage.getItem(`studycontent${this.$route.params.id}`)
    );
    this.studyContentList = data;
    this.othersList = JSON.parse(sessionStorage.getItem("study")).slice(0, 4);
  },
  methods: {
    putBookcontent(data) {
      this.bookcontent = data;
    },
    read(id) {
      if (sessionStorage.getItem(`studycontent${id}`)) {
        this.$router
          .push("/studycontent/" + id)
          .then((res) => {
            this.$router.go(0);
          })
          .catch((err) => {});
      } else {
        this.$axios.default.get(`/dev-api/study/get/${id}`).then((res) => {
          sessionStorage.setItem(`studycontent${id}`, JSON.stringify(res.data));
          this.$router
            .push("/studycontent/" + id)
            .then((res) => {
              this.$router.go(0);
            })
            .catch((err) => {});
        });
      }
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
  margin: 0 10px 10px;
}
.middle .middle-up {
  width: 100%;
  height: 500px;
  background-color: #fff;
  margin-bottom: 10px;
}
.middle .middle-down {
  width: 100%;
  background: #fff;
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