# 前端开发面试题（html与css篇）

# HTML部分

### 1. 行内元素（行级元素、内联元素）、行内块元素、块元素各有什么区别。

1. 行内元素：不可以设置宽高，不独立成行，不能设置上下外边距。
2. 行内块元素：可以设置宽高，不独立成行，可以设置上下外边距。
3. 块元素：可以设置宽高，独立成行，可以设置上下外边距。

### 2. html元素的title属性和alt属性都是做什么用的。

1. 设置title属性，鼠标悬浮元素上，会有一个提示信息，提示内容是title的值。
2. img标签可以设置alt属性，当图片无法正常加载是，可以显示alt属性定义的文本内容。

### 3. 清除浮动有哪些方法

1. 为什么设置元素浮动（当前可以用flex布局替换浮动布局）
2. 浮动元素的特性
3. 使用空div清除浮动。
4. overflow：hidden：扩展overflow的属性
5. 伪元素：扩展伪元素的用法，img不可以添加伪元素，js不能操作伪元素

### 4. 盒子模型有哪些常用的属性，如何使用这些属性。

1. margin
2. padding
3. border
4. box-sizing

### 4. HTML5新增了哪些标签

1. 布局：header、footer、section、aside、nav、article
2. 媒体：audio、video
3. 画板：canvus
4. 矢量图：svg

### 5. px、em、rem的区别和用法。

1. px是固定尺寸
2. em参考父级font-size值
3. rem参考html元素font-size值：多用于移动端百分比布局。

### 6. css选择器权重如何判断。

1. 内联样式
2. 嵌入样式
3. 外部样式

### 7 . 如何使用css的定位（position属性）。

1. 绝对定位
2. 相对定位
3. 固定定位
4. 设置参照物

### 8. 让一个div垂直水平居中

1. 使用定位
2. 使用flex布局

``` css
/* 方法一 */
.container {
    width: 500px;
    height: 500px;
    border: 1px solid red;
    position: relative;
}

.box {
    width: 100px;
    height: 100px;
    background-color: blue;
    /* 垂直水平居中 */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

/* 方法二 */
.container {
    width: 500px;
    height: 500px;
    border: 1px solid red;
    display: flex;
    align-items: center;
    justify-content: center;
}

.box {
    width: 100px;
    height: 100px;
    background-color: blue;
}
```

### 9. 让两个块元素在同一行显示有哪些方法

1. 元素浮动：需要清除浮动，如果不熟练，会引入很多新问题。
2. 设置display:inline | inline-block：边距不好控制
3. flex布局：推荐
5. 定位（永远都不要用）

### 10. css3新增了哪些特性

1. 更多的选择器
2. 边框阴影、文字阴影、圆角、渐变
3. transform:translate|scale|rotate
4. 过渡效果：transition
5. 引入外部字体
6. 动画效果
7. 媒体查询
8. flex布局
9. gird布局

### 11. 设置元素透明度有哪些属性

1. rgba：只有当前元素透明
2. opacity：子元素继承透明属性

### 12. display:none和visibility:hidden的区别

1. display:none 隐藏不占位
2. visibility:hidden隐藏占位

### 14. 如何实现一个下拉菜单

主菜单下方的子菜单初始状态高度为零，当鼠标悬浮主菜单是，通过css3的过渡效果，将子菜单的高度设置为正常高度，就可以实现下来菜单的效果了。

### 15. 浏览器的内核有哪些

1、360浏览器bai：Chrome内核和IE内核。

2、百度浏览器：IE和Webkit双内核。

3、QQ浏览器：Chromium内核+IE双内核。

4、猎豹du浏览器：Trident和WebKit。

5、搜狗浏览器：chromium内核。

1、Trident(IE内核)：该内核程序在1997年的IE4中首次被采用，是微软在Mosaic代码的基础之上修改而来的，并沿用到IE11，也被普遍称作”IE内核”。

2、ecko(Firefox内核)：Netscape6开始采用的内核，Gecko的特点是代码完全公开，因此，其可开发程度很高，全世界的程序员都可以为其编写代码，增加功能。

Webkit(Safari内核, Chrome内核原型, 开源): 它是苹果公司自己的内核，也是苹果的Safari浏览器使用的内核。

3、Blink是一个由Google和Opera Software开发的浏览器排版引擎，Google计划将这个渲染引擎作为Chromium计划的一部分，并且在2013年4月的时候公布了这一消息。

### 16. css有哪些属性可以被继承

1. 不可继承的：baidisplay、dumargin、border、padding、background、height、min-height、max- height、width、min-width、max-width、overflow、position、left、right、top、 bottom、float、clear、table-layout、vertical-align、page-break-after、 page-bread-before和unicode-bidi。
2. 所有子元素可继承：visibility和cursor、z-index。
3. 内联元素可继承：letter-spacing、word-spacing、white-space、line-height、color、font、 font-family、font-size、font-style、font-variant、font-weight、text- decoration、text-transform、direction。
4. 块状元素可继承：text-indent和text-align。
5. 列表元素可继承：list-style、list-style-type、list-style-position、list-style-image。
6. 表格元素可继承：border-collapse。

### 17. display有哪些属性。

1. display:none - 隐藏元素
2. display:block - 将元素转换为块元素
3. display:inline - 将元素转换为行内元素
4. display:inline-block - 将元素转换为行内块元素
5. display:flex - 将容器设置为flex容器
6. display:grid - 将容器设置为grid容器

### 18. 网页布局实现：左侧固定，右侧自适应布局。

第一种方法：做成元素设置浮动，右侧元素设置margin-left值为浮动元素宽度。

``` html
<style>
    .box1 {
        height: 200px;
        width: 200px;
        float: left;
        background-color: yellow;
    }

    .box2 {
        height: 200px;
        width: 100%;
        margin-left: 200px;
        background-color: red;
    }
</style>
<div class="container">
    <div class="box1 box"></div>
    <div class="box2 box"></div>
</div>
```

第二种方法：使用flex布局

``` html
<style>
    .container {
        display: flex;
    }

    .box1 {
        height: 200px;
        width: 200px;
        background-color: yellow;
    }

    .box2 {
        height: 200px;
        flex: 1;
        background-color: red;
    }
</style>
<div class="container">
    <div class="box1 box"></div>
    <div class="box2 box"></div>
</div>
```

### 19. 实现一个文字环绕图片的效果

给图片设置浮动即可。

``` html
<style>
    .container {
        width: 300px;
    }

    .container img {
        width: 200px;
        height: 200px;
        float: left;
    }
</style>
<div class="container">
    <img src="晓舟报告.png" alt="">
    <p>晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告晓舟报告</p>
</div>
```

### 20. 前端需要注意哪些SEO

  1. 合理的 title 、 description 、 keywords ：搜索对着三项的权重逐个减⼩， title值强调重点即可，重要关键词出现不要超过2次，⽽且要靠前，不同⻚⾯ title 要有所不 同； description 把⻚⾯内容⾼度概括，⻓度合适，不可过分堆砌关键词，不同⻚⾯

  description 有所不同； keywords 列举出重要关键词即可

  2. 语义化的 HTML 代码，符合W3C规范：语义化代码让搜索引擎容易理解⽹⻚
  3. 重要内容 HTML 代码放在最前：搜索引擎抓取 HTML 顺序是从上到下，有的搜索引擎对抓 取⻓度有限制，保证重要内容⼀定会被抓取
  4. 重要内容不要⽤ js 输出：爬⾍不会执⾏js获取内容
  5. 少⽤ iframe ：搜索引擎不会抓取 iframe 中的内容
  6. ⾮装饰性图⽚必须加 alt
  7. 提⾼⽹站速度：⽹站速度是搜索引擎排序的⼀个重要指标 

### 21. <img> 的 title 和 alt 有什么区别

  1. 通常当⿏标滑动到元素上的时候显示
  2. alt 是 <img> 的特有属性，是图⽚内容的等价描述，⽤于图⽚⽆法加载时显示、读屏器 阅读图⽚。可提图⽚⾼可访问性，除了纯装饰图⽚外都必须设置有意义的值，搜索引擎会 重点分析。 

