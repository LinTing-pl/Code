import { defineStore } from "pinia";

export const useColorStore = defineStore("color", {
  state: () => {
    return {
      layoutE: null,
      layoutColor: "#f7f8fa",
      menuE: null,
      menuColor: "#545c64",
      pageHeaderE: null,
      pageHeaderColor: "#ffffff",
      setting1E: null,
      setting1Color: "#ffffff",
      setting2E: null,
      setting2Color: "#ffffff",
      setting3E: null,
      setting3Color: "#ffffff",
      setting4E: null,
      setting4Color: "#ffffff",
      setting5E: null,
      setting5Color: "#ffffff",
      setting6E: null,
      setting6Color: "#ffffff",
      setting7E: null,
      setting7Color: "#ffffff",
      setting8E: null,
      setting8Color: "#ffffff",
      setting9E: null,
      setting9Color: "#ffffff",
    };
  },
  actions: {
    changeColor(cls: String, c: any) {
      let E: any = null;
      if (!!c) {
        switch (cls) {
          case "layout":
            this.layoutColor = c;
            break;
          case "menu":
            this.menuColor = c;
            break;
          case "pageHeader":
            this.pageHeaderColor = c;
            break;
          case "setting1":
            this.setting1Color = c;
            break;
          case "setting2":
            this.setting2Color = c;
            break;
          case "setting3":
            this.setting3Color = c;
            break;
          case "setting4":
            this.setting4Color = c;
            break;
          case "setting5":
            this.setting5Color = c;
            break;
          case "setting6":
            this.setting6Color = c;
            break;
          case "setting7":
            this.setting7Color = c;
            break;
          case "setting8":
            this.setting8Color = c;
            break;
          case "setting9":
            this.setting9Color = c;
            break;
        }
      }
      let color = null;
      switch (cls) {
        case "layout":
          E = this.layoutE;
          color = this.layoutColor;
          break;
        case "menu":
          E = this.menuE;
          color = this.menuColor;
          break;
        case "pageHeader":
          E = this.pageHeaderE;
          color = this.pageHeaderColor;
          break;
        case "setting1":
          E = this.setting1E;
          color = this.setting1Color;
          break;
        case "setting2":
          E = this.setting2E;
          color = this.setting2Color;
          break;
        case "setting3":
          E = this.setting3E;
          color = this.setting3Color;
          break;
        case "setting4":
          E = this.setting4E;
          color = this.setting4Color;
          break;
        case "setting5":
          E = this.setting5E;
          color = this.setting5Color;
          break;
        case "setting6":
          E = this.setting6E;
          color = this.setting6Color;
          break;
        case "setting7":
          E = this.setting7E;
          color = this.setting7Color;
          break;
        case "setting8":
          E = this.setting8E;
          color = this.setting8Color;
          break;
        case "setting9":
          E = this.setting9E;
          color = this.setting9Color;
          break;
      }
      E.style.backgroundColor = color;
    },
  },
  persist: true,
});
