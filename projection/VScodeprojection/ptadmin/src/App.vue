<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {};
</script>
<style lang="scss">
html {
  overflow: auto;
}
body {
  margin: 0;
  padding: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100vh;
  width: 100vw;
  display: flex;
  flex-direction: column;
  min-width: 1252px;
  margin: 0;
  padding: 0;
}
</style>
