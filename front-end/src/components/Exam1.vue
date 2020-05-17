<template>
    <div id="exam">
      <div class="part1">
        <div>
            <el-row>
                <el-col :span="10" style="margin-top:15px;">
                    <div class="grid-content bg-purple">
                        <p class="table_title">物品记录表</p>
                    </div>
                </el-col>
                <el-col :span="14" style="padding-top: 30px;">
                    <div class="grid-content bg-purple-light">
                        <div class="button_container" v-if="productTitleType=='button'">
                            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                              <el-form-item label="物流方案类型">
                                    <el-select v-model="formInline.region" placeholder="物流方案类型">
                                        <el-option label="时间最短方案" value="shanghai"></el-option>
                                        <el-option label="价格最低方案" value="beijing"></el-option>
                                    </el-select>
                                </el-form-item>
                                <el-form-item>
                                    <el-button type="primary" @click="onSearch">查询</el-button>
                                </el-form-item>
                                <el-button @click="productTitleType='add'">添加</el-button>
                                <el-button @click="productTitleType='del'">删除</el-button>
                                <el-button @click="productTitleType='change'">修改</el-button>
                                <el-button icon="el-icon-sort-down">综合排序</el-button>
                                <el-button >立即发送</el-button>
                                
                            </el-form>
                        </div>
                    </div>
                </el-col>
            </el-row>
        </div>
        <div class="add" v-if="productTitleType=='add'">
            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-form-item label="vip">
                    <el-input v-model="formInline.user" placeholder="vip"></el-input>
                </el-form-item>
                <el-form-item label="wait_time">
                    <el-input v-model="formInline.user" placeholder="wait_time"></el-input>
                </el-form-item>
                <el-form-item label="mode">
                    <el-input v-model="formInline.user" placeholder="mode"></el-input>
                </el-form-item>
                <el-form-item label="vip">
                    <el-input v-model="formInline.user" placeholder="vip"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="productTitleType='button'">确定新增</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div class="del" v-if="productTitleType=='del'">
            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-form-item label="id">
                    <el-input v-model="formInline.user" placeholder="id"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="productTitleType='button'">确定删除</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div class="change" v-if="productTitleType=='change'">
            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                <el-form-item label="id">
                    <el-input v-model="formInline.user" placeholder="id"></el-input>
                </el-form-item>
                <el-form-item label="vip">
                    <el-input v-model="formInline.user" placeholder="vip"></el-input>
                </el-form-item>
                <el-form-item label="wait_time">
                    <el-input v-model="formInline.user" placeholder="wait_time"></el-input>
                </el-form-item>
                <el-form-item label="mode">
                    <el-input v-model="formInline.user" placeholder="mode"></el-input>
                </el-form-item>
                <el-form-item label="vip">
                    <el-input v-model="formInline.user" placeholder="vip"></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="productTitleType='button'">确定修改</el-button>
                </el-form-item>
            </el-form>
        </div>
        <div class="wuliu_table">
            <el-table :data="wuliuTableData" stripe style="width: 100%">
              <el-table-column prop="id" label="id">
                </el-table-column>
                <el-table-column prop="name" label="名称" width="180">
                </el-table-column>
                <el-table-column prop="waittime" label="等待时间" width="180">
                </el-table-column>
                <el-table-column prop="vip" label="vip" width="180">
                </el-table-column>
                
                <el-table-column prop="destination" label="目的地">
                </el-table-column>
                <el-table-column prop="mode" label="物流方案类型">
                </el-table-column>
                <el-table-column prop="path" label="最短路径">
                </el-table-column>
                <el-table-column prop="status" label="物流状态">
                </el-table-column>
            </el-table>
        </div>
      </div>
       <div class="part2">
        <div>
            <el-row>
                <el-col :span="10" style="margin-top:15px;">
                    <div class="grid-content bg-purple">
                        <p class="table_title">节点记录表</p>
                    </div>
                </el-col>
                <el-col :span="14" style="padding-top: 30px;">
                    <div class="grid-content bg-purple-light">
                        <div class="button_container" v-if="nodeTitleType=='button'">
                            <el-form :inline="true" :model="formInline" class="demo-form-inline">
                             
                                <el-button @click="nodeTitleType='set'" >重新建立节点记录表</el-button>
                               
                                
                                
                                
                            </el-form>
                        </div>
                    </div>
                </el-col>
            </el-row>
        </div>
       
        <div class="set_table" v-if="nodeTitleType=='set'">
          <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="活动名称">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="活动区域">
    <el-select v-model="form.region" placeholder="请选择活动区域">
      <el-option label="区域一" value="shanghai"></el-option>
      <el-option label="区域二" value="beijing"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="活动时间">
    <el-col :span="11">
      <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-time-picker type="fixed-time" placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
    </el-col>
  </el-form-item>
  <el-form-item label="即时配送">
    <el-switch v-model="form.delivery"></el-switch>
  </el-form-item>
  <el-form-item label="活动性质">
    <el-checkbox-group v-model="form.type">
      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
      <el-checkbox label="地推活动" name="type"></el-checkbox>
      <el-checkbox label="线下主题活动" name="type"></el-checkbox>
      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源">
    <el-radio-group v-model="form.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item>
  <el-form-item label="活动形式">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="nodeTitleType='button'">立即创建</el-button>
    <el-button>取消</el-button>
  </el-form-item>
