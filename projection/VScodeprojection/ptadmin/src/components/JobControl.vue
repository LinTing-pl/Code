<template>
  <div style="width: 1030px">
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
      <el-col :span="10">
        <el-button type="primary" @click="adddialog = true">添加兼职</el-button>
        <el-button
          type="success"
          @click="
            trialdialog = true;
            getTrial();
          "
          >兼职审核</el-button
        >
        <el-button
          type="success"
          @click="
            topdialog = true;
            getTop();
          "
          >置顶审核</el-button
        >
      </el-col>
    </el-row>
    <el-table
      height="477"
      :header-cell-style="{ background: '#ecf5ff', fontSize: '25px' }"
      :header-row-style="{ height: '60px' }"
      :row-style="{ height: '120px', width: '900px' }"
      :data="jobData"
      stripe
    >
      <el-table-column width="80"></el-table-column>
      <el-table-column
        width="800"
        header-align="center"
        label="兼职"
        prop="usename"
      >
        <template slot-scope="scope">
          <el-descriptions border>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-tickets"></i>
                兼职工作类型
              </template>
              {{ scope.row.job }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-user"></i>
                发布者
              </template>
              <i
                :class="{ 'el-icon-user': scope.row.cid == scope.row.username }"
              ></i>
              {{ scope.row.username }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-mobile-phone"></i>
                手机号
              </template>
              {{ scope.row.phonenumber }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-location-outline"></i>
                工作地点(市或区)
              </template>
              {{ scope.row.city }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-tickets"></i>
                工作内容
              </template>
              {{ scope.row.content }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-office-building"></i>
                联系地址
              </template>
              {{ scope.row.adress }}
            </el-descriptions-item>
            <el-descriptions-item>
              <template slot="label">
                <i class="el-icon-tickets"></i>
                备注
              </template>
              {{ scope.row.beifen }}
            </el-descriptions-item>
          </el-descriptions>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="120">
        <template slot-scope="scope">
          <el-switch
            style="display: block"
            v-model="scope.row.keysort"
            active-color="#13ce66"
            inactive-color="#ff4949"
            active-text=""
            inactive-text="置顶"
            active-value="1"
            inactive-value="0"
            @change="topthis(scope.row)"
          >
          </el-switch>
          <!-- 修改 -->
          <el-button
            class="bbb"
            type="primary"
            icon="el-icon-edit"
            plain
            size="small"
            @click="openupdate(scope.row)"
          ></el-button>
          <!-- 删除 -->
          <el-button
            class="bbb"
            type="danger"
            icon="el-icon-delete"
            plain
            size="small"
            @click="opendelete(scope.row)"
          ></el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 添加 -->
    <el-dialog
      :visible.sync="adddialog"
      :append-to-body="true"
      :lock-scroll="false"
      title="添加"
      @close="clearaddform"
    >
      <el-descriptions
        class="margin-top"
        :title="'兼职工作类型:' + addform.job"
        :column="3"
        border
      >
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            兼职工作类型
          </template>
          <textarea
            name=""
            id=""
            placeholder="酒店前台"
            v-model="addform.job"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-user"></i>
            发布者
          </template>
          <i class="el-icon-user"></i>
          {{ addform.username }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-mobile-phone"></i>
            手机号
          </template>
          <textarea
            name=""
            id=""
            placeholder="13800008888"
            v-model="addform.phonenumber"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-location-outline"></i>
            工作地点(市或区)
          </template>
          <textarea
            name=""
            id=""
            placeholder="杭州市"
            v-model="addform.city"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            工作内容
          </template>
          <textarea
            name=""
            id=""
            placeholder="担任酒店前台，工作时间12：00~24：00"
            style="min-height: 60px; max-height: 70px"
            v-model="addform.content"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-office-building"></i>
            联系地址
          </template>
          <textarea
            name=""
            id=""
            placeholder="江苏省苏州市吴中区吴中大道 1188 号"
            style="min-height: 60px; max-height: 70px"
            v-model="addform.adress"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            备注
          </template>
          <textarea
            name=""
            id=""
            placeholder="薪水4k/月"
            style="min-width: 600px; max-width: 600px"
            v-model="addform.beifen"
          ></textarea>
        </el-descriptions-item>
      </el-descriptions>
      <template slot="footer">
        <el-button @click="adddialog = false">取 消</el-button>
        <el-button type="primary" @click="addJob">确 定</el-button>
      </template>
    </el-dialog>
    <!-- 编辑 -->
    <el-dialog
      :visible.sync="updatedialog"
      :append-to-body="true"
      :lock-scroll="false"
      title="编辑"
      @close="closeupdate"
    >
      <el-descriptions
        class="margin-top"
        :title="'兼职工作类型:' + updateform.job"
        :column="3"
        border
      >
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            兼职工作类型
          </template>
          <textarea v-model="updateform.job"></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-user"></i>
            发布者
          </template>
          <i
            :class="{ 'el-icon-user': updateform.cid == updateform.username }"
          ></i>
          {{ updateform.username }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-mobile-phone"></i>
            手机号
          </template>
          <textarea v-model="updateform.phonenumber"></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-location-outline"></i>
            工作地点(市或区)
          </template>
          <textarea v-model="updateform.city"></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            工作内容
          </template>
          <textarea
            style="min-height: 60px; max-height: 70px"
            v-model="updateform.content"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-office-building"></i>
            联系地址
          </template>
          <textarea
            style="min-height: 60px; max-height: 70px"
            v-model="updateform.adress"
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            备注
          </template>
          <textarea
            style="min-width: 600px; max-width: 600px"
            v-model="updateform.beifen"
          ></textarea>
        </el-descriptions-item>
      </el-descriptions>
      <template slot="footer" slot-scope="scope">
        <el-button @click="updatedialog = false">取 消</el-button>
        <el-button type="primary" @click="updateJob">确 定</el-button>
      </template>
    </el-dialog>
    <!-- 删除 -->
    <el-dialog
      :visible.sync="deletedialog"
      :append-to-body="true"
      :lock-scroll="false"
      title="删除"
      @close="closedelete"
      class="dd"
    >
      <el-descriptions
        class="margin-top"
        :title="'兼职工作类型:' + deleteform.job"
        :column="3"
        border
      >
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            兼职工作类型
          </template>
          <textarea v-model="deleteform.job" disabled></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-user"></i>
            发布者
          </template>
          <i
            :class="{ 'el-icon-user': deleteform.cid == deleteform.username }"
          ></i>
          {{ deleteform.username }}
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-mobile-phone"></i>
            手机号
          </template>
          <textarea v-model="deleteform.phonenumber" disabled></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-location-outline"></i>
            工作地点(市或区)
          </template>
          <textarea v-model="deleteform.city" disabled></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            工作内容
          </template>
          <textarea
            style="min-height: 60px; max-height: 70px"
            v-model="deleteform.content"
            disabled
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-office-building"></i>
            联系地址
          </template>
          <textarea
            style="min-height: 60px; max-height: 70px"
            v-model="deleteform.adress"
            disabled
          ></textarea>
        </el-descriptions-item>
        <el-descriptions-item>
          <template slot="label">
            <i class="el-icon-tickets"></i>
            备注
          </template>
          <textarea
            style="min-width: 600px; max-width: 600px"
            v-model="deleteform.beifen"
            disabled
          ></textarea>
        </el-descriptions-item>
      </el-descriptions>
      <template slot="footer">
        <el-button @click="deletedialog = false">取 消</el-button>
        <el-button type="primary" @click="deleteJob">确 定</el-button>
      </template>
    </el-dialog>
    <!-- 兼职审核 -->
    <el-dialog
      :visible="trialdialog"
      :append-to-body="true"
      :lock-scroll="false"
      @close="trialdialog = false"
      title="兼职审核"
    >
      <el-table
        height="477"
        :header-cell-style="{
          background: '#ecf5ff',
          fontSize: '24px',
        }"
        :header-row-style="{ height: '60px' }"
        :row-style="{ height: '120px', width: '900px' }"
        :data="trialData"
        stripe
      >
        <el-table-column
          width="600"
          header-align="center"
          label="兼职"
          prop="usename"
        >
          <template slot-scope="scope">
            <el-descriptions border>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  兼职工作类型
                </template>
                {{ scope.row.job }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-user"></i>
                  发布者
                </template>
                <i
                  :class="{
                    'el-icon-user': scope.row.cid == scope.row.username,
                  }"
                ></i>
                {{ scope.row.username }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-mobile-phone"></i>
                  手机号
                </template>
                {{ scope.row.phonenumber }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-location-outline"></i>
                  工作地点(市或区)
                </template>
                {{ scope.row.city }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  工作内容
                </template>
                {{ scope.row.content }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-office-building"></i>
                  联系地址
                </template>
                {{ scope.row.adress }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  备注
                </template>
                {{ scope.row.beifen }}
              </el-descriptions-item>
            </el-descriptions>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template slot-scope="scope">
            <el-button
              type="success"
              class="bbb"
              icon="el-icon-edit"
              @click="passTrial(scope.row)"
              >通过</el-button
            >
            <el-button
              type="danger"
              class="bbb"
              icon="el-icon-delete"
              @click="set0Trial(scope.row)"
              >不通过</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
    <!-- 置顶审核 -->
    <el-dialog
      :visible="topdialog"
      :append-to-body="true"
      :lock-scroll="false"
      @close="topdialog = false"
      title="置顶审核"
    >
      <el-table
        height="477"
        :header-cell-style="{
          background: '#ecf5ff',
          fontSize: '24px',
        }"
        :header-row-style="{ height: '60px' }"
        :row-style="{ height: '120px', width: '900px' }"
        :data="topData"
        stripe
      >
        <el-table-column
          width="600"
          header-align="center"
          label="兼职"
          prop="usename"
        >
          <template slot-scope="scope">
            <el-descriptions border>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  兼职工作类型
                </template>
                {{ scope.row.job }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-user"></i>
                  发布者
                </template>
                <i
                  :class="{
                    'el-icon-user': scope.row.cid == scope.row.username,
                  }"
                ></i>
                {{ scope.row.username }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-mobile-phone"></i>
                  手机号
                </template>
                {{ scope.row.phonenumber }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-location-outline"></i>
                  工作地点(市或区)
                </template>
                {{ scope.row.city }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  工作内容
                </template>
                {{ scope.row.content }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-office-building"></i>
                  联系地址
                </template>
                {{ scope.row.adress }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template slot="label">
                  <i class="el-icon-tickets"></i>
                  备注
                </template>
                {{ scope.row.beifen }}
              </el-descriptions-item>
            </el-descriptions>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="120">
          <template slot-scope="scope">
            <el-button
              type="success"
              class="bbb"
              icon="el-icon-edit"
              @click="passToptrial(scope.row)"
              >置顶</el-button
            >
            <el-button
              type="danger"
              class="bbb"
              icon="el-icon-delete"
              @click="set0Toptrial(scope.row)"
              >不置顶</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </el-dialog>
  </div>
</template>
<script>
export default {
  mounted() {
    this.getData();
  },
  watch: {
    search: function () {
      this.debounce(this.searchdata, 300);
    },
  },
  data() {
    return {
      jobData: [],
      trialData: [],
      topData: [],
      adddialog: false,
      updatedialog: false,
      deletedialog: false,
      trialdialog: false,
      topdialog: false,
      addform: {
        cid: localStorage.getItem("superusername"),
        job: "",
        username: this.getname(),
        keysort: 0,
        toptrial: "0",
      },
      search: "",
      t: null,
      updateform: {},
      deleteform: {},
    };
  },
  methods: {
    getname() {
      return localStorage.getItem("superusername");
    },
    getData() {
      this.$axios.get("/dev-api/job/get").then((res) => {
        this.jobData = res.data;
      });
    },
    addJob() {
      if (
        this.addform.job &&
        this.addform.phonenumber &&
        this.addform.city &&
        this.addform.content &&
        this.addform.adress &&
        this.addform.beifen
      ) {
        this.$axios.post("/dev-api/job/add", this.addform).then(() => {
          this.getData();
          this.adddialog = false;
        });
      } else {
        this.$message({
          message: "请全部填写",
          type: "error",
        });
      }
    },
    clearaddform() {
      this.addform = {
        cid: localStorage.getItem("superusername"),
        job: "",
        username: this.getname(),
        keysort: 0,
      };
      this.adddialog = false;
    },
    searchdata() {
      if (this.search) {
        this.$axios.get(`/dev-api/job/get/${this.search}`).then((res) => {
          this.jobData = res.data;
        });
      } else {
        this.getData();
      }
    },
    updateJob() {
      this.$axios.post("/dev-api/job/update", this.updateform).then(() => {
        this.getData();
        this.closeupdate();
      });
    },
    deleteJob() {
      this.$axios
        .delete(`/dev-api/job/delete/${this.deleteform.id}`)
        .then(() => {
          this.getData();
          this.closedelete();
        });
    },
    getTrial() {
      this.$axios("/dev-api/trial/get1").then((res) => {
        this.trialData = res.data;
      });
    },
    passTrial(data) {
      this.deleteBeford(data.id);
      console.log(data);
      this.$axios
        .post("/dev-api/job/add", {
          adress: data.adress,
          beifen: data.beifen,
          cid: data.cid,
          city: data.city,
          content: data.content,
          job: data.job,
          phonenumber: data.phonenumber,
          username: data.username,
          keysort: 0,
          toptrial: "0",
        })
        .then(() => {
          this.getTrial();
          this.getData();
        });
    },
    deleteBeford(id) {
      this.$axios.delete(`dev-api/trial/delete/${id}`);
    },
    set0Trial(data) {
      data.trial = "0";
      this.$axios.post("dev-api/trial/update", data).then(() => {
        this.getTrial();
      });
    },
    getTop() {
      this.$axios.get("/dev-api/job/gettop1").then((res) => {
        this.topData = res.data;
      });
    },
    passToptrial(data) {
      data.keysort = 1;
      data.toptrial = "2";
      this.$axios.post("/dev-api/job/update", data).then(() => {
        this.getTop();
        this.getData();
      });
    },
    set0Toptrial(data) {
      data.toptrial = "0";
      this.$axios.post("dev-api/job/update", data).then(() => {
        this.getTop();
      });
    },
    debounce(fn, delay) {
      if (this.t !== null) {
        clearTimeout(this.t);
      }
      this.t = setTimeout(() => {
        fn();
      }, delay);
    },
    openupdate(data) {
      this.updatedialog = true;
      this.updateform = data;
    },
    closeupdate() {
      this.updatedialog = false;
      this.updateform = {};
    },
    opendelete(data) {
      this.deletedialog = true;
      this.deleteform = data;
    },
    closedelete() {
      this.deletedialog = false;
      this.deleteform = {};
    },
    topthis(data) {
      if (data.keysort == 1) {
        data.toptrial = "2";
      } else {
        data.toptrial = "0";
      }
      this.$axios.post("/dev-api/job/updatetop", data).then(() => {
        this.getData();
      });
    },
  },
};
</script>
<style lang='scss' scoped>
div.el-row {
  display: flex;
  justify-content: center;
}
::v-deep .el-dialog {
  top: 0%;
  width: 800px;
}
textarea {
  border: none;
  background: #ecf5ff;
  min-width: 120px;
  max-width: 170px;
  min-height: 43px;
  max-height: 61px;
  font-size: 16px;
}
::v-deep .el-table_2_column_5 .cell {
  display: flex;
  flex-direction: column;
  align-items: center;
}
::v-deep .el-table_1_column_3 .cell {
  display: flex;
  flex-direction: column;
  align-items: center;
}
::v-deep .bbb {
  width: 100px;
  margin-left: 0 !important;
  margin-bottom: 3px;
}
.dd ::v-deep span.el-dialog__title {
  color: red;
}
</style>