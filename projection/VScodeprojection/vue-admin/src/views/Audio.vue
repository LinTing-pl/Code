<script setup lang="ts">
import { ref } from 'vue';

const audioEle=ref()
const cvs=ref()
let isInit=false
let isEnable:boolean=false
let ctx:any
let dataArray:any
let analyser:any
let alpha=99
let up=false
const colorArray=['#33ccff', '#ff99cc']
let color=colorArray[0]
const changeHandler=(e:any)=>{
    const file=e.target.files[0]
    if(file){
        const reader=new FileReader()
        reader.readAsDataURL(file)
        reader.onload=function(e){
        audioEle.value.src=e.target?.result
    }
    }
}

const init=()=>{
    if(isInit){
        isEnable=true
        draw()
        return
    }
    ctx=cvs.value.getContext('2d')
    const audCtx=new AudioContext()
    const source=audCtx.createMediaElementSource(audioEle.value)
    analyser=audCtx.createAnalyser()
    analyser.fftSize=512
    dataArray=new Uint8Array(analyser.frequencyBinCount)
    source.connect(analyser)
    analyser.connect(audCtx.destination)
    isInit=true
    isEnable=true
    draw()
}
const draw=()=>{
    if(!isInit)return
    if(!isEnable)return
    requestAnimationFrame(draw)
    const {width,height}=cvs.value
    ctx.clearRect(0,0,width,height)
    analyser.getByteFrequencyData(dataArray)
    const len=dataArray.length/2.5
    const barWidth=width/len/2
    ctx.fillStyle=color+Math.ceil(alpha)
    if(up){
        alpha=alpha+0.5
        if(alpha===99)up=false
    }else{
        alpha=alpha-0.5
        if(alpha===50){
            up=true
            color===colorArray[0]?color=colorArray[1]:color=colorArray[0]
        }
    }
    for(let i=0;i<len;i++){
        const data=dataArray[i]
        const barHeight=data/255*height
        const x1=i*barWidth +width/2
        const x2=width/2 - (i+1)*barWidth
        const y=height-barHeight
        ctx.fillRect(x1,y,barWidth-3,barHeight)
        ctx.fillRect(x2,y,barWidth-3,barHeight)
    }
}
</script>

<template>
    <div class="content-container">
        <canvas ref="cvs"></canvas>
        <div class="opts">
            <label for="ipt">
                <span>上传</span>
            </label>
            <audio ref="audioEle" src="" controls @play="init" @pause="isEnable=false"></audio>
            <input id="ipt" type="file" style="display:none" @change='changeHandler'>
        </div>
    </div>
</template>

<style scoped lang="scss">
.content-container{
  height: 80vh;
  min-height: 350px;
  margin: 20px 40px;
  background: #fff;
  position: relative;
  display: flex;
  flex-direction: column;
  canvas{
    margin: 20px;
    height: 200px;
    background: #000;
    flex: 1;
  }
  .opts{
    flex-shrink: 0;
    align-self: center;
    position: relative;
    span{
        position: absolute;
        border: 1px solid transparent;
        top: 5px;
        left: -80px;
        padding: 8px 12px;
        font-size: 17px;
        background: #f1f3f4;
        border-radius: 8px;
        cursor: pointer;
    }
    span:hover{
        border-color: #646cff;
    }
    audio{
        border: 1px solid transparent;
        border-radius: 26px;
    }
    audio:hover{
        border-color: #646cff;
    }
  }
}
</style>