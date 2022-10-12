# 现有函数 printNumber 可以用一个整数参数调用，并输出该整数到控制台。 
# 
#  
#  例如，调用 printNumber(7) 将会输出 7 到控制台。 
#  
# 
#  给你类 ZeroEvenOdd 的一个实例，该类中有三个函数：zero、even 和 odd 。ZeroEvenOdd 的相同实例将会传递给三个不同线程：
#  
# 
#  
#  线程 A：调用 zero() ，只输出 0 
#  线程 B：调用 even() ，只输出偶数 
#  线程 C：调用 odd() ，只输出奇数 
#  
# 
#  修改给出的类，以输出序列 "010203040506..." ，其中序列的长度必须为 2n 。 
# 
#  实现 ZeroEvenOdd 类： 
# 
#  
#  ZeroEvenOdd(int n) 用数字 n 初始化对象，表示需要输出的数。 
#  void zero(printNumber) 调用 printNumber 以输出一个 0 。 
#  void even(printNumber) 调用printNumber 以输出偶数。 
#  void odd(printNumber) 调用 printNumber 以输出奇数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出："0102"
# 解释：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 5
# 输出："0102030405"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics 多线程 👍 129 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import threading


class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n + 1
        self.Zero = threading.Semaphore(1)
        self.Even = threading.Semaphore(0)
        self.Odd = threading.Semaphore(0)

    # printNumber(x) outputs "x", where x is an integer.

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n):
            self.Zero.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.Odd.release()
            else:
                self.Even.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 2 == 0:
                self.Even.acquire()
                printNumber(i)
                self.Zero.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 2 == 1:
                self.Odd.acquire()
                printNumber(i)
                self.Zero.release()

# leetcode submit region end(Prohibit modification and deletion)
