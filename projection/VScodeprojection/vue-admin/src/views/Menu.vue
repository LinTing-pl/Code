<script setup lang="ts">
import {
  Check,
  Delete,
  Edit,
  Message,
  Search,
  Star,
  Eleme,
  ChatDotRound, ChatLineRound, ChatRound,
} from '@element-plus/icons-vue'
import { ElNotification } from 'element-plus'
import { ref } from 'vue'

const value = ref(4)
const value1 = ref(2)
const icons = [ChatRound, ChatLineRound, ChatDotRound]
const open1 = () => {
  ElNotification({
    title: 'Success',
    message: 'This is a success message',
    type: 'success',
  })
}

const open2 = () => {
  ElNotification({
    title: 'Warning',
    message: 'This is a warning message',
    type: 'warning',
  })
}

const open3 = () => {
  ElNotification({
    title: 'Info',
    message: 'This is an info message',
    type: 'info',
  })
}

const open4 = () => {
  ElNotification({
    title: 'Error',
    message: 'This is an error message',
    type: 'error',
  })
}
const format = (percentage:any) => (percentage === 100 ? 'Full' : `${percentage}%`)
</script>

<template>
    <div class="content-container">
      <el-carousel indicator-position="outside" height="90%">
          <el-carousel-item v-for="item in 4" :key="item">
            <div class="display" v-if="item===1">
              <el-row class="mb-4">
                <el-button>Default</el-button>
                <el-button type="primary">Primary</el-button>
                <el-button type="success">Success</el-button>
                <el-button type="info">Info</el-button>
                <el-button type="warning">Warning</el-button>
                <el-button type="danger">Danger</el-button>
              </el-row>
                <el-row class="mb-4">
                  <el-button plain>Plain</el-button>
                  <el-button type="primary" plain>Primary</el-button>
                  <el-button type="success" plain>Success</el-button>
                  <el-button type="info" plain>Info</el-button>
                  <el-button type="warning" plain>Warning</el-button>
                  <el-button type="danger" plain>Danger</el-button>
                </el-row>
                <el-row class="mb-4">
                  <el-button round>Round</el-button>
                  <el-button type="primary" round>Primary</el-button>
                  <el-button type="success" round>Success</el-button>
                  <el-button type="info" round>Info</el-button>
                  <el-button type="warning" round>Warning</el-button>
                  <el-button type="danger" round>Danger</el-button>
                </el-row>
              
                <el-row>
                  <el-button :icon="Search" circle />
                  <el-button type="primary" :icon="Edit" circle />
                  <el-button type="success" :icon="Check" circle />
                  <el-button type="info" :icon="Message" circle />
                  <el-button type="warning" :icon="Star" circle />
                  <el-button type="danger" :icon="Delete" circle />
                  <el-button type="primary" loading>Loading</el-button>
                  <el-button type="primary" :loading-icon="Eleme" loading>Loading</el-button>
                  <el-button type="primary" loading>
                    <template #loading>
                      <div class="custom-loading">
                        <svg class="circular" viewBox="-10, -10, 50, 50">
                          <path
                            class="path"
                            d="
                            M 30 15
                            L 28 17
                            M 25.61 25.61
                            A 15 15, 0, 0, 1, 15 30
                            A 15 15, 0, 1, 1, 27.99 7.5
                            L 15 15
                          "
                            style="stroke-width: 4px; fill: rgba(0, 0, 0, 0)"
                          />
                        </svg>
                      </div>
                    </template>
                    Loading
                  </el-button>
                </el-row>
            </div>
            <div class="display" v-else-if="item===2">
              <el-rate v-model="value" size="large" />
              <el-rate v-model="value" />
              <el-rate v-model="value" size="small" />
              <el-rate
                v-model="value1"
                :icons="icons"
                :void-icon="ChatRound"
                :colors="['#409eff', '#67c23a', '#FF9900']"
              />
            </div>
            <div class="display display3" v-else-if="item===3">
              <el-button plain @click="open1"> Success </el-button>
              <el-button plain @click="open2"> Warning </el-button>
              <el-button plain @click="open3"> Info </el-button>
              <el-button plain @click="open4"> Error </el-button>
            </div>
            <div class="display" v-else-if="item===4">
              <div class="demo-progress">
    <el-progress :percentage="50" :indeterminate="true" />
    <el-progress :percentage="100" :format="format" :indeterminate="true" />
    <el-progress
      :percentage="100"
      status="success"
      :indeterminate="true"
      :duration="5"
    />
    <el-progress
      :percentage="100"
      status="warning"
      :indeterminate="true"
      :duration="1"
    />
    <el-progress :percentage="50" status="exception" :indeterminate="true" />
  </div>
            </div>
          </el-carousel-item>
        </el-carousel>
    </div>
</template>

<style scoped>
.content-container{
  height: 80vh;
  min-height: 350px;
  margin: 20px 40px;
  background: #fff;
  box-sizing: border-box;
  padding: 10px;
  }
  .el-row{
    margin: 5px;
  }
  .el-button .custom-loading .circular {
  margin-right: 6px;
  width: 18px;
  height: 18px;
  animation: loading-rotate 2s linear infinite;
}
.el-button .custom-loading .circular .path {
  animation: loading-dash 1.5s ease-in-out infinite;
  stroke-dasharray: 90, 150;
  stroke-dashoffset: 0;
  stroke-width: 2;
  stroke: var(--el-button-text-color);
  stroke-linecap: round;
}
.el-carousel:hover{
  animation-play-state: paused;
}
.el-carousel{
  height: 100%;
}
.el-carousel__item{
  height: 100%;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.display{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 100%;
}
.display3{
  flex-direction: row;

}
.demo-progress .el-progress--line {
  margin-bottom: 15px;
  width: 350px;
}
</style>