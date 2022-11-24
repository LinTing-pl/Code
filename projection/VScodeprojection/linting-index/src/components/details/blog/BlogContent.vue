<template>
  <div class="blogcontent-container">
    <div class="left">
      <div class="title">{{ data.title }}</div>
      <div class="date">{{ data.date }}</div>
      <div class="blog-content">
        {{ data.content }}
      </div>
    </div>
    <SideContent></SideContent>
  </div>
</template>
<script>
import SideContent from "../../public/SideContent.vue";
export default {
  components: {
    SideContent,
  },
  data() {
    return {
      data: [],
      id: "",
    };
  },
  created() {
    let storage = sessionStorage.getItem(`blogcontent${this.$route.params.id}`);
    if (storage) {
      let data = JSON.parse(storage);
      this.data = data;
    } else {
      this.getOneBlog();
    }
  },
  watch: {
    //监听route
    $route: {
      handler() {
        this.id = this.$route.params.id;
        if (this.id) {
          //不为空
          let storage = sessionStorage.getItem(
            `blogcontent${this.$route.params.id}`
          );
          if (storage) {
            let data = JSON.parse(storage);
            this.data = data;
          } else {
            this.getOneBlog();
          }
        }
      },
      // immediate: true, //在watch中首次绑定的时候，是否执行handler
    },
  },
  methods: {
    getOneBlog() {
      let id = this.$route.params.id;
      this.$axios.default.get(`/dev-api/blog/get/${id}`).then((res) => {
        sessionStorage.setItem(`blogcontent${id}`, JSON.stringify(res.data));
        this.data = res.data;
      });
    },
  },
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
  min-height: 590px;
  background-color: #fff;
  padding: 10px;
  margin-bottom: 10px;
  font-size: 18px;
  padding: 10px 20px;
  display: flex;
  flex-direction: column;
}
.left div {
  text-align: left;
  padding: 5px;
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
  word-wrap: break-word;
}
.blog-content::-webkit-scrollbar {
  width: 10px;
}
.blog-content:hover::-webkit-scrollbar-thumb {
  background: rgba(195, 230, 236, 0.712);
  border-radius: 5px;
}
</style>