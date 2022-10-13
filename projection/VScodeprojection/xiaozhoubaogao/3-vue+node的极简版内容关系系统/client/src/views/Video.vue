<template>
    <div class="video">
        <el-button type="btn" @click="createVideo">添加视频</el-button>
        <el-table :data="videoList" border>
            <el-table-column align="center" width="100" label="序号" type="index"></el-table-column>
            <el-table-column label="封面">
                <template slot-scope="scope">
                    <img class="pic" :src="scope.row.img" alt />
                </template>
            </el-table-column>
            <el-table-column prop="title" label="姓名"></el-table-column>
            <el-table-column label="详情" width="100">
                <template slot-scope="scope">
                    <el-button @click="getDetail(scope.row.iframe_url)" type="text" size="small">浏览视频</el-button>
                </template>
            </el-table-column>
            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button
                        @click="updateVideo(scope.row.id,scope.row.title,scope.row.img,scope.row.iframe_url)"
                        type="text"
                        size="small"
                    >编辑</el-button>
                    <el-button @click="deleteVideo(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="添加" :visible.sync="videoIsShow" width="800px">
            <div class="test" v-html="video_url"></div>
        </el-dialog>
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
                <el-form-item label="视频标题">
                    <el-input v-model="title"></el-input>
                </el-form-item>
                <el-form-item label="视频地址">
                    <el-input v-model="iframe_url"></el-input>
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
        getDetail(video_url) {
            this.videoIsShow = true;
            this.video_url = video_url;
            console.log(video_url)
        },
        save() {
            if (this.isEdit) {
                request
                    .put(`/video/${this.updateId}`, {
                        title: this.title,
                        img: this.img,
                        iframe_url: this.iframe_url,
                    })
                    .then(() => {
                        this.getVideoList();
                        this.dialogVisible = false;
                    });
            } else {
                request
                    .post(`/video`, {
                        title: this.title,
                        img: this.img,
                        iframe_url: this.iframe_url,
                    })
                    .then(() => {
                        this.getVideoList();
                        this.dialogVisible = false;
                    });
            }
        },
        createVideo() {
            this.dialogVisible = true;
            this.title = "";
            this.iframe_url = "";
            this.isEdit = false;
        },
        deleteVideo(id) {
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning",
            })
                .then(() => {
                    request.delete(`/video/${id}`).then(() => {
                        this.$message({
                            type: "success",
                            message: "删除成功!",
                        });
                        this.getVideoList();
                    });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除",
                    });
                });
        },
        updateVideo(id, title, img, iframe_url) {
            this.dialogVisible = true;
            this.title = title;
            this.isEdit = true;
            this.updateId = id;
            this.iframe_url = iframe_url;
            this.fileList = [{ url: img }];
            this.img = img;
        },
        getVideoList() {
            request.get(`/video?page=1&total=10`).then((res) => {
                this.videoList = res.data.data;
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
            videoList: [],
            iframe_url: "",
            dialogVisible: false,
            title: "",
            isEdit: false,
            updateId: 0,
            img: "",
            videoIsShow: false,
            video_url:"<h1>123</h1>",
            headers: {
                token: "",
            },
        };
    },

    created() {
        this.getVideoList();
    },
};
</script>

<style>
.video .pic {
    width: 50px;
    height: 50px;
}
.video iframe{
    width:100%;
    height:500px;
}
</style>

