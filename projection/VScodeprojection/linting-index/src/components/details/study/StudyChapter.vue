<template>
  <div class="studychapter-container">
    <div
      class="chapter"
      v-for="(item, index) in list"
      :key="index"
      :title="item.chapter"
    >
      <span
        ref="chapter"
        @click="toggleActive(index)"
        :class="{ 'chapter-title': true, active: index === chapterIndex }"
        >{{ item.chapter }}</span
      >
      <div class="sections" ref="sections">
        <div
          ref="section"
          :class="{
            section: true,
            active: index === chapterIndex && index2 === sectionIndex,
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
  created() {
    let id = this.$route.params.id;
    if (sessionStorage.getItem(`chapterIndex${id}`)) {
      this.chapterIndex = parseInt(sessionStorage.getItem(`chapterIndex${id}`));
      this.sectionIndex = parseInt(sessionStorage.getItem(`sectionIndex${id}`));
    }
  },
  mounted() {
    this.$refs.sections[this.chapterIndex].children[this.sectionIndex].click();
    this.$refs.sections[this.chapterIndex].style.height =
      33 * this.$refs.sections[this.chapterIndex].children.length + "px";
  },
  methods: {
    toggleActive(index) {
      this.$refs.chapter[index].classList.toggle("active");
      if (this.$refs.chapter[index].classList.contains("active")) {
        this.$refs.sections[index].style.height =
          33 * this.$refs.sections[index].children.length + "px";
      } else {
        this.$refs.sections[index].style.height = 0;
      }
    },
    sectionActive(e) {
      e.stopPropagation();
      this.$refs.section.forEach((section) => {
        section.classList.remove("active");
      });
      e.target.className = "section active";
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
.studychapter-container {
  width: 212px;
  display: flex;
  flex-direction: column;
  background-color: #fff;
  user-select: none;
  margin-bottom: 10px;
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
  transition: transform 0.3s;
}
.chapter-title.active::before {
  transform: rotate(90deg);
}
.sections {
  height: 0;
  overflow: hidden;
  transition: all 0.5s ease;
}
.section {
  height: 33px;
  line-height: 33px;
  padding: 0px 10px 0px 40px;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
  color: #9b9b9b;
}
.section.active {
  color: #58a6ff;
}
</style>
