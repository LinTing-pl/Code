# 前端开发面试题（JavaScript篇）

### 1. JavaScript中有哪些数据类型：

1. 六种数据类型：数值、字符串、布尔、空、未定义、对象
2. 原始类型（基本类型）与引用类型
3. 类型检查（typeof、instranceof）
4. ES5通过构造函数来模拟类的概念，可以通过instranceof来检查
5. ES6可以自定义类（类型），也可以通过instranceof来检查。
6. ES6中新增了synbol类型。

### 2. === 与 == 有什么区别

1. ===必须类型和值都相等，==只比较值，会做类型转换。
2. ===性能更高，推荐使用。

#### 扩展问题

1. 隐式类型转换有哪些
2. 强制类型转换有哪些：Number、String、toString、parseInt、parseFloat。

### 3. 函数声明与函数表达式有什么区别

1. 扩展预解析
2. 扩展变量声明提升

### 4. JavaScript有哪些常用的内置对象

1. Array
2. Date
3. Math
4. RegExp
5. promise

### 5. 数组有哪些常用的方法？

1. push
2. pop
3. shift
4. unshift
5. splice
6. slice
7. join
8. sort：如何实现升序和降序。
9. filter

### 6. 字符串有哪些常用的属性和方法？

1. split
2. replace
3. indexOf
4. toUpperCase()
5. toLowerCase()
6. trim()

### 7. null和undefined的区别是什么。

1. 如果一个变量未赋值，它的值是undefined

2. 如果需要定义一个变量，这个变量应该存储的值是对象，并且当前声明变量的时候，它是没有初始值的，可以将处置室设置为null。

3. 还有一个方法，如果没有返回值，那么值是undefined。但是通常，会将返回值手动设置为 return null。

### 8. new操作符具体做了些什么

1. 创建一个新对象；
2. 将构造函数的作用域赋给新对象（因此 this 就指向了这个新对象） ；
3. 执行构造函数中的代码（为这个新对象添加属性） ；
4. 返回新对象。

### 9. 如何理解this关键字

1. 对象的方法中使用，this指向该对象。
2. 全局函数中的this指向window
3. 构造函数中的this指向new出来的对象实例（同定义类中的方法）
4. 事件处理中的this指向事件源
5. 闭包中的this指向window 
6. 闭包使用箭头函数，避免this指向window。（简单函数中的this取决于函数定义的位置，普通函数的this取决于函数调用的位置）

### 10. 说说call、apply、bind的区别，在开发中如何应用？

call、apply、bind都可以重新指定函数的对象上下文，区别如下所示：

1. 如果函数有多个参数，需要放在apply方法的第二个参数中，第二个参数为数组，使用apply方法，函数直接被调用。
2. 如果函数有多个参数，需要放在call方法的的二个参数及其以后的参数中，并且依次排列，使用call方法，函数直接被调用。
3. bind与call的使用方法类似，给函数传递参数也是从bind的第二个参数开始，依次排列，区别是bind不会直接调用函数，而是将一个改变对象上下文的新函数作为返回值。需要调用的时候再调用。

实际应用：在封装的防抖方法中，使用call将input作为回调函数的上下文对象，当事件触发时，this可以指向input（不适用call，因为是闭包函数，所以this会指向window对象）。

``` js
let input = document.querySelector("input");
function throttle(fn,delay){
    let mark = true;
    return function(){
        if(mark){
            setTimeout(() => {
                fn.call(this);
                mark = true;
            },delay)
        }
        mark = false;
    }
}
input.oninput = throttle(function(){
    console.log(this.value)
},2000)
```



### 11. 如何使用eval，有何有缺点。

可以将字符串

1. BOM浏览器对象模型
2. DOM是文档对象模型

### 12. 什么是事件冒泡，如何阻止事件冒泡。

实现一个事件冒泡的例子，并阻止事件冒泡。

### 13. 什么是事件委托？有哪些实际应用场景。

1. 为后添加的元素绑定事件。
2. 缩减代码，提升系统性能。

### 14. window的load事件和document的DOMContentLoaded事件有什么区别？

1. load会等待所有html节点和所有图片加载完成后，再执行。
2. DOMContentLoaded会等待所有DOM节点加载完成后再执行，不会等待图片加载完成。

### 15. ES6有哪些新特性？

1. 结构赋值
2. 变量let与常量const。
3. 箭头函数、函数默认值
4. 面向对象的语法，class，extends等
5. 模块化开发：import，export
6. promise对象，处理异步问题
7. async/await函数，处理异步问题

### 16. var和let有什么区别

1. let有块级作用域，var没有
2. let不可以重复定义变量，var可以重复定义。
3. let不会提升变量声明，var会提升。
4. 在实际开发中，可以完全使用let替换var。

### 17. 箭头函数和普通函数有什么区别

箭头函数中的this指向函数定义时的对象，普通函数中的this指向函数调用时的对象。

### 18. 什么是重排和重绘

重排负责元素的几何属性更新（宽高，是否可见），重绘负责元素的样式更新（字体颜色，北京颜色）。而且，重排必然带来重绘，但是重绘未必带来重排。比如，`改变某个元素的背景`，这个就不涉及元素的几何属性，所以只发生重绘。

#### 以下操作会发生重排

1. 添加或删除可见的DOM元素
2. 元素位置改变
3. 元素本身的尺寸发生改变
4. 内容改变
5. 页面渲染器初始化
6. 浏览器窗口大小发生改变

### 19. 实现JavaScript的深度克隆（深拷贝）有几种方法？

``` js
let obj = {
    name:"xx",
    age:2,
    friends:["小明","小强"]
}

function copyObj(oldObj){
    let newObj = {};
    for(let i in oldObj){
        if(oldObj[i] instanceof Object){
            newObj[i] = copyObj(oldObj[i])
        }else{
            newObj[i] = oldObj[i]
        }
    }
    return newObj;
}
let result = copyObj(obj)
result.friends[0] = "123"
console.log(result);
console.log(obj);
```

``` js
function copyObj(oldObj){
    let newObjString = JSON.stringify(oldObj);
    let newObj = JSON.parse(newObjString);
    return newObj;
}
```



### 20. 概述JavaScript的作用域链？

每声明一个函数都会生成一个新的作用域，当前作用域使用变量时，会首先在当前作用域查找这个变量的声明，如果当前作用域没有此变量，就会到上一层作用域查找此变量，直到找到全局变量为止。

### 21. 什么是闭包？闭包有哪些应用场景。

1. 函数嵌套，内部函数就是闭包。
2. 外部函数中定义的变量，在内部函数中可以访问，而内部函数定义的变量，外部函数不可以访问。
3. 外部函数可以通过返回值，将内部函数暴露出去，由于闭包函数被暴露出去，所以外部函数中定义的变量不会因为外部函数执行结束而销毁。利用此特性，可以实现代码的封装。
4. 闭包具有全局性，在浏览器环境中，闭包中的this指向window对象（全局对象）。

### 22. 什么是防抖与节流，用js如何实现？

防抖：

``` js
debounce = function(fn,delay) {
    let timer = null;
    return function(){
        if (timer !== null) {
            clearTimeout(timer);
        }
        timer = setTimeout(() => {
            fn.call(this);
            timer = null;
        }, delay)
    }
}
```



节流

``` js
function throttle(fn,delay){
    let mark = true;
    return function(){
        if(mark){
            setTimeout(() => {
                fn.call(this);
                mark = true;
            },delay)
        }
        mark = false;
    }
}
```



### 23. 说说你对原型的理解，什么是原型链，如果通过原型实现继承。

