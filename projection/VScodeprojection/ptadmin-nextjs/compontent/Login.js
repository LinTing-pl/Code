import styles from "../styles/Login.module.css";
import { useState } from "react";
import axios from "axios";
import { useRouter } from "next/router";

export default function Login(props) {
  function login(username, password) {
    axios
      .post("/dev-api/login", {
        username,
        password,
      })
      .then((success) => {
        if (success.data.code === 200) {
          router.push("./Home");
        }
      });
  }
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("123456");
  const router = useRouter();
  return (
    <div className={styles.main}>
      <div className={styles.loginbox}>
        <div className={styles.tit}>登陆</div>
        <input
          type="text"
          placeholder="账号"
          value={username}
          onChange={(e) => {
            setUsername(e.target.value);
          }}
        />
        <input
          type="password"
          placeholder="密码"
          value={password}
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
        <button onClick={() => login(username, password)}>登陆</button>
        <span>
          没有账号？<a href="#">去注册</a>
        </span>
      </div>
      <div className={styles.square}>
        <ul>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
      <div className={styles.circle}>
        <ul>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
          <li></li>
        </ul>
      </div>
    </div>
  );
}
