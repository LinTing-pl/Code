const jwt = require("jsonwebtoken");
const path = require("path");
const data = require(path.join(__dirname, "./db.json"));
const express = require("express");
const app = express();
const server = require("http").createServer(app);
const cors = require("cors");
const axios = require("axios");

app.use(cors());
app.use(express.json());
const secret = "12asdf!@#ABCASD234234ad@)(*&";

const httpServer = require("http").createServer(app);
const io = require("socket.io")(httpServer, {
  path: "/mychat",
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});
// 存储在线的用户
const users = [
  {
    id: 10,
    nickname: "大白机器人",
    wxid: "dabai",
    robot: true,
  },
];
// 存储离线消息
// [{ 用户的id:  [{fromId：用户的id, content: '', type: 'user'}] }]
let offLineMsgs = [];

io.on("connection", (socket) => {
  const user = JSON.parse(socket.handshake.query.user);
  console.log(user);
  console.log(user.nickname + "连接成功");
  socket.user = user;
  // 验证token
  jwt.verify(user.token, secret, (err, decode) => {
    if (err) {
      socket.emit("login_error", "Token失效，请重新登录");
    } else {
      users.push({
        ...user,
        socketId: socket.id,
      });

      // 检查有没有发送给当前用户的信息
      let msgs = offLineMsgs.filter((u) => u.to === user.id);
      offLineMsgs = offLineMsgs.filter((u) => u.to !== user.id);
      msgs.forEach((msg) => {
        socket.emit("message", {
          from: msg.from,
          to: msg.to,
          content: msg.content,
          type: msg.type,
        });
      });
    }
  });
  // 接受客户端返回的消息
  socket.on("message", async ({ from, to, content, type }) => {
    // from 发消息人的id
    // to 收消息人的id
    // content 内容
    // type: user 或者group
    console.log(from, to, content, type);
    if (type === "user") {
      // 检查在线用户数组中是否有 to 用户，如果没有的话，把消息存储起来
      const toUser = users.find((u) => u.id === to);
      if (toUser) {
        // 判断是否是机器人
        if (toUser.robot) {
          // 机器人
          const url = "http://openapi.turingapi.com/openapi/api/v2";
          const postData = {
            reqType: 0,
            perception: {
              inputText: {
                text: content,
              },
              selfInfo: {
                location: {
                  city: "河北省",
                  province: "邯郸市",
                  street: "中华路",
                },
              },
            },
            userInfo: {
              apiKey: "25d308027eb147d6b440b78db3d8ab23",
              userId: to,
            },
          };

          const { data } = await axios.post(url, postData);
          socket.emit("message", {
            from: to,
            to: from,
            content: data.results[0].values.text,
            type,
          });
          console.log(data);
        } else {
          // 用户在线
          socket.to(toUser.socketId).emit("message", {
            from,
            to,
            content,
            type,
          });
        }
      } else {
        // 用户不在线
        offLineMsgs.push({
          from: from,
          to: to,
          content: content,
          type: type,
        });
      }
    } else if (type === "group") {
    }
  });

  // 连接断开，删除用户
  socket.on("disconnect", () => {
    const index = users.findIndex((u) => {
      return u.id === socket.user.id;
    });
    users.splice(index, 1);
  });
});

io.on("connection_error", (err) => {
  console.log(err);
});

app.use("/v1", (req, res, next) => {
  if (req.url.startsWith("/login")) return next();
  const token = req.headers["token"];

  if (token) {
    jwt.verify(token, secret, (err, decode) => {
      if (err) {
        return res.json({
          success: false,
          message: "无效的Token",
        });
      } else {
        req.decode = decode;
        next();
      }
    });
  } else {
    return res.json({
      success: false,
      message: "没有找到Token",
    });
  }
});

app.post("/v1/login", (req, res) => {
  const wxid = req.body.wxid;
  const password = req.body.password;

  const users = data.users;
  const user = users.find((v) => v.wxid === wxid);
  if (user) {
    if (password === user.password) {
      // 生产 Token
      const token = jwt.sign(
        {
          nickname: user.nickname,
          wxid: user.wxid,
          id: user.id,
        },
        secret,
        {
          expiresIn: "2h",
        }
      );
      res.json({
        success: true,
        message: "登录成功",
        user: {
          id: user.id,
          nickname: user.nickname,
          wxid: user.wxid,
          icon: user.icon,
          robot: user.robot,
          token: token,
        },
      });
    } else {
      res.json({
        success: false,
        message: "登录失败，密码不正确",
      });
    }
  } else {
    res.json({
      success: false,
      message: "登录失败，用户名不存在",
    });
  }
});

app.get("/v1/friends", (req, res) => {
  const user = req.decode;
  const f = data.friends.find((f) => {
    return f.userId === user.id;
  });

  let friends = [];
  f.friends.forEach((id) => {
    const user = data.users.find((u) => {
      return u.id === id;
    });
    friends.push(user);
    friends.sort((v1, v2) => {
      return v1.letter.charCodeAt(0) - v2.letter.charCodeAt(0);
    });
  });

  let set = new Set(friends.map((u) => u.letter));
  const letters = [...set];

  const tmp = letters.map((l) => {
    const f = friends.filter((f) => f.letter === l);
    return {
      letter: l,
      users: f,
    };
  });

  res.send(tmp);
});

// httpServer.listen(5000, () => {
//   console.log('API Server is running. http://127.0.0.1:5000')
// })

httpServer.listen(process.env.PORT || 5000, "0.0.0.0", () => {
  console.log("API Server is running. http://127.0.0.1:5000");
});
