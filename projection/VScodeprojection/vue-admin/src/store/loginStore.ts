import { defineStore } from "pinia";

export const useLoginStore = defineStore("login", {
  state: () => {
    return {
      flag: false,
    };
  },
  actions: {
    login(account: string, psw: string) {
      if (account === "admin" && psw === "123456") {
        this.flag = true;
        return true;
      } else {
        return false;
      }
    },
    exit() {
      this.flag = false;
    },
  },
  persist: true,
});
