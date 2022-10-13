module.exports = app => {
    const { STRING } = app.Sequelize;

    const Video = app.model.define('video',{
        title:STRING,
        iframe:STRING
    })
    
    return Video
}