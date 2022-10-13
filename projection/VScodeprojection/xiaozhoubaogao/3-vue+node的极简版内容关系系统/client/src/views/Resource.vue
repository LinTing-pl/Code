<template>
    <div class="resource">
        <el-button type="btn" @click="createResource">添加资源</el-button>
        <el-table :data="resourceList" border>
            <el-table-column align="center" width="100" label="序号" type="index"></el-table-column>
            <el-table-column prop="title" label="姓名"></el-table-column>
            <el-table-column prop="code" label="提取码"></el-table-column>
            <el-table-column prop="url" label="下载地址"></el-table-column>
            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button
                        @click="updateResource(scope.row.id,scope.row.title,scope.row.code,scope.row.url)"
                        type="text"
                        size="small"
                    >编辑</el-button>
                    <el-button @click="deleteRosource(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="添加" :visible.sync="dialogVisible" width="30%">
            <el-form>
                <el-form-item label="视频标题">
                    <el-input v-model="title"></el-input>
                </el-form-item>
                <el-form-item label="资源地址">
                    <el-input v-model="url"></el-input>
                </el-form-item>
                <el-form-item label="提取码">
                    <el-input v-model="code"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="save">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import request from "../utils/request";
export default {
    methods: {
        getDetail(id) {
            this.$router.push(`/chapter?book_id=${id}`);
        },
        save() {
            if (this.isEdit) {
                request
                    .put(`/resource/${this.updateId}`, {
                        title: this.title,
                        code: this.code,
                        url: this.url,
                    })
                    .then(() => {
                        this.getResourceList();
                        this.dialogVisible = false;
                    });
            } else {
                request
                    .post(`/resource`, {
                        title: this.title,
                        code: this.code,
                        url: this.url,
                    })
                    .then(() => {
                        this.getResourceList();
                        this.dialogVisible = false;
                    });
            }
        },
        createResource() {
            this.dialogVisible = true;
            this.title = "";
            this.isEdit = false;
        },
        deleteRosource(id) {
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
                .then(() => {
                    request.delete(`/resource/${id}`).then(() => {
                        this.$message({
                            type: "success",
                            message: "删除成功!",
                        });
                        this.getResourceList();
                    });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除",
                    });
                });
        },
        updateResource(id,title,code,url) {
            this.dialogVisible = true;
            this.title = title;
            this.isEdit = true;
            this.updateId = id;
            this.url = url
            this.code = code;
        },
        getResourceList() {
            request.get(`/resource?page=1&total=10`).then((res) => {
                this.resourceList = res.data.data;
            });
        },
    },

    data() {
        return {
            resourceList: [],
            url: "",
            dialogVisible: false,
            title: "",
            isEdit: false,
            updateId: 0,
            code: "",
            headers: {
                token: "",
            },
        };
    },

    created() {
        this.getResourceList();
    },
};
</script>

<style scoped>
.resource .pic {
    width: 50px;
    height: 50px;
}
</style>

