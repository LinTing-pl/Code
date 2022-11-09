<template>
  <div class="con">
    <div
      class="chapter"
      @click="toggleActive($event)"
      v-for="(item, index) in list"
      :key="index"
      :title="item.chapter"
    >
      <span
        :class="{ 'chapter-title': true, active: index === chapterIndex }"
        >{{ item.chapter }}</span
      >
      <div class="sections">
        <div
          :class="{
            section: true,
            active2: index === chapterIndex && index2 === sectionIndex,
          }"
          v-for="(item2, index2) in item.sections"
          :key="index2"
          :title="item2.section"
          @click="
            sectionActive($event);
            toStudySrc(item2.section, item2.content, index, index2);
          "
        >
          {{ item2.section }}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      chapterIndex: 0,
      sectionIndex: 0,
    };
  },
  props: ["list"],
  mounted() {
    let id = this.$route.params.id;
    if (sessionStorage.getItem(`chapterIndex${id}`) !== null) {
      this.chapterIndex =
        parseInt(sessionStorage.getItem(`chapterIndex${id}`)) || 0;
      this.sectionIndex =
        parseInt(sessionStorage.getItem(`sectionIndex${id}`)) || 0;
    }
  },
  updated() {
    document.getElementsByClassName("active2")[0].click();
  },

  methods: {
    toggleActive(e) {
      e.target.classList.toggle("active");
    },
    sectionActive(e) {
      let sections = e.path[3].querySelectorAll(".section");
      sections.forEach((section) => {
        section.classList.remove("active2");
      });
      e.target.className = "section active2";
    },
    toStudySrc(title, content, index1, index2) {
      this.$emit("putBookcontent", { title: title, content: content });
      let id = this.$route.params.id;
      sessionStorage.setItem(`sectionIndex${id}`, index2.toString());
      sessionStorage.setItem(`chapterIndex${id}`, index1.toString());
    },
  },
};
</script>
<style lang='scss' scoped>
.con {
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  user-select: none;
}
.chapter {
  position: relative;
  display: flex;
  flex-direction: column;
  cursor: pointer;
}
.chapter-title {
  font-weight: bold;
  position: relative;
  font-size: 18px;
  padding: 10px 0;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}
.chapter-title::before {
  content: ">";
  margin-right: 10px;
  display: inline-block;
  transition: all 0.3s;
}
.chapter-title.active::before {
  transform: rotate(90deg);
}
.sections {
  display: none;
}
.section {
  padding: 5px 10px 5px 40px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  color: #9b9b9b;
}
.chapter-title.active ~ .sections {
  display: block;
}
.section.active2 {
  color: #58a6ff;
}
</style>
