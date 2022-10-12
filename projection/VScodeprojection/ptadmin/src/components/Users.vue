<template>
  <div>
    <el-row style="margin-bottom: 10px">
      <el-col :span="8">
        <el-input
          placeholder="请输入内容"
          v-model="search"
          @keyup.enter.native="searchdata"
        >
          <el-button
            slot="append"
            icon="el-icon-search"
            @click="searchdata"
          ></el-button>
        </el-input>
      </el-col>
      <el-col :span="6">
        <el-button type="primary" @click="adduserdialog = true"
          >添加用户</el-button
        >
      </el-col>
    </el-row>
    <el-table
      id="formtable"
      :data="usersdata.slice((curpage - 1) * pagesize, curpage * pagesize)"
      stripe
      height="477"
      :header-cell-style="{ background: '#ecf5ff' }"
    >
      <el-table-column width="80"> </el-table-column>
      <el-table-column prop="username" label="用户" width="110">
      </el-table-column>
      <el-table-column
        prop="identity"
        sortable
        label="身份"
        width="120"
        header-align="center"
        align="center"
      >
        <template slot-scope="scope">
          <el-button
            type="warning"
            class="b"
            round
            v-if="scope.row.identity == 'HR'"
            >{{ scope.row.identity }}</el-button
          >
          <el-button type="primary" class="b" round v-else>{{
            scope.row.identity
          }}</el-button>
        </template>
      </el-table-column>
      <el-table-column prop="email" label="邮箱" width="180"> </el-table-column>
      <el-table-column prop="phonenumber" label="电话" width="180">
      </el-table-column>
      <el-table-column label="操作" width="210">
        <template slot-scope="scope">
          <!-- 修改 -->
          <el-button
            type="primary"
            icon="el-icon-edit"
            plain
            size="mini"
            @click="openupdate(scope.row)"
          ></el-button>
          <!-- 删除 -->
          <el-button
            type="danger"
            icon="el-icon-delete"
            plain
            size="mini"
            @click="opendelete(scope.row)"
          ></el-button>
          <el-button type="success" size="mini">角色管理</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      id="pagination"
      background
      @size-change="handleSizeChange"
      :page-sizes="[5, 8, 10, 15, 20, 100000]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
      :page-size.sync="pagesize"
      :current-page.sync="curpage"
      @current-change="changecur"
    >
    </el-pagination>
    <!-- 弹出的添加模态框 -->
    <el-dialog
      title="添加"
      :visible.sync="adduserdialog"
      @close="clearuseradd"
      :lock-scroll="false"
      :append-to-body="true"
      class="u"
    >
      <el-form :model="adduserform" :rules="addrules" ref="addform">
        <el-form-item
          prop="username"
          label="用户名"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="adduserform.username"
            auto-complete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="password"
          label="密码"
          :label-width="formLabelWidth"
        >
          <el-input
            type="password"
            v-model="adduserform.password"
            auto-complete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="identity"
          label="身份"
          :label-width="formLabelWidth"
        >
          <el-radio-group v-model="adduserform.identity">
            <el-radio border label="HR"></el-radio>
            <el-radio border label="求职者"></el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item prop="email" label="邮箱" :label-width="formLabelWidth">
          <el-input v-model="adduserform.email" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item
          prop="phonenumber"
          label="手机"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="adduserform.phonenumber"
            auto-complete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="adduserdialog = false">取 消</el-button>
        <el-button
          type="primary"
          @click="
            addUser();
            addPSW();
            addPowers();
          "
          >确 定</el-button
        >
      </div>
    </el-dialog>
    <!-- 编辑 -->
    <el-dialog
      title="编辑"
      :visible.sync="updateuserdialog"
      @close="closeupdate"
      :lock-scroll="false"
      :append-to-body="true"
    >
      <el-form :model="updateusersform" :rules="updateuserrules">
        <el-form-item
          prop="username"
          label="用户名"
          :label-width="formLabelWidth"
        >
          <el-input
            :value="updateusersform.username"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="identity"
          label="身份"
          :label-width="formLabelWidth"
        >
          <el-input
            :value="updateusersform.identity"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item prop="email" label="邮箱" :label-width="formLabelWidth">
          <el-input
            v-model="updateusersform.email"
            auto-complete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="phonenumber"
          label="手机"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="updateusersform.phonenumber"
            auto-complete="off"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="updateuserdialog = false">取 消</el-button>
        <el-button type="primary" @click="updateUser">确 定</el-button>
      </div>
    </el-dialog>
    <!-- 删除 -->
    <el-dialog
      class="d"
      title="删除"
      :visible.sync="deleteuserdialog"
      @close="closedelete"
      :lock-scroll="false"
      :append-to-body="true"
    >
      <el-form :model="deleteusersform">
        <el-form-item
          prop="username"
          label="用户名"
          :label-width="formLabelWidth"
        >
          <el-input
            :value="deleteusersform.username"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="identity"
          label="身份"
          :label-width="formLabelWidth"
        >
          <el-input
            :value="deleteusersform.identity"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item prop="email" label="邮箱" :label-width="formLabelWidth">
          <el-input
            v-model="deleteusersform.email"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          prop="phonenumber"
          label="手机"
          :label-width="formLabelWidth"
        >
          <el-input
            v-model="deleteusersform.phonenumber"
            auto-complete="off"
            disabled
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="deleteuserdialog = false">取 消</el-button>
        <el-button
          type="primary"
          @click="
            deleteuser();
            deletePowers();
          "
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      usersdata: [],
      curpage: null,
      pagesize: 5,
      total: 0,
      search: "",
      adduserdialog: false,
      updateuserdialog: false,
      deleteuserdialog: false,
      formLabelWidth: "120px",
      t: null,
      addrules: {
        username: [
          // required 是否为必填项
          // message 当前规则校验失败时的提示
          // trigger 表单验证的触发实际，blur表示失去焦点时触发
          { required: true, message: "用户名为必填项", trigger: "change" },
          // min 最小长度
          // max 最大长度
          {
            min: 1,
            max: 11,
            message: "用户名长度在 1 到 11 个字符",
            trigger: "change",
          },
        ],
        password: [
          { required: true, message: "密码为必填项", trigger: "change" },
          {
            min: 6,
            max: 20,
            message: "密码长度在 6 到 20 个字符",
            trigger: "change",
          },
        ],
        identity: [
          { required: true, message: "请选择身份", trigger: "change" },
        ],
      },
      adduserform: {},
      updateusersform: {},
      deleteusersform: {},
      updateuserrules: {},
    };
  },
  mounted() {
    this.getdata();
  },
  watch: {
    search: function () {
      this.debounce(this.searchdata, 300);
    },
  },
  methods: {
    debounce(fn, delay) {
      if (this.t !== null) {
        clearTimeout(this.t);
      }
      this.t = setTimeout(() => {
        fn();
      }, delay);
    },
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
    },

    getdata() {
      this.$axios.get("/dev-api/users/get").then((res) => {
        console.log("成功访问users");
        if (res.status === 200) {
          this.usersdata = res.data;
          this.total = res.data.length;
        }
      });
    },
    //分页功能（这个方法是配合ui框架的事件来使用的，当当前页发生改变框架会让这个事件触发一次，使用利用这个特点，当当前页改变时，就获取当前页的数据然后渲染）
    //参数为获取的页码数
    changecur(curpage) {
      console.log("页面", curpage);
    },
    //搜索功能
    searchdata() {
      if (this.search) {
        this.$axios.get(`/dev-api/users/search/${this.search}`).then((res) => {
          if (res.status === 200) {
            console.log("搜索成功");
            this.usersdata = res.data;
            this.total = res.data.length;
            this.curpage = 1;
          }
        });
      } else {
        this.getdata();
      }
    },
    //添加用户
    addUser() {
      this.$axios.post("/dev-api/users/post", this.adduserform).then((res) => {
        console.log("后端添加成功");
        if (res.status === 200) {
          this.$message({
            message: "添加成功",
            type: "success",
          });
          this.getdata();
        } else {
          this.$message.error("添加失败");
        }
      });
      this.adduserdialog = false;
    },
    addPSW() {
      this.$axios.post("/dev-api/users/psw", {
        username: this.adduserform.username,
        password: this.adduserform.password,
      });
    },
    addPowers() {
      if (this.adduserform.identity == "HR") {
        this.$axios.post("/dev-api/powers/add", {
          username: this.adduserform.username,
          identity: this.adduserform.identity,
          launch: "1",
        });
      }
    },
    //情况添加用户的模态框
    clearuseradd() {
      this.$refs.addform.resetFields();
    },
    //编辑用户
    openupdate(data) {
      this.updateuserdialog = true;
      this.updateusersform = data;
    },

    updateUser() {
      this.$axios
        .post(`/dev-api/users/update`, {
          id: this.updateusersform.id,
          email: this.updateusersform.email,
          phonenumber: this.updateusersform.phonenumber,
        })
        .then((res) => {
          if (res.status === 200) {
            console.log("后台更新成功");
            this.$message({
              message: "更新成功",
              type: "success",
            });
          }
          this.updateuserdialog = false;
          this.getdata();
        });
    },
    closeupdate() {
      this.updateusersform = {
        email: "",
        phonenumber: "",
        id: "",
      };
    },
    opendelete(data) {
      this.deleteuserdialog = true;
      this.deleteusersform = data;
    },
    //删除用户
    deleteuser() {
      let id = this.deleteusersform.id;
      this.$axios.delete(`/dev-api/users/delete/${id}`).then((res) => {
        console.log("后端删除成功");
        this.getdata();
        this.$message({
          type: "success",
          message: "删除成功!",
        });
        this.deleteuserdialog = false;
      });
    },
    deletePowers() {
      if (this.deleteusersform.identity == "HR") {
        let id = this.deleteusersform.id;
        this.$axios.delete(`/dev-api/powers/delete/${id}`);
        console.log("11");
      }
    },
    closedelete() {
      this.deleteusersform = {
        email: "",
        phonenumber: "",
        id: "",
      };
    },
  },
};
</script>
<style lang="scss">
button.el-button.b {
  width: 70px;
  padding-left: 0;
  padding-right: 0;
}
</style>
<style lang="scss">
.d span.el-dialog__title {
  color: red !important;
}
.u .el-dialog {
  width: 495px !important;
}
</style>

<style lang="scss" scoped>
#formtable {
  width: 910px;
  overflow: auto;
}
#pagination {
  margin-bottom: 20px;
}
div.el-row {
  display: flex;
  justify-content: center;
}
</style>
