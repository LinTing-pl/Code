<template>
  <view class="box-bg">
    <div class="fatie" @click="toAddform">发帖</div>
    <view class="floor">
      <ul>
        <li @click="toIndex">首页</li>
        <li @click="toFa">发帖</li>
        <li @click="toMe">我的</li>
      </ul>
    </view>
  </view>
</template>
<script>
export default {
  data() {
    return {};
  },
  methods: {
    toIndex() {
      wx.redirectTo({
        url: "/pages/index",
      });
    },
    toFa() {
      wx.redirectTo({
        url: "/pages/fatie",
      });
    },
    toMe() {
      wx.redirectTo({
        url: "/pages/me",
      });
    },
    toAddform() {
      wx.redirectTo({
        url: "/pages/addform",
      });
    },
  },
};
</script>
<style lang='scss' scoped>
.floor {
  position: fixed;
  bottom: 0;
}
.floor ul {
  width: 100vw;
  display: flex;
  justify-content: space-around;
  background: #1e95ff;
}
.floor ul li {
  font-size: 30px;
}
.fatie {
  border-radius: 12px;
  background-color: #1e95ff;
  font-size: 40px;
  text-align: center;
  height: 100px;
  line-height: 100px;
}
</style>