prototype是构造函数的一个属性，可以指向这个类（构造函数）的原型对象，由这个类（构造函数）创建的所有对象，都可以使用原型对象上的属性和方法。

1. hasOwnproperty，判断对象是否包含特定的自身（非继承）属性。
2. isPrototypeOf，用来判断指定对象object1是否存在于另一个对象object2的原型链中，是则返回true，否则返回false。

### 24. js延迟加载有哪些方法

1. defer 属性：`<script>`标签定义了 defer属性，脚本会被延迟到整个页面都解析完毕之后再执行

``` js
<script src="test1.js" defer="defer"></script>
<script src="test2.js" defer="defer"></script>
```

2. async 属性：async和defer一样，都不会阻塞其他资源下载，所以不会影响页面的加载。缺点：不能控制加载的顺序

``` js
<script src="test1.js" async></script>
<script src="test2.js" async></script>
```

3. 将script标签写在body标签结尾，等所有页面加载完成，再加载就是文件。

``` html
<body>
	<h1>hello world</h1>
    <script src="test.js"></script>
</body>
```

### 25. 优化代码有哪些方案。

1.  js延迟加载，可以让用户更早地看到页面效果。
2. vue组件懒加载，可以防止首页加载时间过长。
3. 减少高频率的DOM操作
4. 使用防抖与节流，控制高频触发事件。
5. css选择器层级过多，会影响性能。

### 26. 数组去掉重复元素有哪些方法.

第一种方法

``` js
 let list = [99,89,100,111,89,50,99,100,56];
 let newList = [];

//  检查重复(newList中是否包含指定value)，如果重复返回true，不重复返回false
 function checkRepeat(value){
    for(let i = 0;i<newList.length;i++){
        if(newList[i] === value){
            return true;
        }
    }
    // 遍历之后，没有找到元素，返回false
    return false
 };

 for(let i = 0;i<list.length;i++){
     //通过checkRepeat方法检查newList中是否有list中的元素
    if(checkRepeat(list[i])){
        // 如果有继续遍历
        continue;
    }else{
        //如果没有，将元素插入newList
        newList.push(list[i]);
    }
 }
 //最后得到的newList就是去重之后的结果
 console.log(newList);
```

第二种方法

``` js
let list = [99,89,100,111,89,50,99,100,56];
let newList = [];
let checkObj = {} //用于检测的对象
for(let i = 0;i<list.length;i++){
    /*
        将数组元素作为对象的属性，
        如果对象的这个属性有值，
        说明新数组有这个元素，
        如果对象这个属性没有值，
        说明数组没有这个元素，
        那么就push进新数组
    */
    if(checkObj[list[i]]){  
        continue;
    }else{
        newList.push(list[i]);
        checkObj[list[i]] = 1;
    }
}
console.log(newList)
```



### 27. 如何获取一个数值型数组中，最大值的下标。

### 28. 使用递归函数输出斐波那契数列（计算阶乘）（计算100以内所有正整数加和）

### 29. 排序算法

1. 冒泡排序
  2. 选择排序
  3. 插入排序
  4. 归并排序
  5. 快速排序

### 30. 检索算法

1. 顺序查找
 	7. 二分查找

### 31. 在控制台输出下面组织架构中的所有部门名称，并且确保部门新增与减少，都可以正常遍历所有部门。

``` json
{
    "name":"总部",
    "children":[
        {
            "name":"技术部",
            "children":[
                {
                    "name":"前端组"
                },
                {
                    "name":"Java组"
                },
                {
                    "name":"PHP组"
                }
            ]
        },
        {
            "name":"市场部",
            "children":[
                {
                    "name":"售前"
                },
                {
                    "name":"渠道"
                }
            ]
        },
    ]
}
```

``` js
function showName(department){
    console.log(department.name);
    if(department.children){
        department.children.map((v) => {
            showName(v)
        })
    }
}
showName(tree);
```

# JS进阶部分

### 1 闭包

#### 闭包就是能够读取其他函数内部变量的函数

#### 闭包是指有权访问另一个函数作用域中变量的函数，创建闭包的最常⻅的方式就是在一个函数内创建另一个函数，通过另一个函数访问这个函数的局部变量, 利用闭包可以突破作用链域

#### 闭包的特性：

#### 函数内再嵌套函数

#### 内部函数可以引用外层的参数和变量

#### 参数和变量不会被垃圾回收机制回收

#### 说说你对闭包的理解：

```
使用闭包主要是为了设计私有的方法和变量。闭包的优点是可以避免全局变量的污染
```

``` 

缺点是闭包会常驻内存，会增大内存使用量，使用不当很容易造成内存泄露。在js中，函数即
闭包，只有函数才会产生作用域的概念
```

``` 

闭包 的最大用处有两个，一个是可以读取函数内部的变量，另一个就是让这些变量始终保
持在内存中
```

``` 

闭包的另一个用处，是封装对象的私有属性和私有方法
```

``` 

好处 ：能够实现封装和缓存等；
```

``` 

坏处 ：就是消耗内存、不正当使用会造成内存溢出的问题
```

**使用闭包的注意点**

``` 

transform: scale(0.7);
```

#### 由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包，否

#### 则会造成网⻚的性能问题，在IE中可能导致内存泄露

#### 解决方法是，在退出函数之前，将不使用的局部变量全部删除

### 2 说说你对作用域链的理解


``` 

作用域链的作用是保证执行环境里有权访问的变量和函数是有序的，作用域链的变量只能
向上访问，变量访问到 window 对象即被终止，作用域链向下访问变量是不被允许的
简单的说，作用域就是变量与函数的可访问范围，即作用域控制着变量与函数的可⻅性和
生命周期

```

### 3 JavaScript原型，原型链? 有什么特点？

``` 

每个对象都会在其内部初始化一个属性，就是 prototype (原型)，当我们访问一个对象的
属性时如果这个对象内部不存在这个属性，那么他就会去 prototype 里找这个属性，这个
prototype 又会有自己的 prototype ，于是就这样一直找下去，也就是我们平时所说的
原型链的概念
```

``` 

关系： instance.constructor.prototype = instance.__proto__
```

``` 
特点：

JavaScript 对象是通过引用来传递的，我们创建的每个新对象实体中并没有一份属于
自己的原型副本。当我们修改原型时，与之相关的对象也会继承这一改变当我们需要一个属性的时， Javascript 引擎会先看当前对象中是否有这个属性， 如果没
有的就会查找他的 Prototype 对象是否有这个属性，如此递推下去，一直检索到 Object 内
建对象
```

### 4 请解释什么是事件代理

``` 

事件代理（ Event Delegation ），又称之为事件委托。是 JavaScript 中常用绑定事
件的常用技巧。顾名思义，“事件代理”即是把原本需要绑定的事件委托给父元素，让父元
素担当事件监听的职务。事件代理的原理是DOM元素的事件冒泡。使用事件代理的好处是
可以提高性能

可以大量节省内存占用，减少事件注册，比如在 table 上代理所有 td 的 click事件就
非常棒

可以实现当新增子对象时无需再次对其绑定

```


### 5 Javascript如何实现继承？

#### 构造继承

#### 原型继承

#### 实例继承

#### 拷⻉继承

``` 

原型 prototype 机制或 apply 和 call 方法去实现较简单，建议使用构造函数与原型混
合方式
```

### 6 谈谈This对象的理解

``` 

this 总是指向函数的直接调用者（而非间接调用者）
如果有 new 关键字， this 指向 new 出来的那个对象
在事件中， this 指向触发这个事件的对象，特殊的是， IE中的 attachEvent 中的
this 总是指向全局对象 Window
```

### 7 事件模型

