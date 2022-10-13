module.exports = app => {
    const { STRING,INTEGER,TEXT } = app.Sequelize; 

    const Section = app.model.define('section',{
        title:STRING,      
        orderby:INTEGER,      
        md_text:TEXT,       
        html_text:TEXT,       
        
    })
    Section.associate = function() {  //所属与那本书，指向书籍的主键
        app.model.Section.belongsTo(app.model.Chapter,{
            foreignKey: 'chapter_id',
            as:'chapter'
        })
    }

    return Section;
}