# 对于一个 正整数，如果它和除了它自身以外的所有 正因子 之和相等，我们称它为 「完美数」。 
# 
#  给定一个 整数 n， 如果是完美数，返回 true；否则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：num = 28
# 输出：true
# 解释：28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, 和 14 是 28 的所有正因子。 
# 
#  示例 2： 
# 
#  
# 输入：num = 7
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num <= 10⁸ 
#  
#  Related Topics 数学 👍 172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return False
        ans = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                ans += i
                if i * i < num:
                    ans += num / i

        return ans == num
# leetcode submit region end(Prohibit modification and deletion)