### 22. HTTP的⼏种请求⽅法⽤途

  1. GET ⽅法

    - 发送⼀个请求来取得服务器上的某⼀资源
  2. POST ⽅法

    - 向 URL 指定的资源提交数据或附加新的数据
  3. PUT ⽅法

    - 跟 POST ⽅法很像，也是想服务器提交数据。但是，它们之间有不同。 PUT 指定了资 源在服务器上的位置，⽽ POST 没有
  4. HEAD ⽅法

    - 只请求⻚⾯的⾸部
  5. DELETE ⽅法

    - 删除服务器上的某资源
  6. OPTIONS ⽅法

    - 它⽤于获取当前 URL 所⽀持的⽅法。如果请求成功，会有⼀个 Allow 的头包含类 似 “GET,POST” 这样的信息
  7. TRACE ⽅法

    - TRACE ⽅法被⽤于激发⼀个远程的，应⽤层的请求消息回路
  7. CONNECT ⽅法

    - 把请求连接转换到透明的 TCP/IP 通道

### 23. 从浏览器地址栏输⼊url到显示⻚⾯的步骤

  1. 基础版本

    - 浏览器根据请求的 URL 交给 DNS 域名解析，找到真实 IP ，向服务器发起请求
    - 服务器交给后台处理完成后返回数据，浏览器接收⽂件（ HTML、JS、CSS 、图象等）；
    - 浏览器对加载到的资源（ HTML、JS、CSS 等）进⾏语法解析，建⽴相应的内部数据结构 （如 HTML 的 DOM ）；
    - 载⼊解析到的资源⽂件，渲染⻚⾯，完成
  2. 详细版 

    - 在浏览器地址栏输⼊URL 
    - 浏览器查看缓存，如果请求资源在缓存中并且新鲜，跳转到转码步骤
    
     1. 如果资源未缓存，发起新请求
     2. 如果已缓存，检验是否⾜够新鲜，⾜够新鲜直接提供给客户端，否则与服务器进⾏验 证。
     3. 检验新鲜通常有两个HTTP头进⾏控制 Expires 和 Cache-Control ：
    
      - HTTP1.0提供Expires，值为⼀个绝对时间表示缓存新鲜⽇期
      - HTTP1.1增加了Cache-Control: max-age=,值为以秒为单位的最⼤新鲜时间
    - 浏览器解析URL获取协议，主机，端⼝，path 
    - 浏览器组装⼀个HTTP（GET）请求报⽂ 
    - 浏览器获取主机ip地址，过程如下：
      - 浏览器缓存
      - 本机缓存
      - hosts⽂件
      - 路由器缓存
      - ISP DNS缓存 
      - DNS递归查询（可能存在负载均衡导致每次IP不⼀样） 
    - 打开⼀个socket与⽬标IP地址，端⼝建⽴TCP链接，三次握⼿如下：
      1. 客户端发送⼀个TCP的SYN=1，Seq=X的包到服务器端⼝
      2. 服务器发回SYN=1， ACK=X+1， Seq=Y的响应包 
      3. 客户端发送ACK=Y+1， Seq=Z 
    - TCP链接建⽴后发送HTTP请求
    - 服务器接受请求并解析，将请求转发到服务程序，如虚拟主机使⽤HTTP Host头部判断请 求的服务程序
    - 服务器检查HTTP请求头是否包含缓存验证信息如果验证缓存新鲜，返回304等对应状态码
    - 处理程序读取完整请求并准备HTTP响应，可能需要查询数据库等操作
    - 服务器将响应报⽂通过TCP连接发送回浏览器
    - 浏览器接收HTTP响应，然后根据情况选择关闭TCP连接或者保留重⽤，关闭TCP连接的四 次握⼿如下：
      1. 主动⽅发送Fin=1， Ack=Z， Seq= X报⽂
      2. 被动⽅发送ACK=X+1， Seq=Z报⽂
      3. 被动⽅发送Fin=1， ACK=X， Seq=Y报⽂ 
      4. 主动⽅发送ACK=Y， Seq=X报⽂
    - 浏览器检查响应状态吗：是否为1XX，3XX， 4XX， 5XX，这些情况处理与2XX不同 
    - 如果资源可缓存，进⾏缓存 
    - 对响应进⾏解码（例如gzip压缩） 
    - 根据资源类型决定如何处理（假设资源为HTML⽂档） 
    - 解析HTML⽂档，构件DOM树，下载资源，构造CSSOM树，执⾏js脚本，这些操作没有严 格的先后顺序，以下分别解释 
    - 构建DOM树： 
      1. Tokenizing：根据HTML规范将字符流解析为标记 
      2. Lexing：词法分析将标记转换为对象并定义属性和规则 
      3. DOM construction：根据HTML标记关系将对象组成DOM树 
    - 解析过程中遇到图⽚、样式表、js⽂件，启动下载 
    - 构建CSSOM树： 
      1. Tokenizing：字符流转换为标记流
      2. Node：根据标记创建节点 
      3. CSSOM：节点创建CSSOM树 
    - 根据DOM树和CSSOM树构建渲染树 : 
      1. 从DOM树的根节点遍历所有可⻅节点，不可⻅节点包括：
          - script , meta 这样本身 不可⻅的标签。   
    
           被css隐藏的节点，如 display: none
    
      2. 对每⼀个可⻅节点，找到恰当的CSSOM规则并应⽤ 
      3. 发布可视节点的内容和计算样式 
    - js解析如下： 
      1. 浏览器创建Document对象并解析HTML，将解析到的元素和⽂本节点添加到⽂档中，此 时document.readystate为loading 
      2. HTML解析器遇到没有async和defer的script时，将他们添加到⽂档中，然后执⾏⾏内 或外部脚本。这些脚本会同步执⾏，并且在脚本下载和执⾏时解析器会暂停。这样就可 以⽤document.write()把⽂本插⼊到输⼊流中。同步脚本经常简单定义函数和注册事件
    
      处理程序，他们可以遍历和操作script和他们之前的⽂档内容 
    
      3. 当解析器遇到设置了async属性的script时，开始下载脚本并继续解析⽂档。脚本会在它 下载完成后尽快执⾏，但是解析器不会停下来等它下载。异步脚本禁⽌使⽤ document.write()，它们可以访问⾃⼰script和之前的⽂档元素 
      4. 当⽂档完成解析，document.readState变成interactive 
      5. 所有defer脚本会按照在⽂档出现的顺序执⾏，延迟脚本能访问完整⽂档树，禁⽌使⽤ document.write() 
      6. 浏览器在Document对象上触发DOMContentLoaded事件
      7. 此时⽂档完全解析完成，浏览器可能还在等待如图⽚等内容加载，等这些内容完成载⼊ 并且所有异步脚本完成载⼊和执⾏，document.readState变为complete，window触发 load事件
    - 显示⻚⾯（HTML解析过程中会逐步显示⻚⾯） 
  3. 详细简版 

    - 从浏览器接收 url 到开启⽹络请求线程（这⼀部分可以展开浏览器的机制以及进程与线程 之间的关系） 
    - 开启⽹络线程到发出⼀个完整的 HTTP 请求（这⼀部分涉及到dns查询， TCP/IP 请求， 五层因特⽹协议栈等知识） 
    - 从服务器接收到请求到对应后台接收到请求（这⼀部分可能涉及到负载均衡，安全拦截以
    
    及后台内部的处理等等） 
    
    - 后台和前台的 HTTP 交互（这⼀部分包括 HTTP 头部、响应码、报⽂结构、 cookie 等知 识，可以提下静态资源的 cookie 优化，以及编码解码，如 gzip 压缩等）
    - 单独拎出来的缓存问题， HTTP 的缓存（这部分包括http缓存头部， ETag ， catch￾control 等） 
    - 浏览器接收到 HTTP 数据包后的解析流程（解析 html -词法分析然后解析成 dom 树、解 析 css ⽣成 css 规则树、合并成 render 树，然后 layout 、 painting 渲染、复合图 层的合成、 GPU 绘制、外链资源的处理、 loaded 和 DOMContentLoaded 等） 
    - CSS 的可视化格式模型（元素的渲染规则，如包含块，控制框， BFC ， IFC 等概念） 
    - JS 引擎解析过程（ JS 的解释阶段，预处理阶段，执⾏阶段⽣成执⾏上下⽂， VO ，作 ⽤域链、回收机制等等） 
    - 其它（可以拓展不同的知识模块，如跨域，web安全， hybrid 模式等等内容） 

