<template>
  <div id="app">
    <header><el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1">
    <router-link to="/exam1">
  实验一:最优物流路线计算</router-link></el-menu-item>
  <el-menu-item index="2"><router-link to="/exam2">
  实验二:多进程多用户文件一致性读写访问设计</router-link></el-menu-item>
  <el-menu-item index="3"><router-link to="/exam3">
  实验三:SQL解析器设计</router-link></el-menu-item>
  <el-menu-item index="4"><router-link to="/exam4">
  实验四:互联网+智慧物流质询系统设计</router-link></el-menu-item>
</el-menu></header>
    <router-view></router-view>
    
  </div>
</template>

<script>


export default {
  name: 'App',
  components: {
 
  },
  methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    },
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      };
    },
}
</script>

<style>
/*#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}*/
</style>
