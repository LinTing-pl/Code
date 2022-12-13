<template>
  <div class="nav-tit">
    <div class="nav-back" @click="toHome">返回首页</div>
    后台管理系统
    <el-input
      placeholder="请输入内容"
      v-model="search"
      class="input-with-select"
      @keyup.native.enter="searchSrc"
    >
      <el-select v-model="select" slot="prepend" placeholder="请选择">
        <el-option label="全局搜索" value="全局搜索"></el-option>
        <el-option label="学习手册" value="学习手册"></el-option>
        <el-option label="技术博客" value="技术博客"></el-option>
        <el-option label="教学视频" value="教学视频"></el-option>
        <el-option label="资源下载" value="资源下载"></el-option>
        <el-option label="用户" value="用户"></el-option>
      </el-select>
      <el-button
        slot="append"
        @click="searchSrc"
        icon="el-icon-search"
      ></el-button>
    </el-input>
  </div>
</template>
<script>
export default {
  props: ["searchSelect", "optscount"],
  data() {
    return {
      select: "学习手册",
      search: "",
      compare: {
        study: "学习手册",
        blog: "技术博客",
        video: "教学视频",
        load: "资源下载",
        users: "用户",
      },
      searchcount: 0,
    };
  },
  created() {
    if (sessionStorage.getItem("adminsearchselect")) {
      this.select = sessionStorage.getItem("adminsearchselect");
    }

    this.search = sessionStorage.getItem("adminsearchword");
  },
  updated() {
    sessionStorage.setItem("adminsearchselect", this.select);
  },
  watch: {
    searchSelect: function () {
      this.select = this.compare[this.searchSelect];
    },
    optscount: function () {
      this.searchSrc();
    },
  },
  methods: {
    toHome() {
      this.$router.push("/");
      sessionStorage.removeItem("adminIndex");
    },
    searchSrc() {
      if (!this.search) return;
      sessionStorage.setItem("adminsearchword", this.search);
      let flag;
      switch (this.select) {
        case "全局搜索":
          flag = "all";
          break;
        case "学习手册":
          flag = "study";
          break;
        case "技术博客":
          flag = "blog";
          break;
        case "教学视频":
          flag = "video";
          break;
        case "资源下载":
          flag = "load";
          break;
        case "用户":
          flag = "users";
          break;
      }
      let loading = this.$loading({
        lock: true,
        text: "资源获取中。。。",
        background: "rgba(0, 0, 0, 0.5)",
      });
      this.$axios.default
        .post("dev-api/index/get", {
          flag: flag,
        })
        .then((res) => {
          loading.close();
          let storage = [];
          if (this.select === "全局搜索") {
            let data = [
              ...res.data[0],
              ...res.data[1],
              ...res.data[2],
              ...res.data[3],
            ];

            data.forEach((v) => {
              let src = v.title.toLowerCase();
              let match = this.search.toLowerCase();
              if (src.indexOf(match) !== -1) {
                storage.push(v);
              }
            });
          } else {
            let data = res.data;
            data.forEach((v) => {
              let src = v.title.toLowerCase();
              let match = this.search.toLowerCase();
              if (src.indexOf(match) !== -1) {
                storage.push(v);
              }
            });
          }
          if (this.$router.history.current.name !== "adminsearch") {
            sessionStorage.setItem(
              "adminsearchcontent",
              JSON.stringify(storage)
            );
            this.$router
              .push({ name: "adminsearch" })
              .then((res) => {
                this.$emit("nativeSearch", this.searchcount++);
              })
              .catch((err) => {});
          } else {
            sessionStorage.setItem(
              "adminsearchcontent",
              JSON.stringify(storage)
            );
            this.$emit("nativeSearch", this.searchcount++);
          }
        });
    },
  },
};
</script>
<style lang='scss' scoped>
.nav-tit {
  background: rgb(141, 139, 139);
  height: 60px;
  line-height: 60px;
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 10px;
  position: relative;
  user-select: none;
}
.nav-back {
  position: absolute;
  left: 10px;
  top: 15px;
  font-weight: normal;
  font-size: 15px;
  letter-spacing: normal;
  height: 30px;
  width: 70px;
  line-height: 30px;
  background: #545c64;
  color: #fff;
  border-radius: 10px;
  cursor: pointer;
}
.nav-back:hover {
  background: #ddd;
  color: #545c64;
}
.input-with-select {
  position: absolute;
  top: 10px;
  right: 30px;
  width: 300px;
}
::v-deep.el-select {
  width: 100px;
  font-size: 10px;
}
</style>