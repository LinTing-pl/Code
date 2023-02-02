<template>
  <div class="blogcontent-container">
    <div class="left">
      <div class="left-up">
        <div class="title">{{ data.title }}</div>
        <div class="date">{{ data.date }}</div>
        <div class="blog-content" v-html="data.content"></div>
      </div>
      <div class="left-down">
        <Remark cls="blog" :id="data.id"></Remark>
      </div>
    </div>
    <SideContent></SideContent>
  </div>
</template>
<script>
import SideContent from "../../public/SideContent.vue";
import Remark from "../../public/Remark";
export default {
  components: {
    SideContent,
    Remark,
  },
  data() {
    return {
      data: [],
      id: "",
    };
  },
  created() {
    this.data = JSON.parse(
      sessionStorage.getItem(`blogcontent${this.$route.params.id}`)
    );
  },
  // watch: {
  //   //监听route
  //   $route: {
  //     handler() {
  //       this.id = this.$route.params.id;
  //       if (this.id) {
  //         this.data = JSON.parse(
  //           sessionStorage.getItem(`blogcontent${this.$route.params.id}`)
  //         );
  //       }
  //     },
  //     immediate: true, //在watch中首次绑定的时候，是否执行handler
  //   },
  // },
};
</script>
<style lang='scss' scoped>
.blogcontent-container {
  width: 960px;
  display: flex;
  margin-top: 10px;
}
.left {
  box-sizing: border-box;
  width: 70%;

  .left-up {
    background-color: #fff;
    padding: 10px;
    margin-bottom: 10px;
    font-size: 18px;
    padding: 10px 20px;
    display: flex;
    flex-direction: column;
    div {
      text-align: left;
      padding: 5px;
    }
  }
  .left-down {
    background-color: #fff;
  }
}

.title {
  font-size: 20px;
  font-weight: bold;
}
.date {
  color: #ccc;
}
.blog-content {
  width: 100%;
  height: 470px;
  overflow: auto;
  word-break: break-all;
}
.blog-content::-webkit-scrollbar {
  width: 10px;
}
.blog-content:hover::-webkit-scrollbar-thumb {
  background: rgba(195, 230, 236, 0.712);
  border-radius: 5px;
}
</style>