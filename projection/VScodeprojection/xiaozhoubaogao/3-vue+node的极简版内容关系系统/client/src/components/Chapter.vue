<template>
    <div>
        <el-button type="btn" @click="cheateChapter">添加章</el-button>
        <el-table :data="chapterList" border>
            <el-table-column align="center" width="100" label="序号" type="index"></el-table-column>
            <el-table-column prop="title" label="姓名"></el-table-column>
            <el-table-column label="详情" width="100">
                <template slot-scope="scope">
                    <el-button @click="getDetail(scope.row.id)" type="text" size="small">查看小节</el-button>
                </template>
            </el-table-column>
            <el-table-column label="操作" width="200">
                <template slot-scope="scope">
                    <el-button @click="updateChapter(scope.row.id,scope.row.title,scope.row.orderby)" type="text" size="small">编辑</el-button>
                    <el-button @click="deleteChapter(scope.row.id)" type="text" size="small">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-dialog title="添加" :visible.sync="dialogVisible" width="30%">
            <el-form>
                <el-form-item label="标题">
                    <el-input v-model="title"></el-input>
                </el-form-item><el-form-item label="权重">
                    <el-input v-model="orderby"></el-input>
                </el-form-item>
            </el-form>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="save">确 定</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script>
import request from "../utils/request"
export default {
    methods: {
        getDetail(id){
            this.$router.push(`/section?chapter_id=${id}`)
        },
        save() {
            if(this.isEdit){
                request
                .put(`/chapter/${this.updateId}`, {title:this.title,book_id:this.book_id,orderby:this.orderby})
                .then(() => {
                    this.getChapterList();
                    this.dialogVisible = false;
                });
            }else{
                request
                .post(`/chapter`, {title:this.title,book_id:this.book_id,orderby:this.orderby})
                .then(() => {
                    this.getChapterList();
                    this.dialogVisible = false;
                });
            }
            
        },
        cheateChapter(){
            this.dialogVisible = true;
            this.title = "";
            this.isEdit = false;
            this.orderby = ""
        },
        deleteChapter(id) {
            this.$confirm("此操作将永久删除该文件, 是否继续?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning"
            })
                .then(() => {
                    request
                        .delete(`/chapter/${id}`)
                        .then(() => {
                            this.$message({
                                type: "success",
                                message: "删除成功!"
                            });
                            this.getChapterList();
                        });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除"
                    });
                });
        },
        updateChapter(id,title,orderby){
            this.dialogVisible = true;
            this.title = title;
            this.isEdit = true;
            this.updateId = id;
            this.orderby = orderby;
        },
        getChapterList() {
            // let id = this.$route.params.id;
            request
                .get(`/chapter?book_id=${this.book_id}`)
                .then(res => {
                    this.chapterList = res.data.data;
                });
        },
    },

    data() {
        return {
            chapterList: [],
            dialogVisible: false,
            title:"",
            isEdit:false,
            updateId:0,
            orderby:"",
        };
    },
    computed:{
        book_id(){
            return this.$route.query.book_id;
        }
    },
    created() {
        
        this.getChapterList();
    }
};
</script>