### 24. 如何进⾏⽹站性能优化

  + content ⽅⾯ 
    - 减少 HTTP 请求：合并⽂件、 CSS 精灵、 inline Image
    - 减少 DNS 查询： DNS 缓存、将资源分布到恰当数量的主机名 
    - 减少 DOM 元素数量

  + Server ⽅⾯ 
    - 使⽤ CDN
    - 配置 ETag
    - 对组件使⽤ Gzip 压缩
  + Cookie ⽅⾯ 
    - 减⼩ cookie ⼤⼩
  + css ⽅⾯ 
    - 将样式表放到⻚⾯顶部 
    - 不使⽤ CSS 表达式 
    - 使⽤ <link> 不使⽤ @import
  + Javascript ⽅⾯ 
    - 将脚本放到⻚⾯底部 
    - 将 javascript 和 css 从外部引⼊ 
    - 压缩 javascript 和 css
    - 删除不需要的脚本
    - 减少 DOM 访问 
  + 图⽚⽅⾯ 
    - 优化图⽚：根据实际颜⾊需要选择⾊深、压缩 
    - 优化 css 精灵 
    - 不要在 HTML 中拉伸图⽚ 

### 25. HTTP状态码及其含义

  + 1XX ：信息状态码
    - 100 Continue 继续，⼀般在发送 post 请求时，已发送了 http header 之后服务端 将返回此信息，表示确认，之后发送具体参数信息
  + 2XX ：成功状态码
    - 200 OK 正常返回信息
    - 201 Created 请求成功并且服务器创建了新的资源
    - 202 Accepted 服务器已接受请求，但尚未处理
  + 3XX ：重定向
    - 301 Moved Permanently 请求的⽹⻚已永久移动到新位置。
    - 302 Found 临时性重定向。
    - 303 See Other 临时性重定向，且总是使⽤ GET 请求新的 URI 。
    - 304 Not Modified ⾃从上次请求后，请求的⽹⻚未修改过。
  + 4XX ：客户端错误
    - 400 Bad Request 服务器⽆法理解请求的格式，客户端不应当尝试再次使⽤相同的内 容发起请求。
    - 401 Unauthorized 请求未授权。
    - 403 Forbidden 禁⽌访问。
    - 404 Not Found 找不到如何与 URI 相匹配的资源。
  + 5XX: 服务器错误
    - 500 Internal Server Error 最常⻅的服务器端错误。
    - 503 Service Unavailable 服务器端暂时⽆法处理请求（可能是过载或维护）。 

### 26. 语义化的理解 

  + ⽤正确的标签做正确的事情！
  + HTML 语义化就是让⻚⾯的内容结构化，便于对浏览器、搜索引擎解析； 
  + 在没有样式 CSS 情况下也以⼀种⽂档格式显示，并且是容易阅读的。 
  + 搜索引擎的爬⾍依赖于标记来确定上下⽂和各个关键字的权重，利于 SEO 。 
  + 使阅读源代码的⼈对⽹站更容易将⽹站分块，便于阅读维护理解

### 27. 介绍⼀下你对浏览器内核的理解？ 

  + 主要分成两部分：渲染引擎( layout engineer 或 Rendering Engine )和 JS 引擎 
  + 渲染引擎：负责取得⽹⻚的内容（ HTML 、 XML 、图像等等）、整理讯息（例如加⼊CSS 等），以及计算⽹⻚的显示⽅式，然后会输出⾄显示器或打印机。浏览器的内核的不 同对于⽹⻚的语法解释会有不同，所以渲染的效果也不相同。所有⽹⻚浏览器、电⼦邮件 客户端以及其它需要编辑、显示⽹络内容的应⽤程序都需要内核
  + JS 引擎则：解析和执⾏ javascript 来实现⽹⻚的动态效果 
  + 最开始渲染引擎和 JS 引擎并没有区分的很明确，后来JS引擎越来越独⽴，内核就倾向于 只指渲染引擎 

### 28. html5有哪些新特性、移除了那些元素？

  + HTML5 现在已经不是 SGML 的⼦集，主要是关于图像，位置，存储，多任务等功能的增 加 
    - 绘画 canvas
    - ⽤于媒介回放的 video 和 audio 元素 
    - 本地离线存储 localStorage ⻓期存储数据，浏览器关闭后数据不丢失
    - sessionStorage 的数据在浏览器关闭后⾃动删除 
    - 语意化更好的内容元素，⽐如 article 、 footer 、 header 、 nav 、 section
    - 表单控件， calendar 、 date 、 time 、 email 、 url 、 search
    - 新的技术 webworker 、 websocket 、 Geolocation
  + 移除的元素： 
    - 纯表现的元素： basefont 、 big 、 center 、 font 、 s 、 strike 、 tt 、 u 
    - 对可⽤性产⽣负⾯影响的元素： frame 、 frameset 、 noframes
  + ⽀持 HTML5 新标签：
    - IE8/IE7/IE6 ⽀持通过 document.createElement ⽅法产⽣的标签 
    - 可以利⽤这⼀特性让这些浏览器⽀持 HTML5 新标签 
    - 浏览器⽀持新标签后，还需要添加标签默认的样式 
  + 当然也可以直接使⽤成熟的框架、⽐如 html5shim

### 29. HTML5 的离线储存怎么使⽤，⼯作原理能不能解释⼀下？ 

  + 在⽤户没有与因特⽹连接时，可以正常访问站点或应⽤，在⽤户与因特⽹连接时，更新⽤ 户机器上的缓存⽂件 
  + 原理： HTML5 的离线存储是基于⼀个新建的 .appcache ⽂件的缓存机制(不是存储技 术)，通过这个⽂件上的解析清单离线存储资源，这些资源就会像 cookie ⼀样被存储了下 来。之后当⽹络在处于离线状态下时，浏览器会通过被离线存储的数据进⾏⻚⾯展示 
  + 如何使⽤：
    - ⻚⾯头部像下⾯⼀样加⼊⼀个 manifest 的属性； 
    - 在 cache.manifest ⽂件的编写离线存储的资源 
    - 在离线状态时，操作 window.applicationCache 进⾏需求实现 

    

``` html
      CACHE MANIFEST
      #v0.11
      CACHE:
      js/app.js
      css/style.css
      NETWORK:
      resourse/logo.png
      FALLBACK:
      /offline.html
```

​    

### 30. 浏览器是怎么对 HTML5 的离线储存资源进⾏管理和加载的呢 

  + 在线的情况下，浏览器发现 html 头部有 manifest 属性，它会请求 manifest ⽂件，如果是第⼀次访问 app ，那么浏览器就会根据manifest⽂件的内容下载相应的资源并且进⾏ 离线存储。如果已经访问过 app 并且资源已经离线存储了，那么浏览器就会使⽤离线的资 源加载⻚⾯，然后浏览器会对⽐新的 manifest ⽂件与旧的 manifest ⽂件，如果⽂件没 有发⽣改变，就不做任何操作，如果⽂件改变了，那么就会重新下载⽂件中的资源并进⾏ 离线存储。 
  + 离线的情况下，浏览器就直接使⽤离线存储的资源。 

### 31. 请描述⼀下 cookies ， sessionStorage 和 localStorage 的区别？

  + cookie 是⽹站为了标示⽤户身份⽽储存在⽤户本地终端（Client Side）上的数据（通常 经过加密） 
  + cookie数据始终在同源的http请求中携带（即使不需要），记会在浏览器和服务器间来回 传递
  + sessionStorage 和 localStorage 不会⾃动把数据发给服务器，仅在本地保存 
  + 存储⼤⼩：
    - cookie 数据⼤⼩不能超过4k
    - sessionStorage 和 localStorage 虽然也有存储⼤⼩的限制，但⽐ cookie ⼤得 多，可以达到5M或更⼤
  + 有期时间：
    - localStorage 存储持久数据，浏览器关闭后数据不丢失除⾮主动删除数据
    - sessionStorage 数据在当前浏览器窗⼝关闭后⾃动删除
    - cookie 设置的 cookie 过期时间之前⼀直有效，即使窗⼝或浏览器关闭 

### 32. iframe有那些缺点？

  + iframe 会阻塞主⻚⾯的 Onload 事件
  + 搜索引擎的检索程序⽆法解读这种⻚⾯，不利于 SEO
  + iframe 和主⻚⾯共享连接池，⽽浏览器对相同域的连接有限制，所以会影响⻚⾯的并⾏ 加载
  + 使⽤ iframe 之前需要考虑这两个缺点。如果需要使⽤ iframe ，最好是通过javascript 动态给 iframe 添加 src 属性值，这样可以绕开以上两个问题

### 33. WEB标准以及W3C标准是什么? 

  + 标签闭合、标签⼩写、不乱嵌套、使⽤外链 css 和 js 、结构⾏为表现的分离 

