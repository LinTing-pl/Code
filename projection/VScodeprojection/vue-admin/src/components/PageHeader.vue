<script setup lang="ts">
import '../assets/iconfont/iconfont.js'
import { defineProps, onMounted, ref} from 'vue';
import {useColorStore} from '../store/colorStore'
const props=defineProps(['header','isShow'])
const useColor=useColorStore()
const pageH=ref(null)
onMounted(()=>{
    useColor.pageHeaderE=pageH.value
    useColor.changeColor('pageHeader','')
})
</script>

<template>
    <div class="pageH" ref="pageH"><span v-show="props.isShow" style="color:#545c64">{{ props.header }}</span>
        <div class="right-top">
            <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-search"></use>
            </svg>
            <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-alert"></use>
            </svg>
            <img src="../assets/img/default.jpeg" alt=""><span>麟听 <svg class="icon" aria-hidden="true">
                <use xlink:href="#icon-sanjiao"></use>
            </svg></span>
        </div>
    </div>
</template>

<style scoped lang="scss">

.pageH{
    height: 45px;
    line-height: 45px;
    padding-left: 45px;
    padding-top: 2px;
    background: #ffffff;
    user-select: none;
    position: relative;
    .right-top{
        position: absolute;
        right: 0;
        top: 50%; 
        transform: translateY(-50%);
        svg{
            margin-right: 10px;
            cursor: pointer;
        }
        svg:hover{
            filter: drop-shadow(0 0 20px blue) invert(100%);
        }
        svg:nth-child(2){
            margin-right: 15px;
        }
        svg:nth-last-child(1){
            width: .7em;
            height: .7em;
        }
        img{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            position: relative;
            top: 10px;
            border: 1px solid #000;
            padding: 2px;
            cursor: pointer;
            margin-right: 5px;
        }
        img:hover{
            filter: drop-shadow(0 0 20px blue) ;
        }
        span{
            position: relative;
            top: -7px;
            color:rgb(232, 113, 230);
            margin-right: 16px;
            cursor: pointer;
        }
        span:hover{
            text-decoration: underline;
            svg{
                filter: drop-shadow(0 0 20px blue) invert(100%);
            }
        }
    }
}
</style>