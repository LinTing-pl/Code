<template>
  <div class="container">
    <div class="video-title">{{ videoSrcList.section }}</div>
    <div class="video-date">{{ videoSrcList.date }}</div>
    <div class="video-content">
      <video :src="videoSrcList.mp4" controls></video>
    </div>
  </div>
</template>
<script>
export default {
  props: ["videoSrcList"],
};
</script>
<style lang='scss' scoped>
.container {
  background-color: #fff;
  display: flex;
  flex-direction: column;
  align-items: start;
  padding: 10px;
  margin-bottom: 15px;
}
.video-title {
  font-weight: bold;
  font-size: 20px;
  letter-spacing: 3px;
}
.video-date {
  color: #aaa;
  margin: 12px 0 20px;
}
.video-content {
  width: 100%;
  height: 400px;
  padding-bottom: 20px;
}
.video-content video {
  width: 100%;
  height: 100%;
  cursor: pointer;
}
</style>