``` 

W3C 中定义事件的发生经历三个阶段：捕获阶段（ capturing ）、目标阶段
（ targetin ）、冒泡阶段（ bubbling）
```

``` js

function Parent(){
this.name = 'wang';
}
```

``` js

function Child(){
this.age = 28 ;
}
```

``` js

Child.prototype = new Parent();//继承了Parent，通过原型
```

``` js

var demo = new Child();
alert(demo.age);
alert(demo.name);//得到被继承的属性
```


#### 冒泡型事件：当你使用事件冒泡时，子级元素先触发，父级元素后触发

#### 捕获型事件：当你使用事件捕获时，父级元素先触发，子级元素后触发

#### DOM 事件流：同时支持两种事件模型：捕获型事件和冒泡型事件

``` 

阻止冒泡：在 W3c 中，使用 stopPropagation() 方法；在IE下设置 cancelBubble =
true
阻止捕获：阻止事件的默认行为，例如 click - <a> 后的跳转。在 W3c 中，使用
preventDefault() 方法，在 IE下设置 window.event.returnValue = false
```

### 8 new操作符具体干了什么呢?

``` 

创建一个空对象，并且 this 变量引用该对象，同时还继承了该函数的原型
属性和方法被加入到 this 引用的对象中
新创建的对象由 this 所引用，并且最后隐式的返回 this
```

### 9 Ajax原理

``` 

Ajax 的原理简单来说是在用户和服务器之间加了—个中间层( AJAX 引擎)，通过
XmlHttpRequest 对象来向服务器发异步请求，从服务器获得数据，然后用 javascrip t
来操作 DOM 而更新⻚面。使用户操作与服务器响应异步化。这其中最关键的一步就是从服
务器获得请求数据

Ajax 的过程只涉及 JavaScript 、 XMLHttpRequest和 DOM 。 XMLHttpRequest 是
aja x的核心机制
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

**ajax 有那些优缺点?**

``` 

优点：

通过异步模式，提升了用户体验.

优化了浏览器和服务器之间的传输，减少不必要的数据往返，减少了带宽占用.

Ajax 在客户端运行，承担了一部分本来由服务器承担的工作，减少了大用户量下的服
务器负载。

Ajax 可以实现动态不刷新（局部刷新）


缺点：

安全问题 AJAX 暴露了与服务器交互的细节。

对搜索引擎的支持比较弱。

不容易调试。

```

### 10 如何解决跨域问题?

``` 

首先了解下浏览器的同源策略 同源策略 /SOP（Same origin policy）是一
种约定，由Netscape公司 1995 年引入浏览器，它是浏览器最核心也最基本的
安全功能，如果缺少了同源策略，浏览器很容易受到 XSS 、 CSFR 等攻击。
所谓同源是指" 协议+域名+端口 "三者相同，即便两个不同的域名指向同一个ip
地址，也非同源
```

#### 那么怎样解决跨域问题的呢？

``` 

通过jsonp跨域
```

``` js

document.domain + iframe跨域
```

``` js

var script = document.createElement('script');
script.type = 'text/javascript';
```

``` js

// 传参并指定回调执行函数为onBack
script.src = 'http://www.....:8080/login?user=admin&callback=onBack';
document.head.appendChild(script);
```

``` js

// 回调执行函数
function onBack(res) {
alert(JSON.stringify(res));
}
```

#### 此方案仅限主域相同，子域不同的跨域应用场景

1.父窗口：(http://www.domain.com/a.html)

2.子窗口：(http://child.domain.com/b.html)

``` 

nginx代理跨域

nodejs中间件代理跨域

后端在头部信息里面设置安全域名

```

### 11 模块化开发怎么做？

#### 立即执行函数, 不暴露私有成员

### 12 异步加载JS的方式有哪些？

``` html

<iframe id="iframe" src="http://child.domain.com/b.html"></iframe>
<script>
document.domain = 'domain.com';
var user = 'admin';
</script>
```

``` js

document.domain = 'domain.com';
// 获取父窗口中变量
alert('get js data from parent ---> ' + window.parent.user);
```

``` js

var module1 = (function(){
var _count = 0 ;
var m1 = function(){
//...
};
var m2 = function(){
//...
};
return {
m1 : m1,
m2 : m2
};
})();
```

``` 

基本数据当值发生改变时，那么其对应的指针也将发生改变，故造成 const申明基本数
据类型时
再将其值改变时，将会造成报错， 例如 const a = 3 ; a = 5时 将会报错
但是如果是复合类型时，如果只改变复合类型的其中某个 Value 项时， 将还是正常使用
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

``` 

defer，只支持 IE
async ：
创建 script ，插入到 DOM 中，加载完毕后 callBack
```

### 13 那些操作会造成内存泄漏？

#### 内存泄漏指任何对象在您不再拥有或需要它之后仍然存在

``` 

setTimeout 的第一个参数使用字符串而非函数的话，会引发内存泄漏
闭包使用不当
```

### 14 XML和JSON的区别？

#### 数据体积方面

#### JSON 相对 于XML 来讲，数据的体积小，传递的速度更快些。

#### 数据交互方面

``` 

JSON 与 JavaScript 的交互更加方便，更容易解析处理，更好的数据交互
```

#### 数据描述方面:

``` 

JSON 对数据的描述性比 XML 较差
```

####  传输速度方面:

``` 

JSON 的速度要远远快于 XML
```

### 15 谈谈你对webpack的看法

``` 

WebPack 是一个模块打包工具，你可以使用 WebPack 管理你的模块依赖，并编绎输出模
块们所需的静态文件。它能够很好地管理、打包 Web 开发中所用到的 HTML 、
Javascript 、 CSS 以及各种静态文件（图片、字体等），让开发过程更加高效。对于
不同类型的资源， webpack 有对应的模块加载器。 webpack 模块打包器会分析模块间的
依赖关系，最后 生成了优化且合并后的静态资源
```

### 16 说说你对AMD和Commonjs的理解

``` 

CommonJS 是服务器端模块的规范， Node.js 采用了这个规范。 CommonJS 规范加载模
块是同步的，也就是说，只有加载完成，才能执行后面的操作。 AMD 规范则是非同步加载
模块，允许指定回调函数
```

``` 

AMD 推荐的⻛格通过返回一个对象做为模块对象， CommonJS 的⻛格通过对
module.exports 或 exports 的属性赋值来达到暴露模块对象的目的
```

### 17 常⻅web安全及防护原理

``` 

sql 注入原理
```

``` 

就是通过把 SQL 命令插入到 Web 表单递交或输入域名或⻚面请求的查询字符串，最终
达到欺骗服务器执行恶意的SQL命令
```

``` 

总的来说有以下几点
```

``` 

永远不要信任用户的输入，要对用户的输入进行校验，可以通过正则表达式，或限制⻓
度，对单引号和双 "-" 进行转换等
永远不要使用动态拼装SQL，可以使用参数化的 SQL 或者直接使用存储过程进行数据查
询存取
永远不要使用管理员权限的数据库连接，为每个应用使用单独的权限有限的数据库连接
不要把机密信息明文存放，请加密或者 hash 掉密码和敏感的信息
```

**XSS原理及防范**

``` 

Xss(cross-site scripting) 攻击指的是攻击者往 Web ⻚面里插入恶意 html 标签或
者 javascript 代码。比如：攻击者在论坛中放一个看似安全的链接，骗取用户点击后，
窃取 cookie 中的用户私密信息；或者攻击者在论坛中加一个恶意表单，当用户提交表单
的时候，却把信息传送到攻击者的服务器中，而不是用户原本以为的信任站点
```

