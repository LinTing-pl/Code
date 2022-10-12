<template>
  <div>
    <i
      class="el-icon-circle-plus-outline"
      @click="dialogFormVisible = true"
    ></i>
    <el-dialog
      title="添加/修改图书"
      :visible.sync="dialogFormVisible"
      @close="clear"
    >
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="书名" :label-width="formLabelWidth" prop="title">
          <el-input
            v-model="form.title"
            autocomplete="on"
            placeholder="不加《》"
          ></el-input>
        </el-form-item>
        <el-form-item label="作者" :label-width="formLabelWidth" prop="author">
          <el-input v-model="form.author" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="出版日期"
          :label-width="formLabelWidth"
          prop="date"
        >
          <el-input v-model="form.date" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="出版社" :label-width="formLabelWidth" prop="press">
          <el-input v-model="form.press" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="封面" :label-width="formLabelWidth" prop="cover">
          <el-input
            v-model="form.cover"
            autocomplete="off"
            placeholder="图片 URL"
          ></el-input>
        </el-form-item>
        <el-form-item label="简介" :label-width="formLabelWidth" prop="abs">
          <el-input
            type="textarea"
            v-model="form.abs"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="分类" :label-width="formLabelWidth" prop="cid">
          <el-select v-model="form.category.id" placeholder="请选择分类">
            <el-option label="文学" value="1"></el-option>
            <el-option label="流行" value="2"></el-option>
            <el-option label="文化" value="3"></el-option>
            <el-option label="生活" value="4"></el-option>
            <el-option label="经管" value="5"></el-option>
            <el-option label="科技" value="6"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item prop="id" style="height: 0">
          <el-input
            type="hidden"
            v-model="form.id"
            autocomplete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: "EditForm",
  data() {
    return {
      dialogFormVisible: false,
      form: {
        id: "",
        title: "",
        author: "",
        date: "",
        press: "",
        cover: "",
        abs: "",
        category: {
          id: "",
          name: "",
        },
      },
      formLabelWidth: "120px",
    };
  },
  methods: {
    clear() {
      this.form = {
        id: "",
        title: "",
        author: "",
        date: "",
        press: "",
        cover: "",
        abs: "",
        category: "",
      };
    },
    onSubmit() {
      this.$axios
        .post("/api/books", {
          id: this.form.id,
          cover: this.form.cover,
          title: this.form.title,
          author: this.form.author,
          date: this.form.date,
          press: this.form.press,
          abs: this.form.abs,
          category: this.form.category,
        })
        .then((resp) => {
          if (resp && resp.status === 200) {
            console.log("添加成功", resp);
            this.dialogFormVisible = false;
            this.$emit("onSubmit");
          }
        })
        .catch(function (error) {
          if (error.response) {
            // 请求成功发出且服务器也响应了状态码，但状态代码超出了 2xx 的范围
            console.log("2xx", error.response.data);
            console.log(error.response.status);
            console.log(error.response.headers);
          } else if (error.request) {
            // 请求已经成功发起，但没有收到响应
            // `error.request` 在浏览器中是 XMLHttpRequest 的实例，
            // 而在node.js中是 http.ClientRequest 的实例
            console.log("no response", error.request);
          } else {
            // 发送请求时出了点问题
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    },
  },
};
</script>

<style scoped>
.el-icon-circle-plus-outline {
  margin: 50px 0 0 20px;
  font-size: 100px;
  float: left;
  cursor: pointer;
}
</style>
