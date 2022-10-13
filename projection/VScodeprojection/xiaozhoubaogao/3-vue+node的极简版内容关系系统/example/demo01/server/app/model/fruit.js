module.exports = app => {
    const { STRING } = app.Sequelize;

    const Fruit = app.model.define('fruit',{
        name:STRING
    })
    
    return Fruit
}