### 34. xhtml和html有什么区别?

  + ⼀个是功能上的差别 
    - 主要是 XHTML 可兼容各⼤浏览器、⼿机以及 PDA ，并且浏览器也能快速正确地编译⽹ ⻚ 
  + 另外是书写习惯的差别
    - XHTML 元素必须被正确地嵌套，闭合，区分⼤⼩写，⽂档必须拥有根元素 

### 35. Doctype作⽤? 严格模式与混杂模式如何区分？它们有何意义?

  + ⻚⾯被加载的时， link 会同时被加载，⽽ @imort ⻚⾯被加载的时， link 会同时被加 载，⽽ @import 引⽤的 CSS 会等到⻚⾯被加载完再加载 import 只在 IE5 以上才能识 别，⽽ link 是 XHTML 标签，⽆兼容问题 link ⽅式的样式的权重 ⾼于 @import 的权 重
  + <! DOCTYPE> 声明位于⽂档中的最前⾯，处于 <html> 标签之前。告知浏览器的解析 器， ⽤什么⽂档类型 规范来解析这个⽂档 
  + 严格模式的排版和 JS 运作模式是 以该浏览器⽀持的最⾼标准运⾏
  + 在混杂模式中，⻚⾯以宽松的向后兼容的⽅式显示。模拟⽼式浏览器的⾏为以防⽌站点⽆ 法⼯作。 DOCTYPE 不存在或格式不正确会导致⽂档以混杂模式呈现

### 36. ⾏内元素有哪些？块级元素有哪些？ 空(void)元素有那些？⾏内元 素和块级元素有什么区别？ 

  + ⾏内元素有： a b span img input select strong
  + 块级元素有： div ul ol li dl dt dd h1 h2 h3 h4… p
  + 空元素： <br> <hr> <img> <input> <link> <meta>
  + ⾏内元素不可以设置宽⾼，不独占⼀⾏ 
  + 块级元素可以设置宽⾼，独占⼀⾏ 

### 37. HTML全局属性(global attribute)有哪些

  + class : 为元素设置类标识
  + data-* : 为元素增加⾃定义属性
  + draggable : 设置元素是否可拖拽
  + id : 元素 id ，⽂档内唯⼀
  + lang : 元素内容的的语⾔
  + style : ⾏内 css 样式
  + title : 元素相关的建议信息

### 38. Canvas和SVG有什么区别？

  + svg 绘制出来的每⼀个图形的元素都是独⽴的 DOM 节点，能够⽅便的绑定事件或⽤来修 改。 canvas 输出的是⼀整幅画布
  + svg 输出的图形是⽮量图形，后期可以修改参数来⾃由放⼤缩⼩，不会失真和锯⻮。⽽canvas 输出标量画布，就像⼀张图⽚⼀样，放⼤会失真或者锯⻮

### 39. HTML5 为什么只需要写 <! DOCTYPE HTML>

  + HTML5 不基于 SGML ，因此不需要对 DTD 进⾏引⽤，但是需要 doctype 来规范浏览器 的⾏为
  + ⽽ HTML4.01 基于 SGML , 所以需要对 DTD 进⾏引⽤，才能告知浏览器⽂档所使⽤的⽂档 类型

### 40. 如何在⻚⾯上实现⼀个圆形的可点击区域？

  + svg
  + border-radius
  + 纯 js 实现 需要求⼀个点在不在圆上简单算法、获取⿏标坐标等等

### 41. ⽹⻚验证码是⼲嘛的，是为了解决什么安全问题

  + 区分⽤户是计算机还是⼈的公共全⾃动程序。可以防⽌恶意破解密码、刷票、论坛灌⽔
  + 有效防⽌⿊客对某⼀个特定注册⽤户⽤特定程序暴⼒破解⽅式进⾏不断的登陆尝试

### 42. viewport 

  

``` HTML
  <meta name="viewport" content="width=device-width, initial-scale=1.0, minimu
 // width 设置viewport宽度，为⼀个正整数，或字符串‘device-width’
 // device-width 设备宽度
 // height 设置viewport⾼度，⼀般设置了宽度，会⾃动解析出⾼度，可以不⽤设置
 // initial-scale 默认缩放⽐例（初始缩放⽐例），为⼀个数字，可以带⼩数
 // minimum-scale 允许⽤户最⼩缩放⽐例，为⼀个数字，可以带⼩数
 // maximum-scale 允许⽤户最⼤缩放⽐例，为⼀个数字，可以带⼩数
 // user-scalable 是否允许⼿动缩放 js
  
```

  + 延伸提问 
    - 怎样处理 移动端 1px 被 渲染成 2px 问题

  + 局部处理
    - mate 标签中的 viewport 属性 ， initial-scale 设置为 1
    - rem 按照设计稿标准⾛，外加利⽤ transfrome 的 scale(0.5) 缩⼩⼀倍即可； 
  + 全局处理
    - mate 标签中的 viewport 属性 ， initial-scale 设置为 0.5
    - rem 按照设计稿标准⾛即可

### 43 渲染优化 

  + 禁⽌使⽤ iframe （阻塞⽗⽂档 onload 事件）
    - iframe 会阻塞主⻚⾯的 Onload 事件
    - 搜索引擎的检索程序⽆法解读这种⻚⾯，不利于SEO
    - iframe 和主⻚⾯共享连接池，⽽浏览器对相同域的连接有限制，所以会影响⻚⾯的并 ⾏加载 
    - 使⽤ iframe 之前需要考虑这两个缺点。如果需要使⽤ iframe ，最好是通过javascript
    - 动态给 iframe 添加 src 属性值，这样可以绕开以上两个问题
  + 禁⽌使⽤ gif 图⽚实现 loading 效果（降低 CPU 消耗，提升渲染性能） 
  + 使⽤ CSS3 代码代替 JS 动画（尽可能避免重绘重排以及回流） 
  + 对于⼀些⼩图标，可以使⽤base64位编码，以减少⽹络请求。但不建议⼤图使⽤，⽐较耗 费 CPU
    - ⼩图标优势在于 
      + 减少 HTTP 请求 
      + 避免⽂件跨域 
      + 修改及时⽣效
  + ⻚⾯头部的 <style></style> <script></script> 会阻塞⻚⾯；（因为 Renderer进程中 JS 线程和渲染线程是互斥的）
  + ⻚⾯中空的 href 和 src 会阻塞⻚⾯其他资源的加载 (阻塞下载进程)
  + ⽹⻚ gzip ， CDN 托管， data 缓存 ，图⽚服务器
  + 前端模板 JS+数据，减少由于 HTML 标签导致的带宽浪费，前端⽤变量保存AJAX请求结 果，每次操作本地变量，不⽤请求，减少请求次数
  + ⽤ innerHTML 代替 DOM 操作，减少 DOM 操作次数，优化 javascript 性能
  + 当需要设置的样式很多时设置 className ⽽不是直接操作 style
  + 少⽤全局变量、缓存 DOM 节点查找的结果。减少 IO 读取操作
  + 图⽚预加载，将样式表放在顶部，将脚本放在底部 加上时间戳 对普通的⽹站有⼀个统⼀的思路，就是尽量向前端优化、减少数据库操作、减少磁盘 IO

### 44 meta viewport相关

``` 

<!DOCTYPE html> <!--H5标准声明，使用 HTML5 doctype，不区分大小写-->
<head lang=”en”> <!--标准的 lang 属性写法-->
<meta charset=’utf-8′> <!--声明文档使用的字符编码-->
<meta http-equiv=”X-UA-Compatible” content=”IE=edge,chrome=1′′/> <!--优先使
<meta name=”description” content=”不超过 150 个字符”/> <!--⻚面描述-->
<meta name=”keywords” content=””/> <!-- ⻚面关键词-->
<meta name=”author” content=”name, email@gmail.com”/> <!--网⻚作者-->
<meta name=”robots” content=”index,follow”/> <!--搜索引擎抓取-->
<meta name=”viewport” content=”initial-scale=1, maximum-scale=3, minimum-sc
<meta name=”apple-mobile-web-app-title” content=”标题”> <!--iOS 设备 begin-->
<meta name=”apple-mobile-web-app-capable” content=”yes”/> <!--添加到主屏后的标
是否启用 WebApp 全屏模式，删除苹果默认的工具栏和菜单栏-->
<meta name=”apple-itunes-app” content=”app-id=myAppStoreID, affiliate-data=
<!--添加智能 App 广告条 Smart App Banner（iOS 6+ Safari）-->
<meta name=”apple-mobile-web-app-status-bar-style” content=”black”/>
<meta name=”format-detection” content=”telphone=no, email=no”/> <!--设置苹果
<meta name=”renderer” content=”webkit”> <!-- 启用 360 浏览器的极速模式(webkit)-->
<meta http-equiv=”X-UA-Compatible” content=”IE=edge”> <!--避免IE使用兼容模
<meta http-equiv=”Cache-Control” content=”no-siteapp” /> <!--不让百度转码-
<meta name=”HandheldFriendly” content=”true”> <!--针对手持设备优化，主要是针
<meta name=”MobileOptimized” content=”320′′> <!--微软的老式浏览器-->
<meta name=”screen-orientation” content=”portrait”> <!--uc强制竖屏-->
<meta name=”x5-orientation” content=”portrait”> <!--QQ强制竖屏-->
<meta name=”full-screen” content=”yes”> <!--UC强制全屏-->
<meta name=”x5-fullscreen” content=”true”> <!--QQ强制全屏-->
<meta name=”browsermode” content=”application”> <!--UC应用模式-->
<meta name=”x5-page-mode” content=”app”> <!-- QQ应用模式-->
<meta name=”msapplication-tap-highlight” content=”no”> <!--windows phone
设置⻚面不缓存-->
<meta http-equiv=”pragma” content=”no-cache”>
<meta http-equiv=”cache-control” content=”no-cache”>
<meta http-equiv=”expires” content=”0′′>
```