**XSS防范方法**

``` 

首先代码里对用户输入的地方和变量都需要仔细检查⻓度和对 ”<”,”>”,”;”,”’” 等字符
做过滤；其次任何内容写到⻚面之前都必须加以encode，避免不小心把 html tag 弄出
来。这一个层面做好，至少可以堵住超过一半的XSS 攻击
```

**XSS与CSRF有什么区别吗？**

``` 

XSS 是获取信息，不需要提前知道其他用户⻚面的代码和数据包。 CSRF 是代替用户完成
指定的动作，需要知道其他用户⻚面的代码和数据包。要完成一次 CSRF 攻击，受害者必
须依次完成两个步骤
```

``` 

登录受信任网站 A ，并在本地生成 Cookie
```

``` 

在不登出 A 的情况下，访问危险网站 B
```

**CSRF的防御**

#### 服务端的 CSRF 方式方法很多样，但总的思想都是一致的，就是在客户端⻚面增加伪随机

#### 数

#### 通过验证码的方法

### 18 用过哪些设计模式？

#### 工厂模式：

#### 工厂模式解决了重复实例化的问题，但还有一个问题, 那就是识别问题，因为根本无法

``` 

主要好处就是可以消除对象间的耦合，通过使用工程方法而不是 new 关键字
```

``` 

构造函数模式
```

``` 

使用构造函数的方法，即解决了重复实例化的问题，又解决了对象识别的问题，该模式
与工厂模式的不同之处在于
直接将属性和方法赋值给 this 对象;
```

### 19 为什么要有同源限制？

#### 同源策略指的是：协议，域名，端口相同，同源策略是一种安全协议

``` 

举例说明：比如一个黑客程序，他利用 Iframe 把真正的银行登录⻚面嵌到他的⻚面上，
当你使用真实的用户名，密码登录时，他的⻚面就可以通过 Javascript 读取到你的表单
中 input 中的内容，这样用户名，密码就轻松到手了。
```

### 20 offsetWidth/offsetHeight, clientWidth/clientHeight与

### scrollWidth/scrollHeight的区别

``` 

offsetWidth/offsetHeight 返回值包含 content + padding + border ，效果与
e.getBoundingClientRect()相同
clientWidth/clientHeight 返回值只包含 content + padding ，如果有滚动条，也 不包
含滚动条
scrollWidth/scrollHeight 返回值包含 content + padding + 溢出内容的尺寸
```

### 21 javascript有哪些方法定义对象

``` 

对象字面量： var obj = {};
构造函数： var obj = new Object();
Object.create(): var obj = Object.create(Object.prototype);
```

### 22 常⻅兼容性问题？

``` 

png24 位的图片在iE 6 浏览器上出现背景，解决方案是做成 PNG8
浏览器默认的 margin 和 padding 不同。解决方案是加一个全局的 *
{margin:0;padding:0;} 来统一,，但是全局效率很低，一般是如下这样解决：
```

``` 

IE 下,event 对象有 x , y 属性,但是没有 pageX ,pageY 属性
Firefox 下,event 对象有 pageX, pageY属性,但是没有 x,y 属性.
```

### 23 说说你对promise的了解

``` 

依照 Promise/A+ 的定义， Promise 有四种状态：
```

``` 

pending: 初始状态, 非 fulfilled 或 rejected.
```

``` 

fulfilled: 成功的操作.
```

``` 

rejected: 失败的操作.
```

``` 

settled: Promise 已被 fulfilled 或 rejected，且不是 pending
```

``` 

另外， fulfilled与 rejected一起合称 settled
```

``` 

Promise 对象用来进行延迟(deferred ) 和异步( asynchronous) 计算
```

**Promise 的构造函数**

``` 

构造一个 Promise ，最基本的用法如下：
```

``` 

body,ul,li,ol,dl,dt,dd,form,input,h1,h2,h3,h4,h5,h6,p{
margin: 0 ;
padding: 0 ;
}
```

``` 

var promise = new Promise(function(resolve, reject) {
```

``` 

if (...) { // succeed
```

``` 

resolve(result);
```

``` 

cs s
```

 

``` 

Promise 实例拥有 then 方法（具有 then 方法的对象，通常被称为 thenable ）。
它的使用方法如下：
```

``` 

接收两个函数作为参数，一个在 fulfilled 的时候被调用，一个在 rejected的时候被
调用，接收参数就是 future， onFulfilled 对应 resolve , onRejected 对应
reject
```

### 24 你觉得jQuery源码有哪些写的好的地方

``` 

jquery 源码封装在一个匿名函数的自执行环境中，有助于防止变量的全局污染，然后通
过传入 window 对象参数，可以使 window 对象作为局部变量使用，好处是当 jquery 中
访问 window 对象的时候，就不用将作用域链退回到顶层作用域了，从而可以更快的访问
window对象。同样，传入 undefined 参数，可以缩短查找 undefined 时的作用域链
jquery 将一些原型属性和方法封装在了 jquery.prototype 中，为了缩短名称，又赋值
给了 jquery.fn ，这是很形象的写法
有一些数组或对象的方法经常能使用到， jQuery 将其保存为局部变量以提高访问速度
jquery 实现的链式调用可以节约代码，所返回的都是同一个对象，可以提高代码效率
```

### 25 vue、react、angular

``` 

Vue.js 一个用于创建 web 交互界面的库，是一个精简的 MVVM 。它通过双向数据绑
定把 View 层和 Model 层连接了起来。实际的 DOM 封装和输出格式都被抽象为了
Directives 和 Filters
```

``` 

AngularJS 是一个比较完善的前端 MVVM 框架，包含模板，数据双向绑定，路由，模块
化，服务，依赖注入等所有功能，模板功能强大丰富，自带了丰富的 Angular 指令
```

``` 

react React 仅仅是 VIEW 层是 facebook 公司。推出的一个用于构建 UI 的一个
库，能够实现服务器端的渲染。用了 virtual dom ，所以性能很好。
```

``` js

} else { // fails
reject(Error(errMessage));
}
});
promise.then(onFulfilled, onRejected)
```

### 26 Node的应用场景

#### 特点：

``` 

1 、它是一个 Javascript 运行环境
2 、依赖于 Chrome V8 引擎进行代码解释
3 、事件驱动
4 、非阻塞 I/O
5 、单进程，单线程
```

``` 

优点：
```

``` 

高并发（最重要的优点）
```

``` 

缺点：
```

``` 

1 、只支持单核 CPU ，不能充分利用 CPU
2 、可靠性低，一旦代码某个环节崩溃，整个系统都崩溃
```

### 27 谈谈你对AMD、CMD的理解

``` 

CommonJS 是服务器端模块的规范， Node.js 采用了这个规范。 CommonJS 规范加载模
块是同步的，也就是说，只有加载完成，才能执行后面的操作。 AMD 规范则是非同步加载
模块，允许指定回调函数
```

``` 

AMD 推荐的⻛格通过返回一个对象做为模块对象， CommonJS 的⻛格通过对
module.exports 或 exports 的属性赋值来达到暴露模块对象的目的
```

**es 6 模块 CommonJS、AMD、CMD**

``` 

CommonJS 的规范中，每个 JavaScript 文件就是一个独立的模块上下文（ module
context ），在这个上下文中默认创建的属性都是私有的。也就是说，在一个文件定义的
变量（还包括函数和类），都是私有的，对其他文件是不可⻅的。
CommonJS 是同步加载模块,在浏览器中会出现堵塞情况，所以不适用
AMD 异步，需要定义回调 define方式
es6 一个模块就是一个独立的文件，该文件内部的所有变量，外部无法获取。如果你希
望外部能够读取模块内部的某个变量，就必须使用 export 关键字输出该变量 es6 还可
以导出类、方法，自动适用严格模式
```

