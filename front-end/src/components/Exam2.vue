<template>
    <div id="exam">
        <div class="title">选择你的操作吧！(#^.^#)</div>
        <div v-show="isImg==1"><img src="../assets/8.gif"></div>
        <div v-show="isImg==0">
            <el-table :data="tableData" stripe style="width: 100%">
                <el-table-column prop="date" label="日期" width="180">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="180">
                </el-table-column>
                <el-table-column prop="address" label="地址">
                </el-table-column>
            </el-table>
        </div>
        <div class="foot">
            <div class="top">
                <el-select v-model="value" placeholder="请选择">
                    <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
                <el-button style="margin-left:10px; " @click="isImg=0">查看此表</el-button>
                <el-input v-model="input" placeholder="请输入关键字"></el-input>
                <el-button @click="isImg=0">简单查询</el-button>
                <el-input v-model="input" placeholder="请输入索引"></el-input>
                <el-input v-model="input"  style="margin-left:0" placeholder="请输入关键字"></el-input>
                <el-button @click="isImg=0" >索引查询</el-button>
                <el-button type="primary" @click="isImg=1">结束当前操作</el-button>
            </div>
            <div class="bottom">
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
                        <el-button plain @click="open3" type="primary">确定新增</el-button>
                    </el-form-item>
                </el-form>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Exam2',
    data() {
        return {
            tableData: [{
                date: '2016-05-02',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1518 弄'
            }, {
                date: '2016-05-04',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1517 弄'
            }, {
                date: '2016-05-01',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1519 弄'
            }, {
                date: '2016-05-03',
                name: '王小虎',
                address: '上海市普陀区金沙江路 1516 弄'
            }],
            isImg: 1,
            formInline: {
                name: '',
                vip: '',
                id: '',
                waittime: '',
                mode: '',

            },
            input: '',
            options: [{
                value: '选项1',
                label: '黄金糕'
            }, {
                value: '选项2',
                label: '双皮奶'
            }, {
                value: '选项3',
                label: '蚵仔煎'
            }, {
                value: '选项4',
                label: '龙须面'
            }, {
                value: '选项5',
                label: '北京烤鸭'
            }],
            value: ''

        }
    },
    methods: {
        open3() {
            if (this.isImg == 1) {
                this.$notify({
                    title: '成功',
                    message: '这是一条成功的提示消息',
                    type: 'success'
                });
            } else {
                this.$notify({
                    title: '警告',
                    message: '这是一条警告的提示消息',
                    type: 'warning'
                });
            }

        },
        addTab() {
            let newTabName = ++this.tabIndex + '';
            this.editableTabs2.push({
                title: 'New Tab',
                name: newTabName,
                content: ''
            });
            this.editableTabsValue2 = newTabName;
        },
        removeTab(targetName) {
            let tabs = this.editableTabs2;
            let activeName = this.editableTabsValue2;
            if (activeName === targetName) {
                tabs.forEach((tab, index) => {
                    if (tab.name === targetName) {
                        let nextTab = tabs[index + 1] || tabs[index - 1];
                        if (nextTab) {
                            activeName = nextTab.name;
                        }
                    }
                });
            }

            this.editableTabsValue2 = activeName;
            this.editableTabs2 = tabs.filter(tab => tab.name !== targetName);
        },
        onClick() {
            console.log('touch')
        }

    }

}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#exam {
    margin-top: 40px;
    text-align: center;
}

.title {

    font: 50px Extra large;
    font-family: "PingFang SC";

}

.el-input {

    margin-right: 10px;
}

.top {
    margin-bottom: 20px;
}

.top .el-input {
    width: 10%;
    margin-left: 30px;
}


</style>