import Mock from "mockjs";

// 例1
Mock.mock("/author/get", function () {
  return Mock.mock({
    success: true,
    msg: "",
    obj: {
      account_name: "@name",
      "gender|1": ["male", "female"],
      birthday: Mock.Random.datetime("yyyy-MM-dd"),
      address: "a b c d",
    },
    phone: "15019763969",
    name: "Linting",
  });
});
Mock.mock("/upload/upload", function (e) {
  setTimeout(() => {
    return Mock.mock({
      success: true,
      msg: "上传成功",
    });
  }, 5000);
});
