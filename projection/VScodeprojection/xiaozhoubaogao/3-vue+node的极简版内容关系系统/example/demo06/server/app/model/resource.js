module.exports = app => {
    const { STRING } = app.Sequelize;

    const Resource = app.model.define('resource',{
        title:STRING,  //标题
        code:STRING,   //提取码
        imgurl:STRING, //图片地址
        downloadurl:STRING //下载地址
    })
    
    return Resource
}