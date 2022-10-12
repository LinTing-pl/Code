<template>
  <view class="box-bg">
    <uni-search-bar :focus="true" v-model="searchData" @input="search">
    </uni-search-bar>
    <uni-table
      ref="table"
      border
      stripe
      emptyText="暂无更多数据"
      @selection-change="selectionChange"
    >
      <uni-tr v-for="(item, index) in jobData" :key="index">
        <uni-card>
          <div slot="title">{{ item.job }}</div>
          <text>
            兼职工作类型:{{ item.job }} \n发布者:{{ item.username }} \n手机号:{{
              item.phonenumber
            }}\n工作地点(市或区):{{ item.city }} \n工作内容:{{
              item.content
            }}\n联系地址:{{ item.adress }}\n 备注:{{ item.beifen }}</text
          >
        </uni-card>
      </uni-tr>
    </uni-table>
    <uni-fab
      ref="fab"
      horizontal="right"
      vertical="bottom"
      @fabClick="toAddform"
    />
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
    return {
      jobData: [],
      searchData: "",
    };
  },
  mounted() {
    this.getData();
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
    getData() {
      uni.request({
        url: "http://localhost:8888/dev-api/job/get",
        success: (res) => {
          this.jobData = res.data;
        },
      });
    },
    search() {
      if (this.searchData !== null) {
        uni.request({
          url: `http://localhost:8888/dev-api/job/get/${this.searchData}`,
          success: (res) => {
            this.jobData = res.data;
          },
        });
      } else {
        this.getData();
      }
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
</style>