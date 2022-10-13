<template>
    <div class="blog">
        <el-button type="text" @click="createBlog">新建博客</el-button>
        <el-table :data="blogList" border>
            <el-table-column align="center" width="100" label="序号" type="index"></el-table-column>
            <el-table-column label="封面">
                <template slot-scope="scope">
                    <img class="pic" :src="scope.row.img" alt="">
                </template>
            </el-table-column>
            <el-table-column prop="title" label="标题"></el-table-column>
            <el-table-column label="操作">
                <template slot-scope="scope">
                    <el-button @click="updateBlog(scope.row.id)" type="text" size="small">编辑</el-button>
                    <el-button @click="deleteBlog(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import request from "../utils/request";
export default {
    data() {
        return {
            name: "",
            blogList: [],
        };
    },
    methods: {
        deleteBlog(id) {
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
                .then(() => {
                    request.delete(`/blog/${id}`).then(() => {
                        this.getBlogList();
                    });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除",
                    });
                });
        },
        createBlog() {
            this.$router.push("/createBlog");
        },
        updateBlog(id){
            this.$router.push(`/blog/${id}`);

        },
        getBlogList() {
            request.get("/blog?page=1&total=10").then((res) => {
                this.blogList = res.data.data;
            });
        },
    },
    created() {
        this.getBlogList();
    },
};
</script>

<style scoped>
.blog .pic{
    width:50px;
    height:50px;
}
</style>