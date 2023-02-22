import { defineStore } from "pinia";

export const useIndexStore = defineStore("index", {
  state: () => {
    return {
      menuIndex: "/document",
    };
  },
  persist: {
    storage: window.sessionStorage,
  },
});
