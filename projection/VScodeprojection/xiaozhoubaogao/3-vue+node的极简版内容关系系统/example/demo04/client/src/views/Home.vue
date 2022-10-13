<template>
    <div>
        <button @click="createBlog">添加</button>
        <ul>
            <li v-for="v in list">
                <span>{{ v.title }}</span>
                <button @click="deleteBlog(v.id)">删除</button>
                <button @click="editBlog(v.id)">修改</button>
            </li>
        </ul>
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {
            list: [],
        };
    },
    created() {
        this.getList();
    },
    methods: {
        getList() {
            axios.get("http://127.0.0.1:7001/blog").then((res) => {
                this.list = res.data;
            });
        },
        createBlog() {
            this.$router.push("/create");
        },
        editBlog(id) {
            this.$router.push(`/edit/${id}`);
        },
        deleteBlog(id) {
            axios.delete(`http://127.0.0.1:7001/blog/${id}`).then((res) => {
                this.getList();
            });
        },
    },
};
</script>