### 45 你做的⻚面在哪些流览器测试过？这些浏览器的内核分别是什么?

``` 

* IE : trident 内核
* Firefox ： gecko内核
* Safari : webkit 内核
* Opera :以前是 presto 内核， Opera 现已改用Google - Chrome 的 Blink 内核
* Chrome:Blink (基于 webkit ，Google与Opera Software共同开发)

```

### 46 div+css的布局较table布局有什么优点？

``` 

* 改版的时候更方便 只要改 css 文件。
* ⻚面加载速度更快、结构化清晰、⻚面显示简洁。
* 表现与结构相分离。
* 易于优化（ seo ）搜索引擎更友好，排名更容易靠前。

```

### 47 a：img的alt与title有何异同？b：strong与em的异同？

``` 

alt(alt text) :为不能显示图像、窗体或 applets 的用户代理（ UA ）， alt 属性用
来指定替换文字。替换文字的语言由 lang 属性指定。(在IE浏览器下会在没有 title 时
把 alt 当成 tool tip显示)
```

``` 

title(tool tip) :该属性为设置该属性的元素提供建议性的信息
```

``` 

strong :粗体强调标签，强调，表示内容的重要性
```

``` 

em :斜体强调标签，更强烈强调，表示内容的强调点
```

### 48 你能描述一下渐进增强和优雅降级之间的不同吗

``` 

渐进增强：针对低版本浏览器进行构建⻚面，保证最基本的功能，然后再针对高级浏览器
进行效果、交互等改进和追加功能达到更好的用户体验。
```

``` 

优雅降级：一开始就构建完整的功能，然后再针对低版本浏览器进行兼容。
```

``` 

 区别：优雅降级是从复杂的现状开始，并试图减少用户体验的供给，而渐进增强则是从一个非常基础的，能够起作用的版本开始，并不断扩充，以适应未来环境的需要。降级（功能衰减）意味着往回看；而渐进增强则意味着朝前看，同时保证其根基处于安全地带
```

### 49 为什么利用多个域名来存储网站资源会更有效？

``` 

CDN 缓存更方便
```

``` 

突破浏览器并发限制
```

``` 

节约 cookie 带宽
```

``` 

节约主域名的连接数，优化⻚面响应速度
```

``` 

防止不必要的安全问题
```

### 50 简述一下src与href的区别

``` 

src 用于替换当前元素，href用于在当前文档和引用资源之间确立联系。
```

``` 

src 是 source 的缩写，指向外部资源的位置，指向的内容将会嵌入到文档中当前标签所
在位置；在请求 src 资源时会将其指向的资源下载并应用到文档内，例如 js 脚本，
img 图片和 frame 等元素
```

``` 

<script src ="js.js"></script> 当浏览器解析到该元素时，会暂停其他
资源的下载和处理，直到将该资源加载、编译、执行完毕，图片和框架等元素
也如此，类似于将所指向资源嵌入当前标签内。这也是为什么将js脚本放在底
部而不是头部
```

``` 

href 是 Hypertext Reference 的缩写，指向网络资源所在位置，建立和当前元素（锚
点）或当前文档（链接）之间的链接，如果我们在文档中添加
```

``` 

<link href="common.css" rel="stylesheet"/> 那么浏览器会识别该文档为 css 文
件，就会并行下载资源并且不会停止对当前文档的处理。这也是为什么建议使用 link 方
式来加载 css ，而不是使用 @import 方式
```

### 51 知道的网⻚制作会用到的图片格式有哪些？

``` 

png-8 、 png-24 、 jpeg 、 gif 、 svg
```

#### 但是上面的那些都不是面试官想要的最后答案。面试官希望听到是

``` 

Webp , Apng 。（是否有关注新技术，新鲜事物）
```

``` 

Webp ： WebP 格式，谷歌（google）开发的一种旨在加快图片加载速度的图片格式。图
片压缩体积大约只有 JPEG 的 2/3 ，并能节省大量的服务器带宽资源和数据空间。
Facebook Ebay 等知名网站已经开始测试并使用 WebP 格式。
```

``` 

在质量相同的情况下，WebP格式图像的体积要比JPEG格式图像小 40% 。
```

``` 

Apng ：全称是 “Animated Portable Network Graphics” , 是PNG的位图动画扩展，可
以实现png格式的动态图片效果。 04 年诞生，但一直得不到各大浏览器厂商的支持，直到
日前得到 iOS safari 8的支持，有望代替 GIF 成为下一代动态图标准
```

### 52 在css/js代码上线之后开发人员经常会优化性能，从用户刷新网⻚开始，一次js请求一般情况下有哪些地方会有缓存处理？

``` 

dns 缓存， cdn 缓存，浏览器缓存，服务器缓存
```

### 53 一个⻚面上有大量的图片（大型电商网站），加载很慢，你有哪些方法优化这些图片的加载，给用户更好的体验。

``` 

图片懒加载，在⻚面上的未可视区域可以添加一个滚动事件，判断图片位置与浏览器顶端的距离与⻚面的距离，如果前者小于后者，优先加载。如果为幻灯片、相册等，可以使用图片预加载技术，将当前展示图片的前一张和后一张优先下载。
```

``` 

如果图片为css图片，可以使用 CSSsprite ， SVGsprite ， Iconfont、 Base64 等技
术。
```

``` 

如果图片过大，可以使用特殊编码的图片，加载时会先加载一张压缩的特别厉害的缩略
图，以提高用户体验。
```

``` 

如果图片展示区域小于图片的真实大小，则因在服务器端根据业务需要先行进行图片压
缩，图片压缩后大小与展示一致。
```

### 54 常⻅排序算法的时间复杂度, 空间复杂度

### 55 web开发中会话跟踪的方法有哪些

``` 

cookie
session
url 重写
隐藏 input
ip 地址
```

### 56 HTTP request报文结构是怎样的

 

1. 首行是 Request-Line 包括： 请求方法 ， 请求URI ， 协议版本 ， CRLF
2. 首行之后是若干行 请求头 ，包括 general-header ， request-header 或者 entity-header ，每个一行以CRLF结束
3. 请求头和消息实体之间有一个 CRLF分隔
4. 根据实际请求需要可能包含一个 消息实体 一个请求报文例子如下：

``` 

GET /Protocols/rfc2616/rfc2616-sec5.html HTTP/1.1
Host: www.w3.org
Connection: keep-alive
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, 
Referer: https://www.google.com.hk/
Accept-Encoding: gzip,deflate,sdch
Accept-Language: zh-CN,zh;q=0.8,en;q=0.6
Cookie: authorstyle=yes
If-None-Match: "2cc8-3e3073913b100"
If-Modified-Since: Wed, 01 Sep 2004 13:24:52 GMT
name=qiu&age=25
```

### 57 HTTP response报文结构是怎样的

#### 首行是状态行包括： HTTP版本，状态码，状态描述 ，后面跟一个CRLF

#### 首行之后是 若干行响应头 ，包括： 通用头部，响应头部，实体头部

#### 响应头部和响应实体之间用 一个CRLF空行 分隔

#### 最后是一个可能的 消息实体 响应报文例子如下：

