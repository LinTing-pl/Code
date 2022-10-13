module.exports = app => {
    const { STRING, INTEGER } = app.Sequelize; 

    const Book = app.model.define('book',{
        title:STRING,  
        orderby:INTEGER,  
        img:STRING, 
    })

    return Book;

}