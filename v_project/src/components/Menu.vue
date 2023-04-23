<template>
<el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      :default-openeds="['1','2','3']"
      @open="handleOpen"
      @close="handleClose">
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>功能区</span>
        </template>

        <el-menu-item-group>
          <el-menu-item index="1-1">项目管理</el-menu-item>
          <el-menu-item index="1-2">用例设计</el-menu-item>
          <el-menu-item index="1-2">环境管理</el-menu-item>

        </el-menu-item-group>
        </el-submenu>

      <el-submenu index="2">
        <template slot="title">
        <i class="el-icon-user"></i>
          <span>用户区</span>
        </template>

        <el-menu-item-group>
          <el-menu-item index="1-1">个人信息</el-menu-item>
          <el-menu-item index="1-2">个人贡献</el-menu-item>
          <el-menu-item index="1-2">发送消息</el-menu-item>
          <a href="http://localhost:8081/logout/"><el-menu-item>退出</el-menu-item></a>
          <a href="http://127.0.0.1:8008/help/"><el-menu-item>帮助</el-menu-item></a>
        </el-menu-item-group>
        </el-submenu>

      <el-submenu index="3">
        <template slot="title">
        <i class="el-icon-setting"></i>
          <span>维护区</span>
        </template>

        <el-menu-item-group>
          <a href="http://127.0.0.1:8008/admin/"><el-menu-item>进入后台</el-menu-item></a>
          <el-menu-item index="1-2">发布公告</el-menu-item>
          <el-menu-item index="1-2">查看日志</el-menu-item>
          <el-menu-item index="1-2">权限管理</el-menu-item>
        </el-menu-item-group>
        </el-submenu>

    </el-menu>
</template>

<script>
export default {
  name: "Menu",
  data(){
    return{

    }
  }
}
</script>

<style scoped>

</style>