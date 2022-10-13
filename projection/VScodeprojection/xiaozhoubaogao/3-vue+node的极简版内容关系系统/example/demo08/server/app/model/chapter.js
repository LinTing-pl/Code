module.exports = app => {
    const { STRING,INTEGER } = app.Sequelize; 

    const Chapter = app.model.define('chapter',{
        title:STRING,  
    })
    Chapter.associate = function() {  
        app.model.Chapter.belongsTo(app.model.Book,{
            foreignKey: 'book_id',
            as:'book'
        })
    }
    return Chapter;

}