### 28 那些操作会造成内存泄漏

#### 内存泄漏指任何对象在您不再拥有或需要它之后仍然存在

``` 

setTimeout 的第一个参数使用字符串而非函数的话，会引发内存泄漏
闭包、控制台日志、循环（在两个对象彼此引用且彼此保留时，就会产生一个循环）
```

### 29 web开发中会话跟踪的方法有哪些

``` 

cookie
session
url 重写
隐藏 input
ip 地址
```

### 30 介绍js的基本数据类型

``` 

Undefined 、 Null 、 Boolean 、 Number 、 String
```

### 31 介绍js有哪些内置对象

``` 

Object 是 JavaScript 中所有对象的父对象
数据封装类对象： Object 、 Array 、 Boolean 、 Number 和 String
其他对象： Function 、 Arguments 、 Math 、 Date 、 RegExp 、 Error
```

### 32 说几条写JavaScript的基本规范

#### 不要在同一行声明多个变量

``` 

请使用 ===/!== 来比较 true/false 或者数值
使用对象字面量替代 new Array 这种形式
不要使用全局函数
Switch 语句必须带有 default 分支
If 语句必须使用大括号
for-in 循环中的变量 应该使用 var 关键字明确限定作用域，从而避免作用域污
```

### 33 JavaScript有几种类型的值

``` 

栈：原始数据类型（ Undefined ， Null ， Boolean ， Number 、 String ）

堆：引用数据类型（对象、数组和函数）

两种类型的区别是：存储位置不同；
原始数据类型直接存储在栈( stack)中的简单数据段，占据空间小、大小固定，属于被频
繁使用数据，所以放入栈中存储；

引用数据类型存储在堆( heap )中的对象,占据空间大、大小不固定,如果存储在栈中，将会
影响程序运行的性能；引用数据类型在栈中存储了指针，该指针指向堆中该实体的起始地
址。当解释器寻找引用值时，会首先检索其
在栈中的地址，取得地址后从堆中获得实体
```

### 34 javascript创建对象的几种方式

``` 

javascript 创建对象简单的说,无非就是使用内置对象或各种自定义对象，
当然还可以用 JSON ；但写法有很多种，也能混合使用
```

#### 对象字面量的方式

``` 

用 function 来模拟无参的构造函数
```

``` 

person={firstname:"Mark",lastname:"Yun",age: 25 ,eyecolor:"black"};
```

 

用 function 来模拟参构造函数来实现（用 this 关键字定义构造的上下文属性）

#### 用工厂方式来创建（内置对象）

#### 用原型方式来创建

``` 

用 function 来模拟无参的构造函数
```

``` js

person={firstname:"Mark",lastname:"Yun",age: 25 ,eyecolor:"black"};
```

``` js

person={firstname:"Mark",lastname:"Yun",age: 25 ,eyecolor:"black"};
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

``` 

阻止冒泡：在 W3c 中，使用 stopPropagation() 方法；在IE下设置 cancelBubble =
true
阻止捕获：阻止事件的默认行为，例如 click - <a> 后的跳转。在 W3c 中，使用
preventDefault() 方法，在 IE下设置 window.event.returnValue = false
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

#### 用混合方式来创建

### 35 eval是做什么的

#### 它的功能是把对应的字符串解析成 JS 代码并运行

``` 

应该避免使用 eval ，不安全，非常耗性能（ 2 次，一次解析成 js 语句，一次执行）
由 JSON 字符串转换为JSON对象的时候可以用 eval，var obj =eval('('+ str +')')
```

### 36 null，undefined 的区别

``` 

undefined 表示不存在这个值。
```

``` 

undefined :是一个表示"无"的原始值或者说表示"缺少值"，就是此处应该有一个值，但
是还没有定义。当尝试读取时会返回 undefined
```

``` 

例如变量被声明了，但没有赋值时，就等于 undefined
```

``` 

null 表示一个对象被定义了，值为“空值”
```

``` 

null : 是一个对象(空对象, 没有任何属性和方法)
```

``` 

例如作为函数的参数，表示该函数的参数不是对象；
```

``` 

在验证 null 时，一定要使用 === ，因为 ==无法分别 null 和 undefined
```

### 37 ["1", "2", "3"].map(parseInt) 答案是多少

``` js

wangcai.eat();
```

``` js

function Car(name,price){
this.name=name;
this.price=price;
}
Car.prototype.sell=function(){
alert("我是"+this.name+"，我现在卖"+this.price+"万元");
}
var camry =new Car("凯美瑞", 27 );
camry.sell();
```

``` 

[1, NaN, NaN] 因为 parseInt 需要两个参数 (val, radix)，其中 radix 表示解
析时用的基数。
map 传了 3 个 (element, index, array) ，对应的 radix 不合法导致解析失败。
```

### 38 javascript 代码中的"use strict"; 是什么意思

``` 

use strict 是一种 ECMAscript 5 添加的（严格）运行模式,这种模式使得 Javascript
在更严格的条件下运行,使 JS编码更加规范化的模式,消除 Javascript 语法的一些不合
理、不严谨之处，减少一些怪异行为
```

### 39 JSON 的了解

``` 

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
```

``` 

它是基于 JavaScript 的一个子集。数据格式简单, 易于读写, 占用带宽小
```

``` 

JSON 字符串转换为JSON对象:
```

#### JSON 对象转换为JSON字符串：

### 40 js延迟加载的方式有哪些

``` 

defer 和 async 、动态创建 DOM 方式（用得最多）、按需异步载入 js
```

### 41 同步和异步的区别

#### 同步：浏览器访问服务器请求，用户看得到⻚面刷新，重新发请求, 等请求完，⻚面刷新，

#### 新内容出现，用户看到新内容, 进行下一步操作

#### 异步：浏览器访问服务器请求，用户正常操作，浏览器后端进行请求。等请求完，⻚面不

#### 刷新，新内容也会出现，用户看到新内容

``` js

var obj =eval('('+ str +')');
var obj = str.parseJSON();
var obj = JSON.parse(str);
```

``` js

var last=obj.toJSONString();
var last=JSON.stringify(obj);
```


### 42 渐进增强和优雅降级

#### 渐进增强 ：针对低版本浏览器进行构建⻚面，保证最基本的功能，然后再针对高级浏览器

#### 进行效果、交互等改进和追加功能达到更好的用户体验。

#### 优雅降级 ：一开始就构建完整的功能，然后再针对低版本浏览器进行兼容

### 43 defer和async

``` 

defer 并行加载 js 文件，会按照⻚面上 script 标签的顺序执行
async 并行加载 js 文件，下载完成立即执行，不会按照⻚面上 script 标签的顺序执
行
```

### 44 说说严格模式的限制

#### 变量必须声明后再使用

#### 函数的参数不能有同名属性，否则报错

``` 

不能使用 with 语句
禁止 this 指向全局对象
```

### 45 attribute和property的区别是什么

``` 

attribute 是 dom 元素在文档中作为 html 标签拥有的属性；
property 就是 dom 元素在 js 中作为对象拥有的属性。
对于 html 的标准属性来说， attribute 和 property是同步的，是会自动更新的
但是对于自定义的属性来说，他们是不同步的
```

### 46 谈谈你对ES 6 的理解

``` 

新增模板字符串（为 JavaScript 提供了简单的字符串插值功能）
箭头函数
for-of （用来遍历数据—例如数组中的值。）
arguments 对象可被不定参数和默认参数完美代替。
ES6 将p romise 对象纳入规范，提供了原生的 Promise 对象。
增加了 let 和 const 命令，用来声明变量。
增加了块级作用域。
let 命令实际上就增加了块级作用域。
```