``` 

HTTP/1.1 200 OK
Date: Tue, 08 Jul 2014 05:28:43 GMT
Server: Apache/2
Last-Modified: Wed, 01 Sep 2004 13:24:52 GMT
ETag: "40d7-3e3073913b100"
Accept-Ranges: bytes
Content-Length: 16599
Cache-Control: max-age=21600
Expires: Tue, 08 Jul 2014 11:28:43 GMT
P3P: policyref="http://www.w3.org/2001/05/P3P/p3p.xml"
Content-Type: text/html; charset=iso-8859-1
{"name": "qiu", "age": 25}
```

# css部分

### 1 css sprite是什么, 有什么优缺点

``` 

概念：将多个小图片拼接到一个图片中。通过 background-position 和元素尺寸调节需
要显示的背景图案。

```

``` 

优点：
```

``` 

减少 HTTP 请求数，极大地提高⻚面加载速度
增加图片信息重复度，提高压缩比，减少图片大小
```

``` 

更换⻛格方便，只需在一张或几张图片上修改颜色或样式即可实现
```

``` 

缺点：
```

#### 图片合并麻烦

#### 维护麻烦，修改一个图片可能需要从新布局整个图片，样式

### 2 display: none; 与 visibility: hidden; 的区别

#### 联系：它们都能让元素不可⻅

#### 区别：

``` 

display:none ;会让元素完全从渲染树中消失，渲染的时候不占据任何空间；
visibility: hidden;不会让元素从渲染树消失，渲染师元素继续占据空间，只是内
容不可⻅
display: none ;是非继承属性，子孙节点消失由于元素从渲染树消失造成，通过修改
子孙节点属性无法显示 ；visibility: hidden; 是继承属性，子孙节点消失由于继承
了 hidden ，通过设置 visibility: visible; 可以让子孙节点显式
修改常规流中元素的 display 通常会造成文档重排。修改 visibility 属性只会造成
本元素的重绘。
读屏器不会读取 display: none ;元素内容；会读取 visibility: hidden; 元素内容
```

### 3 link 与 @import 的区别

``` 

1. link 是 HTML 方式， @import 是CSS方式
2. link 最大限度支持并行下载， @import 过多嵌套导致串行下载，出现 FOUC (文档样式

短暂失效)

3. link 可以通过 rel="alternate stylesheet" 指定候选样式
4. 浏览器对 link 支持早于 @import ，可以使用 @import 对老浏览器隐藏样式
5. @import 必须在样式规则之前，可以在css文件中引用其他文件
6. 总体来说： link 优于 @import

```

### 4 什么是FOUC? 如何避免

``` 

Flash Of Unstyled Content ：用户定义样式表加载之前浏览器使用默认样式显示文
档，用户样式加载渲染之后再从新显示文档，造成⻚面闪烁。
解决方法 ：把样式表放到文档的 <head>
```

### 5 如何创建块级格式化上下文(block formatting context), BFC有什么用

#### 创建规则：

#### 根元素

``` 

浮动元素（ float不取值为 none ）

绝对定位元素（ position取值为 absolute 或 fixed ）

display 取值为 inline-block 、 table-cell 、 table-caption 、 flex 、

inline-flex之一的元素

overflow不取值为 visible 的元素
```

``` 

作用：
```

``` 

可以包含浮动元素

不被浮动元素覆盖

阻止父子元素的 margin 折叠

```

### 6 display、float、position的关系

``` 

如果 display 取值为 none ，那么 position和 float 都不起作用，这种情况下元素不
产生框
否则，如果 position 取值为 absolute 或者 fixed，框就是绝对定位的， float 的计
算值为 none ， display 根据下面的表格进行调整。
否则，如果 float 不是 none ，框是浮动的， display 根据下表进行调整
否则，如果元素是根元素， display 根据下表进行调整
其他情况下 display 的值为指定值
总结起来： 绝对定位、浮动、根元素都需要调整 display
```

### 7 清除浮动的几种方式，各自的优缺点

``` 

父级 div 定义 height

结尾处加空 div 标签 clear:both

父级 div 定义伪类 :after 和 zoom

父级 div 定义 overflow:hidden

父级 div 也浮动，需要定义宽度

结尾处加 br 标签 clear:both

```

#### 比较好的是第 3 种方式，好多网站都这么用

### 8 为什么要初始化CSS样式?

#### 因为浏览器的兼容问题，不同浏览器对有些标签的默认值是不同的，如果没对 CSS 初始化

#### 往往会出现浏览器之间的⻚面显示差异。

#### 当然，初始化样式会对 SEO 有一定的影响，但⻥和熊掌不可兼得，但力求影响最小的情况

#### 下初始化

### 9 css 3 有哪些新特性

``` 

新增各种 css 选择器

圆⻆ border-radius

多列布局

阴影和反射

文字特效 text-shadow

线性渐变

旋转 transform

```

**CSS 3 新增伪类有那些？**

``` 

p:first-of-type 选择属于其父元素的首个 <p> 元素的每个 <p> 元素。

p:last-of-type 选择属于其父元素的最后 <p> 元素的每个 <p> 元素。

p:only-of-type 选择属于其父元素唯一的 <p> 元素的每个 <p> 元素。

p:only-child 选择属于其父元素的唯一子元素的每个 <p> 元素。

p:nth-child(2) 选择属于其父元素的第二个子元素的每个 <p> 元素。

:after 在元素之前添加内容,也可以用来做清除浮动。

:before 在元素之后添加内容。

:enabled 已启用的表单元素。

:disabled 已禁用的表单元素。

:checked 单选框或复选框被选中。

```

### 10 display有哪些值？说明他们的作用

``` 

block 转换成块状元素。

inline 转换成行内元素。

none 设置元素不可⻅。

inline-block 象行内元素一样显示，但其内容象块类型元素一样显示。

list-item 象块类型元素一样显示，并添加样式列表标记。

```

``` 

table 此元素会作为块级表格来显示
inherit 规定应该从父元素继承 display 属性的值
```

### 11 介绍一下标准的CSS的盒子模型？低版本IE的盒子模型有什么不同

### 的？

#### 有两种， IE盒子模型、 W3C 盒子模型；

``` 

盒模型： 内容(content)、填充(padding )、边界(margin )、 边框( border )；

区 别： IE的c ontent 部分把 border 和 padding 计算了进去;
```

### 12 CSS优先级算法如何计算？

#### 优先级就近原则，同权重情况下样式定义最近者为准

#### 载入样式以最后载入的定位为准

``` 

优先级为: !important > id > class > tag ; !important 比 内联优先级高
```

### 13 对BFC规范的理解？

#### 它决定了元素如何对其内容进行定位, 以及与其他元素的关系和相互作用

### 14 谈谈浮动和清除浮动

#### 浮动的框可以向左或向右移动，直到他的外边缘碰到包含框或另一个浮动框的边框为止。

#### 由于浮动框不在文档的普通流中，所以文档的普通流的块框表现得就像浮动框不存在一

#### 样。浮动的块框会漂浮在文档普通流的块框上

### 15 position的值， relative和absolute定位原点是

``` 

absolute ：生成绝对定位的元素，相对于 static 定位以外的第一个父元素进行定位

fixed ：生成绝对定位的元素，相对于浏览器窗口进行定位

relative ：生成相对定位的元素，相对于其正常位置进行定位

static 默认值。没有定位，元素出现在正常的流中

inherit 规定从父元素继承 position 属性的值

```

### 16 display:inline-block 什么时候不会显示间隙？(携程)

#### 移除空格

``` 

使用 margin 负值
```

``` 

使用 font-size:0
letter-spacing
word-spacing
```

### 17 PNG\GIF\JPG的区别及如何选

``` 

GIF :
```

``` 

8 位像素， 256 色
无损压缩
支持简单动画
支持 boolean 透明
适合简单动画
```

``` 

JPEG :
```

``` 

颜色限于 256
有损压缩
可控制压缩质量
不支持透明
适合照片
```

``` 

PNG :
```

``` 

有 PNG8 和 truecolor PNG
PNG8 类似 GIF 颜色上限为 256 ，文件小，支持 alpha 透明度，无动画
适合图标、背景、按钮
```

### 18 行内元素float:left后是否变为块级元素？

``` 

行内元素设置成浮动之后变得更加像是 inline-block （行内块级元素，设置
成这个属性的元素会同时拥有行内和块级的特性，最明显的不同是它的默认宽
度不是 100% ），这时候给行内元素设置 padding-top 和 padding-bottom
或者 width 、 height 都是有效果的
```

