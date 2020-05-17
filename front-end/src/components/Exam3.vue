<template>
    <div id="exam">
        <el-row>
            <el-col :span="9" style="margin-left: 30px">
                <div class="grid-content bg-purple">
                    <div class="sql" >
                        <p>在此执行sql语句</p>
                        <el-input type="textarea" :autosize="{ minRows: 10, maxRows: 20}" placeholder="请输入内容" v-model="textarea2">
                        </el-input>
                        <div style="margin-top: 10px"> <el-button type="primary" @click="onSubmit">立即执行</el-button>
                        <el-button>取消</el-button></div>
                        
                    </div>
                </div>
            </el-col>
            <el-col :span="12">
                <div class="grid-content bg-purple-light"></div>
            </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
    name: 'Exam3',
    data() {
        return {
            textarea2: '',

        }
    }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>