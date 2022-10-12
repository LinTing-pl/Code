<template>
  <!-- 兼职工作类型:{{ item.job }} \n发布者:{{ item.username }} \n手机号:{{
              item.phonenumber
            }}\n工作地点(市或区):{{ item.city }} \n工作内容:{{
              item.content
            }}\n联系地址:{{ item.adress }}\n 备注:{{ item.beifen }} -->
  <view
    ><uni-forms ref="baseForm" :modelValue="baseFormData">
      <uni-forms-item label="兼职工作类型" required>
        <uni-easyinput
          v-model="baseFormData.job"
          placeholder="请输入兼职工作名称"
        />
      </uni-forms-item>
      <uni-forms-item label="发布者" required>
        <uni-easyinput
          v-model="baseFormData.username"
          placeholder="请输入发布者名称"
        />
      </uni-forms-item>
      <uni-forms-item label="手机号" required>
        <uni-easyinput
          v-model="baseFormData.phonenumber"
          placeholder="请输入手机号"
        />
      </uni-forms-item>
      <uni-forms-item label="工作地点(市或区)" required>
        <uni-easyinput
          v-model="baseFormData.city"
          placeholder="请输入工作地点(市或区)"
        />
      </uni-forms-item>
      <uni-forms-item label="工作内容" required>
        <uni-easyinput
          v-model="baseFormData.content"
          placeholder="请输入工作内容"
        />
      </uni-forms-item>
      <uni-forms-item label="联系地址" required>
        <uni-easyinput
          v-model="baseFormData.adress"
          placeholder="请输入联系地址"
        />
      </uni-forms-item>
      <uni-forms-item label="备注">
        <uni-easyinput
          type="textarea"
          v-model="baseFormData.beifen"
          placeholder="请输入薪资等"
        />
      </uni-forms-item>
      <button class="button" type="primary" @click="submitAddform">
        提交审核
      </button></uni-forms
    ></view
  >
</template>
<script>
export default {
  data() {
    return {
      baseFormData: {
        cid: "11",
        trial: "1",
      },
    };
  },
  methods: {
    submitAddform() {
      uni.request({
        url: "http://localhost:8888/dev-api/trial/add",
        data: this.baseFormData,
        method: "POST",
        success: () => {
          this.baseFormData = {
            cid: "11",
            trial: "1",
          };
        },
      });
    },
  },
};
</script>
<style lang='scss' scoped>
</style>