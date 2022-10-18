<template>
  <div class="middle-Container">
    <div class="top">
      {{ bookcontent.title || title }}
    </div>
    <div class="bookcontent">
      {{ bookcontent.content || content }}
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      title: "",
      content: "",
    };
  },
  props: ["bookcontent"],
  mounted() {
    let data = JSON.parse(localStorage.getItem("bookcontent"));
    this.title = data.title;
    this.content = data.content;
  },
};
</script>
<style lang='scss' scoped>
.middle-Container {
  height: 100%;
  width: 100%;
}
.top {
  height: 20px;
  margin: 0 14px;
  padding: 14px;
  text-align: left;
  font-weight: bold;
  font-size: 20px;
  border-bottom: 1px solid #ddd;
}
.bookcontent {
  box-sizing: border-box;
  width: 100%;
  height: 100%;
  padding: 10px 28px;
  white-space: normal;
  word-wrap: break-word;
  text-align: left;
  line-height: 1.5;
  font-size: 17px;
}
</style>