</el-form>
        </div>
        
        <div class="node_table" v-if="nodeTitleType=='button'">
            <el-table :data="nodeTableData" stripe style="width: 100%">
                <el-table-column prop="id" label="id" width="180">
                </el-table-column>
                <el-table-column prop="name" label="名称" width="180">
                </el-table-column>
                <el-table-column prop="neighbor" label="邻近节点">
                </el-table-column>
                <el-table-column prop="price" label="到达邻近节点耗费资金">
                </el-table-column>
            </el-table>
        </div>
      </div> 
    </div>
</template>
<script>
export default {
    name: 'Exam1',
    methods: {
        onSearch() {
            console.log('submit!');
        }
    },
    data() {
        return {
          form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
            formInline: {
                user: '',
                region: ''
            },
            wuliuTableData: [{
                id: 1,
                name: '苹果',
                mode:'最短时间物流方案',
                vip:21,
                destination: '上海市普陀区金沙江路 1518 弄',
                path:'上海-北京-成都',
                waittime:234,
                status:'正在路上'
            }, {
                id: 1,
                name: '苹果',
                mode:'最短时间物流方案',
                vip:21,
                destination: '上海市普陀区金沙江路 1518 弄',
                 path:'上海-北京-成都',
                 waittime:234,
                status:'已送达'
            }, {
                id: 1,
                name: '苹果',
                mode:'最短时间物流方案',
                vip:21,
                destination: '上海市普陀区金沙江路 1518 弄',
                 path:'上海-北京-成都',
                 waittime:234,
                status:'正在路上'
            }, {
                id: 1,
                name: '苹果',
                mode:'最短时间物流方案',
                vip:21,
                destination: '上海市普陀区金沙江路 1518 弄',
                 path:'上海-北京-成都',
                 waittime:234,
                status:'未发送'
            }],
             nodeTableData: [{
                id:1,
                name: '北京',
                neighbor:'上海，成都',
                price:'50,100'
               
            }, {
               id:2,
                name: '上海',
                neighbor:'上海，成都',
                price:'50,100'
            }, {
               id:3,
                name: '成都',
               neighbor:'上海，成都',
                price:'50,100'
            }, {
               id:4,
                name: '深圳',
                neighbor:'上海，成都',
                price:'50,100'
            }],
            productTitleType: 'button',
            nodeTitleType: 'button',
        }
    }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.table_title {
    font: 18px large;
    font-family: "PingFang SC";
    padding-left: 300px;
    /*margin-top: 20px*/
}
/*.part1 .part2{
  width: 85%;
  margin-left: 7.5%;
}*/
/*.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }*/
</style>