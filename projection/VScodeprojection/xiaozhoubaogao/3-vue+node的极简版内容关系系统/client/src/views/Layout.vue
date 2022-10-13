<template>
    <div class="layout">
        <div class="menu">
            <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
                <el-radio-button :label="false">展开</el-radio-button>
                <el-radio-button :label="true">收起</el-radio-button>
            </el-radio-group>
            <el-menu
                default-active="1-4-1"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                :collapse="isCollapse"
                router
            >
                <el-menu-item index="/book">
                    <i class="el-icon-menu"></i>
                    <span slot="title">
                        书籍管理
                    </span>
                </el-menu-item>
                <el-menu-item index="/blog">
                    <i class="el-icon-document"></i>
                    <span slot="title">博客管理</span>
                </el-menu-item>
                <el-menu-item index="/video">
                    <i class="el-icon-setting"></i>
                    <span slot="title">视频管理</span>
                </el-menu-item>
                <el-menu-item index="/resource">
                    <i class="el-icon-setting"></i>
                    <span slot="title">资源列表</span>
                </el-menu-item>
                <el-submenu index="1">
                    <template slot="title">
                        <i class="el-icon-location"></i>
                        <span slot="title">用户管理</span>
                    </template>
                    <el-menu-item index="/user">用户列表</el-menu-item>
                    <el-menu-item @click="logout">注销</el-menu-item>
                </el-submenu>
            </el-menu>
        </div>
        <div class="container">
            <router-view></router-view>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isCollapse: false,
        };
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        logout() {
            localStorage.setItem("token","");
            location.reload();
        },
    },
};
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
}
.layout a {
    color: #000;
    text-decoration: none;
}
.layout {
    display: flex;
}
.layout .menu {
    width: 200px;
}
.layout .container {
    width: 100%;
}
.layout .breadcrumb {
    padding: 10px;
}
</style>



