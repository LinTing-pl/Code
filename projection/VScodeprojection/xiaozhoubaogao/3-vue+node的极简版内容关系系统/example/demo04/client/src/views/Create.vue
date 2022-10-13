<template>
    <div>
        <h1>添加数据<button @click="postData">保存</button></h1>
        <input type="text" placeholder="博客标题" v-model="content.title">
        <mavon-editor @change="changeText" v-model="content.md_text"/>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data(){
        return {
            content:{
                title:"",
                md_text:"",
                html_text:""
            }
        }
    },
    methods:{
        postData(){
            axios.post("http://127.0.0.1:7001/blog",{content:this.content}).then(res => {
                this.$router.push("/")
            })
        },
        changeText(value,render){
            this.content.md_text = value;
            this.content.html_text = render;
        }
    }
}
</script>