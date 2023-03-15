import introJs from "intro.js";
import "intro.js/introjs.css";

const intro = introJs();
// 更多配置参数请到官方文档查看
intro.setOptions({
  nextLabel: "下一个", // 下一个按钮文字
  prevLabel: "上一个", // 上一个按钮文字
  skipLabel: "跳过", // 跳过按钮文字
  doneLabel: "完成", // 完成按钮文字
  hidePrev: true, // 在第一步中是否隐藏上一个按钮
  hideNext: true, // 在最后一步中是否隐藏下一个按钮
  exitOnOverlayClick: false, // 点击叠加层时是否退出介绍
  showStepNumbers: false, // 是否显示红色圆圈的步骤编号
  disableInteraction: true, // 是否禁用与突出显示的框内的元素的交互，就是禁止点击
  showBullets: true, // 是否显示面板指示点
});

export default intro;
