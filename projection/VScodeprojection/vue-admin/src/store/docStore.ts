import { defineStore } from "pinia";
export const useDocStore = defineStore("doc", {
  state: () => {
    return {
      docList: [
        {
          id: 6,
          title: "愿",
          content:
            "“愿你在二十岁的人生里听一个月的歌\n看三个月的书睡四个月的觉\n做四个月的梦怀揣着一辈子的梦想\n依旧闪闪发光”",
        },
        {
          id: 5,
          title: "祝福",
          content:
            "愿你一生努力 ，一生被爱 ，想要的都拥有 ，得不到的都释怀，只愿你被这世界温柔相待",
        },
        { id: 4, title: "未来", content: "万千不舍，离别祝好，未来一帆风顺！" },
        { id: 3, title: "祝", content: "祝，春生夏明朗，秋祺冬瑞康。" },
        {
          id: 2,
          title: "希望",
          content:
            "希望你每天早晨起来，整个世界都是一份打开的、闪闪发光的巨大礼物。",
        },
        {
          id: 1,
          title: "望",
          content: "所有人都祝你快乐，我只愿你历经山河觉得人间值得",
        },
      ],
    };
  },
  actions: {
    add(data: any) {
      data["id"] = this.docList[0].id + 1;
      this.docList.unshift(data);
    },
    delete(id: any) {
      let index = this.docList.findIndex((v) => v.id === id);
      this.docList.splice(index, 1);
    },
    update(data: any) {
      this.docList = data;
    },
  },
  persist: true,
});
