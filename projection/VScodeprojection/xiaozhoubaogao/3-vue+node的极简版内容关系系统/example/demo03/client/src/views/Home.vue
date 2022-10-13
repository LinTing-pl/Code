<template>
    <div>
        <h1>我是首页<button @click="postData">添加数据</button></h1>
        <mavon-editor @change="changeText" v-model="content.md_text"/>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data(){
        return {
            content:{
                md_text:"",
                html_text:""
            }
        }
    },
    created(){
        this.getData();
    },
    methods:{
        getData(){
            axios.get("http://127.0.0.1:7001/show",{content:this.content}).then(res => {
                this.content.md_text = res.data.md_text;
            })
        },
        postData(){
            axios.post("http://127.0.0.1:7001/create",{content:this.content}).then(res => {
                console.log(res.data);
            })
        },
        changeText(value,render){
            this.content.md_text = value;
            this.content.html_text = render;
        }
    }
}
</script>