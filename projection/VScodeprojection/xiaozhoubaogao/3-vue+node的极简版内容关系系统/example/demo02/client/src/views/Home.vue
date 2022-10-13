<template>
    <div>
        <h1>我是首页</h1>
        <form @submit.prevent="postData">
            <input type="text" placeholder="标题" v-model="title" />
            <input type="text" placeholder="iframe地址" v-model="iframe" />
            <button>添加</button>
        </form>
        <ul>
            <li v-for="(v, i) in list">
                <span>{{ v.title }}</span
                >|
                <span>{{ v.iframe }}</span>
                <button @click="del(v.id)">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            title: "",
            iframe: "",
            list: [],
        };
    },
    created(){
        this.getlist();
    },
    methods: {
        getlist() {
            axios.get("http://127.0.0.1:7001/video").then((res) => {
                this.list = res.data;
            });
        },
        postData() {
            axios.post("http://127.0.0.1:7001/video",{
                title:this.title,
                iframe:this.iframe
            }).then((res) => {
                this.getlist();
            });
        },
        del(id){
            axios.delete(`http://127.0.0.1:7001/video/${id}`).then((res) => {
                this.getlist();
            });
        }
    },
};
</script>