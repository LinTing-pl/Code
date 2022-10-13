   /*i表示当前图片的下标和当前圆点的下标（图片和圆点是对应关系）*/
   var i = 0;
   var timer;
   $(function() {
       /*Step 1： 设置页面刚加载出来显示的是第一张图片*/
       $(".lunbo").eq(0).show().siblings().hide();
       /*开始做图片轮播，使用定时器*/
       start();
       /*Step 2： 鼠标移入小圆点的时候，首先清除定时器，找到当前圆点的索引，改变当前显示的图片，使其变换成圆点对应的图片，当前圆点变换样式*/
       $("b").hover(function() {
           clearInterval(timer);
           i = $(this).index();
           change();
       }, function() {
           /*鼠标移出的时候，重新启动定时器*/
           start();
       });
       /*Step 3： 点击左边按钮时候，显示当前图片的左边的第一个图片，再点击，依次向左，图片变换，圆点样式变换。当停止点击按钮时，图片依旧一定时间内显示下一个图片（右边的第一个）*/
       $(".left").click(function() {
           i--;
           /*当图片已经是第一个，再点击的时候，显示最后一张图片*/
           if (i == -1) {
               i = 3;
           }
           change();
       });
       /*Step 4： 点击右边按钮时候，显示当前图片的右边的第一个图片，原理同左边图片效果*/
       $(".right").click(function() {
           i++;
           /*当图片已经是最后一个，再点击的时候，显示第一张图片*/
           if (i == 3) {
               i = 0;
           }
           change();
       });
   });
   /*开始轮播函数*/
   function start() {
       /*定时器，每个图片在页面上停留的时间是3s*/
       timer = setInterval(function() {
           i++;
           if (i == 3) {
               i = 0;
           }
           change();
       }, 2000);
   }
   /*当前图片及对应圆点变换函数*/
   function change() {
       /*当前图片淡入，其他图片淡出*/
       $(".lunbo").eq(i).fadeIn(300).siblings().stop(true, true).fadeOut(0);
       /*当前圆点添加类current，其他圆点删除其类current*/
       $("b").eq(i).addClass("current").siblings().removeClass("current");
   }