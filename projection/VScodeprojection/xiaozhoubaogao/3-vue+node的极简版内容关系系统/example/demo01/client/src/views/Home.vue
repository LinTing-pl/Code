<template>
    <div>
        <h1>我是首页</h1>
        <form @submit.prevent="postData">
            <input type="text" v-model="fruit">
            <button>添加</button>
        </form>
        <ul>
            <li v-for="(v) in list">
                <span>{{v.name}}</span>
                <button @click="del(v.id)">删除</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios"
export default {
    created(){
        this.getList();
    },
    data(){
        return {
            list:[],
            fruit:""
        }
    },
    methods:{
        getList(){
            axios.get("http://127.0.0.1:7001/fruit").then(res => {
                this.list = res.data
            })
        },
        postData(){
            axios.post("http://127.0.0.1:7001/fruit",{fruit:this.fruit}).then(res => {
                this.getList();
            })
        },
        del(i){
            axios.delete(`http://127.0.0.1:7001/fruit/${i}`).then(res => {
                this.getList();
            })
        }
    }
}
</script>