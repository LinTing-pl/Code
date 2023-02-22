<script setup lang="ts">
import { onMounted, ref } from 'vue';
import Error from '../components/Error.vue';
import {showError} from '../utils/error.js'
let errorCode=ref('304')
let btnDefault=ref()
let btnHandler=(e:any)=>{
  errorCode.value=e.target.innerText;
}
onMounted(() => {
  btnDefault.value.click()
})
</script>

<template>
    <div class="content-container">
      <div class="opts">
        <button ref="btnDefault" @click="btnHandler">304</button>
        <button @click="btnHandler">404</button>
        <button @click="btnHandler">504</button>
        <button @click="showError(errorCode,true)">报{{ errorCode }}错误</button>
      </div>
      <Error :error-type="errorCode"></Error>
    </div>
</template>

<style scoped lang="scss">
.content-container{
  height: 80vh;
  min-height: 350px;
  margin: 20px 40px;
  background: #fff;
  position: relative;
  overflow: hidden;
  .opts{
    border: 2px solid #edeff2;
    border-radius: 10px;
    position: relative;
    top: 10px;
    left: 10px;
    width: 220px;
    button{
      margin: 2px;
    }
  }
  }
</style>