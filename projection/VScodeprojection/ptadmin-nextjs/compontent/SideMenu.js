import "antd/dist/antd.css";
import styles from "../styles/SideMenu.module.css";
import {
  AppstoreOutlined,
  MailOutlined,
  SettingOutlined,
} from "@ant-design/icons";
import { Menu } from "antd";
import { useRouter } from "next/router";

function getItem(label, key, icon, children, type) {
  return {
    key,
    icon,
    children,
    label,
    type,
  };
}

const items = [
  getItem("用户管理", "sub1", <MailOutlined />, [
    getItem("用户列表", "/Users"),
  ]),
  getItem("权限管理", "sub2", <AppstoreOutlined />, [
    getItem("权限列表", "/Powers"),
    getItem("内容列表", "/JobControl"),
  ]),
];

const SideMenu = () => {
  const onClick = (e) => {
    console.log("click ", e);
    router.push(e.key);
  };
  const router = useRouter();
  return (
    <Menu
      className={styles.menu}
      onClick={onClick}
      style={{
        width: 256,
      }}
      defaultSelectedKeys={["/Users"]}
      defaultOpenKeys={["sub1"]}
      mode="inline"
      items={items}
    />
  );
};

export default SideMenu;
