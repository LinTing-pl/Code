<template>
  <div class="emoji">
    <i class="icon iconfont icon-look" @click="value = !value"></i>
    <div class="emojiBox" v-show="value">
      <li
        @click="handleEmojiClick(emoji.code)"
        v-for="emoji in emojis"
        :key="emoji.code"
      >
        <img
          :src="'/images/emoji/' + emoji.file"
          :data="emoji.code"
          :title="emoji.title"
        />
      </li>
    </div>
  </div>
</template>
<script>
export default {
  props: ["modelValue"],
  emits: ["update:modelValue", "update-code"],
  computed: {
    value: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit("update:modelValue", value);
      },
    },
    emojis() {
      return this.state.emojis;
    },
  },
  methods: {
    handleEmojiClick(code) {
      this.$emit("update-code", code);
    },
  },
};
</script>
<style lang='scss' scoped>
</style>