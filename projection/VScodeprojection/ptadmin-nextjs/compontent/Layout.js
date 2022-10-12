import mainstyles from "../styles/Main.module.css";
import Nav from "./Nav";
import SideMenu from "./SideMenu";
export default function Layout({ children }) {
  return (
    <div>
      <Nav></Nav>
      <div className={mainstyles.main}>
        <SideMenu></SideMenu>
        {children}
      </div>
    </div>
  );
}
