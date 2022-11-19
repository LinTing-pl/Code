<template>
  <div class="studysrc-container">
    <div class="top">
      {{ bookcontent.title }}
    </div>
    <div class="bookcontent">
      {{ bookcontent.content }}
    </div>
  </div>
</template>
<script>
export default {
  props: ["bookcontent"],
};
</script>
<style lang='scss' scoped>
.studysrc-container {
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