<template>
  <div>
    <el-table
      :data="rolesList.slice((curpage - 1) * pagesize, curpage * pagesize)"
      stripe
      height="477"
      style="width: 600px"
      :header-cell-style="{ background: '#ecf5ff' }"
    >
      <el-table-column width="80"></el-table-column>
      <el-table-column prop="username" label="角色名称" width="110">
      </el-table-column>
      <el-table-column
        class="ttt"
        prop="identity"
        label="身份"
        width="120"
        header-align="center"
        align="center"
      >
        <template slot-scope="scope">
          <el-button type="warning" class="b" round>{{
            scope.row.identity
          }}</el-button>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="290">
        <template slot-scope="scope">
          <!-- 修改 -->
          <el-switch
            style="display: block"
            active-color="#13ce66"
            inactive-color="#ff4949"
            active-value="1"
            inactive-value="0"
            active-text="允许发布兼职"
            inactive-text="禁止发布兼职"
            v-model="scope.row.launch"
            @change="changeLaunch(scope.row)"
          >
          </el-switch>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
      id="pagination"
      background
      :page-sizes="[5, 8, 10, 15, 20, 100000]"
      layout="total, sizes, prev, pager, next, jumper"
      :total="total"
      :page-size.sync="pagesize"
      :current-page.sync="curpage"
      @current-change="changecur"
    >
    </el-pagination>
  </div>
</template>

<script>
export default {
  data() {
    return {
      rolesList: [],
      total: 0,
      pagesize: 5,
      curpage: null,
    };
  },
  mounted() {
    this.getrolesdata();
  },
  methods: {
    getrolesdata() {
      this.$axios.get("/dev-api/powers/get").then((res) => {
        this.rolesList = res.data;
        this.total = res.data.length;
      });
    },
    changecur(curpage) {
      console.log("页面", curpage);
    },
    changeLaunch(data) {
      this.$axios.post("/dev-api/powers/update", data);
    },
  },
};
</script>
<style lang="scss" scoped>
#pagination {
  margin-bottom: 20px;
}
</style>
