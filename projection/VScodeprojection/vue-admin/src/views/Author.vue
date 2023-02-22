<script setup lang="ts">
import { getCurrentInstance } from 'vue';
const proxy:any = getCurrentInstance()
const _this:any=proxy.appContext.config.globalProperties
_this.$axios.get('/author/get').then((resp:any)=>{
    console.log(resp);
})
</script>

<template>
    <div class="content-container">
        
    </div>
</template>

<style scoped>
.content-container{
    height: 80vh;
    min-height: 350px;
    margin: 20px 40px;
    background: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}
</style>