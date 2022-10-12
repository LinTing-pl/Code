# 给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 11
# 输出：0
# 解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 数学 二分查找 👍 312 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur, base = 1, 9
        while n > cur * base:
            n -= cur * base
            cur += 1
            base *= 10
        n -= 1
        num = 10 ** (cur - 1) + n // cur
        idx = n % cur
        return num // (10 ** (cur - 1 - idx)) % 10
# leetcode submit region end(Prohibit modification and deletion)
