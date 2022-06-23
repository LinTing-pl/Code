# 给定一个正整数 n ，你可以做如下操作： 
# 
#  
#  如果 n 是偶数，则用 n / 2替换 n 。 
#  如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。 
#  
# 
#  返回 n 变为 1 所需的 最小替换次数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 4
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2³¹ - 1 
#  
#  Related Topics 贪心 位运算 记忆化搜索 动态规划 👍 234 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n % 2 == 0: return 1 + self.integerReplacement(n // 2)
        return 2 + min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1))
# leetcode submit region end(Prohibit modification and deletion)
