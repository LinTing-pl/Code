# 给你一个类： 
# 
#  
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# } 
# 
#  三个不同的线程 A、B、C 将会共用一个 Foo 实例。 
# 
#  
#  线程 A 将会调用 first() 方法 
#  线程 B 将会调用 second() 方法 
#  线程 C 将会调用 third() 方法 
#  
# 
#  请设计修改程序，以确保 second() 方法在 first() 方法之后被执行，third() 方法在 second() 方法之后被执行。 
# 
#  提示： 
# 
#  
#  尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。 
#  你看到的输入格式主要是为了确保测试的全面性。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出："firstsecondthird"
# 解释：
# 有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 
# third() 方法。正确的输出是 "firstsecondthird"。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,3,2]
# 输出："firstsecondthird"
# 解释：
# 输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正
# 确的输出是 "firstsecondthird"。 
# 
#  
# 
#  
#  
# 提示：
# 
#  
#  nums 是 [1, 2, 3] 的一组排列 
#  
#  Related Topics 多线程 👍 373 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from threading import Lock


class Foo(object):
    def __init__(self):
        self.firstJobDone=Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstJobDone.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.firstJobDone:
            printSecond()
            self.secondJobDone.release()
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        
        # printThird() outputs "third". Do not change or remove this line.

        with self.secondJobDone:
            printThird()
# leetcode submit region end(Prohibit modification and deletion)
