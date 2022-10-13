<template>
    <div>
        <div>
            <el-upload
                action="http://127.0.0.1:7001/upload"
                list-type="picture-card"
                :limit="1"
                :on-exceed="handleExceed"
                :on-success="success"
                :file-list="fileList"
            >
                <i class="el-icon-plus"></i>
            </el-upload>
            <input type="text" placeholder="标题" v-model="content.title" />
            <input type="text" placeholder="提取码" v-model="content.code" />
            <input type="text" placeholder="下载地址" v-model="content.downloadurl" />
            <button @click="postData">添加</button>
        </div>
        <ul v-if="list.length">
            <li v-for="v in list">
                <img :src="v.imgurl" alt="">
                <span>{{v.title}}</span>
                <span>提取码：{{v.code}}</span>
                <span>下载地址：{{v.downloadurl}}</span>
                <button @click="deleteData(v.id)">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios"
export default {
    data() {
        return {
            list:[],
            fileList: [],
            content: {
                title: "",
                imgurl: "",
                code: "",
                downloadurl: "",
            },
        };
    },
    created(){
        this.getList();
    },
    methods: {
        handleExceed(files, fileList) {
            this.$message.warning("只能上传一张图片！");
        },
        success(res) {
            this.content.imgurl = res.data.file;
        },
        getList(){
            axios.get(`http://127.0.0.1:7001/resource`).then(res => {
                this.list = res.data
            })
        },
        postData(){
            axios.post(`http://127.0.0.1:7001/resource`,{content:this.content}).then(res => {
                this.getList();
            })
        },
        deleteData(id){
            axios.delete(`http://127.0.0.1:7001/resource/${id}`).then(res => {
                this.getList();
            })
        }
    },
};
</script>
<style scoped>
img{
    width:100px;
    height:100px;
}
</style>