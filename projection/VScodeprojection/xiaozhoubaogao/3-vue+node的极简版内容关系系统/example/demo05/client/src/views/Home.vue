<template>
    <div>
        <el-upload
            action="http://127.0.0.1:7001/upload"
            list-type="picture-card"
            :limit="3"
            :on-exceed="handleExceed"
            :on-success="success"
            :file-list="fileList"
        >
        <i class="el-icon-plus"></i>
        </el-upload>
    </div>
</template>

<script>
export default {
    data() {
        return {
            // 初始化照片数据，用于数据修改
            fileList: [
                {
                    name: "name",
                    url:"http://127.0.0.1:7001/uploads/1601346176222.jpg",
                }
            ],
        };
    },
    methods: {
        handleExceed(files, fileList) {
            this.$message.warning("只能上传一张图片！");
        },
        success(res){
            console.log(res.data.file);
        }
    },
};
</script>