``` 

还有就是引入 module 模块的概念
```

### 47 ECMAScript 6 怎么写class么

``` 

这个语法糖可以让有 OOP 基础的人更快上手 js ，至少是一个官方的实现了
但对熟悉 js 的人来说，这个东⻄没啥大影响；一个 Object.creat() 搞定继承，比
class 简洁清晰的多
```

### 48 什么是面向对象编程及面向过程编程，它们的异同和优缺点

#### 面向过程就是分析出解决问题所需要的步骤，然后用函数把这些步骤一步一步实现，使用

#### 的时候一个一个依次调用就可以了

#### 面向对象是把构成问题事务分解成各个对象，建立对象的目的不是为了完成一个步骤，而

#### 是为了描叙某个事物在整个解决问题的步骤中的行为

#### 面向对象是以功能来划分问题，而不是步骤

### 49 面向对象编程思想

#### 基本思想是使用对象，类，继承，封装等基本概念来进行程序设计

#### 优点

#### 易维护

#### 采用面向对象思想设计的结构，可读性高，由于继承的存在，即使改变需求，那么维

#### 护也只是在局部模块，所以维护起来是非常方便和较低成本的

#### 易扩展

#### 开发工作的重用性、继承性高，降低重复工作量。

#### 缩短了开发周期

### 50 对web标准、可用性、可访问性的理解

``` 

可用性（Usability）：产品是否容易上手，用户能否完成任务，效率如何，以及这过程中
用户的主观感受可好，是从用户的⻆度来看产品的质量。可用性好意味着产品质量高，是
企业的核心竞争力
可访问性（Accessibility）：Web内容对于残障用户的可阅读和可理解性
可维护性（Maintainability）：一般包含两个层次，一是当系统出现问题时，快速定位并解
决问题的成本，成本低则可维护性好。二是代码是否容易被人理解，是否容易修改和增强
功能。
```

### 51 如何通过JS判断一个数组

``` 

instanceof 方法
instanceof 运算符是用来测试一个对象是否在其原型链原型构造函数的属性
```

``` 

constructor 方法
constructor属性返回对创建此对象的数组函数的引用，就是返回对象相对应的构造
函数
```

#### 最简单的方法

``` 

这种写法，是 jQuery 正在使用的
```

``` 

ES5 新增方法 isArray()
```

### 52 谈一谈let与var的区别

``` 

let 命令不存在变量提升，如果在 let 前使用，会导致报错
如果块区中存在 let 和 const 命令，就会形成封闭作用域
```

``` js

var arr = [];
arr instanceof Array; // true
```

``` js

var arr = [];
arr.constructor == Array; //true
```

``` js

Object.prototype.toString.call(value) == '[object Array]'
// 利用这个方法，可以写一个返回数据类型的方法
var isType = function (obj) {
return Object.prototype.toString.call(obj).slice( 8 ,- 1 );
}
```

``` 

let 命令不存在变量提升，如果在 let 前使用，会导致报错
如果块区中存在 let 和 const 命令，就会形成封闭作用域
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

``` 

阻止冒泡：在 W3c 中，使用 stopPropagation() 方法；在IE下设置 cancelBubble =
true
阻止捕获：阻止事件的默认行为，例如 click - <a> 后的跳转。在 W3c 中，使用
preventDefault() 方法，在 IE下设置 window.event.returnValue = false
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

#### 不允许重复声明，因此，不能在函数内部重新声明参数

### 53 map与forEach的区别

``` 

forEach 方法，是最基本的方法，就是遍历与循环，默认有 3 个传参：分别是遍历的数组
内容 item 、数组索引 index、和当前遍历数组 Array
map 方法，基本用法与 forEach 一致，但是不同的，它会返回一个新的数组，所以在
callback需要有 return 值，如果没有，会返回 undefined
```

### 54 谈一谈你理解的函数式编程

``` 

简单说，"函数式编程"是一种"编程范式"（programming paradigm），也就是如何编写程
序的方法论
它具有以下特性：闭包和高阶函数、惰性计算、递归、函数是"第一等公⺠"、只用"表达式"
```

### 55 谈一谈箭头函数与普通函数的区别？

``` 

函数体内的 this 对象，就是定义时所在的对象，而不是使用时所在的对象
不可以当作构造函数，也就是说，不可以使用 new 命令，否则会抛出一个错误
不可以使用 arguments 对象，该对象在函数体内不存在。如果要用，可以用 Rest 参数
代替
不可以使用 yield 命令，因此箭头函数不能用作 Generator 函数
```

### 56 谈一谈函数中this的指向

``` 

this的指向在函数定义的时候是确定不了的，只有函数执行的时候才能确定this到底指向
谁，实际上this的最终指向的是那个调用它的对象
```

``` 

《javascript语言精髓》中大概概括了 4 种调用方式：
```

``` 

方法调用模式
```

``` 

函数调用模式
```

``` 

构造器调用模式
```

``` js

graph LR
A-->B
```


``` 

apply/call调用模式
```

### 57 异步编程的实现方式

#### 回调函数

#### 优点：简单、容易理解

#### 缺点：不利于维护，代码耦合高

#### 事件监听(采用时间驱动模式，取决于某个事件是否发生)：

#### 优点：容易理解，可以绑定多个事件，每个事件可以指定多个回调函数

#### 缺点：事件驱动型，流程不够清晰

#### 发布/订阅(观察者模式)

#### 类似于事件监听，但是可以通过‘消息中心ʼ，了解现在有多少发布者，多少订阅者

``` 

Promise对象
```

``` 

优点：可以利用then方法，进行链式写法；可以书写错误时的回调函数；
缺点：编写和理解，相对比较难
```

``` 

Generator函数
```

``` 

优点：函数体内外的数据交换、错误处理机制
缺点：流程管理不方便
```

``` 

async函数
```

``` 

优点：内置执行器、更好的语义、更广的适用性、返回的是Promise、结构清晰。
缺点：错误处理机制
```

### 58 对原生Javascript了解程度

``` 

数据类型、运算、对象、Function、继承、闭包、作用域、原型链、事件、 RegExp 、
JSON 、 Ajax 、 DOM 、 BOM 、内存泄漏、跨域、异步装载、模板引擎、前端 MVC 、
路由、模块化、 Canvas 、 ECMAScript
```

### 59 Js动画与CSS动画区别及相应实现

#### CSS3 的动画的优点

#### 在性能上会稍微好一些，浏览器会对 CSS3 的动画做一些优化

#### 代码相对简单

#### 缺点

#### 在动画控制上不够灵活

#### 兼容性不好

``` 

JavaScript 的动画正好弥补了这两个缺点，控制能力很强，可以单帧的控制、变换，同
时写得好完全可以兼容 IE6 ，并且功能强大。对于一些复杂控制的动画，使用
javascript 会比较靠谱。而在实现一些小的交互动效的时候，就多考虑考虑 CSS 吧
```

### 60 JS 数组和对象的遍历方式，以及几种方式的比较

``` 

通常我们会用循环的方式来遍历数组。但是循环是 导致js 性能问题的原因之
一。一般我们会采用下几种方式来进行数组的遍历
```

``` 

for in 循环
```

``` 

for 循环
```

``` 

forEach
```

``` 

这里的 forEach 回调中两个参数分别为 value ， index
forEach 无法遍历对象
IE不支持该方法； Firefox 和 chrome 支持
forEach 无法使用 break ， continue 跳出循环，且使用 return 是跳过本次循
环
```

