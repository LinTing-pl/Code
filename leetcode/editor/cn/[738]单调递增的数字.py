# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。 
# 
#  给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  
# 输入: n = 332
# 输出: 299
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= n <= 10⁹ 
#  
#  Related Topics 贪心 数学 👍 257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 111111111
        result = 0
        for _ in range(9):
            while result + ones > n:
                ones //= 10
            result += ones
        return result
# leetcode submit region end(Prohibit modification and deletion)
