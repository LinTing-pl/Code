# 给你一个类： 
# 
#  
# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }
# 
#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
#  
# 
#  两个不同的线程将会共用一个 FooBar 实例： 
# 
#  
#  线程 A 将会调用 foo() 方法，而 
#  线程 B 将会调用 bar() 方法 
#  
# 
#  请设计修改程序，以确保 "foobar" 被输出 n 次。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1
# 输出："foobar"
# 解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 2
# 输出："foobarfoobar"
# 解释："foobar" 将被输出两次。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics 多线程 👍 161 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from threading import Lock


class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.LockFoo = Lock()
        self.LockBar = Lock()
        self.LockBar.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """

        for i in range(self.n):
            self.LockFoo.acquire()
            printFoo()
            self.LockBar.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """

        for i in range(self.n):
            self.LockBar.acquire()
            printBar()
            self.LockFoo.release()

# leetcode submit region end(Prohibit modification and deletion)