``` 

这两种方法应该非常常⻅且使用很频繁。但实际上，这两种方法都存在性能问题
```

``` 

在方式一中， for-in 需要分析出 array 的每个属性，这个操作性能开销很大。用在
key 已知的数组上是非常不划算的。所以尽量不要用 for-in，除非你不清楚要处理哪
些属性，例如 JSON 对象这样的情况
```

``` 

在方式 2 中，循环每进行一次，就要检查一下数组⻓度。读取属性（数组⻓度）要比读局部
变量慢，尤其是当 array 里存放的都是 DOM 元素，因为每次读取都会扫描一遍⻚面上
的选择器相关元素，速度会大大降低
```

### 61 gulp是什么

``` 

gulp 是前端开发过程中一种基于流的代码构建工具，是自动化项目的构建利器；它不仅
能对网站资源进行优化，而且在开发过程中很多重复的任务能够使用正确的工具自动完成
```

``` 

Gulp的核心概念：流
流，简单来说就是建立在面向对象基础上的一种抽象的处理数据的工具。在流中，定义了
一些处理数据的基本操作，如读取数据，写入数据等，程序员是对流进行所有操作的，而
不用关心流的另一头数据的真正流向
gulp正是通过流和代码优于配置的策略来尽量简化任务编写的工作
Gulp的特点：
易于使用 ：通过代码优于配置的策略，gulp 让简单的任务简单，复杂的任务可管理
构建快速 利用 Node.js 流的威力，你可以快速构建项目并减少频繁的 IO 操作
易于学习 通过最少的 API ，掌握 gulp 毫不费力，构建工作尽在掌握：如同一系列
流管道
```

### 62 说一下Vue的双向绑定数据的原理

``` 

vue.js 则是采用数据劫持结合发布者-订阅者模式的方式，通过
Object.defineProperty() 来劫持各个属性的 setter ， getter ，在数据变动时发布
消息给订阅者，触发相应的监听回调
```

### 63 事件的各个阶段

#### 1 ：捕获阶段 ---> 2 ：目标阶段 ---> 3 ：冒泡阶段

``` 

document ---> target 目标 ----> document
由此， addEventListener 的第三个参数设置为 true 和 false的区别已经非常清晰了
true 表示该元素在事件的“捕获阶段”（由外往内传递时）响应事件
false表示该元素在事件的“冒泡阶段”（由内向外传递时）响应事件
```

### 64 let var const

**let**

``` 

允许你声明一个作用域被限制在块级中的变量、语句或者表达式
let绑定不受变量提升的约束，这意味着let声明不会被提升到当前
该变量处于从块开始到初始化处理的“暂存死区”
```

**var**

``` 

声明变量的作用域限制在其声明位置的上下文中，而非声明变量总是全局的
由于变量声明（以及其他声明）总是在任意代码执行之前处理的，所以在代码中的任意位
置声明变量总是等效于在代码开头声明
```

**const**

#### 声明创建一个值的只读引用 (即指针)

``` 

基本数据当值发生改变时，那么其对应的指针也将发生改变，故造成 const申明基本数
据类型时
再将其值改变时，将会造成报错， 例如 const a = 3 ; a = 5时 将会报错
但是如果是复合类型时，如果只改变复合类型的其中某个 Value 项时， 将还是正常使用
```

### 65 快速的让一个数组乱序

### 66 如何渲染几万条数据并不卡住界面

#### 这道题考察了如何在不卡住⻚面的情况下渲染数据，也就是说不能一次性将几

#### 万条都渲染出来，而应该一次渲染部分 DOM ，那么就可以通过

``` 

requestAnimationFrame 来每 16 ms 刷新一次
```

``` js

var arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ];
arr.sort(function(){
return Math.random() - 0.5;
})
console.log(arr);
```

``` 

声明变量的作用域限制在其声明位置的上下文中，而非声明变量总是全局的
由于变量声明（以及其他声明）总是在任意代码执行之前处理的，所以在代码中的任意位
置声明变量总是等效于在代码开头声明
```

``` js

var demo = new Child();
alert(demo.age);
alert(demo.name);//得到被继承的属性
```


### 67 希望获取到⻚面中所有的checkbox怎么做？

#### 不使用第三方框架

### 68 怎样添加、移除、移动、复制、创建和查找节点

#### 创建新节点

``` js

function add() {
// 优化性能，插入不会造成回流
const fragment = document.createDocumentFragment();
for (let i = 0 ; i < once; i++) {
const li = document.createElement("li");
li.innerText = Math.floor(Math.random() * total);
fragment.appendChild(li);
}
ul.appendChild(fragment);
countOfRender += 1 ;
loop();
}
function loop() {
if (countOfRender < loopCount) {
window.requestAnimationFrame(add);
}
}
loop();
}, 0 );
</script>
</body>
</html>
```

``` js

var domList = document.getElementsByTagName(‘input’)
var checkBoxList = [];
var len = domList.length; //缓存到局部变量
while (len--) { //使用while的效率会比for循环更高
if (domList[len].type == ‘checkbox’) {
checkBoxList.push(domList[len]);
}
}
```

#### 添加、移除、替换、插入

#### 查找

### 69 正则表达式

``` 

正则表达式构造函数 var reg=new RegExp(“xxx”) 与正则表达字面量 var
reg=// 有什么不同？匹配邮箱的正则表达式？
```

``` 

当使用 RegExp() 构造函数的时候，不仅需要转义引号（即 \ ”表示”），并且还需要双反
斜杠（即 \\ 表示一个 \ ）。使用正则表达字面量的效率更高
```

邮箱的正则匹配：

### 70 Javascript中callee和caller的作用？

``` 

caller 是返回一个对函数的引用，该函数调用了当前函数；
callee 是返回正在被执行的 function 函数，也就是所指定的 function对象的正文
```

``` js

createDocumentFragment() //创建一个DOM片段
createElement() //创建一个具体的元素
createTextNode() //创建一个文本节点
```

``` js

appendChild() //添加
removeChild() //移除
replaceChild() //替换
insertBefore() //插入
```

``` js

getElementsByTagName() //通过标签名称
getElementsByName() //通过元素的Name属性的值
getElementById() //通过元素Id，唯一性
```

``` js

caller 是返回一个对函数的引用，该函数调用了当前函数；
callee 是返回正在被执行的 function 函数，也就是所指定的 function对象的正文
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

``` 

阻止冒泡：在 W3c 中，使用 stopPropagation() 方法；在IE下设置 cancelBubble =
true
阻止捕获：阻止事件的默认行为，例如 click - <a> 后的跳转。在 W3c 中，使用
preventDefault() 方法，在 IE下设置 window.event.returnValue = false
```

``` js

/** 1. 创建连接 **/
var xhr = null;
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null);
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText);
} else {
/** false **/
fail && fail(xhr.status);
}
}
}
```

#### 那么问题来了？如果一对兔子每月生一对兔子；一对新生兔，从第二个月起就

``` 

开始生兔子；假定每对兔子都是一雌一雄，试问一对兔子，第n个月能繁殖成
多少对兔子？（使用 callee 完成）
```

### 71 window.onload和$(document).ready

``` 

原生 JS 的 window.onload 与 Jquery 的 $(document).ready(function()
{}) 有什么不同？如何用原生JS实现Jq的 ready方法？
```

``` js

window.onload() 方法是必须等到⻚面内包括图片的所有元素加载完毕后才能执行。
$(document).ready() 是 DOM 结构绘制完毕后就执行，不必等到加载完毕
```

``` js

