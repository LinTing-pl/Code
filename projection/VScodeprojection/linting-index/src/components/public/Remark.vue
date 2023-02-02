<template>
  <div class="remark-content">
    <div class="remark-area">
      <input type="text" class="up" v-model="remarkContent" />
      <button class="btn" @click="remark">发表评论</button>
    </div>
    <div class="remark-side" v-if="data.length">
      <ul class="ul">
        <li class="li" v-for="(item, index) in data" :key="index">
          <svg class="icon userImg" aria-hidden="true">
            <use xlink:href="#icon-user-circle-o"></use>
          </svg>
          <div class="content">
            <div class="remark-content">{{ item.content }}</div>
            <div class="recall">
              <input type="text" />
              <button class="recall-btn" @click="recall($event, item)">
                回复
              </button>
              <button class="extend-btn" @click="extend(item)">
                {{ item.isShow ? "收起" : "展开" }}
              </button>
            </div>
            <div v-show="item.isShow">
              <ul class="sub-ul">
                <li
                  class="sub-li"
                  v-for="(item1, index1) in item.subContent"
                  :key="index1"
                >
                  <span>{{ item1[0] }}:</span>
                  <span>{{ item1[1] }}</span>
                </li>
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import "../../../public/css/iconfont.js";
export default {
  props: ["cls", "id"],
  created() {
    this.$axios.default
      .get(`/dev-api/${this.cls}/get/${this.id}`)
      .then((resp) => {
        if (resp.data.remark) {
          this.data = JSON.parse(resp.data.remark);
        }
      });
  },
  data() {
    return {
      data: [],
      remarkContent: "",
    };
  },
  methods: {
    remark() {
      this.data.unshift({
        content: this.remarkContent,
        subContent: [],
        isShow: false,
      });
      this.remarkContent = "";
      let data = JSON.parse(JSON.stringify(this.data));
      data = data.map((v) => {
        v.isShow = false;
        return v;
      });
      this.$axios.default
        .post(`/dev-api/${this.cls}/update`, {
          remark: JSON.stringify(data),
          id: this.id,
        })
        .then((resp) => {});
    },
    recall($event, item) {
      let val = $event.target.parentNode.children[0].value;
      if (val !== "") {
        let user = localStorage.getItem("user");
        item.subContent.unshift([user, val]);
        $event.target.parentNode.children[0].value = "";
        if (!item.isShow) {
          item.isShow = true;
        }
        let data = JSON.parse(JSON.stringify(this.data));
        data = data.map((v) => {
          v.isShow = false;
          return v;
        });
        this.$axios.default
          .post(`/dev-api/${this.cls}/update`, {
            remark: JSON.stringify(data),
            id: this.id,
          })
          .then((resp) => {});
      }
    },
    extend(item) {
      item.isShow = !item.isShow;
    },
  },
};
</script>
<style lang='scss' scoped>
.icon {
  width: 1em;
  height: 1em;
  vertical-align: -0.15em;
  fill: currentColor;
  overflow: hidden;
}
.remark-content {
  width: 100%;
  margin: 0 0 45px 0;
}
.remark-area {
  width: 100%;
  text-align: left;
  .up {
    width: 86%;
    outline: none;
  }
  .btn {
    width: 12%;
    border: 1px solid transparent;
    background: #108cff;
    border-radius: 3px;
    margin-left: 2px;
  }
  .btn:hover {
    color: #fff;
    cursor: pointer;
    border: 1px solid #000;
  }
}
.remark-side {
  width: 100%;
  .ul {
    list-style: none;
    text-align: left;
    padding: 10px;
    border-radius: 4px;
    margin: 2px 0 0;
    border: 1px solid #767676;
    .li {
      margin-bottom: 4px;
      .userImg {
        width: 35px;
        height: 35px;
        border-radius: 50%;
      }
      .content {
        display: inline-block;
        border: 1px solid #76767690;
        padding: 3px;
        border-radius: 4px;
        margin-left: 5px;
        width: calc(100% - 48px);
        word-break: break-all;
        font-size: 15px;
        margin-top: 5px;
        vertical-align: top;
        position: relative;
        .remark-content {
          border-bottom: 1px solid #76767670;
          padding-bottom: 4px;
          margin-bottom: 1px;
        }
        .recall {
          input {
            width: 85%;
            border: 1px solid #76767610;
            border-radius: 3px;
          }
          input:hover,
          input:focus {
            outline: 1px solid #76767670;
          }
          .recall-btn {
            cursor: pointer;
            margin: 0 4px;
            padding: 0;
          }
          .extend-btn {
            cursor: pointer;
            padding: 0;
            border: none;
            outline: none;
            color: #76767670;
            background: transparent;
          }
          .extend-btn:hover {
            color: #000;
            text-decoration: underline;
          }
        }
        .sub-ul {
          list-style: none;
          padding: 0;
        }
        .sub-li {
          display: flex;
          span:nth-child(1) {
            white-space: nowrap;
            margin-right: 5px;
          }
        }
      }
      .remark-content::before {
        content: "";
        border: 5px solid transparent;
        border-right: 5px solid #76767680;

        position: absolute;
        left: -11px;
        top: 6px;
      }
    }
  }
}
</style>