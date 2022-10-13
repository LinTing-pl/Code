<template>
    <div>
        <h1>修改数据<button @click="postData">保存</button></h1>
        <input type="text" placeholder="博客标题" v-model="content.title">
        <mavon-editor @change="changeText" v-model="content.md_text"/>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data(){
        return {
            id:this.$route.params.id,
            content:{
                title:"",
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
            axios.get(`http://127.0.0.1:7001/blog/${this.id}`,{content:this.content}).then(res => {
                this.content.md_text = res.data.md_text;
                this.content.html_text = res.data.html_text;
                this.content.title = res.data.title;
            })
        },
        postData(){
            axios.put(`http://127.0.0.1:7001/blog/${this.id}`,{content:this.content}).then(res => {
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