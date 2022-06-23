# 编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是： 
# 
#  
#  如果这个数字可以被 3 整除，输出 "fizz"。 
#  如果这个数字可以被 5 整除，输出 "buzz"。 
#  如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。 
#  
# 
#  例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14
# , fizzbuzz。 
# 
#  假设有这么一个类： 
# 
#  
# class FizzBuzz {
#   public FizzBuzz(int n) { ... }               // constructor
#   public void fizz(printFizz) { ... }          // only output "fizz"
#   public void buzz(printBuzz) { ... }          // only output "buzz"
#   public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
#   public void number(printNumber) { ... }      // only output the numbers
# } 
# 
#  请你实现一个有四个线程的多线程版 FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用： 
# 
#  
#  线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。 
#  线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。 
#  线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。 
#  线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。 
#  
# 
#  
# 
#  提示： 
# 
#  
#  本题已经提供了打印字符串的相关方法，如 printFizz() 等，具体方法名请参考答题模板中的注释部分。 
#  
# 
#  
#  Related Topics 多线程 👍 78 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import threading


class FizzBuzz(object):
    def __init__(self, n):
        self.n = n + 1
        self.Fizz = threading.Semaphore(0)
        self.Fizzbuzz = threading.Semaphore(0)
        self.Buzz = threading.Semaphore(0)
        self.Num = threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        """
        :type printFizz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 != 0:
                self.Fizz.acquire()
                printFizz()
                self.Num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        """
        :type printBuzz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 3 != 0 and i % 5 == 0:
                self.Buzz.acquire()
                printBuzz()
                self.Num.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        """
        :type printFizzBuzz: method
        :rtype: void
        """
        for i in range(1, self.n):
            if i % 3 == 0 and i % 5 == 0:
                self.Fizzbuzz.acquire()
                printFizzBuzz()
                self.Num.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n):
            self.Num.acquire()
            if i % 3 == 0 and i % 5 == 0:
                self.Fizzbuzz.release()
            elif i % 3 == 0:
                self.Fizz.release()
            elif i % 5 == 0:
                self.Buzz.release()
            else:
                printNumber(i)
                self.Num.release()

# leetcode submit region end(Prohibit modification and deletion)
