# 前端面试题（Vue篇）

### 1. vue核心插件和工具有哪些

1. vue-cli：构建项目
2. vue-router：路由控制
3. vuex：状态管理
4. nuxt.js：vue服务器渲染

### 1. 说说Vue的双向数据绑定原理

vue的双向数据绑定是基于Object.defineProperty方法实现的，此方法用法如下：

``` js
let obj = {
    title:"old value"
};
Object.defineProperty(obj,"title",{
    get(){
        console.log("调用get方法");
        return "new value"; //返回属性值，没有返回则属性值为undefined
    },
    set(value){//value为设置的属性值
        console.log(`调用了set方法，值为${value}`) 
    }
})
obj.title = "hello world" //执行set
console.log(obj.title); //执行get，获取"new value"（而不是old value）
```



### 2. 组件间传值有哪些方法

1. 父级组件传递给子级组件：属性
2. 子级组件传递给父级组件：自定义事件
3. 非父子级组件传递数据：自定义store或使用vuex

### 3. 为什么要使用vuex

随着应用功能的增加，组件传值会提升项目复杂度，使用vuex可以将公共的数据统一交由vuex定义的state来管理，方便数据传递。但是引入vuex同样也会增加项目的复杂度，所以是否使用vuex，取决于开发者如何衡量传递数据的项目复杂度和引入vuex增加的项目复杂度。

### 4. Vue全家桶有哪些

1. vue-cli
2. vue-router
3. vuex

### 5. vue导航守卫的方法是什么，有哪些参数，为什么要使用路由守卫。

``` js
router.beforeEach((to, from, next) => {
  // ...
})
```

1. to：即将要进入的目标
2. from：当前导航正要离开的路由
3. next：一定要调用这个方法才能实现页面的跳转，可以通过参数指定挑战后的路径。

### 6. v-for为什么要加key

### 7. 什么是虚拟DOM

### 8. Vue的data为什么是一个函数

### 9. v-model我再一个fanction中修改了两次，会比较多少次。

### 10. 改了两次之后，页面会显示第一个值然后跳转到第二个值，还是直接显示第二个值。

### 11. keeplive切换，mounted函数会触发吗？

### 12. computed和watch的区别

### 13. 描述一下组件的声明周期

### 14. store是如何实现更新的

### 15. 用v-for渲染数组，数组长度为5，改变数组第一个元素，页面数据会更新吗？如果使用push方法，页面数据会更新吗？如果用一个数组长度为2的数字去覆盖此数组，页面数据会更新吗？

### 16. Vue的生命周期中的beforeCreated可以调用this里面的数据吗？

### 17. Vue的生命周期中的beforeDestory可以条用this里面的数据吗？beforeDestory看到的是当前的页面还是跳转之后的页面。

### 18. ref拿到的dom和GetElementById拿到的DOM有什么区别？

### 19. Vue中有哪些时间修饰符，作用分别是什么？

### 20. v-if和v-show有什么区别，哪一个会触发mounted

### 21. vue-loader是什么，有什么用途。

### 22. $nextTick是什么

### 23. scss是什么，如何在vue中使用scss。

### 24. vue如何监听对象或者数组中某个属性的变化。

### 26. vuex有哪些核心属性，分别是什么？

### 27. 在v-model中如何使用vuex中state的值。

### 28. mutation和action有什么区别

### 29. 如何定义动态路由，如何传递动态参数

### 30. router和route的区别

### 31. vue.config.js中的常用配置有哪些