### 19 在网⻚中的应该使用奇数还是偶数的字体？为什么呢？

``` 

偶数字号相对更容易和 web 设计的其他部分构成比例关系
```

### 20 ::before 和 :after中双冒号和单冒号 有什么区别？解释一下这 2 个

### 伪元素的作用

#### 单冒号( : )用于 CSS3 伪类，双冒号(:: )用于 CSS3 伪元素

#### 用于区分伪类和伪元素

### 21 如果需要手动写动画，你认为最小时间间隔是多久，为什么？（阿

### 里）

``` 

多数显示器默认频率是 60Hz ，即 1 秒刷新 60 次，所以理论上最小间隔为
1/60*1000ms ＝ 16.7ms
```

### 22 CSS合并方法

``` 

避免使用 @import 引入多个 css 文件，可以使用 CSS 工具将 CSS 合并为一个 CSS文
件，例如使用 Sass\Compass 等
```

### 23 CSS不同选择器的权重(CSS层叠的规则)

``` 

！important 规则最重要，大于其它规则

行内样式规则，加 1000

对于选择器中给定的各个 ID 属性值，加 100

对于选择器中给定的各个类属性、属性选择器或者伪类选择器，加 10

对于选择其中给定的各个元素标签选择器，加 1

如果权值一样，则按照样式规则的先后顺序来应用，顺序靠后的覆盖靠前的规则

```

### 24 列出你所知道可以改变⻚面布局的属性

``` 

position 、 display 、 float 、 width、 height 、 margin 、 padding 、
top 、 left 、 right、`
```

### 25 CSS在性能优化方面的实践

``` 

css 压缩与合并、 Gzip 压缩

css 文件放在 head 里、不要用 @import

尽量用缩写、避免用滤镜、合理使用选择器
```

### 26 CSS 3 动画（简单动画的实现，如旋转等）

``` 

依靠 CSS3 中提出的三个属性： transition 、 transform 、 animation

transition ：定义了元素在变化过程中是怎么样的，包含 transition-property 、
transition-duration 、 transition-timing-function 、 transition-delay 。
transform ：定义元素的变化结果，包含 rotate 、 scale 、 skew 、 translate 。
animation ：动画定义了动作的每一帧（ @keyframes ）有什么效果，包括 animation-
name ， animation-duration、 animation-timing-function 、 animation-
delay 、 animation-iteration-count 、 animation-direction
```

### 27 base 64 的原理及优缺点

#### 优点可以加密，减少了 HTTTP 请求

#### 缺点是需要消耗 CPU 进行编解码

### 28 几种常⻅的CSS布局

#### 流体布局

``` css
.left {
    float: left;
    width: 100px;
    height: 200px;
    background: red;
}

.right {
    float: right;
    width: 200px;
    height: 200px;
    background: blue;
}

.main {
    margin-left: 120px;
    margin-right: 220px;
    height: 200px;
    background: green;
}
```

#### 圣杯布局

``` html
<div class="container">
    <div class="left"></div>
    <div class="right"></div>
    <div class="main"></div>
</div>
```

``` css
.container {
    margin-left: 120px;
    margin-right: 220px;
}

.main {
    float: left;
    width: 100%;
    height: 300px;
    background: green;
}

.left {
    position: relative;
    left: -120px;
    float: left;
    height: 300px;
    width: 100px;
    margin-left: -100%;
    background: red;
}

.right {
    position: relative;
    right: -220px;
    float: right;
    height: 300px;
    width: 200px;
    margin-left: -200px;
    background: blue;
}
```

``` html
<div class="container">
    <div class="main"></div>
    <div class="left"></div>
    <div class="right"></div>
</div>
```

#### 双⻜翼布局

``` css
.content {
    float: left;
    width: 100%;
}

.main {
    height: 200px;
    margin-left: 110px;
    margin-right: 220px;
    background: green;
}

.main::after {
    content: '';
    display: block;
    font-size: 0;
    height: 0;
    zoom: 1;
    clear: both;
}

.left {
    float: left;
    height: 200px;
    width: 100px;
    margin-left: -100%;
    background: red;
}

.right {
    float: right;
    height: 200px;
    width: 200px;
    margin-left: -200px;
    background: blue;
}
```

``` html
<div class="content">
    <div class="main"></div>
</div>
<div class="left"></div>
<div class="right"></div>
```

### 29 stylus/sass/less区别

#### 均具有“变量”、“混合”、“嵌套”、“继承”、“颜色混合”五大基本特性

``` 

Scss 和 LESS 语法较为严谨， LESS 要求一定要使用大括号“{}”， Scss 和 Stylus 可以通过缩进表示层次与嵌套关系

Scss 无全局变量的概念， LESS 和 Stylus 有类似于其它语言的作用域概念

Sass 是基于 Ruby 语言的，而 LESS 和 Stylus 可以基于 NodeJS NPM 下载相应库后进行编译；
```

### 30 postcss的作用

#### 可以直观的理解为：它就是一个平台。为什么说它是一个平台呢？因为我们直接用它，感

#### 觉不能干什么事情，但是如果让一些插件在它上面跑，那么将会很强大

``` 

PostCSS 提供了一个解析器，它能够将 CSS 解析成抽象语法树
通过在 PostCSS 这个平台上，我们能够开发一些插件，来处理我们的 CSS ，比如热⻔
的： autoprefixer
postcss 可以对sass处理过后的 css 再处理 最常⻅的就是 autoprefixer
```

### 31 css样式（选择器）的优先级

#### 计算权重确定

``` 

!important

内联样式

后写的优先级高

```

### 32 自定义字体的使用场景

``` 

宣传/品牌/ banner 等固定文案

字体图标
```

### 33 如何美化CheckBox

``` 

<label> 属性 for 和 id

隐藏原生的 <input>

:checked + <label>
```

### 34 伪类和伪元素的区别

#### 伪类表状态

#### 伪元素是真的有元素

#### 前者单冒号，后者双冒号

### 35 base64 的使用

#### 用于减少 HTTP 请求

#### 适用于小图片

``` 

base64 的体积约为原图的 4/3
```

### 36 自适应布局

#### 思路：

``` 

左侧浮动或者绝对定位，然后右侧 margin 撑开
使用 <div> 包含，然后靠负 margin 形成 bfc
使用 flex
```

### 37 请用CSS写一个简单的幻灯片效果⻚面

``` 

知道是要用 CSS3 。使用 animation 动画实现一个简单的幻灯片效果
```

``` css
/**css**/
.ani {
    width: 480px;
    height: 320px;
    margin: 50px auto;
    overflow: hidden;
    box-shadow: 0 0 5px rgba(0, 0, 0, 1);
    background-size: cover;
    background-position: center;
    -webkit-animation-name: "loops";
    -webkit-animation-duration: 20s;
    -webkit-animation-iteration-count: infinite;
}
```

### 38 什么是外边距重叠？重叠的结果是什么？

``` 

外边距重叠就是margin-collapse
```

#### 在CSS当中，相邻的两个盒子（可能是兄弟关系也可能是祖先关系）的外边距可以结合成

#### 一个单独的外边距。这种合并外边距的方式被称为折叠，并且因而所结合成的外边距称为

#### 折叠外边距。

#### 折叠结果遵循下列计算规则 ：

#### 两个相邻的外边距都是正数时，折叠结果是它们两者之间较大的值。

#### 两个相邻的外边距都是负数时，折叠结果是两者绝对值的较大值。

#### 两个外边距一正一负时，折叠结果是两者的相加的和。

### 39 rgba()和opacity的透明效果有什么不同？

``` 

rgba() 和 opacity 都能实现透明效果，但最大的不同是 opacity 作用于元素，以及元素内的所有内容的透明度，

