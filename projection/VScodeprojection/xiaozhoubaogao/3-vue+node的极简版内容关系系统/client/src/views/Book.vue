<template>
    <div class="book">
        <el-button type="btn" @click="createBook">添加书籍</el-button>
        <el-table :data="bookList" border>
            <el-table-column align="center" width="100" label="序号" type="index"></el-table-column>
            <el-table-column label="封面">
                <template slot-scope="scope">
                    <img class="pic" :src="scope.row.img" alt />
                </template>
            </el-table-column>
            <el-table-column prop="title" label="姓名"></el-table-column>
            <el-table-column label="详情" width="100">
                <template slot-scope="scope">
                    <el-button @click="getDetail(scope.row.id)" type="text" size="small">查看章</el-button>
                </template>
            </el-table-column>
            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button
                        @click="updateBook(scope.row.id,scope.row.title,scope.row.img,scope.row.orderby)"
                        type="text"
                        size="small"
                    >编辑</el-button>
                    <el-button @click="deleteBook(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="添加" :visible.sync="dialogVisible" width="30%">
            <div id="cover">
                <span class="cover_cover">上传封面:</span>
                <el-upload
                    :action="getUploadUrl()"
                    list-type="picture-card"
                    :on-preview="handleSuccess"
                    :on-remove="handleRemove"
                    :headers="headers"
                    :on-success="handleSuccess"
                    :file-list="fileList"
                >
                    <i class="el-icon-plus"></i>
                </el-upload>
            </div>
            <el-form>
                <el-form-item label="书籍名称">
                    <el-input v-model="title"></el-input>
                </el-form-item>
                <el-form-item label="排序权重">
                    <el-input v-model="orderby"></el-input>
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
                    .put(`/book/${this.updateId}`, {
                        title: this.title,
                        img: this.img,
                        orderby: this.orderby,
                    })
                    .then(() => {
                        this.getBookList();
                        this.dialogVisible = false;
                    });
            } else {
                request
                    .post(`/book`, {
                        title: this.title,
                        img: this.img,
                        orderby: this.orderby,
                    })
                    .then(() => {
                        this.getBookList();
                        this.dialogVisible = false;
                    });
            }
        },
        createBook() {
            this.dialogVisible = true;
            this.title = "";
            this.isEdit = false;
        },
        deleteBook(id) {
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
                .then(() => {
                    request.delete(`/book/${id}`).then(() => {
                        this.$message({
                            type: "success",
                            message: "删除成功!",
                        });
                        this.getBookList();
                    });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除",
                    });
                });
        },
        updateBook(id,title,img,orderby) {
            this.dialogVisible = true;
            this.title = title;
            this.isEdit = true;
            this.updateId = id;
            this.orderby = orderby
            this.fileList = [{ url: img }];
            this.img = img;
        },
        getBookList() {
            request.get(`/book?page=1&total=10`).then((res) => {
                this.bookList = res.data.data;
            });
        },
        getUploadUrl() {
            return process.env.VUE_APP_UPLOAD_API;
        },
        //上传图片
        handleRemove(file, fileList) {
            console.log(file);
            console.log(fileList);
        },
        handlePreview(file) {
            console.log(file);
        },
        handleSuccess(response, file, fileList) {
            console.log(file);
            console.log(fileList);
            this.img = response.data.file;
        },
    },

    data() {
        return {
            fileList: [],
            bookList: [],
            orderby: "",
            dialogVisible: false,
            title: "",
            isEdit: false,
            updateId: 0,
            img: "",
            headers: {
                token: "",
            },
        };
    },

    created() {
        this.getBookList();
    },
};
</script>

<style scoped>
.book .pic {
    width: 50px;
    height: 50px;
}
</style>

