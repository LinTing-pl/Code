<script setup lang="ts">
import BMap from '../components/BMap.vue'
</script>

<template>
    <div class="content-container">
        <BMap class="bm-view" ak="Ndu4iww5PUNFuDfy8RPoIG4EbWdGCPHI" center="大同">
  </BMap>
    </div>
</template>

<style scoped lang="scss">
.content-container{
  height: 80vh;
  margin: 20px 40px;
  min-height: 350px;
}
</style>