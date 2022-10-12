<template>
  <view class="box-bg">
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
</style>