<template>
    <div id="exam">
        <el-row>
            <el-col :span="2">
                <div class="grid-content bg-purple">
                    <div class="navigation">
                        <div style="margin-bottom: 20px;">
                            <el-button size="small" @click="addTab(editableTabsValue2)">
                                新增表
                            </el-button>
                        </div>
                        <el-tabs v-model="editableTabsValue2" type="card" closable @tab-remove="removeTab" tab-position="left" @tab-click="onClick">
                            <el-tab-pane v-for="item in editableTabs2" :key="item.name" :label="item.title" :name="item.name">
                                {{item.content}}
                            </el-tab-pane>
                        </el-tabs>
                    </div>
                </div>
            </el-col>
            <el-col :span="22">
                <div class="grid-content bg-purple-light">
                    <div class="table">
                        <el-table :data="tableData" border style="width: 100%">
                            <el-table-column prop="date" label="日期" width="180">
                            </el-table-column>
                            <el-table-column prop="name" label="姓名" width="180">
                            </el-table-column>
                            <el-table-column prop="address" label="地址">
                            </el-table-column>
                        </el-table>
                    </div>
                </div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
    name: 'Exam2',
    data() {
        return {
            editableTabsValue2: '2',
            editableTabs2: [{
                title: 'sheet 1',
                name: '1',
                content: ''
            }, {
                title: 'sheet 2',
                name: '2',
                content: ''
            }],
            tabIndex: 2,
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
            }]

        }
    },
    methods: {
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
#exam{
    margin-top: 40px;
}
</style>