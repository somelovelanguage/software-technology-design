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
                                        <el-select v-model="formInline.mode" placeholder="物流方案类型">
                                            <el-option label="时间最短方案" value="shanghai"></el-option>
                                            <el-option label="价格最低方案" value="beijing"></el-option>
                                        </el-select>
                                    </el-form-item>
                                    <el-form-item>
                                        <el-button type="primary" @click="onSearch">查询</el-button>
                                    </el-form-item>
                                    <el-button @click="productTitleType='add' " >添加</el-button>
                                    <el-button @click="productTitleType='del'" >删除</el-button>
                                    <el-button @click="productTitleType='change'" >修改</el-button>
                                    <el-button icon="el-icon-sort-down" @click="sortProducts()">综合排序</el-button>
                                    <el-button>立即发送</el-button>
                                </el-form>
                            </div>
                        </div>
                    </el-col>
                </el-row>
            </div>
            <div class="add" v-if="productTitleType=='add'">
                <el-form :inline="true" :model="formInline" class="demo-form-inline">
                    
                    <el-form-item label="wait_time">
                        <el-input v-model="formInline.waittime" placeholder="wait_time"></el-input>
                    </el-form-item>
                    <el-form-item label="mode">
                        <el-input v-model="formInline.mode" placeholder="mode"></el-input>
                    </el-form-item>
                    <el-form-item label="vip">
                        <el-input v-model="formInline.vip" placeholder="vip"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="productTitleType='button';addProduct()">确定新增</el-button>
                    </el-form-item>
                </el-form>
            </div>
            <div class="del" v-if="productTitleType=='del'">
                <el-form :inline="true" :model="formInline" class="demo-form-inline">
                    <el-form-item label="id">
                        <el-input v-model="formInline.id" placeholder="id"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="productTitleType='button';delProduct()">确定删除</el-button>
                    </el-form-item>
                </el-form>
            </div>
            <div class="change" v-if="productTitleType=='change'">
                <el-form :inline="true" :model="formInline" class="demo-form-inline">
                    <el-form-item label="id">
                        <el-input v-model="formInline.id" placeholder="id"></el-input>
                    </el-form-item>
                   
                    <el-form-item label="wait_time">
                        <el-input v-model="formInline.waittime" placeholder="wait_time"></el-input>
                    </el-form-item>
                    <el-form-item label="mode">
                        <el-input v-model="formInline.mode" placeholder="mode"></el-input>
                    </el-form-item>
                    <el-form-item label="vip">
                        <el-input v-model="formInline.vip" placeholder="vip"></el-input>
                    </el-form-item>
                    <el-form-item>
                        <el-button type="primary" @click="productTitleType='button';changeProduct">确定修改</el-button>
                    </el-form-item>
                </el-form>
            </div>
            <div class="wuliu_table">
                <el-table :data="nodesData" stripe style="width: 100%">
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
                                    <el-button @click="nodeTitleType='set'; setNodes" >重新建立节点记录表</el-button>
                                </el-form>
                            </div>
                        </div>
                    </el-col>
                </el-row>
            </div>
            <div class="set_table" v-if="nodeTitleType=='set'">
                <el-form :model="dynamicValidateForm" ref="dynamicValidateForm" label-width="100px" class="demo-dynamic">
                    <el-form-item v-for="(domain, index) in dynamicValidateForm.domains" :key="domain.key" :prop="'domains.' + index + '.value'" :rules="{
      required: true, message: '节点名不能为空', trigger: 'blur'
    }">
                        节点名称<el-input v-model="domain.value"></el-input>
                        <el-button @click.prevent="removeDomain(domain)">删除</el-button>
                    </el-form-item>
                    <!-- 路径start -->
                    <el-form-item v-for="(path, index) in dynamicValidateForm.paths" :key="path.key" :prop="'paths.' + index + '.value'" :rules="{
      required: true, message: '不能为空', trigger: 'blur'
    }">
                        路径起点<el-input v-model="path.start"></el-input>
                        路径终点<el-input v-model="path.end"></el-input>
                        路径耗费时间<el-input v-model="path.time"></el-input>
                        路径耗费资金<el-input v-model="path.price"></el-input>
                        <el-button @click.prevent="removePath(path)">删除</el-button>
                    </el-form-item>
                    <!-- 路径end -->
                    <el-form-item>
                        <el-button type="primary" @click="submitForm('dynamicValidateForm')">提交</el-button>
                        <el-button @click="addDomain">新增节点</el-button>
                        <el-button @click="addPath">新增路径</el-button>
                        <el-button @click="resetForm('dynamicValidateForm')">重置</el-button>
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
                    <el-table-column prop="time" label="到达邻近节点耗费时间">
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
    created: function() {
        //request for nodetable
        console.log('created');
        this.getNodes();

    },
    methods: {
        addProduct() {
            this.$http.request({
                method: 'post',
                url: '/api/products',
                data:{

                }
            }).then(response => {
              console.log(response)
            }

            )
        },
        sortProducts(){
          this.$http.request({
                method: 'get',
                url: '/api/products'
            }).then(response => {
              console.log(response)
            }

            )
        },
        changeProduct() {
            this.$http.request({
                method: 'put',
                url: '/api/product',
                data:{
                  'id':this.formInline.id
                }
            }).then(response => {
              console.log(response)
            }

            )
        },
        delProduct() {
          console.log('del')
          // console.log(typeof(this.formInline.id))
            this.$http.request({
                method: 'delete',
                url: '/api/product',
                data:{
                  'id':this.formInline.id
                }
            }).then(response => {
              console.log(response)
            }

            )
        },
        getNodes() {
            this.$http.request({
                method: 'get',
                url: '/api/nodes'
            }).then(response => {if (response.length == 0) console.log('未建立节点表');
                else {
                    this.nodesData = response;
                }}
                
            )
        },
        setNodes() {
            this.$http.request({
                method: 'post',
                url: '/api/nodes',
                data: {

                }
            }).then(response => {if (response.status == 'success') {
                    console.log('建立节点表成功');
                    this.getNodes();

                } else {
                    console.log('建立节点表失败');
                }}
                
            )

        },
        onSearch() {
            console.log('submit!');
        },
        submitForm(formName) {
            this.$refs[formName].validate((valid) => {
                if (valid) {
                    alert('submit!');
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
        },
        removeDomain(item) {
            var index = this.dynamicValidateForm.domains.indexOf(item)
            if (index !== -1) {
                this.dynamicValidateForm.domains.splice(index, 1)
            }
        },
        removePath(item) {
            var index = this.dynamicValidateForm.paths.indexOf(item)
            if (index !== -1) {
                this.dynamicValidateForm.paths.splice(index, 1)
            }
        },
        addDomain() {
            this.dynamicValidateForm.domains.push({
                value: '',
                key: Date.now()
            });
        },
        addPath() {
            this.dynamicValidateForm.paths.push({
                value: '',
                key: Date.now()
            });
        }
    },
    data() {
        return {
           formInline: {
          name: '',
          vip: '',
          id:'',
          waittime:'',
          mode:'',
          
        },
            dynamicValidateForm: {
                domains: [{
                    value: ''
                }],
                paths: [{
                    start: '',
                    end: '',
                    time: '',
                    price: ''
                }],

            },
           
            
            nodesData: [{
                id: 1,
                name: '苹果',
                mode: '最短时间物流方案',
                vip: 21,
                destination: '上海市普陀区金沙江路 1518 弄',
                path: '上海-北京-成都',
                waittime: 234,
                status: '正在路上'
            }, {
                id: 1,
                name: '苹果',
                mode: '最短时间物流方案',
                vip: 21,
                destination: '上海市普陀区金沙江路 1518 弄',
                path: '上海-北京-成都',
                waittime: 234,
                status: '已送达'
            }, {
                id: 1,
                name: '苹果',
                mode: '最短时间物流方案',
                vip: 21,
                destination: '上海市普陀区金沙江路 1518 弄',
                path: '上海-北京-成都',
                waittime: 234,
                status: '正在路上'
            }, {
                id: 1,
                name: '苹果',
                mode: '最短时间物流方案',
                vip: 21,
                destination: '上海市普陀区金沙江路 1518 弄',
                path: '上海-北京-成都',
                waittime: 234,
                status: '未发送'
            }],
            nodeTableData: [{
                id: 1,
                name: '北京',
                neighbor: '上海，成都',
                price: '50,100',
                time: '123,132'

            }, {
                id: 2,
                name: '上海',
                neighbor: '上海，成都',
                price: '50,100',
                time: '123,132'
            }, {
                id: 3,
                name: '成都',
                neighbor: '上海，成都',
                price: '50,100',
                time: '123,132'
            }, {
                id: 4,
                name: '深圳',
                neighbor: '上海，成都',
                price: '50,100',
                time: '123,132'
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

.set_table .el-input {
    margin-left: 10px;
    margin-right: 20px;
    width: 10%;
}
</style>