var result=[];
function fn(n){ //典型的斐波那契数列
if(n== 1 ){
return 1 ;
}else if(n== 2 ){
return 1 ;
}else{
if(result[n]){
return result[n];
}else{
//argument.callee()表示fn()
result[n]=arguments.callee(n- 1 )+arguments.callee(n- 2 );
return result[n];
}
}
}
```

``` 

开始生兔子；假定每对兔子都是一雌一雄，试问一对兔子，第n个月能繁殖成
多少对兔子？（使用 callee 完成）
```

### 72 addEventListener()和attachEvent()的区别

``` 

addEventListener() 是符合W 3 C规范的标准方法; attachEvent() 是IE低版本的非标
准方法
addEventListener() 支持事件冒泡和事件捕获; - 而 attachEvent() 只支持事件冒泡
addEventListener() 的第一个参数中,事件类型不需要添加 on ; attachEvent() 需要
添加 'on'
如果为同一个元素绑定多个事件, addEventListener() 会按照事件绑定的顺序依次执行,
attachEvent() 会按照事件绑定的顺序倒序执行
```

### 73 获取⻚面所有的checkbox

### 74 数组去重方法总结

**方法一、利用ES 6 Set去重（ES 6 中最常用）**

**方法二、利用for嵌套for，然后splice去重（ES 5 中最常用）**

#### 双层循环，外层循环元素，内层循环时比较值。值相同时，则删去这个值。

#### 想快速学习更多常用的 ES6 语法

**方法三、利用indexOf去重**

``` 

新建一个空的结果数组， for 循环原数组，判断结果数组是否存在当前元
素，如果有相同的值则跳过，不相同则 push 进数组
```

``` js

function unique(arr){
for(var i= 0 ; i<arr.length; i++){
for(var j=i+ 1 ; j<arr.length; j++){
if(arr[i]==arr[j]){ //第一个等同于第二个，splice方法删除
arr.splice(j, 1 );
j--;
}
}
}
return arr;
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefin
console.log(unique(arr))
//[1, "true", 15, false, undefined, NaN, NaN, "NaN", "a", {...}, {...}]
```


**方法四、利用sort()**

``` 

利用 sort() 排序方法，然后根据排序后的结果进行遍历及相邻元素比对
```

#### 方法五、利用对象的属性不能相同的特点进行去重

``` js

function unique(arr) {
if (!Array.isArray(arr)) {
console.log('type error!')
return;
}
arr = arr.sort()
var arrry= [arr[ 0 ]];
for (var i = 1 ; i < arr.length; i++) {
if (arr[i] !== arr[i- 1 ]) {
arrry.push(arr[i]);
}
}
return arrry;
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefin
console.log(unique(arr))
// [0, 1, 15, "NaN", NaN, NaN, {...}, {...}, "a", false, null, true, "true", un
```

 

 

 

**方法六、利用includes**

**方法七、利用hasOwnProperty**

``` 

利用 hasOwnProperty 判断是否存在对象属性
```

**方法八、利用filter**

#### 方法九、利用递归去重

**方法十、利用Map数据结构去重**

``` js

function unique(arr) {
return arr.filter(function(item, index, arr) {
//当前元素，在原始数组中的第一个索引==当前索引值，否则返回当前元素
return arr.indexOf(item, 0 ) === index;
});
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefin
console.log(unique(arr))
//[1, "true", true, 15, false, undefined, null, "NaN", 0, "a", {...}, {...}]
```

``` js

function unique(arr) {
var array= arr;
var len = array.length;
```

``` js

array.sort(function(a,b){ //排序后更加方便去重
return a - b;
})
```

``` js

function loop(index){
if(index >= 1 ){
if(array[index] === array[index- 1 ]){
array.splice(index, 1 );
}
loop(index - 1 ); //递归loop，然后数组去重
}
}
loop(len- 1 );
return array;
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefin
console.log(unique(arr))
//[1, "a", "true", true, 15, false, 1, {...}, null, NaN, NaN, "NaN", 0, "a",
```

``` js

function arrayNonRepeatfy(arr) {
let map = new Map();
let array = new Array(); // 数组用于返回结果
for (let i = 0 ; i < arr.length; i++) {
if(map .has(arr[i])) { // 如果有该key值
```

``` 

阻止冒泡：在 W3c 中，使用 stopPropagation() 方法；在IE下设置 cancelBubble =
true
阻止捕获：阻止事件的默认行为，例如 click - <a> 后的跳转。在 W3c 中，使用
preventDefault() 方法，在 IE下设置 window.event.returnValue = false
```

 

 

``` 

创建一个空 Map 数据结构，遍历需要去重的数组，把数组的每一个元素作为
key 存到 Map 中。由于 Map 中不会出现相同的 key 值，所以最终得到的就
是去重后的结果
```

**方法十一、利用reduce+includes**

**方法十二、[...new Set(arr)]**

### 75 （设计题）想实现一个对⻚面某个节点的拖曳？如何做？（使用

### 原生JS）

``` 

给需要拖拽的节点绑定 mousedown , mousemove , mouseup 事件
mousedown 事件触发后，开始拖拽
mousemove 时，需要通过 event.clientX 和 clientY 获取拖拽位置，并实时更新位置
mouseup 时，拖拽结束
```

``` js

map .set(arr[i], true);
} else {
map .set(arr[i], false); // 如果没有该key值
array .push(arr[i]);
}
}
return array ;
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefi
console.log(unique(arr))
//[1, "a", "true", true, 15, false, 1, {...}, null, NaN, NaN, "NaN", 0, "a",
```

``` js

function unique(arr) {
return arr.filter(function(item, index, arr) {
//当前元素，在原始数组中的第一个索引==当前索引值，否则返回当前元素
return arr.indexOf(item, 0 ) === index;
});
}
var arr = [ 1 , 1 ,'true','true',true,true, 15 , 15 ,false,false, undefined,undefin
console.log(unique(arr))
//[1, "true", true, 15, false, undefined, null, "NaN", 0, "a", {...}, {...}]
```

创建一个空 Map 数据结构，遍历需要去重的数组，把数组的每一个元素作为
key 存到 Map 中。由于 Map 中不会出现相同的 key 值，所以最终得到的就
是去重后的结果
``` js

/** 1. 创建连接 **/
var xhr = null; 
xhr = new XMLHttpRequest()
/** 2. 连接服务器 **/
xhr.open('get', url, true)
/** 3. 发送请求 **/
xhr.send(null); 
/** 4. 接受请求 **/
xhr.onreadystatechange = function(){
if(xhr.readyState == 4 ){
if(xhr.status == 200 ){
success(xhr.responseText); 
} else {
/** false **/
fail && fail(xhr.status); 
}
}
}

```


#### 需要注意浏览器边界的情况

### 76 Javascript全局函数和全局变量

#### 全局变量

```

Infinity 代表正的无穷大的数值。
NaN 指示某个值是不是数字值。
undefined 指示未定义的值。

```

**全局函数**

```

decodeURI() 解码某个编码的 URI 。
decodeURIComponent() 解码一个编码的 URI 组件。
encodeURI() 把字符串编码为 URI。
encodeURIComponent() 把字符串编码为 URI 组件。
escape() 对字符串进行编码。
eval() 计算 JavaScript 字符串，并把它作为脚本代码来执行。
isFinite() 检查某个值是否为有穷大的数。
isNaN() 检查某个值是否是数字。
Number() 把对象的值转换为数字。
parseFloat() 解析一个字符串并返回一个浮点数。
parseInt() 解析一个字符串并返回一个整数。
String() 把对象的值转换为字符串。
unescape() 对由 escape() 编码的字符串进行解码

```

