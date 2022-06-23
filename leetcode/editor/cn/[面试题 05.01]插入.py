# 给定两个整型数字 N 与 M，以及表示比特位置的 i 与 j（i <= j，且从 0 位开始计算）。 
# 
#  编写一种方法，使 M 对应的二进制数字插入 N 对应的二进制数字的第 i ~ j 位区域，不足之处用 0 补齐。具体插入过程如图所示。 
# 
#  
# 
#  题目保证从 i 位到 j 位足以容纳 M， 例如： M = 10011，则 i～j 区域至少可容纳 5 位。 
# 
#  
# 
#  示例1: 
# 
#  
#  输入：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
#  输出：N = 1100(10001001100)
#  
# 
#  示例2: 
# 
#  
#  输入： N = 0, M = 31(11111), i = 0, j = 4
#  输出：N = 31(11111)
#  
#  Related Topics 位运算 👍 54 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def insertBits(self, N, M, i, j):
        """
        :type N: int
        :type M: int
        :type i: int
        :type j: int
        :rtype: int
        """
        for k in range(i, j + 1):
            N &= ~(1 << k)
        return N | (M << i)
# leetcode submit region end(Prohibit modification and deletion)
