import styles from "../styles/Main.module.css";
import SideMenu from "./SideMenu";
import { createMemoryHistory } from "history";
import Users from "./Users";

export default function Main() {
  return (
    <div className={styles.main}>
      <SideMenu></SideMenu>
      <Users></Users>
    </div>
  );
}
