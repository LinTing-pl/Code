<script setup lang="ts">
import { nextTick, onMounted, ref } from 'vue';
import {useColorStore} from '../store/colorStore'
const useColor=useColorStore()
const setting1=ref(null)
const setting2=ref(null)
const setting3=ref(null)
const setting4=ref(null)
const setting5=ref(null)
const setting6=ref(null)
const setting7=ref(null)
const setting8=ref(null)
const setting9=ref(null)

onMounted(() => {
  useColor.setting1E=setting1.value
  useColor.changeColor('setting1','')
  useColor.setting2E=setting2.value
  useColor.changeColor('setting2','')
  useColor.setting3E=setting3.value
  useColor.changeColor('setting3','')
  useColor.setting4E=setting4.value
  useColor.changeColor('setting4','')
  useColor.setting5E=setting5.value
  useColor.changeColor('setting5','')
  useColor.setting6E=setting6.value
  useColor.changeColor('setting6','')
  useColor.setting7E=setting7.value
  useColor.changeColor('setting7','')
  useColor.setting8E=setting8.value
  useColor.changeColor('setting8','')
  useColor.setting9E=setting9.value
  useColor.changeColor('setting9','')
})
let inputHandler=(e:any,cls:String)=>{
    useColor.changeColor(cls,e.target.value)
}
let btnHandler=(cls:string)=>{
    if(cls==='layout'&&useColor.layoutColor!=='#f7f8fa'){
        useColor.changeColor('layout','#f7f8fa')
    }else if(cls==='menu'&&useColor.menuColor!=='#545c64'){
        useColor.changeColor('menu','#545c64')
    }else if(cls==='pageHeader'&&useColor.pageHeaderColor!=='#ffffff'){
        useColor.changeColor('pageHeader','#ffffff')
    }else if(cls==='setting1'&&useColor.setting1Color!=='#ffffff'){
        useColor.changeColor('setting1','#ffffff')
    }else if(cls==='setting2'&&useColor.setting2Color!=='#ffffff'){
        useColor.changeColor('setting2','#ffffff')
    }else if(cls==='setting3'&&useColor.setting3Color!=='#ffffff'){
        useColor.changeColor('setting3','#ffffff')
    }else if(cls==='setting4'&&useColor.setting4Color!=='#ffffff'){
        useColor.changeColor('setting4','#ffffff')
    }else if(cls==='setting5'&&useColor.setting5Color!=='#ffffff'){
        useColor.changeColor('setting5','#ffffff')
    }else if(cls==='setting6'&&useColor.setting6Color!=='#ffffff'){
        useColor.changeColor('setting6','#ffffff')
    }else if(cls==='setting7'&&useColor.setting7Color!=='#ffffff'){
        useColor.changeColor('setting7','#ffffff')
    }else if(cls==='setting8'&&useColor.setting8Color!=='#ffffff'){
        useColor.changeColor('setting8','#ffffff')
    }else if(cls==='setting9'&&useColor.setting9Color!=='#ffffff'){
        useColor.changeColor('setting9','#ffffff')
    }
}
</script>

<template>
    <div class="content-container">
        <div class="div1" ref="setting1">
            <div>
                <span>Layout布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('layout')" value="red">默认</button>
                <input type="color"  @input="inputHandler($event,'layout')" :value="useColor.layoutColor">
            </div>
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting1')" value="red">默认</button>
                <input type="color"  @input="inputHandler($event,'setting1')" :value="useColor.setting1Color">
            </div>
        </div>
        <div class="div1" ref="setting2">
            <div >
                <span>Menu布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('menu')">默认</button>
                <input type="color"  @input="inputHandler($event,'menu')" :value="useColor.menuColor">
            </div>
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting2')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting2')" :value="useColor.setting2Color">
            </div>
        </div>
        <div class="div1" ref="setting3">
            <div >
                <span>PageHeader布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('pageHeader')">默认</button>
                <input type="color"  @input="inputHandler($event,'pageHeader')" :value="useColor.setting3Color">
            </div>
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting3')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting3')" :value="useColor.setting3Color">
            </div>
        </div>
        <div class="div1" ref="setting4">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting4')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting4')" :value="useColor.setting4Color">
            </div>
        </div>
        <div class="div1" ref="setting5">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting5')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting5')" :value="useColor.setting5Color">
            </div>
        </div>
        <div class="div1" ref="setting6">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting6')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting6')" :value="useColor.setting6Color">
            </div>
        </div>
        <div class="div1" ref="setting7">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting7')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting7')" :value="useColor.setting7Color">
            </div>
        </div>
        <div class="div1" ref="setting8">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting8')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting8')" :value="useColor.setting8Color">
            </div>
        </div>
        <div class="div1" ref="setting9">
            <div >
                <span>本地布局:</span>
                <button class="defaultcolor-btn" @click="btnHandler('setting9')">默认</button>
                <input type="color"  @input="inputHandler($event,'setting9')" :value="useColor.setting9Color">
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
.content-container{
  height: 80vh;
  min-height: 350px;
  margin: 20px 40px;
  display: grid;
  grid-template-rows: repeat(3,30%);
  grid-template-columns: repeat(3,32%);
  grid-row-gap: 5%;
  grid-column-gap: 2%;
  .div1{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background: #ffffff;
    box-shadow:0 0 5px rgb(240, 242, 243),
    inset 0 0 10px rgb(240, 242, 243);
    // filter: 
    span{
        display: inline-block;
        width: 130px;
        text-align: right;
    }
  }
}
.defaultcolor-btn{
    margin: 5px;
}
</style>