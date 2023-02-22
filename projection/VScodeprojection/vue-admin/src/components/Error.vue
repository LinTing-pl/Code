<script setup lang="ts">
import '../assets/iconfont/iconfont.js'
import { defineProps, onBeforeUpdate} from "vue";
import router from '../router';
const props = defineProps(["errorType","global",'onClick']);
let back=()=>{
    router.go(-1)
    props.onClick()
}

let info=''
switch(props.errorType){
    case '304':info='请求的网站未改变';break
    case '404':info='服务器未找到';break
    case '504':info='服务器请求超时';break
    default:info=`${props.errorType}错误功能正在开发`
}
onBeforeUpdate(() => {
    switch(props.errorType){
    case '304':info='请求的网站未改变';break
    case '404':info='服务器未找到';break
    case '504':info='服务器请求超时';break
    default:info=`${props.errorType}错误功能正在开发`
}
})
</script>

<template>
    <div>
        <svg class="icon icon1" aria-hidden="true">
            <use xlink:href="#icon-weihuzhong"></use>
        </svg>
        <svg v-if="props.global" @click="back" class="icon icon2" aria-hidden="true">
            <use xlink:href="#icon-error"></use>
        </svg>
        <span class="info">{{ info }}</span>
    </div>
</template>

<style scoped>
div{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%,-55%);
}
.icon1{
    width: 20em;
    height: 20em;
}
.icon2{
    width: 3em;
    height: 3em;
    position: absolute;
    right: 0px;
    top: 0px;
    cursor: pointer;
}
.icon2:hover{
    filter: drop-shadow(0 0 3px #000);
}
.info{
    display: inline-block;
    position: absolute;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
}
</style>