而 rgba() 只作用于元素的颜色或其背景色。（设置 rgba 透明的元素的子元素不会继承透明效果！）
```

### 40 css中可以让文字在垂直和水平方向上重叠的两个属性是什么？

``` css
@-webkit-keyframes "loops" {
    0% {
        background: url(http://d.hiphotos.baidu.com/image/w%3D400/sign=c01e6

    }

    25% {
        background: url(http://b.hiphotos.baidu.com/image/w%3D400/sign=edee1

    }

    50% {
        background: url(http://b.hiphotos.baidu.com/image/w%3D400/sign=937da

    }

    75% {
        background: url(http://g.hiphotos.baidu.com/image/w%3D400/sign=7d375

    }

    100% {
        background: url(http://c.hiphotos.baidu.com/image/w%3D400/sign=cfb23

    }
}
```

``` 

垂直方向： line-height

水平方向： letter-spacing

```

### 41 如何垂直居中一个浮动元素？

**如何垂直居中一个 <img>?（用更简便的方法。）**

### 42 px和em的区别

``` 

/**方法一：已知元素的高宽**/
```

``` css
#div1 {
    background-color: #6699FF;
    width: 200px;
    height: 200px;
    position: absolute; //父元素需要相对定位
    top: 50%;
    left: 50%;
    margin-top: -100px; //二分之一的height，width
    margin-left: -100px;
}
```

``` 

/**方法二:**/
```

``` css
#div1 {
    width: 200px;
    height: 200px;
    background-color: #6699FF;
    margin: auto;
    position: absolute; //父元素需要相对定位
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
}
```

``` css
#container

/**<img>的容器设置如下**/
    {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
```

``` 

px 和 em 都是⻓度单位，区别是， px的值是固定的，指定是多少就是多少，计算比较
容易。 em 得值不是固定的，并且 em 会继承父级元素的字体大小。

浏览器的默认字体高都是 16px 。所以未经调整的浏览器都符合: 1em=16px 。那么
12px=0.75em , 10px=0.625em 。
```

### 43 Sass、LESS是什么？大家为什么要使用他们？

#### 他们是 CSS 预处理器。他是 CSS 上的一种抽象层。他们是一种特殊的语法/语言编译成

#### CSS 。

``` 

例如Less是一种动态样式语言. 将CSS赋予了动态语言的特性，如变量，继承，运算， 函
数. LESS 既可以在客户端上运行 (支持 IE 6+, Webkit , Firefox )，也可一在服务端
运行 (借助 Node.js )
```

**为什么要使用它们？**

``` 

结构清晰，便于扩展。

可以方便地屏蔽浏览器私有语法差异。这个不用多说，封装对- 浏览器语法差异的重复处理，减少无意义的机械劳动。

可以轻松实现多重继承。

完全兼容 CSS 代码，可以方便地应用到老项目中。LESS 只- 是在 CSS 语法上做了扩展，所以老的 CSS 代码也可以与 LESS 代码一同编译
```

### 44 知道css有个content属性吗？有什么作用？有什么应用？

``` 

css的 content 属性专⻔应用在 before/after 伪元素上，用于来插入生成
内容。最常⻅的应用是利用伪类清除浮动。
```

``` css
/**一种常⻅利用伪类清除浮动的代码**/
.clearfix:after {
    content: "."; //这里利用到了content属性
    display: block;
    height: 0;
    visibility: hidden;
    clear: both;
}

.clearfix {
    *zoom: 1;
}
```

### 45 水平居中的方法

``` 

元素为行内元素，设置父元素 text-align:center

如果元素宽度固定，可以设置左右 margin 为 auto ;

如果元素为绝对定位，设置父元素 position 为 relative ，元素设left:0;right:0;margin:auto;

使用 flex-box 布局，指定 justify-content 属性为center

display 设置为 tabel-ceil
```

### 46 垂直居中的方法

``` 

将显示方式设置为表格， display:table-cell ,同时设置 vertial-align：middle

使用 flex 布局，设置为 align-item：center

绝对定位中设置 bottom:0,top:0 ,并设置 margin:auto

绝对定位中固定高度时设置 top:50%，margin-top 值为高度一半的负值

文本垂直居中设置 line-height 为 height 值
```

### 47 如何使用CSS实现硬件加速？

#### 硬件加速是指通过创建独立的复合图层，让GPU来渲染这个图层，从而提高性

#### 能，

``` 

一般触发硬件加速的 CSS 属性有 transform 、 opacity 、 filter ，为了避免 2 D动画
在 开始和结束的时候的 repaint 操作，一般使用 tranform:translateZ(0)
```

### 48 重绘和回流（重排）是什么，如何避免？

#### DOM的变化影响到了元素的几何属性（宽高）, 浏览器重新计算元素的几何属性，其他元素

#### 的几何

#### 属性和位置也会受到影响，浏览器需要重新构造渲染树，这个过程称为重排，浏览器将受

#### 到影响的部分

#### 重新绘制到屏幕上的过程称为重绘。引起重排的原因有

#### 添加或者删除可⻅的DOM元素，

#### 元素位置、尺寸、内容改变，

#### 浏览器⻚面初始化，

#### 浏览器窗口尺寸改变，重排一定重绘，重绘不一定重排，

#### 减少重绘和重排的方法 ：

#### 不在布局信息改变时做 DOM 查询

``` 

使用 cssText 或者 className 一次性改变属性

使用 fragment

对于多次重排的元素，如动画，使用绝对定位脱离文档流，让他的改变不影响到其他元素
```

### 49 说一说css 3 的animation

``` 

css 3 的 animation 是css 3 新增的动画属性，这个css 3 动画的每一帧是通过 @keyframes
来声明的， keyframes 声明了动画的名称，通过 from 、 to或者是百分比来定义
每一帧动画元素的状态，通过 animation-name 来引用这个动画，同时css 3 动画也可以定
义动画运行的时⻓、动画开始时间、动画播放方向、动画循环次数、动画播放的方式，
这些相关的动画子属性有： animation-name 定义动画名、 animation-duration 定义
动画播放的时⻓、 animation-delay 定义动画延迟播放的时间、 animation-
direction 定义 动画的播放方向、 animation-iteration-count 定义播放次数、
animation-fill-mode 定义动画播放之后的状态、 animation-play-state 定义播放状
态，如暂停运行等、 animation-timing-function
定义播放的方式，如恒速播放、艰涩播放等。

```

### 50 左边宽度固定，右边自适应

#### 左侧固定宽度，右侧自适应宽度的两列布局实现

html结构

``` 

在外层 div （类名为 outer ）的 div 中，有两个子 div，类名分别为
left 和 right ，其中 left 为固定宽度，而 right 为自适应宽度
```

**方法 1 ：左侧div设置成浮动：float: left，右侧div宽度会自拉升适应**

``` html
<div class="outer">
    <div class="left">固定宽度</div>
    <div class="right">自适应宽度</div>
</div>
```

**方法 2 ：对右侧:div进行绝对定位，然后再设置right=0，即可以实现宽度自适应**

#### 绝对定位元素的第一个高级特性就是其具有自动伸缩的功能，当我们将

``` 

width 设置为 auto 的时候（或者不设置，默认为 auto ），绝对定位元
素会根据其 left 和 right 自动伸缩其大小
```

``` css
.outer {
    width: 100%;
    height: 500px;
    background-color: yellow;
}

.left {
    width: 200px;
    height: 200px;
    background-color: red;
    float: left;
}

.right {
    height: 200px;
    background-color: blue;
}
```

``` css
.outer {
    width: 100%;
    height: 500px;
    background-color: yellow;
    position: relative;
}

.left {
    width: 200px;
    height: 200px;
    background-color: red;
}

.right {
    height: 200px;
    background-color: blue;
    position: absolute;
    left: 200px;
    top: 0;
    right: 0;
}
```

**方法 3 ：将左侧div进行绝对定位，然后右侧div设置margin-left: 200 px**

**方法 4 ：使用flex布局**

### 51 两种以上方式实现已知或者未知宽度的垂直水平居中

``` css
.outer {
    width: 100%;
    height: 500px;
    background-color: yellow;
    position: relative;
}

.left {
    width: 200px;
    height: 200px;
    background-color: red;
    position: absolute;
}

.right {
    height: 200px;
    background-color: blue;
    margin-left: 200px;
}
```

``` css
.outer {
    width: 100%;
    height: 500px;
    background-color: yellow;
    display: flex;
    flex-direction: row;
}

.left {
    width: 200px;
    height: 200px;
    background-color: red;
}

.right {
    height: 200px;
    background-color: blue;
    flex: 1;
}
```

### 52 如何实现小于 12 px的字体效果

``` css
/** 1 **/
.wraper {
    position: relative;

    .box {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 100px;
        height: 100px;
        margin: -50px 0 0 -50px;
    }
}
```

``` css
/** 2 **/
.wraper {
    position: relative;

    .box {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }
}
```

``` css
/** 3 **/
.wraper {
    .box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
}
```

``` css
/** 4 **/
.wraper {
    display: table;

    .box {
        display: table-cell;
        vertical-align: middle;
    }
}
```

``` 

transform:scale() 这个属性只可以缩放可以定义宽高的元素，而行内元素
是没有宽高的，我们可以加上一个 display:inline-block ;
```

``` 

css 的属性，可以缩放大小
```

