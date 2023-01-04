<template>
  <div class="container">
    <!-- 好友列表 -->
    <div class="friend-wrapper">
      <!-- 搜索框 -->
      <Search v-model="searchValue"></Search>
      <!-- 好友列表 -->
      <div class="friend-list">
        <ul>
          <li class="friend-item">
            <div class="list-title">新的朋友</div>
            <div class="friend-info">
              <img
                width="36"
                height="36"
                src="/images/newfriend.jpg"
                class="avatar"
              />
              <div class="remark">新的朋友</div>
            </div>
          </li>
          <li v-for="item in friends" :key="item.letter" class="friend-item">
            <div class="list-title">{{ item.letter }}</div>
            <div
              :class="{
                active: selectedUserId === user.id,
                'friend-info': true,
              }"
              @click="selectedUserId = user.id"
              v-for="user in item.users"
              :key="user.id"
            >
              <img
                width="36"
                height="36"
                :src="'/images/face/' + user?.icon"
                class="avatar"
              />
              <div class="remark">{{ user.nickname }}</div>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <div class="friend-info">
      <!-- 好友详情 -->
      <div class="info-wrapper">
        <div class="friend-info">
          <div class="es-info">
            <div class="left">
              <div class="people">
                <div class="nickname">{{ currentUser?.nickname }}</div>
                <div
                  :class="
                    currentUser?.sex === 'male'
                      ? 'gender-male'
                      : 'gender-female'
                  "
                ></div>
              </div>
              <div class="signature">{{ currentUser?.summary }}</div>
            </div>
            <div class="right">
              <img
                class="avatar"
                width="60"
                height="60"
                :src="'/images/face/' + currentUser?.icon"
              />
            </div>
          </div>
          <div class="detInfo">
            <div class="remark">
              <span>备&nbsp;&nbsp;&nbsp;注</span>{{ currentUser?.remark }}
            </div>
            <div class="area">
              <span>地&nbsp;&nbsp;&nbsp;区</span>{{ currentUser?.area }}
            </div>
            <div class="wxid"><span>微信号</span>{{ currentUser?.wxid }}</div>
          </div>
          <div class="send" @click="handleSend">
            <span>发消息</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import "../assets/css/friend.less";
import Search from "../components/Search.vue";
export default {
  components: { Search },
  async created() {
    this.selectedUserId = this.friends[0]?.users[0]?.id;
  },
  computed: {
    currentUser() {
      let user = null;
      for (let i = 0; i < this.friends.length; i++) {
        const friend = this.friends[i];
        user = friend.users.find((v) => v.id === this.selectedUserId);
        if (user) {
          break;
        }
      }
      return user;
    },
    friends() {
      return this.state.friends;
    },
  },
  data() {
    return {
      searchValue: "",
      selectedUserId: 0,
    };
  },
  methods: {
    handleSend() {
      const recent = {
        user: {
          id: this.currentUser?.id,
          nickname: this.currentUser?.nickname,
          icon: this.currentUser?.icon,
          robot: this.currentUser?.robot,
        },
        messages: [],
      };
      const index = this.state.recents.findIndex(
        (v) => v.user.id === recent.user.id
      );
      if (index === -1) {
        this.state.recents.unshift(recent);
      } else {
        const tmp = this.state.recents.splice(index, 1);
        this.state.recents.unshift(tmp[0]);
      }
      localStorage.setItem(
        "recents" + this.state.user.id,
        JSON.stringify(this.state.recents)
      );
      this.$router.push("/chat");
    },
  },
};
</script>
<style lang='scss' scoped>
</style>