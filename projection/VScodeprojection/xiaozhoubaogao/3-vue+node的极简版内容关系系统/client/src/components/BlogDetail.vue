<template>
    <div>
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
        <div class="title">
            <el-input v-model="title" placeholder="节名称" class="title_titlei"></el-input>
        </div>

        <div id="main">
            <!-- 富文本编辑器 -->
            <mavon-editor
                class="title_titlem"
                ref="md"
                @change="changeData"
                @imgAdd="imgAdd"
                @imgDel="imgDel"
                v-model="md_text"
            />
            <div>
                <!-- 保存 -->
                <el-button type="success" @click="save" class="title_titleb">保存</el-button>
            </div>
        </div>
    </div>
</template>

<script>
import request from "../utils/request";
export default {
    data() {
        return {
            fileList: [],
            md_text: "",
            html_text: "",
            img: "",
            title: "",
            headers: {
                token: "",
            },
        };
    },
    methods: {
        save(){
            if(this.id){
                this.updateBlog();
            }else{
                this.createBlog();
            }
        },
        createBlog(){
            request({
                url:"/blog",
                method:"post",
                data:{
                    md_text:this.md_text,
                    html_text:this.html_text,
                    img:this.img,
                    title:this.title
                }
            }).then(() => {
                this.$router.push("/blog")
            })
        },
        updateBlog(){
            request({
                url:`/blog/${this.id}`,
                method:"put",
                data:{
                    md_text:this.md_text,
                    html_text:this.html_text,
                    img:this.img,
                    title:this.title
                }
            }).then(() => {
                this.$router.push("/blog")
            })
        },
        getUploadUrl() {
            return process.env.VUE_APP_UPLOAD_API;
        },
        changeData(md_text,html_text) {
            this.html_text = html_text;
        },
        imgAdd(pos, $file) {
            // 第一步.将图片上传到服务器.
            var formdata = new FormData();
            formdata.append("image", $file);
            console.log($file, "$file");
            request({
                url: process.env.VUE_APP_UPLOAD_API,
                method: "post",
                data: formdata,
                headers: { "Content-Type": "multipart/form-data" },
            })
                .then((res) => {
                    // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)

                    // 说明
                    /**
                     * $vm 指为mavonEditor实例，可以通过如下两种方式获取
                     * 1. 通过引入对象获取: `import {mavonEditor} from ...` 等方式引入后，`$vm`为`mavonEditor`
                     * 2. 通过$refs获取: html声明ref : `<mavon-editor ref=md ></mavon-editor>，`$vm`为 `this.$refs.md`
                     */
                    // 开发环境使用使用开发环境取消注释
                    // let url = "http://127.0.0.1:7007" + res.data.file;
                    let url = res.data.data.file;
                    this.$refs.md.$img2Url(pos, url);
                })
                .catch((err) => {
                    console.log(err);
                });
        },
        imgDel() {},
        upload() {},
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
        }
    },
    computed:{
        id(){
            return this.$route.params.id;
        }
    },
    created(){
        //判断是修改还是新建
        if(this.id){
            request({
                url:`/blog/${this.id}`,
                method:"get",
            }).then((res) => {
                let blog = res.data.data;
                this.title = blog.title;
                this.fileList = [
                    {url:blog.img}
                ]
                this.img = blog.img;
                this.md_text = blog.md_text;
                this.html_text = blog.html_text;
            })
        }
    }
};
</script>