exports.dateformate = time => {
    let date = new Date(time);
    let year = date.getFullYear();
    let month = date.getMonth()+1;
    let day = date.getDate();
    let result = `${year}年${month}月${day}日`;
    return result
};

