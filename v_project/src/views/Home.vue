<template>
  <div id="home" style="height: 100%">
    <el-container style="height: 100%">

      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

      <el-container>
        <el-header style="height: 80px">
          <img src="/static/title.gif" alt="" style="height: 60px;padding-top: 8px">

        </el-header>
        <el-main>
          <el-card class="box-card" style="width: 500px;min-height: 300px">
          </el-card >

          <div style="float: right">
          <el-card class="box-card" style="width: 500px;min-height: 300px;">

          </el-card>
          </div>

        </el-main>
        <el-footer style="overflow-y:auto;min-height: 160px;padding-top: 15px;text-align: left">
          <el-card class="box-card" style="width: 100%;min-height: 90%;background: linear-gradient(to left,white,#e5ffff)">
            <div v-for="o in tj_datas.notices" class="text item">
              {{'平台更新日志：'+o.content}}
            </div>
          </el-card>
        </el-footer>
      </el-container>
    </el-container>

  </div>
</template>

<script>
// @ is an alias to /src
  import Menu from '../components/Menu.vue'
  import axios from 'axios'

  export default {
    name: 'home',
    data(){
      return{
        tj_datas:{
          notices:[]
        }

      };
    },
    methods:{

    },
    components: {
      Menu,

    },
    mounted:function () {
      axios('http://127.0.0.1:8008/get_tj_datas').then(res=>{
        this.tj_datas = res.datas;
      })
    }
  }
</script>


<style>
  .el-header {
    background-color: #c5eded;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-footer {
    background-color: #f4f1f2;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: white;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>