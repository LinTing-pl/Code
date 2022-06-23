# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。 
# 
#  示例1: 
# 
#  
#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
#  
# 
#  示例2: 
# 
#  
#  输入：A = 1，B = 2
#  输出：2
#  
# 
#  提示: 
# 
#  
#  A，B范围在[-2147483648, 2147483647]之间 
#  
#  Related Topics 位运算 👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def convertInteger(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        a = 0
        c = A ^ B
        for i in range(32):
            t = c >> i & 1
            a += t
        return a
# leetcode submit region end(Prohibit modification and deletion)
